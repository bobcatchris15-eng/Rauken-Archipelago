# Implementation roadmap — toolkit first

**Status:** Proposed executable plan. **Wicked Engine is the chosen active renderer target** based on user local testing; engine integration and target-hardware results remain unimplemented/unmeasured.  
**Source baseline:** main at ce04d13e5dfcb4b8256db431a100427542fbee44, reviewed 2026-10-10.  
**Working setting name:** The Stalthosian Archipelago; repository slug Rauken-Archipelago is historical. Do not rename modules, repository, or game without a separate decision.  
**First executable milestone:** an agent-operable, engine-neutral content production and validation toolkit. This is **not** a playable vertical slice.

Read [Toolkit implementation](toolkit.md) for work items and exact handoffs, and [Parallel work packages](parallel-work.md) for bounded concurrent assignments.

**Squad execution:** [Machine-readable 77-task Wicked-first DAG, dispatcher and acceptance gates](../../tasks/README.md) translates this plan into agent-ready bounded work. The graph is canonical for dispatch; this document remains rationale and design authority.

## 1. Baseline and priority order

The existing 20 topical documents, planning index, and root README describe a coherent game direction but no code, chosen language, locked content schema or completed renderer benchmark. Their authority is:

1. User-approved, latest research-register decisions and [Vision](../vision-and-principles.md).
2. Domain ownership in [Simulation architecture](../simulation-architecture.md), [Spatial activation](../spatial-activation.md) and [HeroView](../hero-view.md).
3. Design/appearance in [Visual direction](../visual-direction.md), [Creatures](../creatures.md), [Flora](../flora.md), [Fauna catalog](../fauna-actor-catalog.md) and [Plant visual catalog](../plant-visual-catalog.md).
4. Candidate techniques in [Asset toolkit](../asset-toolkit.md), [Rendering experiments](../rendering-experiments.md) and [World generation](../world-generation.md). Treat concrete algorithms in older texts as options when newer display-first doctrine supersedes their depth.

**Nonnegotiable product constraints:** natural-history visual credibility; coherent contact and behavior; direct body-relative movement; animal senses distinct from the player's camera; wildlife staged beyond the whole reachable detached-camera envelope; selectively persistent visible changes; routine hidden ecology cheap and largely dormant. Five planned Hero Beasts, expandable ~50 non-hero visual actors and ~200 botanically distinguishable forms are *content directions, not first-milestone checklists or simulation subsystem counts*. Dense attractive terrain is intentionally composition-first, with causal drainage and passability but no historical geological simulation. A GTX 1080 8 GB / first-generation Ryzen at native 1080p with a 30 FPS **full-scene objective** is the performance reference, not a measured achievement.

## 2. Gap analysis — decisions and artifacts absent today

| Gap | Why it blocks agent execution | Proposed owner/artifact |
|---|---|---|
| Installed tool inventory and version policy | Scripts cannot assume Blender, Python, compiler, codecs, engine locations or compatible plugin builds | TOOL-01, a read-only Windows doctor and local tool lock |
| Machine-readable species and asset contracts | Morphology, age, licenses, geometry, collision, edible targets and variation are prose only | TOOL-02 JSON Schemas and sample profiles |
| End-to-end command/receipt protocol | Current command names have no input/output format, exit codes, failure policy or idempotence | TOOL-03 CLI, logs, manifests and artifact staging |
| Reusable offline morphology engines | Named six reference plants are not generator implementations | TOOL-04 through TOOL-08 |
| Rig, animation and plant contact interfaces | Renderers cannot compare meaningful hero movement or plant bending against equivalent inputs | TOOL-09 and TOOL-10 |
| Licensing/reference traceability | Training/reference images and PlantFactory/PlantCatalog outputs can be misused or redistributed incorrectly | TOOL-02, TOOL-11 |
| Grounded visual and automated QA | Near-photorealism and biodiversity are undefined without consistent evidence/review sheets | TOOL-11 and TOOL-12 |
| Neutral world sample | Wicked can silently lose content or shader features compared with authored neutral asset masters | WORLD-01, RND-003 |
| Performance repeatability | An average FPS or screenshot hides shader/streaming, overdraw, hitches and VRAM cost | BENCH-02, BENCH-03 |
| Small runtime contract examples | Image/contact/streaming probes need stable IDs and semantic event payloads without full ecology | ARCH-01 |
| Parallel integration discipline | Several agents would race on scene formats, naming, shared files and tool installers | [Parallel work packages](parallel-work.md) |

There is **no full-scene measurement yet** demonstrating that Wicked meets the frame target on the reference PC. There is also no justification to implement exact population accounting, weather-history replay, per-plant ticking, live erosion or per-branch rigid-body physics.

## 3. Recommended sequence and gates

### Stage 0 — Freeze interface conventions, not art direction

**Execute:** TOOL-01, TOOL-02, TOOL-03 in dependency order. Write schemas, the first working CLI commands, test fixtures and the reproducible Windows environment doctor. Declare coordinate axes, units, texture color spaces, IDs and source/cooked separation. Capture reference hardware and graphics-driver details locally rather than inventing them.

**Gate G0 — workshop can be operated unattended:** with a clean source checkout and documented local dependencies, a worker can invoke doctor, schema validation and one fixture processing command from PowerShell, receive machine-readable status, identify any missing dependency and reproduce a hash/receipt. Missing optional tools do not crash unrelated commands.

### Stage 1 — Prove the asset factory on varied organisms

**Execute:** six reference plants from [Flora](../flora.md): Splitcrown, Softbough, Jointreed, Royal frond, Basketfern, and bracket fungus on a log. Add Smalltrotter's skeletal/anatomical proxy with distinct juvenile and adult appearance. Generators may use Blender Python/Geometry Nodes, with PlantFactory adapters developed into agent-controlled native/plugin/Windows UI automation when necessary. No hidden manual prerequisites; PlantFactory access is not mandatory for the Blender-native G1 fallback. Include neutral beauty and diagnostic renders, collision/contact proxies, and real topology/silhouette variety. Start with geometry and schema quality rather than a requirement to finish production-quality photorealism in one pass.

**Gate G1 — every reference asset passes a round-trip:** profile + stable seed -> editable source -> validated GLB/other documented interchange -> stage/variant comparison -> QA sheet -> publish receipt. Failing assets do not land in the published manifest. Human art review is an explicit gate; validators cannot prove naturalistic appearance.

### Stage 2 — Build one neutral landscape and a Wicked import scene

**Execute:** WORLD-01 authoring/export of Splitstone, with a dense ~512×512 m Wicked renderer test area and a separate ~1×1 km traversable geography exercise. Create equivalent plant instance positions/coverage, a stream/ravine/bluff/wet hollow, rock interfaces, sunlight/overcast/wet states, several visible wildlife proxies and repeatable camera paths. This is a scene/terrain/asset test bed, not a game slice or a promise of future engine APIs.

**Gate G2 — neutral-to-Wicked scene fidelity:** shared source geometry, materials/roughness, instance/seeding manifest, camera routes and comparable coverage are loaded faithfully in Wicked. Compare against neutral source/Blender reference images and hash/instance manifests. Derived WISCENE/shader formats and unsupported/lost attributes are documented; density cannot be reduced quietly to make the performance target easier.

### Stage 3 — Wicked appearance, materials and measured optimization

**Execute:** RND-001 through RND-009 and MAT-001 through MAT-003 with the V1–V10 render/activation experiments in [Rendering experiments](../rendering-experiments.md). Start with reproducible Wicked import and calibrated material/rig fixtures, then measure thin-leaf transmission, alpha mips, roughness, wetness, wind/branch pivots, foliage overdraw, animal-driven shrub deformation, water, weather and stream/reveal hitches. Execute native standalone Wicked builds on the reference computer with repeated 1080p camera paths, genuine CPU/GPU/VRAM timings and side-by-side authored-source visual evidence. [Wicked material pipeline](wicked-material-pipeline.md) is the binding visual production specification.

**Gate G3 — documented Wicked readiness:** compare neutral reference and Wicked moving footage, reproducible build/route manifests, raw frametime distributions (median/P95/P99 and below-30 events), CPU/GPU/VRAM diagnosis and concrete shader/asset optimization tradeoffs. **Provisional performance target:** representative full-scene Wicked P99 at or below 33.3 ms, preferably with headroom; if it fails, record measured bottlenecks and targeted Wicked fixes. This gate does not require building a second renderer or revisiting the engine choice.

### Stage 4 — Minimal real runtime contracts, then a continuously explorable world

Only **after G3**, establish in-process interfaces for SimCore, StalthosState, StalthosSim, FloraSim, FaunaSim, BeastCore, InteractionsCore, HeroSim and HeroView. Begin with a cheap synthetic facade sufficient to test streaming, camera separation, visible browse transactions and persistent scenery exceptions. Actual playable animal life, successive lives and distribution across islands belong in succeeding implementation plans. Runtime composition remains modular, not microservices.

**Gate G4 — visible invariants:** body-relative steering works independently of orbit-camera azimuth; detached-camera sight/hearing does not grant HeroSim information; local wildlife exists before it is revealed; one browse/contact yields one visible change; revisiting a hill preserves recent placement; significant altered trees and retained known animals do not duplicate or resurrect. No forced universal detailed ecological solver.

### Stage 5 — Content breadth and world expansion

Once the pipeline and runtime import are trustworthy, develop generator/rig family coverage and visually distinguishable profiles toward the open-ended fauna and flora palette; test compositions across Main Island, Rainridge, Stone Island and Outer Reach. Compare silhouette sheets, contact reels and animal-scale traversals rather than counts of raw meshes. Add favorite species freely with shared family behavior and profile-driven habitat tags. Never make 50/200 a fixed maximum, a release blocker, or a mandate for hundreds of independent biological subsystems.

## 4. Dependency graph

    TOOL-01 environment doctor
       └─ TOOL-02 schemas/provenance ── TOOL-03 CLI/receipts ──────┐
                                 ├─ TOOL-04 woody branches        │
                                 ├─ TOOL-05 ferns/jointed stems   ├─ TOOL-11 QA/visual sheets
                                 ├─ TOOL-06 fungi/surface assets  │          │
                                 ├─ TOOL-09 creature/animation ───┘          │
                                 └─ TOOL-10 local vegetation contact         │
    WORLD-01 terrain+placements <──────── schemas/asset export ───────────────┘
       └─ Wicked import + material mapping ── thin-leaf/wetness/contact tests ── reference-PC traces
                                      └─ G3 measured Wicked readiness
                                            └─ ARCH-01 runtime contracts
                                                  └─ expandable fauna/flora/world

Arrows are handoff constraints, not rigid serial scheduling. Plant families, creature reference design, terrain reference gathering, the benchmark harness scaffolding and QA review templates can advance **in parallel** once the foundational schema is accepted. Integrate through manifests and published artifacts; do not let all agents edit one canonical scene file simultaneously.

## 5. Technical contracts across all phases

**Offline tool boundaries:** PowerShell launchers and Python orchestration, Blender Python in its own runtime, external tools as versioned adapters. Profiles, interchange geometry and proof artifacts remain engine-neutral; **only derived adapters/compiled artifacts target Wicked**. Scriptable is a requirement; specific Python package versions and optional authoring packages are still **To test**.

**Units and spaces (proposed until fixture validation):** meters, seconds, radians where APIs call for them; a documented right/left-hand transform convention; no invisible unit guessing; colors explicitly tagged linear versus sRGB; tangent handedness verified after import. Prefer glTF/GLB as common exchange, not a hard rule when it loses needed data. Semantic sidecars contain interaction targets, collision proxies and environmental affordances unsupported by the interchange format. Maintain source masters, optimized variants and cooked engine copies separately.

**State ownership:** the future renderer never owns biological truth; flora damage and season come from FloraSim/StalthosState snapshots; InteractionsCore commits an observed visible interaction once; FaunaSim stages cheap local wildlife; HeroView knows camera/image/audio, not the animal's true perception. Track current scene/simulation chunk occupancy without equating it to render culling.

**Determinism:** within a pinned tool set, same normalized profile + seed + assets must reconstruct equivalent geometry and stable names/anchors; bit-identical GPU renders across drivers are **not** required. Record hashes, tool versions, nondeterministic steps and machine profile. A partial failed build cannot overwrite a validated published output.

**Legality:** all downloaded reference photos/scans/textures/meshes need source and license records; “accessible on the web” is not a redistribution license. For optional PlantFactory, keep independently authored plants distinct from licensed PlantCatalog derivations and never assume an exported model grants unrestricted marketplace resale.

**Observability:** log stdout JSON contract, detailed stderr/file logs, diagnostics, geometry counts, texture dimensions/formats, draw/skin cost, estimated and observed resource usage and capture links. Separate visual quality approval from machine validation.

## 6. Suggested repository structure (after G0)

    docs/implementation/             # this plan, decisions and review
    tools/stalthos.ps1               # Windows-first task entry
    toolkit/                         # Python orchestration/validators/adapters
      cli/ schemas/ adapters/ generators/ qa/ tests/
    profiles/
      plants/ creatures/ environments/
    scenes/
      splitstone/                    # neutral terrain, placements, camera routes
    reference/
      index/                         # metadata and permitted small previews only
    assets-source/                   # authored source; LFS policy after sizing
    artifacts/                       # ignored generated builds and receipts
    benchmarks/
      manifests/ routes/ analyses/
      wicked/                        # sole active renderer adapter

**Proposed**, not a directive to instantiate empty packages immediately. Generated caches, third-party executables, downloaded proprietary models and bulk licensed photos stay out of regular Git. Git LFS is for intentionally reviewed large original assets, not a blanket solution to unbounded outputs. Establish .gitignore, LFS rules and storage budget before committing binary data.

## 7. Change control and acceptance discipline

- Each ticket includes owner, input contract, output artifacts, exact reproducibility command, dependencies, proof/capture and pass/fail criteria.
- Keep facts separate from assumptions: **Decided / Proposed / To test / Unknown**. Never turn illustrative scene dimensions or performance guesses into approved universal tunables.
- Every tool or shader optimization needs before/after visual evidence **and** comparable measurements. No static image can alone approve locomotion, branch bending or silhouette shimmer.
- Contracts may be versioned; breaking changes require fixture migration, adapter tests and a research-register entry when crossing domain ownership.
- Automated tests should include reproducibility, source-to-interchange round trip, metadata completeness, duplicate stable ID detection, no-publish-on-failure and meaningful errors on missing optional dependencies.
- Avoid expensive work that doesn't affect close-view visuals, credible ordinary behavior, player-controlled embodiment or visible continuity. Structural complexity requires an observed failure of a cheaper method.

## 8. What this plan deliberately does not authorize

No competing renderer build; no claim that 30 FPS or photorealism has been achieved; no final sizes, map areas or exact terrain distribution; no playable vertical slice; no compulsory science-grade population, hydrology or physiological simulation; no bulk licensing downloads without provenance; no paid API use; no remote agent execution assumed. Work packages can be handed to independent coding agents, but this document does not claim any have been dispatched.

## 9. Documentation traceability

- Product and fidelity: [Vision](../vision-and-principles.md), [Research register](../research-register.md)
- Toolset and six reference plants: [Asset toolkit](../asset-toolkit.md), [Flora](../flora.md)
- Anatomy/hero rig: [Creatures](../creatures.md), [Visual direction](../visual-direction.md)
- Renderer tests and frame target: [Rendering experiments](../rendering-experiments.md)
- Landforms and Splitstone: [World generation](../world-generation.md), [Geography](../geography.md)
- Wildlife/plant catalogs: [Fauna actor catalog](../fauna-actor-catalog.md), [Plant visual catalog](../plant-visual-catalog.md)
- Activation and runtime ownership: [Simulation architecture](../simulation-architecture.md), [Spatial activation](../spatial-activation.md), [HeroSim](../hero-sim.md), [HeroView](../hero-view.md)

Source/vendor facts should be checked against versioned upstream documentation when implemented. The present plan does not assert compatibility of untested engine plugins, PlantFactory automation, graphics capture tools or driver combinations.
