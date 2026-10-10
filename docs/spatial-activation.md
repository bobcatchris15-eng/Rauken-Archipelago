# Spatial activation — simulated, perceived and presented regions

**Domain:** Chunk activation/retirement and world-to-HeroView data flow. **Status:** Planning design; distances and budgets uncommitted.

## Principle

**The world required for a believable experience must exist before it is rendered.** FloraSim and FaunaSim instantiate organisms when **simulation regions** activate, not only at the renderer's request. Simulation radius must cover Smalltrotter's immediate surroundings and a buffer around the entire **bounded HeroView camera envelope**, while keeping cost bounded.

The map itself, persistent botanical state, and regional fauna populations remain available at coarse scale beyond activated chunks. There is no requirement to individually simulate every distant animal or tiny plant.

## Separate spatial interests

| Region | Anchor(s) | Primary purpose |
|---|---|---|
| **Active simulation** | Hero position, bounded camera envelope, route/hazard lookahead | Locally instantiate/advance plants and wildlife so encounters are already underway |
| **Hero perception** | Smalltrotter's body, senses, attention, physical occlusion | Determine what she actually detects and reacts to |
| **Render visibility** | Camera frustum, distance, visibility/LOD | Display scenery, flora, fauna and atmospheric effects the *player* sees |
| **Coarse world** | Regional map/population and environmental history | Habitat distributions and resources for inactive areas |

These areas **overlap but are not identical**. Hearing and weather events can extend beyond sight. Distant mountains/sea can render using low-detail geometry beyond active fauna simulation. The detached camera may see over a nearby ridge without Smalltrotter perceiving what is there.

## SimCore activation policy

Maintain an activity footprint derived from:
1. Smalltrotter's body position and a minimum safety/interaction radius.
2. The camera's *entire allowed local tether envelope*, not only its current frustum; prewarm regions near envelope edges.
3. Sensory/hazard lookahead, movement speed, navigation and upcoming camera motion.
4. A hysteresis margin and grace time to prevent thrashing when crossing chunk borders.

When possible, prioritize available resources: **HeroSim and physical contact first**, then active nearby fauna, needed flora and anticipation, then less relevant ambient individuals. Do not introduce a separate per-frame biome sim to fill the area.

A camera can't outrun fauna activation at a ridge crest without some quality fallback; prefetch/budget ahead of time, and if necessary show distant static proxies instead of suddenly generating an entire herd inside the view.

## FloraSim region instantiation

On simulation-region activation, FloraSim reconstructs **the botanical state that should exist there now** from:
- Species distributions/habitat suitability and stable map seeds.
- Persistent individual trees, durable important plants, past interactions and patches in RaukenState.
- RaukenSim accumulated season/weather histories since their last evaluation.

It returns organism or population-patch snapshots **as a spatial batch**, not per-plant renderer polling. The visible area can then render all appropriate plant instances, including thousands of blades/fronds derived from patch descriptions without giving every blade an individual biology record.

On deactivation, retain botanical truth/history, discard costly active representation, and do not reset trees when the player returns. Plant state is independent of camera and view.

## FaunaSim region instantiation

Before an activation, a region can have **only** population/cohort descriptions and habitat activity expectations: what species, broad abundances and age classes plausibly occur. Animals have **no mandatory pre-existing personal identities**.

Upon region activation:
- Reserve a budget/count from appropriate local population cohorts.
- Instantiate currently relevant individuals, with anatomical variation and lightweight current state/behavior.
- Let them browse, rest, bask, watch, yawn, scratch, avoid hazards and pursue motivated actions *before* player or camera sees them.
- Most animals are **transient** and retire back into the population when no longer needed.
- **Long-term individual retention is narrowly limited to already-instantiated, mature members of designated largest species** (and only if retained by policy); no island-wide generation of individual adult giants to populate a database.
- Retained giants only need compact identity, age/size, distinctive appearance, coarse condition and approximate reappearance eligibility/location; no daily route, memory or ongoing personal biography.
- Recently disturbed/encountered locations may keep coarse cooldown/occupancy data to prevent instant identical respawns, not per-animal diaries.

**Dolores example:** If Smalltrotter never goes anywhere near the relevant Rainridge habitat, Dolores need not exist as a simulated individual at all. A regional constrictor population is sufficient. If a suitable adult is instantiated when the local region becomes active, that individual *may* earn retention; its identity isn't simulated in advance because its species is large.

Keep cohort accounting consistent when animals are added/retired. Biological conditions (satiety, fatigue, thermal comfort, stress, pain) guide local behavior without costly full individual memory/schedules.

## HeroSim and HeroView

HeroSim should receive *usable environmental stimuli* and a spatial/physical view from the domain sims: what Smalltrotter can see/hear/smell/touch, not all internal biological state of every nearby creature. It interprets them through BeastCore. HeroView receives HeroSim's body/experience output, and independently obtains renderable world chunks from the streamer.

HeroView's camera is bounded to a local tether anchored to Smalltrotter, so the required active fauna/flora footprint can be deliberately sized. Camera flight never grants HeroSim sensory access to unseen wildlife.

## Transition lifecycle

1. **Prewarm:** asynchronously/selectively prepare likely adjacent simulation chunks, based on hero movement and the bounded camera.
2. **Activate:** FloraSim bulk advances plant state; FaunaSim instantiates wildlife from local cohorts; scenery/physics access prepared.
3. **Run:** active animals have multirate response, ordinary local behaviors and interactions; plants receive events and deferred progress, not per-frame ticking.
4. **Present:** HeroView requests camera-visible chunks independently; renderer consumes domain-provided snapshots.
5. **Retire:** transient animals return to cohorts; qualifying instantiated mature giants may retain compact records; FloraSim saves/checkpoints plant changes; visual proxies discard.
6. **Catch up:** when revisited, advance weather/plant/population aggregates to current time and reconstruct without duplication.

The steps are conceptual, not a required blocking main-thread pipeline. Large batch instantiation and retirement must be spread across frames or async jobs within measured budgets.

## Acceptance

- Camera peeks over a nearby ridge to find wildlife already resting/browsing, not reacting only because it was drawn.
- A background population on another island has no list of invented individually named adults.
- Instantiating, retiring and revisiting a region does not double animal counts or reset a damaged tree.
- Camera movement doesn't cause the animal to acquire new senses.
- Wildlife stays active briefly when hidden or crossing frustum edges; moving renderer chunks never directly retires FaunaSim individuals.
- 1080p GTX 1080 benchmark reports both activation spikes and graphics/CPU costs; exact activation distances remain tunable.

Related: [HeroView](hero-view.md), [FloraSim](flora-sim.md), [FaunaSim](fauna-sim.md), [Simulation architecture](simulation-architecture.md).
