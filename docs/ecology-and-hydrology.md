# Ecology and hydrology — shared ecological principles

**Domain:** Interactions among terrain, water, living systems and disturbance. **Status:** Revised planning direction. Ownership is defined in [Simulation architecture](simulation-architecture.md) and its domain documents.

## World model

Create one persistent ecological reality with **StalthosState** storing identities/history and the domain simulations owning their facts. The renderer is a consumer, not an alternate source of biological truth.

Causal chain: **geology → relief/substrate → exposure/drainage/water → soils/microclimate → plants → consumers/decomposers → occasional disturbance and lightweight recovery**. This is a guide to plausible appearance and consequences, **not** a commitment to detailed ecosystem succession.

Biomes are descriptive landscape assemblages, not abrupt boundaries. Habitat suitability emerges from continuous variables, including sunlight, temperature, rainfall, soil depth, moisture and chemistry, salinity, wind shelter, slope and disturbance.

## Climate

- Broadly warm, Late Cretaceous-inspired seasonal regime; local rain shadows, upland mist and sheltered ravine microclimates.
- Wet and dry seasons, with year-to-year anomalies; storms localized by weather patterns, not triggered by player proximity.
- Track coarse-grid temperature, rainfall, solar exposure, humidity, wind, cloud and evaporation.
- Microclimate from canopy, slope aspect, rock exposure, proximity to water, cold/moist air drainage and salt spray.
- Fog and dampness can be plausible in Rainridge valleys; exposed Outer Reach plateaus contrast with spring-fed basins.

## Hydrology — primarily a map property

Watercourses, springs, permanent ponds, aquifer-influenced zones, wetlands, soil drainage and floodplain shapes are **authored or generated with the map** and remain geographically stable across ordinary game years. Distance from freshwater informs flora distribution, but must combine with **relative height above water**, soil permeability, shade, slope and baseline rainfall. Expose these as precomputed environmental suitability/moisture fields.

**StalthosSim** owns day/night, seasons, regional weather, current wetness and exceptional storms/floods. Storms temporarily raise river levels and inundate **known flood-prone terrain**, then recede. Avoid continuous groundwater storage/pressure/transport simulation, channel erosion, riverbed remodeling and full fluid dynamics.

Available water still has accessibility, depth, salt content, temperature and approximate current; a wet-looking inlet is not automatically drinkable. Rainfall history may influence botanical growth without actually moving terrain.

## Soil, substrates and plants

Each region has substrate texture/chemistry, soil thickness, drainage and organic matter. Mineral-rich Outer Reach soils may strongly constrain plant adaptations. Limestone Stone Island soils and karst hydrology vary sharply at small scales.

Plant individuals or population patches track:
- Identity/functional group and phenology.
- Establishment requirements and growth potential.
- Edible standing biomass by accessible layer/type.
- Age, stress, damage, browsing history, death and decomposition.
- Coarse establishment/regeneration opportunity where it materially affects habitat appearance; detailed propagule dispersal and individual seedling life histories are not required.
- Coarse response to canopy openness, drought, flooding and physical disturbance; no mandatory individual competition solver.

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
- Occasional storm windthrow, branchfall and rare localized landslips, preserving affected tree identities, deadwood and conspicuous canopy openings.
- Local browsing creates recognizable depletion and possibly bushier regrowth where biologically reasonable.
- Dead vegetation becomes litter, wood and microbial/fungal substrate; nutrients recycle.

Most terrain remains fixed. Major storms may cause discrete treefall, debris or rare local rockfall, but should not progressively remake riverbeds. Familiarity relies on persistence.

**Provisional limit on forest change:** use existing deterministic adult-tree seeds and compact damage/death overrides, plus coarse cover patches that can respond to a canopy opening and occasionally establish new durable trees. The goal is visible, recognizable change across revisits—not a succession, seed-bank, competition or wildfire-spread simulator. Wildfire is a **deferred possibility**, not required scope. Add sophistication only after a simple in-engine demonstration shows a worthwhile appearance/gameplay improvement; see [FloraSim](flora-sim.md).

## Scale and performance

Separate *rendering* from *simulation* fidelity. **HeroSim** maintains full responsive physiology; **FaunaSim** instantiates local wildlife from regional cohorts at simulation-chunk activation, uses multirate responsive local behavior and retains only bounded, previously instantiated individuals while identity matters (bonded peers, dependent young or selected notable adults); it otherwise uses coarse populations, all with shared **BeastCore** rules. **FloraSim** advances individual trees and population patches lazily using StalthosSim's stored environmental interval summaries and discrete events. **SimCore** coordinates global time and scheduling; **StalthosState** preserves identities and history. **InteractionsCore** validates cross-domain resource transfers and damage.

Use event scheduling, low-frequency growth/accounting and deterministic spatial seeds. Separate render-chunk rebuild from ecological updates; batch many plant changes rather than one mesh rebuild per bite.

Don't equate offscreen simplification with resetting resources. Return visits should show plausible consequences.

## Tests and measures

- Ecological viability for the flagship juvenile throughout a normal seasonal cycle in a local watershed.
- Regional water balance without unexplained permanent ponds or absurd flood magnitudes.
- Food patches recover at appropriate timescales and browsing leaves visible traces.
- An island changes in player's absence without hitches on revisit.
- Conditions determine wildlife distributions; never hardcode predatory ambushes to player location.
- Instrument per-tick CPU, save/load cost, memory and local detail promotion/demotion.

Cross-references: [Architecture](simulation-architecture.md), [StalthosSim](stalthos-sim.md), [FloraSim](flora-sim.md), [FaunaSim](fauna-sim.md), [HeroSim](hero-sim.md), [World generation](world-generation.md).

## Simulation chunks versus camera visibility

FaunaSim and FloraSim prepare locally appropriate organisms in **simulation chunks extending beyond Smalltrotter's senses and the entire bounded HeroView camera envelope**. Organisms are not created by the render frustum. Long-term identity belongs to significant trees/the Hero Beast and selectively to *already-instantiated* socially relevant or notable wildlife (including bonded peers and dependent young)—not to every regional fauna cohort. See [Spatial activation](spatial-activation.md) and [HeroView](hero-view.md).
