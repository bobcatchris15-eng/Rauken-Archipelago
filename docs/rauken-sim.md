# RaukenSim — environmental simulation

**Domain:** Regional environment, weather and transient hazards. **Status:** Conceptual specification.

## Responsibility and authority

RaukenSim produces the **environmental truth consumed by FloraSim, FaunaSim, HeroSim and the renderer**. SimCore owns the clock; RaukenSim advances its environmental processes on that shared timeline. RaukenState persists its current conditions and compact histories.

## Static, precomputed spatial inputs

World-generation outputs: height, slope/aspect, bedrock/substrate, soil type/drainage, climatological rainfall and heat tendencies, drainage and river network, streams, springs, ponds, stable groundwater influence, water salinity baselines, wetlands, exposure/shelter, canopy potential and floodplain masks.

Distance from water is useful for plant distribution but cannot be the sole moisture rule: account for relative elevation, soil permeability, drainage, shade and local rain. **No detailed underground water simulation at runtime.** Ordinary channel shapes and springs are effectively fixed within the lifespan of the game.

## Dynamic environmental outputs

- Global solar/day-night time and seasonal phase as derived from SimCore.
- Spatially coherent weather cells: air temperature, wind, rainfall, humidity, cloud, visibility.
- Local modifiers: hill shading, windward/leeward exposure, canopy shelter, evaporative wetness.
- Wetness, approximate soil-moisture modifier and temporary surface conditions.
- Rivers/pools at typical seasonal level; storm-driven rise and decline where mapped.
- Water depth, current class, salinity and accessibility flags for biological and traversal requests.
- Events: storm front, exceptional wind, prolonged dry spell, heavy rain, flood/high tide where warranted.

The environment may appear dynamic without moving the terrain or resimulating erosion.

## Storms and floods

Use weather intensity, regional antecedent wetness and **precomputed drainage/flood masks** to raise water temporarily along known channels, banks and low-ground overflow paths. The result influences traversability, drowning/injury, flora stress and rendered water.

The expensive simulations to **avoid**: per-frame hydrodynamics across the archipelago, riverbed incision, aquifer pressure solves, detailed sediment advection and continuous geomorphic replacement. Rare authored/triggered rockfall or deadwood fall is a discrete physical/ecological change, not an erosion system.

## Consumption contracts

- **FloraSim**: baseline suitability + accumulated heat/moisture/season/exceptional event history for lazy growth and mortality.
- **FaunaSim**: local thermal, water, visibility and wind conditions for behavior and population risks at variable cadence.
- **HeroSim**: more frequent sampling for thermal comfort, exposure and nearby water safety.
- **Renderer**: cached sun, clouds, wind fields, rain, wetness, stream/flood state. The renderer may interpolate appearance each frame but cannot decide whether rainfall occurred.
- **BeastCore**: receives environmental values through its owners; does not query weather omnisciently to select actions.

## History and bounded cost

Provide interval summaries: temperature/rain accumulation, drought duration, degree-hours in suitable conditions, flood exposure and major event timestamps. Use coarse spatial grids and deterministic event seeds. Save/checkpoint history in RaukenState. Unobserved weather still advances on the world clock; plant growth can catch up later.

## Ordered interval-and-event history contract

**A precipitation sum is not a plant-growth history.** Two regions can receive the same total rain but differ sharply if one has an extended drought then a flood. RaukenSim must preserve enough **sequence** for downstream simulation, without recording every weather frame.

Represent regional history chronologically as compact intervals:
- Interval start/end, season/solar phase and starting relevant wetness/thermal condition.
- Rainfall total and intensity class; representative temperature with minima/maxima and accumulated growing degree-time.
- Heat/cold threshold exposure, soil moisture stress and **longest uninterrupted dry/wet spells**, saturation duration.
- Approximate peak wind/flood depth/current, duration above damaging thresholds and any persistent hazard flags.
- Distinct timestamped exceptional events, e.g. storm damage, inundation onset/peak/recession, rare windthrow or fire if present.

**Split intervals whenever chronology changes the answer**—especially drought onset/break, flooding, seasonal transitions and damage thresholds. A single interval cannot replace drought-then-flood with averaged conditions. Evaluate long histories **in order**, using coarse analytic integration within stable stretches and precise handling at event boundaries. Species/soil threshold logic lives in FloraSim; RaukenSim supplies sufficient measurements/events, not a separate history per plant.

Keep the history as shared **region or climate-cell** records in RaukenState, plus event IDs to prevent double application. Use snapshots/checkpoints and a per-consumer reconciliation watermark (or equivalent safe reference bound) before compaction: never delete an event an unevaluated tree/patch still needs. Exact interval length, number of fields and retention policy must be benchmarked against reconstruction fidelity and save size.

## Test cases

1. Windward Rainridge wet, sheltered lee drier, without hard biome seams.
2. Spring-fed Main Island ravine supports wetter habitat than adjacent ridge despite similar rainfall.
3. Storm raises water on established floodplain; land and stream return close to previous state afterward.
4. FloraSim can advance 100 days using **ordered** compact intervals/events without replaying every weather tick; equal rainfall totals but different drought/flood sequences yield different outcomes.
5. Quiescent years do not rearrange gullies/stream courses.
6. Renderer, HeroSim and FloraSim agree about the same rain and soil-moisture episode.

Related: [World generation](world-generation.md), [Ecology](ecology-and-hydrology.md), [Architecture](simulation-architecture.md).
