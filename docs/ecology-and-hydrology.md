# Ecology and hydrology — shared display-level principles

**Domain:** Habitat appearance, nearby ecological interactions and the minimum persistence needed for a convincing world. **Status:** Display-first direction; engineering parameters remain experimental. Ownership stays in [Simulation architecture](simulation-architecture.md).

## World model

**The archipelago is a visually ambitious, deliberately shallow natural-history illusion.** Geological/habitat references help determine where plants, water and animals *look and behave* plausible; there is no obligation to solve a closed ecosystem. Preserve immediately observable interactions and conspicuous changes across visits, but use densities, seasonal variants, seeds and simple probabilities for most offscreen processes.

The guiding visual relationship is **terrain/substrate → plausible water/exposure → plant composition → animal presence/behavior**. This drives placement and presentation, not a complete dynamic nutrient or energy system.

## Climate

Give each island/terrain region a coarse climate profile, a seasonal curve and smooth current weather state. Precomputed modifiers create sheltered damp ravines, exposed rocky ridges, lee-side drying and rainward mist without a high-resolution atmospheric model. Weather should look and sound coherent and affect obvious animal behavior or traversal.

No fine-grained microclimate thermodynamics or long chronological rain/heat histories. Save only exceptional events with visible durable consequences.

## Hydrology — primarily a map property

Rivers, streams, springs, marshes, baseline water availability, salinity and drainage are offline world-generation outputs. Map-generated moisture suitability considers elevation above water, soil permeability, shelter and broad rainfall tendency instead of just distance to a river.

Runtime water uses simple seasonal level adjustments, approximate current/tide/depth where relevant, and predefined floodable areas. A swollen creek may block a familiar crossing; wet soil may affect footing; drinking from sea/brackish water remains inappropriate.

Do not solve groundwater transport, watershed water budgets, long-term erosion, sediment advection or general fluid dynamics. Persistent damage comes from a rare explicit event, not replayed flood history.

## Soil, substrate, plant communities

Substrate/soil/habitat tags guide convincing vegetation distribution, rooting/contact and visual condition. Stable procedural seeds and current season produce most flora; patch-level cover, browse/depletion and recovery drive inexpensive changes.

Prominent trees, important shrubs and directly observed damage/death can retain compact identities and visual exception records. Ordinary herbs, ground cover, moss, fungi and litter remain mostly patch/variant state. A changed canopy opening can cheaply change surrounding cover. No detailed seedling competition, seed bank, nutrient conservation or per-leaf accounting.

## Food webs

Represent plausible niches: herbivores, small omnivores/insectivores, flying animals, terrestrial/shore predators, scavengers and detritivores. Choose regional occupancy from habitat suitability, coarse abundance and season. Local visible animals must have convincing routines, limited senses, hunger/rest cues, simple interactions and no omniscient player hunting.

Offscreen population change, browsing pressure, dispersal, mortality and small-animal food availability may be stochastic, approximate and occasional. Do not model exact energy flows or complete demographic balances. Retain distinctive social/dependent individuals under the bounded FaunaSim policy; prevent visibly duplicated or resurrected encountered animals.

## Seasonal change and disturbance

- Seasonal leaf density/color, fruiting, shedding and habitat appearance from species/region profiles.
- Temporary weather, water levels, mud and exposed/wet surfaces affecting immediate behavior and navigation.
- Visible browse removal or a reduced shrub-patch density, followed by plausible delayed recovery.
- Occasional fallen trees, branch loss, deadwood, carcasses or local canopy openings with **saved recognizable results**.
- Coarse decomposition and regrowth stages chosen for visual credibility, not a detailed microbial or nutrient model.

The appearance of a living environment matters; simulating the complete invisible process does not. Mechanistic fire spread, complex succession and continuously evolving riverbeds remain out of scope.

## Spatial fidelity and cost

**Observed/contacting:** excellent vegetation, lighting, anatomy, movement, collision/reach, locally consistent feeding and responses.

**Nearby/hidden:** believable lightweight animal states prepared beyond the entire HeroView camera tether so turning the camera does not spawn creatures. Stable flora patches support quick reveals.

**Remote:** region profile, species density, current season, simple elapsed-time condition and a few durable exceptions. Recreate an acceptable present scene without historical replay. Exact hidden biographies, rainfall chronologies, food-energy ledgers and lifetime tree physiological models are not required.

SimCore schedules activation; StalthosSim supplies coarse weather; FloraSim owns plant presentation/patch state; FaunaSim animals/occupancy; HeroSim uses shared simple BeastCore rules; InteractionsCore coordinates visible contacts; StalthosState stores observable persistent facts. **No additional ecology runtime subsystems.**

## Acceptance tests

- A striking local habitat looks coherent from a juvenile's perspective, with enough visual variety to reward lingering.
- An approached animal was already resting or feeding before it came into view.
- Browsed vegetation responds visibly and does not instantly pop back on camera or reload.
- A recognizable storm-felled tree, injured companion, offspring, nest or corpse remains consistent upon revisit.
- Drought and flooding visibly affect landscape and traversal using cheap weather signals.
- Revealing a region after long absence is bounded in CPU, memory and latency.
- A complex ecological algorithm is adopted **only if** a simpler proxy demonstrably produces an observable failure.

See [Simulation architecture](simulation-architecture.md), [StalthosSim](stalthos-sim.md), [FloraSim](flora-sim.md), [FaunaSim](fauna-sim.md), [World generation](world-generation.md), and [Vision](vision-and-principles.md).
