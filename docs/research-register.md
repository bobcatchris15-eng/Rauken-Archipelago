# Research register, assumptions and decisions

**Purpose:** Keep scientific evidence separate from invented lore and distinguish approved creative directions from provisional implementation choices.

## Accepted creative direction

- **Name (superseding earlier Rauken-era direction):** **The Stalthosian Archipelago**, with **Stalthos** as a convenient informal regional shorthand and **Stalthosian** as adjective. Name is invented, loosely inspired by early Germanic/Old English foundation/stone vocabulary; do **not** present Stalthos as an attested historical word. Repository slug stays Rauken-Archipelago until explicitly renamed.
- Four major islands at different separation ages, with abundant minor islands.
- Main Island: Driftless/Baraboo-like dissected uplands fading into broad Wisconsin Central Plain-like country with isolated resistant caprock buttes.
- Rich, irregular drowned-upland coastlines, sheltered rocky mossy inlets and ravines, dramatic outcrops and strong geological silhouettes throughout.
- Density and exploration appeal outweigh exact geographic probabilities; preserve plausible cause and consistent drainage.
- Outer Reach's dry iron-weathered uplands vs sheltered productive Green Hollows is strongly favored.
- Five playable Hero Beasts: Smalltrotter dwarf titanosaur flagship (juvenile bristles and adult osteoderms); Brackenback true ankylosaurid; Thistletail small flightless feathered omnivore; Longstride medium roaming predator; Reedcrest medium basal hadrosauroid with a bonded small peer group.
- Direct movement is the strongest voluntary player action; routine animal behavior continues concurrently. Uncommanded HeroSim can live and travel autonomously, observed by HeroView's unobtrusive documentary camera. Optional slow-time contextual responses are explicitly player-invoked, not automatic pop-ups.
- Near-photorealism on GTX 1080 + early Ryzen with 30 FPS floor. Flax and Wicked lead, no confirmed engine winner.
- **Current logical names:** **StalthosState** (formerly RaukenState/WorldState), **StalthosSim** (formerly RaukenSim), **BeastCore** (formerly AnimalCore), **InteractionsCore**, SimCore, FloraSim, FaunaSim, HeroSim and HeroView. Names are planning contracts, not compiled interfaces.
- Static hydrological geography and plant moisture suitability belong to map design; StalthosSim handles weather, seasons and temporary floods without routine erosion/groundwater simulation.

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

Adopt logical in-process modules: **SimCore** schedules, **StalthosState** persists, **StalthosSim** supplies physical conditions, **FloraSim** owns lazily evaluated plants, **FaunaSim** wild animals, **HeroSim** the player, **BeastCore** reusable physiology and perception, **InteractionsCore** validated ecological transfers. Don't substitute the original names WorldState, AnimalCore or unnamed interaction layer.

Do not tick plants based on render visibility. Nearby animals need active multirate updates (immediate pain/startle; slower hunger/thirst/growth) while offscreen fauna may be aggregated. Choose time-pacing formulas after playable experiments, preserving comparable rules for player and NPC animals. This architecture does not mandate separate executables, network APIs or specific tick frequencies.

## Adversarial architecture review refinements — 2026-10-09

**No new runtime domains approved.** Preserve the established named component boundaries and ecology-first, presentation-driven scope. Tighten existing contracts rather than constructing a universal simulation framework.

1. **FaunaSim:** persistent regional age/population ledger; abstract/active/retained reservations conserve accounting counts across activation/retirement. Cohort-level food demand causes finite, persistent FloraSim forage depletion through InteractionsCore; no individual biographies or exact remote trophic accounting required.
2. **StalthosSim:** chronological compact environmental intervals and exceptional event records (drought duration, heat exposure, saturation, flood maxima and sequence), not simply aggregate rainfall/temperature means.
3. **SimCore/spatial activation:** biological reconciliation, local active simulation and presentation are separate readiness tiers; bounded queue jobs, version/cursor checks and camera-tether prewarm. Don't synchronously catch up whole chunks on a camera turn.
4. **Fidelity:** preserve domain consequences independently of temporal cadence and graphical detail. **Do not** build a generalized causal-importance scoring framework.
5. **FloraSim/asset tooling:** significant plants use stable structural segment addresses; InteractionsCore finite/idempotent mutations; save compact current scars/structure rather than every bite. No per-leaf IDs.
6. **Time:** one world-time source, responsive realtime motion/reflexes, BeastCore physiology over world intervals plus actual activity costs, shared species developmental rules with acknowledged gameplay compression. Exact factors pending tests.

**Open experiments:** repeated region cycling and demographic balance; equal-rainfall/different-sequence biological outcome; old-chunk camera reveal latency; deterministic branch-damage regeneration; identical player/NPC life-history inputs under accelerated world time. Avoid false precision from exact ecological bookkeeping where the model is deliberately statistical.

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

For each answered scientific question, record source link/DOI, exact supported claim, caveats, conflicting interpretations and how The Stalthosian Archipelago extrapolates. For each technical experiment, record source revision, hardware, binary/settings, raw measurements and visual comparison. Never cite the existence of an unpublished benchmark as proof of performance.

In future updates, append dated decisions with reasons, alternatives considered, test results and cross-domain impacts. This file should preserve *why* choices were made without taking ownership of each domain's final specification.

## HeroView, fauna retention and spatial activation — 2026-10-09

**Agreed direction:** Name the embodiment/presentation/control interface **HeroView**. Direct WASD is relative to the animal's body (W always forward from Smalltrotter), while an orbit camera maintains chosen composition and translates to follow her as she walks across frame. A **bounded** local detached camera may inspect a nearby ridge but never fly to another island. Camera position and movement authority are distinct; free-camera input can pick a **persistent destination** for HeroSim to execute.

**Intent priority:** routine hunger/thirst do not casually override player commands; acute fear/pain/startle can briefly interrupt, with direct WASD carrying stronger authority than autonomous destination travel. HeroSim perceives through Smalltrotter's bodily senses, not from the player's detached camera.

**Spatial activation:** SimCore prewarms FaunaSim and FloraSim regions beyond the hero's own sensory extent and the full reachable bounded camera envelope. Local animals and plants are instantiated from their regional simulation state before they are shown. Vegetation need not have a per-blade biological agent.

**Wildlife memory policy (superseded by the later 2026-10-09 life-history decision below):** FaunaSim still represents most wildlife as cohorts and avoids global personal biographies. Bounded **already-instantiated** identities may persist for bonded Reedcrest peers, dependent Longstride young/caregivers, notable mature giants and similarly meaningful encounters; never a registry of uninstantiated animals.

**Provisional/tune:** camera radius and tether shape; activation buffers; exact physics controls; fear thresholds; retained adult budget. These are not fixed distances or performance claims.

## Direct locomotor intent clarification — 2026-10-09

**Decision:** HeroView's direct steering expresses desired body-relative movement, not step-by-step limb control or autonomous navigation. Shared BeastCore motor competence handles gait, balance, footing and small local avoidance. The maximum **automatic lateral route deviation** is bounded by a camera-projected **central-third-width steering corridor**; broad detours belong to the player's own turning or to explicit autonomous destination navigation.

**If no local admissible route exists:** the Hero Beast stops at the obstruction and may look/sniff/inspect while the held direction remains. A changed steering input retries immediately; releasing direct steering restores full autonomous behavior, which can move off another way. No autopilot loop repeatedly routes around the obstacle during held WASD.

**Compatibility interpretation:** constrain candidate *deviation from the projected intended path*, not the animal's absolute screen X position, otherwise the established broadside orbit/follow camera and across-screen movement would contradict the new rule. HeroView supplies the visual constraint without granting HeroSim sensory omniscience; BeastCore remains camera-agnostic. Test exact projection horizon/hysteresis and camera movement; no new navigation subsystem approved.

## Stalthosian name, Hero Beasts and life-history decisions — 2026-10-09 (supersedes earlier entries)

**Naming.** The canonical fictional geographical name and working game title are **The Stalthosian Archipelago**; shorthand **Stalthos**. The project is an invented world; the name is invented, not a quoted historical Old English or Germanic word. Old Rauken-branded identifiers and the file stalthos-sim.md have been updated in planning text. The GitHub repository slug remains historical; changing the actual repo name was not requested.

**Playable roster.** Five lineages with distinct anatomy and ecology: **Smalltrotter** (insular dwarf titanosaur, independent young, juvenile nape bristles), **Brackenback** (true ankylosaurid, low browser, generalized defensive response to any distressed smaller animal and occasional suspicion/posturing at innocent bushes/rocks), **Thistletail** (small flightless feathered opportunist using genuine microforage), **Longstride** (medium roaming predator, prolonged parental following), and **Reedcrest** (basal hadrosauroid, bonded small peer kindergarten from near-synchronously hatching neighboring nests). Names, measurements and fossil-inspired anatomy remain provisional design hypotheses, **not evidence that these precise behaviors were fossilized**.

**Five childhoods and parenting styles.** Every new player life **hatches as an ordinary member of a selected species within an existing local population**. Smalltrotter young are soon on their own; Brackenback juveniles mingle near protective unrelated adults/aunties/uncles; Reedcrest young form strongly bonded peer groups of two to four companions alongside the playable animal; Thistletail attends offspring only briefly, like some ground fowl; Longstride parents provide the longest care, with growing youngsters following, learning, sometimes falling behind and finally dispersing. Playing a hatchling Longstride means encountering a wild caregiving parent. Child care and individual lifetime continuation can last beyond the brief nesting sequence.

**Breeding.** All five species can court/mate, nest, lay/incubate and hatch using species-appropriate behavior. A focused **nest-to-hatch episode targets about thirty minutes or less** of player time by interruptible, coherent SimCore world-time acceleration, while offspring dependence can span normal later play. No breeding-stat or inherited-progression game, no detailed genetics or mandatory mating, and no guaranteed clutch survival.

**Player authority.** Direct body-relative locomotion has highest voluntary precedence. Compatible head/neck/mouth/social activity (e.g., Smalltrotter plucking shrubs while walking) is autonomous even during direct control. A small **slow-time contextual response** chooser opens only on deliberate request and produces intents, not scripted outcomes. Otherwise HeroSim fully governs the animal, including meaningful travel; it does not merely idle nearby. HeroView defaults to animal-centered third-person, can become a gently orbiting documentary camera when left alone, and retains a locally bounded detached view. Significant *sensed* alarms may orient animal/camera at the same point and recall a detached view smoothly; direct camera input cancels. Brackenback's innocent-bush scares may be lesser alarms, not repeated forced camera swings.

**Death and retention.** Death changes the inhabited animal, not the world. A new playable life starts as another wild hatchling. Surviving nests, offspring, cohorts, corpses and previously instantiated individualized animals may continue. Retained identity is **bounded and conditional**, advanced coarsely by elapsed world time, and can decay into cohorts when social/dependent/notable justification ends. No long-lived memory for every individual, no population duplication and no respawning the dead. Reedcrest's peers and Longstride dependent offspring are reasons for temporary individuality, not a separate complex memory simulation. Cross-island followers navigate and survive real crossings or fail; no teleports.

**Remain open to research/testing:** taxonomy, exact developmental/parental intervals, physical speed/mass, activation and identity budgets, camera alarm thresholds and animation/feeding compatibility, nested world-time scaling, terrain sizes, renderer. These are tuning/research topics rather than additional creative-direction approvals. No source evidence is asserted for invented species parenting.

## Bounded animal working memory and ordinary home-range behavior — 2026-10-10

**Decision:** HeroSim/BeastCore animal memory is a capped, short-lived working set for current attention, temporarily hidden dangers, interrupted actions and nearby resources. Observations expire; there is no cumulative landmark/route map, generalized learning system or long-term home-position target. Recent habituation may temporarily suppress repeated false alarms but fades. Exact item count and expiry time remain tunable rather than fixed requirements.

**Autonomy:** an adequately supplied, comfortable Smalltrotter is an ordinary animal in a local ecological range, not an independent explorer. The player supplies most intentions for exceptional journeys. Uncommanded animals can travel among local resources and may shift range under real environmental, social or physiological pressure; no artificial idle-radius fence. When released after player-directed relocation, the Hero Beast resumes living where it is instead of automatically navigating back to an old range.

**Important distinction:** persistent body state, nests, population ecology and explicitly bounded socially significant identities (e.g. Reedcrest peers, dependent Longstride young) remain authoritative under their existing systems. They are **not** an excuse for durable geographic/biographical memory. FaunaSim ordinary wildlife follows the same transient-attention policy. Do not implement an animal learning/history subsystem.

## Detached HeroView listening and owned intentions — 2026-10-10

**Decision:** The detached camera carries the *player's ears* (camera-centered world audio), while BeastCore/HeroSim retains the Hero Beast's **anatomically located sensory hearing**. Both interpret shared positioned sound sources from fauna, weather/water and inexpensive habitat ambience. A predator call heard from the detached camera may not be heard or reacted to by the Hero Beast. Player-only audio never causes HeroSim alarm or an alarm-driven camera recall. Body/physiology cues can be mixed unobtrusively without ignoring distance.

**Decision:** Camera detachment doesn't suspend/replace the animal's autonomy. A player-designated destination or contextual goal is **adopted as the animal's own voluntary intention** with elevated source/priority, using the same behavior, perception and locomotor execution as spontaneous goals. Completing, abandoning or cancelling returns control to autonomous goal selection. No separate scripted path-following motor controller or noticeable player-controlled animation change. A player may suggest an out-of-sight destination, but cannot transmit camera-only predator/wildlife knowledge.

**Implementation boundary:** Add no new audio or cognition subsystem. Reuse local spatial sound events, camera audio listener, existing BeastCore sensing, and HeroSim's singular intention arbitration. Choose audio propagation fidelity, transition/crossfade timing and internal intent metadata through experiments; not a commitment to ray-traced acoustics.

## Provisional lightweight forest disturbance — 2026-10-09

**Accepted provisionally, depth explicitly constrained.** A forest may change recognizably across successive Hero Beast lives through occasional individual treefall, damage/death, small canopy openings, coarse understory response and infrequent new tree recruitment. This supports the near-photorealistic environment and enduring sense of place; it is not approval for a full forest ecology simulator. Geological erosion and dynamic riverbed evolution remain out of scope.

**Implementation boundary:** keep existing FloraSim / StalthosSim / StalthosState responsibility. Substantial adult trees have stable logical IDs and deterministic branching seeds, but tens of thousands of trees **must not require full active biology, per-frame updating or separate bulky mutable records**. Reconstruct unchanged trees from seeds; persist compact exceptions (lost branches, uprooting, dead/standing/fallen trunks), coarse canopy/cover changes and new recruited tree identities. Lazily reconcile and checkpoint resulting state so old events need not be replayed indefinitely.

**Explicitly deferred:** mechanistic wildfire propagation and succession, seed dispersal/seed banks, per-seedling competition, fine-grained forest light/nutrient dynamics and generalized multi-stage ecological recovery. A simple damaged/burned patch might be visually represented later if demonstrated useful; this is **not** a wildfire simulation commitment. Do not add a new subsystem or expand scope before evaluating a simpler in-engine forest.

**Acceptance demonstration:** revisit a distinctive woodland after years of shared world time and recognize its geology and baseline mature trees while observing a persistent fallen tree, a sunnier clearing, changed understory cover or a few durable recruits. No resurrection of dead seeded trees, unbounded historical replay, or tree/patch save/activation spikes. Treat advanced succession as unnecessary unless this visibly fails.
