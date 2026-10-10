# Simulation architecture — ownership, time and persistence

**Status:** Proposed architecture, adopted naming; interfaces and rates remain open to implementation experiments.

This document defines the boundaries between simulations. It does **not** prescribe separate processes, network services, databases or an ECS framework. Prefer in-process modules and explicit contracts until profiling justifies more machinery.

## The named components

| Component | Authoritative responsibility | What it explicitly does not own |
|---|---|---|
| **SimCore** | Simulation scheduling, deterministic order, global world-time progression, acceleration/pause/catch-up, event delivery coordination | Weather, biological truth, rendering |
| **RaukenState** | Persistent identities, spatial indexing, chunk/region records, saves, timestamps, compact history and coherent snapshot access | Running physiology or changing weather, universal messaging for every operation |
| **RaukenSim** | Current environmental conditions, world-time-derived seasons and day/night, regional weather, surface moisture and temporary storm/flood states | Geological erosion, living organisms, simulation scheduler |
| **FloraSim** | Persistent trees, shrubs, herbs, ferns, moss/fungal colonies, growth, biomass, phenology, damage, death and botanical populations | Rendering, universal weather calculation, animal hunger |
| **FaunaSim** | Nonplayer animal individuals and populations, movement/decisions, active multirate physiological state and distant ecological approximations | Player intent and UI, plant growth, independent physiology formulas |
| **HeroSim** | Player animal state, player-intention arbitration, high-fidelity sensory/physiological response, individual development and feedback | Separate player-only biological laws, weather, render implementation |
| **BeastCore** | Shared animal anatomy, metabolic rules, digestion, injury, homeostasis, perception and behavioral primitives used by HeroSim and FaunaSim | Ownership of animals, standalone ticking simulator |
| **InteractionsCore** | Validated cross-domain transactions, durable ecological transfers and relevant change events | AI decision making, rendering, per-frame collision processing, its own ecology simulation |
| **Renderer / audio / physics** | Presentation, motion and local physical feedback using state snapshots, interactions and high-rate controls | Deciding rainfall, simulating plant age, saving biological authority |

**Ownership rule:** each mutable domain fact has exactly one authoritative simulator. RaukenState stores the fact and coordinates durable access, but does not invent it. BeastCore provides common rules without independently owning any living animal. InteractionsCore coordinates cross-owner changes, not all internal reads.

## Data and control flow

```text
          SIMCORE — timeline, update queues, event order
                              |
                   RAUKENSTATE — identity/save
                   /          |           \
       RAUKENSIM          FLORASIM       FAUNASIM
       environment         plants         wildlife
           |                                |
           +---------------- INTERACTIONSCORE +
           |                   |              |
           +---------------- HERO SIM <-------+
                              |
                     Player intentions
                    (BEASTCORE shared by
                     HeroSim and FaunaSim)

    World/biological snapshots + changes ---> Renderer
    Physical contacts/sensory inputs ------> relevant sims
```

This is a **logical diagram**, not a requirement that all paths route through RaukenState or InteractionsCore. Local, frequent operations can use direct in-process interfaces. Rendering chunks and active simulation regions are different concepts.

## Time semantics

**SimCore owns the authoritative global timeline.** RaukenSim derives solar time, season and weather from it and stores environmental histories. Physics and immediately sensed events operate at normal realtime responsiveness even when world time is accelerated. SimCore can change how much simulated world time passes per wall-clock second, including fast-forward through rest or quiet intervals.

Growth pacing is a **separately tunable species life-history transformation**, not arbitrary animation scaling or a HeroSim-only secret clock. The player should see meaningful juvenile development within an enjoyable session, but siblings and comparable animals must follow compatible rules. Test a combination of world-time acceleration, nonlinear early growth and conditional growth based on nutrition. Do not automatically scale every action, reaction, hunger response and footstep by the visual aging multiplier.

Time contracts:
- **High-rate immediate:** player locomotion/physics, contact, acute pain/startle and steering.
- **Frequent animal state:** thermal discomfort, ongoing pain, attention, fatigue, hydration and gut processes at different frequencies and on relevant events.
- **Slow ecology:** growth, reproduction, decay, phenology, population changes.
- **Regional weather:** weather and storm events on its own intervals, queried by position or delivered as changes.
- **Deferred catch-up:** inactive plants and distant fauna integrate elapsed simulation time and relevant events when required.

Exact frequencies are **not fixed**. Event responsiveness and measured cost matter more than making a timer for every statistic.

## Environmental history and lazy evaluation

The environment is based on mostly fixed map geography: streams/springs, soils, baseline moisture, slopes and flood susceptibility are generated offline. RaukenSim updates weather, seasons, surface wetness and temporary water levels **without detailed groundwater transport or routine erosion**.

When FloraSim evaluates an organism last updated at time T, it requests the appropriate RaukenSim interval summary (rain/temperature/drought/flood exposure) and applies InteractionsCore disturbance records (e.g., herbivory, storm damage). It updates the plant to current simulated time without reconstructing every intervening frame.

RaukenState must retain enough summaries/events to support this. Compact history only after relevant owners are safely advanced/checkpointed; never discard unprocessed events because a render chunk unloaded.

## Simulated vs visible

**Visibility never determines whether an organism exists or has biological effects.**

When a render chunk is requested:
1. Streamer consults RaukenState for identities and location records.
2. FloraSim advances relevant plant individuals/population patches to the requested world time in a **bulk** request.
3. FaunaSim supplies any represented local animals or proxies; near-simulation activity is managed independently of visual chunk requests.
4. Renderer receives organism snapshots, stable seeds, materials, environmental state and interaction anchors.
5. Renderer instantiates/interpolates geometry and audio locally. It does not poll each tree for updates every frame.
6. Subsequent visible changes are **events** or amortized updates: browsing, broken branches, flowering thresholds, major growth. Wind/wetness animation may respond to cached RaukenSim fields each render frame.
7. Render unload discards visuals only, not organism state.

Animal proximity can trigger simulation-fidelity promotion, but does not mean spawning organisms from nothing. Distant populations may use regional aggregates and resource budgets; reconciling those with known individuals must preserve identity and avoid double-counting.

## InteractionsCore contract

Cross-domain interactions use intent → validate → reserve/commit → publish:
- Feeding: BeastCore/HeroSim or FaunaSim selects accessible plant tissue, FloraSim validates remaining biomass, InteractionsCore transfers **only the successfully removed quantity** to the consumer. Repeated simultaneous bites cannot duplicate biomass.
- Drinking: water-state access from RaukenSim; HeroSim/FaunaSim ingest water with salinity/depth/access checks. Not all visually wet surfaces are freshwater.
- Storm injury: RaukenSim reports weather, FloraSim evaluates tree vulnerability, InteractionsCore records fallen-tree/resource transition, HeroSim/FaunaSim reacts to collision or obstruction.
- Death/decay: deceased organism leaves persistent remains in RaukenState; its living owner no longer counts live biomass; ecological decomposition/foraging consumes the remains without double claims.

No network-style distributed transaction system is needed. An ordered in-process command and result with unique event IDs and deterministic reconciliation should suffice initially. High-rate bone contacts, lookups and shading never go through this transaction layer.

## Cross-domain invariants

1. The same plant stays recognizable after unload/reload and after decades; growth/damage from a stable seed and persistent structural changes.
2. Same animal physiology rules for player and wild animals, with different evaluation fidelity.
3. A storm changes physiology, plant water stress and visual wetness from **one** authoritative environmental state.
4. Concurrent consumers cannot each claim the same finite forage/resource.
5. No offscreen reset of plants, animals, weather consequences or resources.
6. Render visibility and simulation activation have independent budgets.
7. Simulation fast-forward has a deterministic, bounded catch-up strategy and accounts for ecologically significant events.
8. Normal year-to-year terrain stays recognizable; only exceptional temporary flood masks and rare authored disturbance alter local traversal.
9. No hidden omniscience: sensing depends on sensory modality, distance, occlusion, wind and attention.
10. Every system can be tested headlessly with fixed seeds, time ranges and event traces.

## Interface sketch — concepts, not code

- SimCore: advance, schedule, change time scale, pause, query simulation timestamp.
- RaukenState: get spatial entity records, stable IDs, save/checkpoint, history cursor, region snapshots.
- RaukenSim: sample environment at position/time, get interval summary, sample water depth/current/salinity, environmental change events.
- FloraSim: advance plant batch, query plant resource, apply validated damage, get render snapshot.
- FaunaSim: advance near/far agents, query animal perception/state, reconcile regional populations.
- HeroSim: accept player intent, advance high-fidelity animal, report state/behavioral output.
- BeastCore: integrate physiological quantities, evaluate sensors, derive drives/reflexes, compute developmental state.
- InteractionsCore: execute typed, validated resource/damage/reproduction transitions and emit completion events.

## Planning references

[RaukenSim](rauken-sim.md) · [FloraSim](flora-sim.md) · [FaunaSim](fauna-sim.md) · [HeroSim](hero-sim.md) · [Ecology](ecology-and-hydrology.md) · [Gameplay](gameplay.md)
