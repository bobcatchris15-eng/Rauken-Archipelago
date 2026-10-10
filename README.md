# The Stalthosian Archipelago

A fictional Late Cretaceous-inspired island archipelago and small-dinosaur life simulator.

**Repository status: planning only.** No engine, programming language, asset schema, or implementation is selected yet.

The player inhabits an animal—not a human character controlling an animal-shaped avatar. The world is a persistent, interconnected ecology where landscape, weather, vegetation, growth and ordinary animal behavior are the central experience. The geography is deliberately striking and compressed for exploration.

Start with the **[planning index](docs/README.md)** and **[simulation architecture](docs/simulation-architecture.md)**. These are specifications, not running systems.

## Production principle: a beautiful, cheap illusion

**The Stalthosian Archipelago is a display-first natural-history illusion, not an internally exact ecosystem model.** Near-photorealistic scenery, convincing animal movement and believable observable consequences have priority over scientifically detailed invisible ecology. Generate, stage, approximate and discard hidden state freely **unless doing so would expose a contradiction to the player**. Preserve local interaction outcomes, recurring landmarks, important relationships and visible changes with the smallest practical state.

An expensive ecological mechanism is **opt-in**, only when a cheaper approximation demonstrably fails an observable gameplay/visual test. Do not turn an impressive visual requirement into a demand for full physiology, hydrology, nutrient budgets, population dynamics or weather-event replay.

**Biodiversity production priority:** An expandable first creative palette of roughly **50 distinctive non-hero wildlife actors** and **200 varied plant silhouettes/leaf systems** is preferable to a tiny roster with exhaustive simulated ecology. Specific requested species are always welcome; neither number is a cap. See [Fauna actor catalog](docs/fauna-actor-catalog.md) and [Plant visual catalog](docs/plant-visual-catalog.md).

## Current guiding choices

- Four major, irregular islands and smaller islets; each island supports multiple connected ecological landscapes.
- Ancient uplands, deeply eroded and partially flooded into branching rocky coastlines.
- Terrain and habitat density prioritized over strict geomorphological proportions; geological *causality* still matters.
- Five planned Hero Beasts: Smalltrotter (dwarf titanosaur and visual flagship), Brackenback (ankylosaurid), Thistletail (flightless feathered opportunist), Longstride (medium wandering predator), and Reedcrest (basal hadrosauroid with bonded peers). Smalltrotter's bristles are fictional, not proven sauropod quills.
- Each life begins at hatching within an existing species population; death ends that life, not the world.
- Direct steering is the strongest voluntary player input. Compatible routine browsing, drinking and social reactions continue during movement; an optional player-invoked slow-time contextual control expresses more specific intentions.
- Without commands the Hero Beast lives autonomously, with an optional gentle documentary camera.
- Breeding/nesting/hatching are playable, accelerated and species-specific; extended parenting can outlast the nesting episode.
- Natural hazards, physiology and environmental conditions are more prevalent than predator encounters.
- Visual ambition is near-photorealism, on a reference GTX 1080 8 GB plus first-generation Ryzen with a 30 FPS floor.
- Flax and Wicked Engine are leading **candidates**, pending measured benchmarks.
- All production should be agent-friendly, reproducible, inspectable and source-controlled.
- Named boundaries: **SimCore** (time/scheduling), **StalthosState** (persistence), **StalthosSim** (environment), **FloraSim** (plants/fungi), **FaunaSim** (wildlife), **HeroSim** (player), **BeastCore** (shared animal biology) and **InteractionsCore** (validated cross-domain exchanges), and **HeroView** (bounded camera and the human-facing embodiment controls).
- Watercourses, soils and plant suitability are mainly map-generated. Runtime weather, population pressure, growth and physiology use simple bounded approximations, with lasting visible exceptions saved explicitly. No requirement for physically correct ecology.

No content here should be treated as a finalized implementation choice without the explicit decisions noted in the individual specifications.

## Camera, continuity and biological activation

[HeroView](docs/hero-view.md) normally watches the Hero Beast through an animal-centered orbit/follow camera. The locally tethered detached camera is optional; significant sensed alarms can coordinate attention and recall it to an animal-centered view. Camera observations never grant the animal otherwise unknown information.

[Spatial activation](docs/spatial-activation.md) prewarms plants and wildlife beyond the full camera tether. FaunaSim stores regional populations and instantiates individuals only when locally relevant. Certain **already-instantiated** animals can retain compact records during social ties, dependent parenting or other justified encounters; these advance coarsely while dormant and may naturally lose individual identity. See [FaunaSim](docs/fauna-sim.md).

The Stalthosian Archipelago is the setting and working game title. The GitHub repository slug is historical. Planning only; no gameplay implementation yet.
