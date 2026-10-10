# Spatial activation — simulated, perceived and presented regions

**Domain:** Chunk activation/retirement and world-to-HeroView data flow. **Status:** Planning design; distances and budgets uncommitted.

## Principle

**The world required for a believable experience must exist before it is rendered.** FloraSim and FaunaSim instantiate organisms when **simulation regions** activate, not only at the renderer's request. Simulation radius must cover the Hero Beast's immediate surroundings and a buffer around the entire **bounded HeroView camera envelope**, while keeping cost bounded.

The map itself, persistent botanical state, and regional fauna populations remain available at coarse scale beyond activated chunks. There is no requirement to individually simulate every distant animal or tiny plant.

## Separate spatial interests

| Region | Anchor(s) | Primary purpose |
|---|---|---|
| **Active simulation** | Hero position, bounded camera envelope, route/hazard lookahead | Locally instantiate/advance plants and wildlife so encounters are already underway |
| **Hero perception** | the Hero Beast's body, senses, attention, physical occlusion | Determine what she actually detects and reacts to |
| **Render visibility** | Camera frustum, distance, visibility/LOD | Display scenery, flora, fauna and atmospheric effects the *player* sees |
| **Coarse world** | Regional map/population and environmental history | Habitat distributions and resources for inactive areas |

These areas **overlap but are not identical**. Hearing and weather events can extend beyond sight. Distant mountains/sea can render using low-detail geometry beyond active fauna simulation. The detached camera may see over a nearby ridge without the Hero Beast perceiving what is there.

## SimCore activation policy

Maintain an activity footprint derived from:
1. the Hero Beast's body position and a minimum safety/interaction radius.
2. The camera's *entire allowed local tether envelope*, not only its current frustum; prewarm regions near envelope edges.
3. Sensory/hazard lookahead, movement speed, navigation and upcoming camera motion.
4. A hysteresis margin and grace time to prevent thrashing when crossing chunk borders.

When possible, prioritize available resources: **HeroSim and physical contact first**, then active nearby fauna, needed flora and anticipation, then less relevant ambient individuals. Do not introduce a separate per-frame biome sim to fill the area.

A camera can't outrun fauna activation at a ridge crest without some quality fallback; prefetch/budget ahead of time, and if necessary show distant static proxies instead of suddenly generating an entire herd inside the view.

## Bounded reconciliation and readiness

Prewarming is a **work queue with a budget**, not an instruction to instantiate an entire valley synchronously. Track region biological timestamp, region/content version, last committed event cursor and per-stage readiness:

1. **Dormant:** generated maps, persistent ecological records and cohort/resource summaries only.
2. **Reconciled:** FloraSim/FaunaSim aggregate consequences advanced to a known world-time checkpoint.
3. **Locally active:** appropriate organisms and immediate behaviors loaded where interactions/senses may occur.
4. **Presented:** requested camera geometry, animation and audio resources ready at specific LOD.

Readiness levels may overlap and are not mandatory one-way lifecycle states. Rendering may draw low-detail distant scenery well outside active fauna simulation, but never fabricate an active animal in an unreconciled region merely because the camera rotated.

**Work policy:** SimCore prioritizes bodily collision/perception and urgent local interactions, then regions approaching the Hero Beast or the reachable HeroView camera envelope, then background ecological catch-up and decorative preparation. Bound reconciliation jobs by measured CPU work/step and total queued memory. Amortize large plant cohorts, old damage journals and fauna activation over multiple jobs; maintain region version/timestamp so stale job results cannot overwrite newer changes.

Activation hysteresis and predicting camera motion help, but the camera may reach a ridge before high-detail work finishes. Have a graceful fallback: display a **consistent cheaper snapshot/proxy** if available, with committed damage/depletion respected, and refine as soon as ready. No forced synchronous multi-year catch-up on camera turning and no visible creature popping into existence in the current frustum. Tether distance and work margins must be tuned together.

**Causal work is not distance-only:** even dormant regional populations periodically or lazily settle consequential forage consumption, demographic changes and environmental histories. Individual movement/animation is unnecessary for those settlements. Avoid a general-purpose importance-scoring engine; simple domain queues and deadlines are enough.

## FloraSim region instantiation

On simulation-region activation, FloraSim reconstructs **the botanical state that should exist there now** from:
- Species distributions/habitat suitability and stable map seeds.
- Persistent individual trees, durable important plants, past interactions and patches in StalthosState.
- StalthosSim accumulated season/weather histories since their last evaluation.

It returns organism or population-patch snapshots **as a spatial batch**, not per-plant renderer polling. The visible area can then render all appropriate plant instances, including thousands of blades/fronds derived from patch descriptions without giving every blade an individual biology record.

On deactivation, retain botanical truth/history, discard costly active representation, and do not reset trees when the player returns. Plant state is independent of camera and view.

## FaunaSim region instantiation

Before an activation, a region can have **only** population/cohort descriptions and habitat activity expectations: what species, broad abundances and age classes plausibly occur. Animals have **no mandatory pre-existing personal identities**.

Upon region activation:
- Reserve a budget/count from appropriate local population cohorts.
- Instantiate currently relevant individuals, with anatomical variation and lightweight current state/behavior.
- Let them browse, rest, bask, watch, yawn, scratch, avoid hazards and pursue motivated actions *before* player or camera sees them.
- Most animals are **transient** and retire back into the population when no longer needed.
- **Long-term individual retention is limited to already-instantiated animals with justified ongoing identity**, including bonded Reedcrest peers, dependent Longstride young/caregivers and selected notable mature giants. Never pre-generate an archipelago-wide personal wildlife registry.
- Retained individuals need compact identity, age/size, distinctive appearance, condition, broad whereabouts and only relevant social/dependent ties; coarse world-time advancement happens before reactivation. Death, dispersal and identity decay remain possible.
- Recently disturbed/encountered locations may keep coarse cooldown/occupancy data to prevent instant identical respawns, not per-animal diaries.

**Dolores example:** If the Hero Beast never goes anywhere near the relevant Rainridge habitat, Dolores need not exist as a simulated individual at all. A regional constrictor population is sufficient. If a suitable adult is instantiated when the local region becomes active, that individual *may* earn retention; its identity isn't simulated in advance because its species is large.

Keep cohort accounting consistent when animals are added/retired. Biological conditions (satiety, fatigue, thermal comfort, stress, pain) guide local behavior without costly full individual memory/schedules.

## HeroSim and HeroView

HeroSim should receive *usable environmental stimuli* and a spatial/physical view from the domain sims: what the Hero Beast can see/hear/smell/touch, not all internal biological state of every nearby creature. It interprets them through BeastCore. HeroView receives HeroSim's body/experience output, and independently obtains renderable world chunks from the streamer.

HeroView's camera is bounded to a local tether anchored to the Hero Beast, so the required active fauna/flora footprint can be deliberately sized. Camera flight never grants HeroSim sensory access to unseen wildlife.

## Transition lifecycle

1. **Prewarm:** asynchronously/selectively prepare likely adjacent simulation chunks, based on hero movement and the bounded camera.
2. **Activate:** FloraSim bulk advances plant state; FaunaSim instantiates wildlife from local cohorts; scenery/physics access prepared.
3. **Run:** active animals have multirate response, ordinary local behaviors and interactions; plants receive events and deferred progress, not per-frame ticking.
4. **Present:** HeroView requests camera-visible chunks independently; renderer consumes domain-provided snapshots.
5. **Retire:** transient animals return to cohorts; qualifying already-instantiated companions, dependent young and notable wildlife may retain compact records while warranted; FloraSim saves/checkpoints plant changes; visual proxies discard.
6. **Catch up:** when revisited, including by later playable lives, advance weather/plant/population aggregates **and eligible retained individuals** to current time, then reconstruct without duplication or revival of the dead.

The steps are conceptual, not a required blocking main-thread pipeline. Large batch instantiation and retirement must be spread across frames or async jobs within measured budgets.

## Follower movement and world continuity

A Hero Beast's death does not purge warmed regions, invalidate nests or delete prior companions. The next hatchling activates its own surroundings through normal scheduling. Previously instantiated retained individuals elsewhere remain only if their coarse timestamped state warrants it, and can be reactivated when the new player approaches suitable areas. Crossing cliffs, channels or islands is a physically negotiated action for each Reedcrest companion or Longstride youngster; simply following the player or its parent never teleports an animal into place. Once an animal's individual identity expires, cohort state remains truthful without double population accounting.

## Acceptance

- Camera peeks over a nearby ridge to find wildlife already resting/browsing, not reacting only because it was drawn.
- A background population on another island has no list of invented individually named adults.
- Instantiating, retiring and revisiting a region does not double animal counts or reset a damaged tree.
- Camera movement doesn't cause the animal to acquire new senses.
- Wildlife stays active briefly when hidden or crossing frustum edges; moving renderer chunks never directly retires FaunaSim individuals.
- 1080p GTX 1080 benchmark reports both activation spikes and graphics/CPU costs; exact activation distances remain tunable.

Related: [HeroView](hero-view.md), [FloraSim](flora-sim.md), [FaunaSim](fauna-sim.md), [Simulation architecture](simulation-architecture.md).
