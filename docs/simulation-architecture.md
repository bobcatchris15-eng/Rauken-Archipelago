# Simulation architecture — state, activation, perception and presentation

**Status:** Agreed logical boundaries; algorithms, distances and implementation framework remain provisional. These are **modules**, not independent network services.

## Fidelity policy — believable on the outside, cheap on the inside

**Decided:** this is a staged natural-history illusion, not a scientifically closed ecology. Prioritize (1) visual and physical contact quality, (2) observable animal behavior and immediate responses, (3) continuity of conspicuous changes and relationships, and only then (4) approximate hidden environmental/population state. A sophisticated invisible model needs a demonstrated improvement over a cheap proxy before implementation.

**A useful simulation state is the smallest state that prevents noticeable contradictions.** Regions may be generated from seeds and a few habitat/season/occupancy variables. Nearby creatures become detailed actors before they enter view; distant ones remain approximate densities. Most plants are static or low-rate display variants; only visibly important individual damage, death or recovery needs persistence. Do not use scientific internal accuracy as a proxy for visual quality.

Keep the existing domain names and ownership rules to prevent double rendering, duplicate known animals and forgotten player-visible effects. Those correctness constraints are *targeted*, not permission to build complete nutrient, thermodynamic, weather, population or metabolic ledgers. See [Vision](vision-and-principles.md).

## Named components

| Component | Owns | Does not own |
|---|---|---|
| **SimCore** | Shared timeline, variable time scale, scheduling, ordering, spatial **simulation chunk activation** | Weather, animal biology, camera |
| **StalthosState** | Persisted world/region/plant records, regional fauna cohorts, bounded eligible retained identities, saves and event history | A complete persistent biography for every animal; simulation itself |
| **StalthosSim** | Weather, day/night, seasons, local wetness, temporary storm/flood conditions and environment history | Runtime erosion/geology, organisms |
| **FloraSim** | All relevant botanical/fungal individuals and patches; growth, health, resources, death, lazy catch-up | Per-frame renderer polling |
| **FaunaSim** | Local active wildlife drawn from population cohorts, behavior, physiology at suitable fidelity; *optional bounded retention of previously instantiated relevant individuals* | Individual identities for never-instantiated wildlife, lifelong memories for ordinary animals |
| **HeroSim** | Current Hero Beast biology, autonomous behavior, player-intent arbitration, senses and involuntary responses | Camera knowledge or camera movement |
| **BeastCore** | Shared animal physiology, sensation, growth and behavior primitives used by HeroSim and FaunaSim | Its own ticking population |
| **InteractionsCore** | Validated cross-domain resource/damage/state transfers and outcome events | A master AI decision layer |
| **HeroView** | Player input/focus, direct movement/destinations, invoked contextual slow-time responses, documentary/alarm camera and human-facing experience | Biological truth, unrestricted spectator flight, injecting camera sight into HeroSim |
| **Renderer/physics/audio** | Scene rendering, local physical contact/animation and audio implementation | Persistence/biological authority, weather decisions |

**Ownership invariant:** one domain owns each mutable ecological fact. StalthosState stores agreed persistent representations without becoming a per-frame database bottleneck; InteractionsCore coordinates only significant cross-domain operations. Direct local reads and high-rate interactions should remain inexpensive.

## Conceptual data flow

```text
  Human  ->  HeroView (input focus, camera, destination picking)
                      | player intention
                      v
                   HeroSim <---- BeastCore shared with FaunaSim
                body + perception
                 ^     ^      ^
          StalthosSim FloraSim FaunaSim <--- SimCore simulation activation
              \        |      /
                   InteractionsCore
                         |
                    StalthosState

  World snapshots: StalthosState + domain sims -> scene streamer -> renderer
  Subjective/body signals: HeroSim ---------------------------> HeroView
  Visual/audio scene + body presentation ---------------------> human
```

This is **not** a fixed synchronous API chain. HeroSim senses a world through the Hero Beast's own body, not through the camera. The renderer ingests world renderables from the streamer/domain snapshots without routing whole scene graphs through HeroSim.

## Voluntary intentions and acoustic perspectives

**One HeroSim intention system:** player suggestions (destination/contextual goals) are accepted as ordinary Hero Beast goals with **higher voluntary priority/provenance**, not executed by a separate camera-controlled locomotion or decision system. HeroSim handles actual route execution, movement and reflexes; BeastCore remains the shared physical/sensory competence. Once a suggested goal finishes or fails, HeroSim continues normal life. Merely detaching the HeroView camera does not change the animal's autonomy or preserve it in an idle state.

**One set of spatial sound sources, two listeners:** HeroSim/BeastCore hears from the Hero Beast's ears and interprets species-specific perception. HeroView's primary audio listener hears from the player camera's physical position, including while detached. FaunaSim/StalthosSim/world ambience provide sounds without needing two independent sound-world simulations. Player-only camera audio must never modify HeroSim's sensory state or trigger its alarm-driven camera recall. Physiological feedback can be mixed subtly without pretending the listener is beside the animal. Coarse habitat ambience avoids instantiating invisible individual insects just to make environmental sound.

**The only allowed camera-to-animal exception remains an intention's destination or deliberately selected contextual target**, not associated secret terrain/wildlife facts. The camera and the animal may witness or hear different things; those discrepancies are part of the intended documentary experience.

## Spatial lifecycle: three independent extents

1. **Active simulation:** SimCore prewarms and activates chunks around the Hero Beast, including a buffer beyond the **entire reachable envelope** of HeroView's nearby detached camera. FaunaSim begins local behaviors before the ridge is rendered; FloraSim bulk reconstructs the right plants/patches.
2. **Hero perception:** BeastCore/HeroSim evaluate what the Hero Beast could perceive from her body (eyes/ears/smell/contact, occlusion, attention); no omniscient camera data.
3. **Rendered scene:** HeroView's camera frustum and LOD choose what's drawn, including distant static scenery. The camera can show something she does not notice.

**A simulation chunk is not the same as a render chunk.** A renderer chunk unloading cannot kill a local animal. Camera flight over a nearby hill shouldn't cause a new herd to spring into existence only because it is now visible. Camera tether and simulation-buffer distances are open tuning parameters; avoid whole-island active simulation when the hero is far away.

[Spatial activation](spatial-activation.md) describes the activation/retirement lifecycle.

## What becomes instantiated

**Flora:** On simulation activation, FloraSim resolves plant individuals and colonies from static suitability, deterministic seeds and compact persistent overrides, lazily advancing growth to current world time. Substantial trees retain stable *logical identities* and recognizable age, shape, mortality and damage across reloads; unchanged seeded trees need not each have an individually updated database row. Low ground cover and localized canopy-gap recovery can use coarse population patches. **Forest disturbance/regeneration is provisional and shallow**, not a dedicated succession, seed-bank, competition, wildfire-spread or erosion engine.

**Fauna:** Before local activation, regions have rough species density/age mix, not individual biographies. On activation FaunaSim stages plausible wildlife (including outside camera view); these live, rest, browse, observe and react. Most retire to approximate regional availability. Only **previously instantiated** animals with meaningful bonds, dependence or selected notable encounters may keep compact dormant identity; no imagined individuals are registered across remote islands.

Individual retention and simulation fidelity are different axes: an active small transient creature can have responsive behavior; a retained social or notable individual can sleep as a tiny saved record. A small active/retained exclusion record prevents recognizable duplicate animals on reactivation. A short locality disturbance/cooldown may discourage conspicuous instant replacement without keeping per-animal biographies.

## HeroSim, HeroView and successive lives

**Direct body-relative steering** is the strongest voluntary human intervention. Ordinary hunger, curiosity and social impulses must not redirect player locomotion. Genuine physical incapacity or exceptional short reflexes can affect action. **Player-invoked** contextual response choices and persistent TravelTo destinations are higher-level intentions HeroSim must enact or fail under physical/sensory conditions, not guaranteed animations, strikes, mating outcomes or navigation.

**Direct locomotor correction policy:** BeastCore supplies camera-independent motor competence (foot placement, balance, small avoidance); HeroSim accepts movement intents from HeroView and rejects self-chosen route deviations exceeding a **central-third-wide screen-space corridor around the intended projected course**. If no valid local route exists, the Hero Beast stops and may inspect the obstacle until direct input changes or is released. Release restores ordinary full autonomy; destination mode remains free to plan wide routes. This corridor limits *automatic lateral deviation*, not deliberate side-on travel across a moving camera's entire screen. HeroView supplies projection/framing only, never extra animal sensory knowledge.

Compatible local behavior continues during direct locomotion: a Smalltrotter can pluck shrubs while walking, Reedcrest exchange calls, Thistletail snap up nearby morsels and Brackenback glance at questionable scenery without prompts. With no player locomotion or maintained deliberate intent, **full HeroSim autonomy** travels, feeds, rests, socializes, courts, parents, responds to danger and can die. No mandatory idle radius or protective documentary-only variant.

HeroView normally presents an animal-centered third-person orbit/follow camera, independent of the Hero Beast's heading. A bounded locally detached camera remains available; it never supplies the animal with omniscience. After camera inactivity, HeroView may gently transition to continuous documentary framing, following the Hero Beast's actual life without cinematic teleports or staged events. Significant *sensed* alarms may coordinate animal and camera attention on the same approximate world point and recall a detached camera smoothly toward the animal. Player camera input can immediately interrupt any automatic composition.

A newly selected Hero Beast **hatches as an ordinary population member** within appropriate species habitat, with its natural parental and juvenile circumstances. Breeding/nesting are playable: a short, accelerated, world-consistent nesting-to-hatching episode targets roughly thirty minutes or less, whereas dependent care may continue through ordinary play much longer. No genetic-optimization or inherited character-progression system.

Death terminates the current animal, **not the persistent world**. A new hatchling enters an existing population with no prior Hero Beast relationships or powers. Previously instantiated individuals remain under the same bounded FaunaSim identity-retention/decay policy, coarsely advancing while inactive, even between player lives. No life-change purge, teleporting companions or demographically duplicated wildlife.

## Resolution is not a single distance-based level

Use **three practical presentation levels**, not an abstract general-purpose fidelity solver:

1. **Observed/contacting:** full animation, physically valid reach, movement and collisions, immediate reactions and directly visible outcomes. A browsed shrub changes; an encountered animal behaves continuously.
2. **Nearby but hidden:** simple actors, reduced-rate behavior and prewarming far enough beyond the full HeroView tether to prevent on-camera spawning. No detailed lifelong history.
3. **Remote/forgotten:** regional population density, habitat condition, season, seeded variation and a *small list of conspicuous exceptions* (e.g. a fallen landmark tree or surviving bonded companion). No offscreen individual activity replay.

Render detail is still chosen separately from animal sensing and activation. Save only information a return visit or ongoing relationship could expose. A small number of coarse counters and timestamped exception records is sufficient for most regions. Never implement a generalized importance predictor or force accurate distant ecological accounting.
## Four cross-domain contracts before implementation

1. **Visible contacts commit once:** InteractionsCore validates local physical reach/contact and updates the relevant *visible* food, injury or structural state without duplicate application. Patch-level foliage depletion is enough where individual bites are not distinguishable.
2. **Recognizable exceptions survive:** StalthosState keeps identities/state for the current Hero Beast, eligible existing social/dependent animals, destroyed or conspicuously altered trees, important nests/carcasses and other player-observable changes. Ordinary organisms remain seed/patch based.
3. **No obvious generation seams:** SimCore prepares plausible local animals beyond the complete detached-camera envelope and keeps recent occupancy long enough to avoid on-camera appearance/disappearance. Promotion/retirement of an encountered or retained individual must not create a duplicate.
4. **Bounded cheap updates:** StalthosSim supplies current seasonal/weather conditions and **occasional consequential event records**, not compulsory ordered climate chronology. FloraSim and FaunaSim resolve distant changes via elapsed-time formulas, probabilities or coarse region updates. No long historical replay on a camera turn.

These are small contracts among the **existing modules**, not new systems. Stable branch IDs, detailed demographic reservations, event journals and resource conservation are *optional targeted techniques*, justified only by an observable failure of simpler representations. See [FaunaSim](fauna-sim.md), [StalthosSim](stalthos-sim.md), [FloraSim](flora-sim.md) and [Spatial activation](spatial-activation.md).
## Time and update rates

SimCore owns **one shared calendar/world clock**, optionally sped up for rest and nesting. Realtime controls, body motion, collision and startle remain responsive. A few species parameters drive age, stage-specific appearance, reproductive maturity and late-life decline. Approximate condition (food/water/comfort/fatigue/injury) may affect behavior, but no exact digestion chemistry, energy conservation or multi-variable heat equation is required. Nearby HeroSim and FaunaSim use **compatible simple BeastCore rules**, with different update frequencies.

- **Immediate:** player input, collision, visible bites, near-animal reactions and danger.
- **Occasional:** active animal activity selection, condition changes, weather presentation and visible resource patch updates.
- **On demand / elapsed-time:** growth stage, seasonal variation, dormant population density and coarse vegetation recovery.
- **Exceptional events:** explicit flood, injury, dead tree, persistent nest or other conspicuous state changes.

Rest/time-skips should check for meaningful interrupts without replaying every hidden frame. Tune one set of affordable rates by observable tests rather than requiring every background physiological quantity to integrate continuously.
## Environment and cross-domain changes

World generation supplies stable terrain, streams, soil/habitat and baseline plant distributions. StalthosSim drives simple seasonal weather and temporary flood/wetness masks, not actual fluid balance or erosion. FloraSim chooses growth/coverage variants and changes visible plants using stable seeds, patch state and saved exceptions. FaunaSim uses habitat occupancy and a few condition/behavior rules, not a complete food-web economy.

InteractionsCore coordinates only local or conspicuous cross-domain results (e.g. food visually removed, a physical injury, a felled tree, a nest lost), with just enough protection against double application. Offscreen browsing and decomposition may be cheap changes to patch appearance or habitat tendency, without proving conservation of biomass. Rendering wind/wetness animation need not cause biology updates.
## Invariants / quality checks

1. Adult trees maintain stable shape and accumulated damage after arbitrary chunk cycling.
2. An active animal is already resting/browsing before Smalltrotter or the bounded camera sees it; the renderer's visibility does not generate it.
3. No remote island-wide individual wildlife registry. Long-term retained individuals are eligible **only after actual instantiation**, for bounded social, dependent and notable reasons.
4. Encountered or retained wildlife never doubles, visibly respawns or resurrects at activation boundaries; remote background population estimates may be approximate rather than exactly balanced.
5. HeroView may observe unseen predators; **HeroSim does not learn of them** until Smalltrotter's own senses detect them.
6. From a front-facing orbit camera, W moves Smalltrotter toward camera; moving sideways across the view leads to camera translation, not forced heading recenter.
7. A locally detached camera can inspect a nearby hill but is physically bounded from remote-island flight.
8. Ordinary thirst/hunger do not hijack direct steering or an active destination. Strong fear/pain can interrupt, especially during autonomous travel.
9. A comfortable, recently fed large predator may simply watch a juvenile sauropod and return to resting.
10. A flood affects movement/plant conditions/rendering consistently, then recedes with familiar terrain intact.
11. Time acceleration preserves a consistent visible aging/development rhythm for the player and comparable NPCs, without requiring exact internal metabolic accounting.
12. Test deterministic scene reconstruction, continuity across region cycling, visible bite/damage effects, bounded activation cost, comparable stage progression, physical follower strait travel and multi-life individual persistence. Test deep climate-history or branch-segment bookkeeping only if the simpler scheme visibly fails.

## Related specifications

[HeroView](hero-view.md) · [Spatial activation](spatial-activation.md) · [HeroSim](hero-sim.md) · [FaunaSim](fauna-sim.md) · [FloraSim](flora-sim.md) · [StalthosSim](stalthos-sim.md) · [Gameplay](gameplay.md)
