# Spatial activation — simulated, perceived and presented regions

**Domain:** Chunk activation/retirement and world-to-HeroView data flow. **Status:** Planning design; distances and budgets uncommitted.

## Principle

**The world required for a believable experience must be *staged* before rendering.** FloraSim prepares plants and FaunaSim nearby animals when local regions activate, not when a camera turns toward them. Simulation radius must cover the Hero Beast's immediate surroundings and a buffer around the entire **bounded HeroView camera envelope**, while keeping cost bounded.

The map itself, persistent botanical state, and regional fauna populations remain available at coarse scale beyond activated chunks. There is no requirement to individually simulate every distant animal or tiny plant.

## Separate spatial interests

| Region | Anchor(s) | Primary purpose |
|---|---|---|
| **Active simulation** | Hero position, bounded camera envelope, route/hazard lookahead | Locally instantiate/advance plants and wildlife so encounters are already underway |
| **Hero perception** | the Hero Beast's body, senses, attention, physical occlusion | Determine what she actually detects and reacts to |
| **Render visibility** | Camera frustum, distance, visibility/LOD | Display scenery, flora, fauna and atmospheric effects the *player* sees |
| **Coarse world** | Habitat profiles, approximate abundance and visible saved exceptions | Cheap plausible state for inactive areas |

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

The objective is **fast, seamless staging**, not historical biological reconstruction. Use a small bounded work queue to prepare local habitat appearance and simple acting fauna before the Hero Beast or full detached camera envelope can expose them.

Practical levels:
1. **Remote:** static terrain/habitat, approximate species density, seasonal parameters and saved conspicuous exceptions.
2. **Prepared nearby:** plants and lightweight animals generated from current region/season and seeds, with known individual/tree exceptions applied.
3. **Active/presented:** nearby animals respond and move; detailed geometry/animation follows camera needs independently.

Reject stale async results if an observable change (e.g., browse damage or a fallen tree) superseded them. **No chronological weather replay, exact remote population settlement or multi-century plant reconciliation.** A simple seed + season + elapsed-time snapshot works for ordinary regions.

Prewarm beyond occluding ridges and keep brief occupancy hysteresis to avoid wildlife materializing when a camera turns. A consistent low-detail proxy is preferable to a synchronous load spike. Rendering never controls animal existence or grants HeroSim extra knowledge.

## FloraSim region instantiation

On simulation-region activation, FloraSim reconstructs **the botanical state that should exist there now** from:
- Habitat suitability and stable map seeds.
- Saved conspicuous tree/plant changes and coarse patches in StalthosState.
- StalthosSim current season and inexpensive elapsed-time recovery.

It returns organism or population-patch snapshots **as a spatial batch**, not per-plant renderer polling. The visible area can then render all appropriate plant instances, including thousands of blades/fronds derived from patch descriptions without giving every blade an individual biology record.

On deactivation, retain conspicuous botanical exceptions, discard costly active representation, and do not reset familiar damaged trees when the player returns. Plant state is independent of camera and view.

## FaunaSim region instantiation

Before an activation, a region can have **only** population/cohort descriptions and habitat activity expectations: what species, broad abundances and age classes plausibly occur. Animals have **no mandatory pre-existing personal identities**.

Upon region activation:
- Sample plausible local wildlife abundance from regional density, excluding known active/retained individuals.
- Instantiate currently relevant individuals, with anatomical variation and lightweight current state/behavior.
- Let them browse, rest, bask, watch, yawn, scratch, avoid hazards and pursue motivated actions *before* player or camera sees them.
- Most animals are **transient** and retire into approximate regional occupancy without exact cohort settlement.
- **Long-term individual retention is limited to already-instantiated animals with justified ongoing identity**, including bonded Reedcrest peers, dependent Longstride young/caregivers and selected notable mature giants. Never pre-generate an archipelago-wide personal wildlife registry.
- Retained individuals need compact identity, age/size, distinctive appearance, condition, broad whereabouts and only relevant social/dependent ties; coarse world-time advancement happens before reactivation. Death, dispersal and identity decay remain possible.
- Recently disturbed/encountered locations may keep coarse cooldown/occupancy data to prevent instant identical respawns, not per-animal diaries.

**Dolores example:** If the Hero Beast never goes anywhere near the relevant Rainridge habitat, Dolores need not exist as a simulated individual at all. A regional constrictor population is sufficient. If a suitable adult is instantiated when the local region becomes active, that individual *may* earn retention; its identity isn't simulated in advance because its species is large.

Keep known animal identities and visible occupancy consistent when animals are added/retired; exact unseen demographic balance is unnecessary. Biological conditions (satiety, fatigue, thermal comfort, stress, pain) guide local behavior without costly full individual memory/schedules.

## HeroSim and HeroView

HeroSim should receive *usable environmental stimuli* and a spatial/physical view from the domain sims: what the Hero Beast can see/hear/smell/touch, not all internal biological state of every nearby creature. It interprets them through BeastCore. HeroView receives HeroSim's body/experience output, and independently obtains renderable world chunks from the streamer.

HeroView's camera is bounded to a local tether anchored to the Hero Beast, so the required active fauna/flora footprint can be deliberately sized. Camera flight never grants HeroSim sensory access to unseen wildlife.

## Transition lifecycle

1. **Prewarm:** asynchronously/selectively prepare likely adjacent simulation chunks, based on hero movement and the bounded camera.
2. **Activate:** FloraSim prepares seasonal patch appearances; FaunaSim stages plausible local wildlife; scenery/physics access prepared.
3. **Run:** active animals have multirate response, ordinary local behaviors and interactions; plants receive events and deferred progress, not per-frame ticking.
4. **Present:** HeroView requests camera-visible chunks independently; renderer consumes domain-provided snapshots.
5. **Retire:** transient animals return to approximate regional availability; qualifying previously instantiated companions, dependent young and notable wildlife retain compact records; FloraSim saves conspicuous changes; visual proxies discard.
6. **Refresh:** on revisit, build plausible current-season habitat and population from cheap elapsed-time rules, advance eligible retained individuals coarsely and reapply saved exceptions. No long history replay, duplication or resurrection.

The steps are conceptual, not a required blocking main-thread pipeline. Large batch instantiation and retirement must be spread across frames or async jobs within measured budgets.

## Follower movement and world continuity

A Hero Beast's death does not purge warmed regions, invalidate nests or delete prior companions. The next hatchling activates its own surroundings through normal scheduling. Previously instantiated retained individuals elsewhere remain only if their coarse timestamped state warrants it, and can be reactivated when the new player approaches suitable areas. Crossing cliffs, channels or islands is a physically negotiated action for each Reedcrest companion or Longstride youngster; simply following the player or its parent never teleports an animal into place. Once an animal's individual identity expires, coarse regional abundance remains plausible without preserving a perfect population ledger.

## Acceptance

- Camera peeks over a nearby ridge to find wildlife already resting/browsing, not reacting only because it was drawn.
- A background population on another island has no list of invented individually named adults.
- Instantiating, retiring and revisiting a region does not duplicate recognized animals or reset conspicuous plant damage.
- Camera movement doesn't cause the animal to acquire new senses.
- Wildlife stays active briefly when hidden or crossing frustum edges; moving renderer chunks never directly retires FaunaSim individuals.
- 1080p GTX 1080 benchmark reports both activation spikes and graphics/CPU costs; exact activation distances remain tunable.

Related: [HeroView](hero-view.md), [FloraSim](flora-sim.md), [FaunaSim](fauna-sim.md), [Simulation architecture](simulation-architecture.md).
