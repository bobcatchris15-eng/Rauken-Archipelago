# Ecology and hydrology — shared ecological principles

**Domain:** Interactions among terrain, water, living systems and disturbance. **Status:** Revised planning direction. Ownership is defined in [Simulation architecture](simulation-architecture.md) and its domain documents.

## World model

Create one persistent ecological reality with **RaukenState** storing identities/history and the domain simulations owning their facts. The renderer is a consumer, not an alternate source of biological truth.

Causal chain: **geology → relief/substrate → exposure/drainage/water → soils/microclimate → plants → consumers/decomposers → disturbance and succession**.

Biomes are descriptive landscape assemblages, not abrupt boundaries. Habitat suitability emerges from continuous variables, including sunlight, temperature, rainfall, soil depth, moisture and chemistry, salinity, wind shelter, slope and disturbance.

## Climate

- Broadly warm, Late Cretaceous-inspired seasonal regime; local rain shadows, upland mist and sheltered ravine microclimates.
- Wet and dry seasons, with year-to-year anomalies; storms localized by weather patterns, not triggered by player proximity.
- Track coarse-grid temperature, rainfall, solar exposure, humidity, wind, cloud and evaporation.
- Microclimate from canopy, slope aspect, rock exposure, proximity to water, cold/moist air drainage and salt spray.
- Fog and dampness can be plausible in Rainridge valleys; exposed Outer Reach plateaus contrast with spring-fed basins.

## Hydrology — primarily a map property

Watercourses, springs, permanent ponds, aquifer-influenced zones, wetlands, soil drainage and floodplain shapes are **authored or generated with the map** and remain geographically stable across ordinary game years. Distance from freshwater informs flora distribution, but must combine with **relative height above water**, soil permeability, shade, slope and baseline rainfall. Expose these as precomputed environmental suitability/moisture fields.

**RaukenSim** owns day/night, seasons, regional weather, current wetness and exceptional storms/floods. Storms temporarily raise river levels and inundate **known flood-prone terrain**, then recede. Avoid continuous groundwater storage/pressure/transport simulation, channel erosion, riverbed remodeling and full fluid dynamics.

Available water still has accessibility, depth, salt content, temperature and approximate current; a wet-looking inlet is not automatically drinkable. Rainfall history may influence botanical growth without actually moving terrain.

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
- Temporary floodwater across established channels/floodplains; a crossing may become unsafe and later recover.
- Drought-driven changes in usable forage and drinking locations.
- Storm windthrow, landslips, branchfall, decay and colonization.
- Local browsing creates recognizable depletion and possibly bushier regrowth where biologically reasonable.
- Dead vegetation becomes litter, wood and microbial/fungal substrate; nutrients recycle.

Most terrain remains fixed. Major storms may cause discrete treefall, debris or rare local rockfall, but should not progressively remake riverbeds. Familiarity relies on persistence.

## Scale and performance

Separate *rendering* from *simulation* fidelity. **HeroSim** maintains full responsive physiology; **FaunaSim** uses active multirate nearby animals and coarse offscreen populations, all with shared **BeastCore** rules. **FloraSim** advances individual trees and population patches lazily using RaukenSim's stored environmental interval summaries and discrete events. **SimCore** coordinates global time and scheduling; **RaukenState** preserves identities and history. **InteractionsCore** validates cross-domain resource transfers and damage.

Use event scheduling, low-frequency growth/accounting and deterministic spatial seeds. Separate render-chunk rebuild from ecological updates; batch many plant changes rather than one mesh rebuild per bite.

Don't equate offscreen simplification with resetting resources. Return visits should show plausible consequences.

## Tests and measures

- Ecological viability for the flagship juvenile throughout a normal seasonal cycle in a local watershed.
- Regional water balance without unexplained permanent ponds or absurd flood magnitudes.
- Food patches recover at appropriate timescales and browsing leaves visible traces.
- An island changes in player's absence without hitches on revisit.
- Conditions determine wildlife distributions; never hardcode predatory ambushes to player location.
- Instrument per-tick CPU, save/load cost, memory and local detail promotion/demotion.

Cross-references: [Architecture](simulation-architecture.md), [RaukenSim](rauken-sim.md), [FloraSim](flora-sim.md), [FaunaSim](fauna-sim.md), [HeroSim](hero-sim.md), [World generation](world-generation.md).
