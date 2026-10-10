# StalthosSim — environmental simulation

**Domain:** Regional environment, weather and transient hazards. **Status:** Conceptual specification.

## Responsibility and authority

StalthosSim produces **shared, approximate environmental state** consumed by FloraSim, FaunaSim, HeroSim and the renderer; it need not be meteorologically exact. SimCore owns the clock; StalthosSim advances its environmental processes on that shared timeline. StalthosState persists its current conditions and compact histories.

## Static, precomputed spatial inputs

World-generation outputs: height, slope/aspect, bedrock/substrate, soil type/drainage, climatological rainfall and heat tendencies, drainage and river network, streams, springs, ponds, stable groundwater influence, water salinity baselines, wetlands, exposure/shelter, canopy potential and floodplain masks.

Distance from water is useful for plant distribution but cannot be the sole moisture rule: account for relative elevation, soil permeability, drainage, shade and local rain. **No detailed underground water simulation at runtime.** Ordinary channel shapes and springs are effectively fixed within the lifespan of the game.

## Dynamic environmental outputs

StalthosSim needs a **small set of presentation/behavior controls** rather than a detailed meteorology model:

- Shared time of day and season (from SimCore); broad regional temperature and rain tendency.
- Coarse, spatially coherent weather state: sunny/overcast/raining/storming, wind, approximate temperature and dampness. Smoothly interpolate appearance; no atmospheric fluid solve.
- Static climate, terrain shelter and canopy masks add cheap local variations so a ravine looks wetter than its ridge.
- Known waterways and floodplain masks gain a simple temporary level/unsafe-crossing state. Brackish/saltwater remains unsuitable for drinking.
- Rare **consequential events** (e.g. damaging storm, river crossing flooded, tree knocked down) may be kept as small saved exceptions if they affect visible outcomes.

Only expose extra variables when a specific visual effect, navigation decision or creature behavior genuinely uses them. The renderer gets the current presentation state; FloraSim/FaunaSim/HeroSim may consume coarse condition values without requiring scientific heat or water budgets.
## Storms and floods

Use weather intensity, regional antecedent wetness and **precomputed drainage/flood masks** to raise water temporarily along known channels, banks and low-ground overflow paths. The result influences traversability, drowning/injury, flora stress and rendered water.

The expensive simulations to **avoid**: per-frame hydrodynamics across the archipelago, riverbed incision, aquifer pressure solves, detailed sediment advection and continuous geomorphic replacement. Rare authored/triggered rockfall or deadwood fall is a discrete physical/ecological change, not an erosion system.

## Consumption contracts

- **FloraSim**: baseline suitability, current season/wetness tendency and specific persistent damage outcomes for cheap growth/appearance updates.
- **FaunaSim**: local thermal, water, visibility and wind conditions for behavior and population risks at variable cadence.
- **HeroSim**: more frequent sampling for thermal comfort, exposure and nearby water safety.
- **Renderer**: cached sun, clouds, wind fields, rain, wetness, stream/flood state. The renderer may interpolate appearance each frame but cannot decide whether rainfall occurred.
- **BeastCore**: receives environmental values through its owners; does not query weather omnisciently to select actions.

## History and bounded cost

For inactive regions, store little more than a seed, current season/region state, last coarse update time and occasional **persistent event outcomes**. When revisited, advance vegetation variants and habitat/population tendencies with elapsed-time rules. A dry season may reduce greenery; an explicitly saved storm-destroyed tree remains destroyed.

**Do not reconstruct an exact historical sequence of heat, rainfall, drought or flood intervals for normal background ecology.** No long event journal, per-species climate-integral cache or reference-counted weather history. If an unusual event is observable and lasting, store its *result* or a small timestamped exception directly. Favor a stable current scene over numerically reconstructing its invisible past.
## Ordered interval-and-event history contract

**Superseded by the display-first decision.** The previous requirement to preserve chronological weather intervals for every plant/region is not part of the baseline design.

Use simple seasonal condition curves, a coarse weather event generator, optional bounded drought/wetness flags and occasional persisted damaging-event outcomes. Two unvisited regions with identical current season and habitat data may legitimately resolve to the same vegetation state even if their imagined rainfall histories differ. They need only differ when a previously visible or consequential exception demands it.

During a rest/time skip, evaluate meaningful active-region dangers and established persistent events at coarse checkpoints; never replay a hidden century of weather frames. Add chronology only if a concrete visual/gameplay test exposes an obvious contradiction that cannot be solved by one or two cheap flags.
## Test cases

1. Windward Rainridge wet, sheltered lee drier, without hard biome seams.
2. Spring-fed Main Island ravine supports wetter habitat than adjacent ridge despite similar rainfall.
3. Storm raises water on established floodplain; land and stream return close to previous state afterward.
4. FloraSim can advance 100 days from season, coarse weather tendency and saved exceptions at bounded cost; no ordered rainfall reconstruction required.
5. Quiescent years do not rearrange gullies/stream courses.
6. Renderer, HeroSim and FloraSim agree about the same rain and soil-moisture episode.

Related: [World generation](world-generation.md), [Ecology](ecology-and-hydrology.md), [Architecture](simulation-architecture.md).
