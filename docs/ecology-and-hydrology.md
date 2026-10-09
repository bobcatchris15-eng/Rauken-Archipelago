# Ecology, climate, hydrology and persistence

**Domain:** Physical and biological world processes. **Status:** System design hypotheses, not tuned equations.

## World model

Create one consistent world state that generates both ecological resources and visual representations. Avoid parallel 'ecology spreadsheet' and 'decorative foliage' that disagree.

Causal chain: **geology → relief/substrate → exposure/drainage/water → soils/microclimate → plants → consumers/decomposers → disturbance and succession**.

Biomes are descriptive landscape assemblages, not abrupt boundaries. Habitat suitability emerges from continuous variables, including sunlight, temperature, rainfall, soil depth, moisture and chemistry, salinity, wind shelter, slope and disturbance.

## Climate

- Broadly warm, Late Cretaceous-inspired seasonal regime; local rain shadows, upland mist and sheltered ravine microclimates.
- Wet and dry seasons, with year-to-year anomalies; storms localized by weather patterns, not triggered by player proximity.
- Track coarse-grid temperature, rainfall, solar exposure, humidity, wind, cloud and evaporation.
- Microclimate from canopy, slope aspect, rock exposure, proximity to water, cold/moist air drainage and salt spray.
- Fog and dampness can be plausible in Rainridge valleys; exposed Outer Reach plateaus contrast with spring-fed basins.

## Hydrology

Separate **catchment water balance** from visible water-surface rendering:
- Watershed graph and contributing area.
- Precipitation → infiltration / storage / evaporation / runoff.
- Groundwater/springs and coarse aquifer storage.
- River reaches with discharge, water level, velocity class and channel connectivity.
- Floodplain storage, seasonal ponds, saturated ground and wetland cells.
- Coast tides, storm setup and salinity intrusion in lower streams and brackish pools.
- Terrain/sediment change as infrequent event/geomorphology updates; do not run full free-surface CFD across all islands.

Some streams are permanent and spring-fed; others flow only after rain. Water is a resource with **depth, access, freshness, current and contamination risk**, not just a blue material.

Failure cases to test: rain upstream creates dangerous flash flood downstream; a dry season separates pools; tidal creeks become brackish; water appears at plausible permeable/impermeable contacts; steep slopes drain and low depressions retain moisture.

## Soil, substrates and plants

Each region has substrate texture/chemistry, soil thickness, drainage and organic matter. Mineral-rich Outer Reach soils may strongly constrain plant adaptations. Limestone Stone Island soils and karst hydrology vary sharply at small scales.

Plant individuals or population patches track:
- Identity/functional group and phenology.
- Establishment requirements and growth potential.
- Edible standing biomass by accessible layer/type.
- Age, stress, damage, browsing history, death and decomposition.
- Reproductive output and propagule dispersal at coarse resolution.
- Response to canopy shade, competition, drought, flood and physical disturbance.

Persistent prominent trees and conspicuous plants keep identities. Low ground vegetation may be regenerated from population-state patches and deterministic seeds.

## Food webs

Animals do not spawn only because the player is nearby. Maintain plausible populations and home ranges for herbivores, opportunists, predators and decomposers.

Broad ecology groups: primary producers, browsers/grazers, insectivores/omnivores, terrestrial or shoreline predators, carrion users, detritivores, soil/fungal decomposers, pollinators and seed dispersers.

A low-detail ecological population may be simulated statistically offscreen; locally observed or individually notable animals become detailed entities while preserving continuity.

Predation matters, but hunger, dehydration, flood, terrain, infection and accidental interactions should more frequently threaten the player.

## Seasonal processes and disturbance

- Seasonal shoot growth, plant dormancy/stress, fruiting and shedding.
- Flood scour and sediment deposition; changed river crossings.
- Drought-driven changes in usable forage and drinking locations.
- Storm windthrow, landslips, branchfall, decay and colonization.
- Local browsing creates recognizable depletion and possibly bushier regrowth where biologically reasonable.
- Dead vegetation becomes litter, wood and microbial/fungal substrate; nutrients recycle.

Major storms and geomorphic changes are **occasional**; don't oscillate the whole map rapidly for visual drama. Familiarity relies on persistence.

## Scale and performance

Four linked simulation tiers (suggested, subject to measured CPU cost):
1. **Immediate:** visible animals/plants, interaction volumes, water contact, gait and feeding.
2. **Nearby:** individual significant organisms, patch resources, animal routes, short-interval water state.
3. **Regional:** soil/climate water balance, plant cohorts, populations and major habitat transitions.
4. **Distant:** coarse aggregates for islands with little or no player observation, advancing consistently with elapsed time.

Use event scheduling, low-frequency growth/accounting and deterministic spatial seeds. Separate render-chunk rebuild from ecological updates; batch many plant changes rather than one mesh rebuild per bite.

Don't equate offscreen simplification with resetting resources. Return visits should show plausible consequences.

## Tests and measures

- Ecological viability for the flagship juvenile throughout a normal seasonal cycle in a local watershed.
- Regional water balance without unexplained permanent ponds or absurd flood magnitudes.
- Food patches recover at appropriate timescales and browsing leaves visible traces.
- An island changes in player's absence without hitches on revisit.
- Conditions determine wildlife distributions; never hardcode predatory ambushes to player location.
- Instrument per-tick CPU, save/load cost, memory and local detail promotion/demotion.

Cross-references: [Flora](flora.md), [Creatures](creatures.md), [Gameplay](gameplay.md), [World generation](world-generation.md).
