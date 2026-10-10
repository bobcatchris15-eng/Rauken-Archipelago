# Research register, assumptions and decisions

**Purpose:** Keep scientific evidence separate from invented lore and distinguish approved creative directions from provisional implementation choices.

## Accepted creative direction

- **Name:** The Rauken (not 'Veyran Archipelago' or 'Rauken Isles').
- Four major islands at different separation ages, with abundant minor islands.
- Main Island: Driftless/Baraboo-like dissected uplands fading into broad Wisconsin Central Plain-like country with isolated resistant caprock buttes.
- Rich, irregular drowned-upland coastlines, sheltered rocky mossy inlets and ravines, dramatic outcrops and strong geological silhouettes throughout.
- Density and exploration appeal outweigh exact geographic probabilities; preserve plausible cause and consistent drainage.
- Outer Reach's dry iron-weathered uplands vs sheltered productive Green Hollows is strongly favored.
- Juvenile dwarf titanosaur is flagship; juvenile shaggy-looking sparse bristles/quills and adult scattered osteoderms, textured skin.
- Player controls intention/motion; automatic nearby feeding/drinking and other routine animal behavior.
- Near-photorealism on GTX 1080 + early Ryzen with 30 FPS floor. Flax and Wicked lead, no confirmed engine winner.
- **Accepted names:** **RaukenState** replaces WorldState, **BeastCore** replaces AnimalCore, and **InteractionsCore** names the cross-domain interaction layer. Other owners: SimCore, RaukenSim, FloraSim, FaunaSim, HeroSim.
- Static hydrological geography and plant moisture suitability belong to map design; RaukenSim handles weather, seasons and temporary floods without routine erosion/groundwater simulation.

## Explicitly provisional

| Question | Current hypothesis | What resolves it |
|---|---|---|
| Island area | Compact, ARK-inspired; Main ~20–30 km², others smaller | Build and inhabit a 1×1 km reference patch |
| Island ages | Rainridge ~6 My, Stone ~0.8 My, Outer Reach ~12 My since last firm connection | Fictional paleogeographic timeline with barrier logic |
| Juvenile/body size | 1.3–1.8 m start, 5–6 m adult, approx. tonne range | Volumetric anatomy, biomechanical reasonableness |
| Juvenile bristles | Derived keratin-like quill covering | Design choice; **not** an evidenced titanosaur condition |
| Osteoderm count/placement | Scattered nodules/plates along dorsal zones | Fossil comparison then fictional anatomy |
| Botanical roster | Named fictional analogues of flowering plants, conifers, ferns, horsetails, cycads, fungi | Habitat modeling and source-backed morphology |
| Adult longevity, seasonal timing | Not decided | Life-history research and gameplay trials |
| Food chemical/nutrition values | Species-sensitive, generalist browser | Biological parameters and measured tuning |
| Reference display | Baseline 1080p | Confirm user monitor and target resolution |
| Runtime engine | Flax/Wicked shortlist | Same-scene, same-hardware benchmarks |
| Temporary storm/flood fidelity | Precomputed flood masks and approximate water levels | Traversal and performance tests |
| Fluid time and juvenile growth | Noticeable early maturation; shared species growth and optional global time acceleration | Playtest rate, siblings and physiological balance |
| Fauna/Flora simulation cadence | Active multirate animals, lazy plants, rendering independent | Continuity + cost benchmarks |

## Architecture decision — 2026-10-09

Adopt logical in-process modules: **SimCore** schedules, **RaukenState** persists, **RaukenSim** supplies physical conditions, **FloraSim** owns lazily evaluated plants, **FaunaSim** wild animals, **HeroSim** the player, **BeastCore** reusable physiology and perception, **InteractionsCore** validated ecological transfers. Don't substitute the original names WorldState, AnimalCore or unnamed interaction layer.

Do not tick plants based on render visibility. Nearby animals need active multirate updates (immediate pain/startle; slower hunger/thirst/growth) while offscreen fauna may be aggregated. Choose time-pacing formulas after playable experiments, preserving comparable rules for player and NPC animals. This architecture does not mandate separate executables, network APIs or specific tick frequencies.

## Sources to read and verify

These are starting leads to be checked for bibliographic accuracy, licensing and what each actually supports. They are **not** proof that fictional features existed.

### Paleontology, ecology, fossils
- Hațeg Island reviews and Maastrichtian paleoenvironments: identify correct geological units, stratigraphic intervals and flora/fauna assemblages.
- Magyarosaurus bone histology and dwarf titanosaur size.
- Titanosaur skin impressions, embryonic scales and osteoderms (e.g., Saltasaurus/Rapetosaurus studies).
- 2025 Diamantinasaurus gut-content paper: examine actual identified vegetation and feeding interpretation.
- Living plant fermentation studies in Mesozoic analogues; avoid assigning sheep-rumen fermentability directly to sauropods.
- Early grass records (phytoliths in Late Cretaceous coprolites); reconstruct plausible sparse rather than modern lawnlike cover.
- Late Cretaceous Hațeg monocots, conifers, angiosperm leaves, ferns and spores; seed/reproductive body evidence.
- Living birds/mammals with age-changing integument as **analogy**, not proof of bristled sauropods.

### Geology and physical environment
- Wisconsin Geological & Natural History Survey: Baraboo quartzite, Driftless gorge forms, Central Sand Plain sandstone remnants/caprock.
- New Zealand Marlborough Sounds: drowned river systems (rias), peninsulas and shelving inlets.
- La Gomera/Madeira ravines and humidity gradients; limestone/karst island terrain.
- Socotra, New Caledonia ultramafic laterites, Lord Howe coastal stacks as **landscape references**, not evidence of Cretaceous co-location.
- Island biogeography literature: separation, intermittent dispersal and endemism.
- Catchment hydrology, flash flooding, saltwater intrusion and spring/aquifer behavior.

### Technical
- Official Flax terrain/foliage API and source: https://docs.flaxengine.com/manual/foliage/index.html
- Wicked current upstream: https://github.com/turanszkij/WickedEngine
- Bentley PlantFactory licensing: https://www.bentley.com/products/e-on-software/
- PresentMon: https://github.com/GameTechDev/PresentMon
- Geometry optimization: https://meshoptimizer.org/
- Blender automation: https://docs.blender.org/manual/en/latest/advanced/command_line/index.html

## Planned decisions requiring real tests

1. Does a denser, partially composed 1 km² watershed engage more than strict geology at juvenile viewpoint?
2. What is the smallest viable habitat-area/population scale at the chosen island size?
3. How many nearby vegetation instances survive real wind, shadows and animal interaction under 33.3 ms?
4. Do Flax foliage clusters handle batched ecological changes efficiently enough, or should a separate renderer own them?
5. Can Wicked's control justify its tooling/integration burden on the reference machine?
6. Does bristle geometry remain high-quality without alpha cards or groom strands?
7. How much developmental morphology is necessary to make the sauropod's growth believable?
8. Can players infer thirst/nutrition/condition without permanent status bars?

## Research discipline

For each answered scientific question, record source link/DOI, exact supported claim, caveats, conflicting interpretations and how The Rauken extrapolates. For each technical experiment, record source revision, hardware, binary/settings, raw measurements and visual comparison. Never cite the existence of an unpublished benchmark as proof of performance.

In future updates, append dated decisions with reasons, alternatives considered, test results and cross-domain impacts. This file should preserve *why* choices were made without taking ownership of each domain's final specification.
