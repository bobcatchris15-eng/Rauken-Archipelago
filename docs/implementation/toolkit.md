# Toolkit implementation — detailed work breakdown

**Status:** Proposed, implementation-ready work specification; no implementation exists yet.  
**Parent:** [Roadmap](README.md). **Agent interfaces:** [Parallel work packages](parallel-work.md).  
**Scope:** a Windows-first, reproducible, engine-neutral digital natural-history workshop. Build real scripts and sample assets in this order, **not a playable vertical slice**. Runtime engine remains undecided.

## A. Design invariants

1. **Observable art is the product.** Spend offline effort on silhouettes, anatomy, branch hierarchy, textures, normals, LODs, believable placement and movement. Do not develop hidden growth/energy/food-web solvers to prove the toolkit.
2. **An agent must operate it without clicking.** Every essential operation has a documented CLI path, machine-readable result, deterministic seed handling, actionable diagnostic and a test fixture. Blender GUI can remain available for expert manual revisions.
3. **Source is recoverable.** Declare morphology in human-editable profiles, preserve .blend or similar native masters and bake optimized exports as derived, hash-addressed artifacts.
4. **One neutral canonical handoff.** Blender/source producers do not emit Flax-only or Wicked-only authored masters. Engine adapters transform a shared interchange/manifest after asset QA.
5. **Aesthetic acceptance is separate from schema validity.** Renders, moving reviews, silhouette contact sheets and human scrutiny decide whether something is good-looking; validators decide whether it is repeatable, importable and correctly licensed.
6. **No unbudgeted dependencies.** Prefer free/open-source tools and local inference/production. A third-party package, cloud API or proprietary asset library cannot become mandatory without a version/license/provenance review.
7. **Do not certify performance by topology alone.** Test overdraw, shadowing, draw calls, skinning, upload/streaming and GPU memory on the stated reference computer when available.

## B. Foundation: tasks TOOL-01 through TOOL-03

### TOOL-01 — Windows toolchain and environment doctor

**Input:** fresh Windows checkout; user-installed tools may be absent.  
**Owner:** tooling/infrastructure worker. **Depends on:** none.

Implement a single PowerShell entry point with a read-only discovery command. Initial runtime proposal: Windows PowerShell launcher compatible with Windows PowerShell 5.1 where feasible; support PowerShell 7 without requiring it. Python 3.x with a **pinned tested minor version** for orchestration; use an isolated venv and lock file once dependencies are verified. Do **not** make Blender's internal Python inherit incompatible host-site packages.

Probe and report:
- OS build, architecture, processor, RAM, GPU, dedicated VRAM, graphics driver and current display modes;
- Git, Git LFS, Python executable/version, Blender executable/version and supported Blender background mode;
- available C++ compiler, Windows SDK, .NET/Flax build dependencies, optional Wicked/Flax source locations;
- meshoptimizer/gltfpack or glTF Transform, Khronos glTF Validator, Compressonator, Material Maker, KTX tools if available;
- RenderDoc, PresentMon, Tracy and optional image/video tooling;
- optional PlantFactory, without making it a blocking dependency;
- disk free space, target cache/artifact locations, and permission to create scratch files.

**Rules:** no silent installations or license acceptance; never download large binaries on doctor. Tool paths must be overrideable via a local untracked config or env vars. Produce a compatibility/capability matrix, not a fabricated yes/no for unknown tool behavior. Distinguish **Required for current command**, **Optional**, **Missing**, **Untested** and **Incompatible**.

**Artifacts:** tools/stalthos.ps1; toolkit/doctor; docs/toolchain-setup.md; versioned tool lock manifest; mock test fixtures.  
**Command target:** .\tools\stalthos.ps1 doctor --json  
**Acceptance:** succeeds and reports capabilities when optional tools are absent; exits with a documented nonzero code for critical environment failures; gives exact tool/version/path and fixes; does not mutate tool installations. Run once in a minimally provisioned shell and once on the reference PC.

### TOOL-02 — schemas, naming, provenance and sample profiles

**Owner:** data/contracts worker. **Depends on:** initial TOOL-01 path and decision on CLI packaging; can draft independently.

Define **versioned JSON Schemas** (2020-12 or another pinned, documented draft) for:
- toolchain.lock / discovered capability record;
- asset profile shared identity and kind-specific plant/creature/material/environment payloads;
- references and usage rights/provenance;
- input build manifest + upstream/source hash graph;
- neutral output asset bundle and engine import sidecars;
- skeleton/attachment, collision and interaction affordances;
- validation, preview and benchmark receipts;
- deterministic instance placement and terrain layer manifests.

Use YAML **only as an author-friendly profile format** if its parser is pinned, secure and validates against the same JSON Schema; generated receipts and machine exchanges should be canonical UTF-8 JSON. Do not invent unvalidated duplicated truth between YAML and JSON.

**Minimum common fields (proposed names):**
- schema_version, logical_asset_id, asset_type, display_name, profile_revision, generator_family, source_content_sha256;
- morphology variant ID, generation_seed, age/life_stage, season/appearance state where relevant;
- source attribution, license ID/text or URL, copyright and whether the reference may be distributed versus cited only;
- tool and adapter versions, input dependency hashes, transform/coordinate metadata and deterministic sub-seed derivation;
- measured dimension bounds, export paths, mesh/material/texture/rig summaries and preview paths;
- habitat/suitability and food/browse tags only as cheap *metadata*—not full ecological parameter vectors;
- semantic affordances such as branch bending groups, plant bite regions, sockets, bone tags, collision proxies and foot/mouth contact points;
- QA flags, human-review status, publish eligibility and engine-specific conversion notes.

**Identity:** a fictional taxon/form ID is different from a generator family, asset revision, seeded appearance variant and placed-world instance ID. Maintain stable logical IDs independent of file paths or procedural node order. Derive reproducible sub-seeds using a specified stable hashing algorithm, never the randomized default Python hash. Instance IDs must survive reexport and transform changes where intended. Model normal unimportant variation as reproducible seed+profile, conspicuous scar/damage as sparse overrides later.

**Contracts:** units in meters, documented handedness/axis conventions at each boundary, explicitly tested conversion to glTF and each candidate engine, agreed up/front vectors, time units, stage units, animation names, material color-space tags. Bake/export scales and coordinate transforms must be validated by a calibrated cube, reference biped and ground alignment fixture. No undocumented axis swaps.

**Artifacts:** toolkit/schemas; toolkit/schema-validators; profiles/plants/softbough.yaml, profiles/plants/royal-frond.yaml, profiles/creatures/smalltrotter.yaml; fixture references and expected failures; schema changelog.

**Acceptance:** fixtures round-trip deterministically; missing license/ID/axis/scale/rig or invalid references fail with field-level diagnostics; a staged version upgrade can be detected; profile extension does not require rewriting a runtime module; valid profile is accepted with no renderer installed.

### TOOL-03 — CLI commands, build graph, status receipts, publish

**Owner:** core CLI worker. **Depends on:** TOOL-01 and approved TOOL-02 schema v0.1.

Start with **actually implemented** commands before exposing every planned verb as a fake success:
- doctor; profile validate; build plant; build creature-proxy; preview turntable; qa asset; export neutral; publish; batch run.
- Planned later aliases/verbs from [Asset toolkit](../asset-toolkit.md): research_species, generate_plant_variants, rig_creature, bake_materials, generate_lods, render_growth_stages, benchmark_asset.

Suggested interface (syntax is **proposed**, not a claim of existing commands):

    .\tools\stalthos.ps1 doctor --json
    .\tools\stalthos.ps1 profile validate profiles/plants/softbough.yaml
    .\tools\stalthos.ps1 build plant --profile profiles/plants/softbough.yaml --seed 42 --stage juvenile
    .\tools\stalthos.ps1 preview turntable --asset-id plant.softbough --lighting neutral
    .\tools\stalthos.ps1 qa asset --asset-id plant.softbough --strict
    .\tools\stalthos.ps1 publish --asset-id plant.softbough --review approved

**Execution model:** wrapper -> canonical config+input hashes -> ordered dependency DAG -> isolated scratch workspace -> external tool subprocesses (Blender background/bpy, compressors etc.) -> validation -> atomic staged publish. Each operation is resumable at artifact granularity, idempotent for identical inputs, and independently re-runnable. Keep stdout as one JSON result or streamed documented JSON Lines; details go to structured log files and stderr. Never mix banner text into the machine-readable stdout stream.

Recommended receipt fields: operation_id, command, status, started_at/ended_at, tool_fingerprint, schema_version, input_hashes, seed, artifact list with sha256, metric paths, preview paths, warnings/errors, exit_code. If reproducibility is conditional (e.g. GPU render), label it. If a blender script or image bake crashes, mark the build failed and leave prior published artifact untouched.

**Exit contract (proposed):** 0 success; 2 bad arguments/profile; 3 missing/unsupported dependency; 4 generation/export failed; 5 QA failed; 6 publish/provenance refused; 7 benchmark unavailable or capture failed. Detailed errors still have stable machine codes (e.g. missing_blender, invalid_uv, unlicensed_reference, unresolved_interaction_socket).

**Artifacts:** CLI package, deterministic build/cache manager, Windows launcher, adapter capability registry, receipt builder, golden tests and developer guide.

**Acceptance:** zero manual clicks for reference build; interrupt/retry does not publish partial assets; a broken source dependency invalidates only affected downstream cache entries; no stale preview or run result falsely claims success. Empty profiles and intentionally corrupt GLBs fail for the right reason.

## C. Morphology generators: tasks TOOL-04 through TOOL-08

Use Blender Python/Geometry Nodes as the principal authored geometry route, with source files tracked deliberately. Default to specialized **structural families**, not one random mesh generator masquerading as 200 species. Separate base topology, named botanical/anatomical parameters, age, appearance and seeded irregularity. Tests must compare actual silhouette at animal eye height.

### TOOL-04 — woody trees and flexible shrubs

**Reference assets:** Splitcrown and Softbough, plus exploratory sample of differing branch architectures.  
**Outputs:** editable branch/trunk hierarchy, root flare, age variants, leaf placement, native asset, neutral GLB, LODs, simplified wind hierarchy, individual/cluster collider proxies, semantics for bending and browsing. Tree branch allometry can be stylized but should not look like procedural cylinders stapled together.

**Build order:** branching grammar + hierarchical nodes; bark/root/trunk geometry; shoots/leaf or needle geometry and UVs; asymmetry/seasonal/age controls; LOD/impostors; wind masks; Softbough contact envelope/browse zones; turntables in three growth stages and juvenile-height walks.

**QA:** correct attachment and plant-ground integration; recognizable species shape survives variance; browse targets at plausible height; deformation recovers; no detached leaf cards; canopy and wind remain convincing as camera moves. A saved, conspicuous missing limb can be represented by a compact damage override without mandatory segment IDs for every branch.

### TOOL-05 — ferns, compound fronds and segmented plants

**Reference assets:** Royal frond, Basketfern, Jointreed.  
**Outputs:** rachis/pinna structure with correct frond curvature and progressively smaller pinnae; different crown/frond families; segmented/jointed horsetail stems and whorls; growth-stage/litter variants, stiffness and wind masks.

**QA:** side-view silhouette distinguishes Royal frond from Basketfern and from crossed cards; pinna anatomy is visible close up without obvious periodic artifacts; Jointreed thickets hold separate crisp stems, not merely color-tinted opaque tubes; far representation avoids shimmering and alpha-overdraw blowup.

### TOOL-06 — fungi, moss, litter, and substrate integration

**Reference:** bracket fungus attached to a decaying log; optional gilled fungi/lichen test patches only when foundational interface is ready.  
**Outputs:** substrate-anchor interface, dampness/death/wetness material variants, decals/geometry transition at the log, batchable scatter, contact-scale texture tests.

**QA:** not floating, not repeated identically everywhere, believable material response in overcast/wet light; source attribution preserved. Decorative fungus can remain static; do not build a nutrient network.

### TOOL-07 — procedural variant/composition system

**Inputs:** approved shape family + morphology profile + world/habitat tags + stable seed.  
**Outputs:** constrained species-preserving variants, local canopy/understory grouping, density placement maps, per-view silhouette review sheets, repeat/redundancy metrics, recoverable instance transforms.

**Variants:** branch ratios, crown asymmetry, leaf structures, stem stiffness, broken/dead foliage and species age only within approved ranges. Material recoloring does not count as a unique plant species. Leave room for rare conspicuous shape variants and named landmarks. Site water/soil/sun relationships come from world-generated suitability masks, not white noise.

**QA:** same seed/profile recreates same positions and shape metadata; nearby hill revisit retains placement; a different seed is visibly variable yet recognizably same species; no obvious checkerboard/random-uniform density pattern. A scene should have recognizable dominant forms and rare discoveries without distributing every plant everywhere.

### TOOL-08 — offline material and optimization pipeline

**Inputs:** editable high-poly/geometry, target visual budget and import capabilities.  
**Outputs:** UV-validated bakes for base color, tangent-space normals, roughness, ambient occlusion where useful, material masks, optional thickness/transmission, compressed target textures, selected mesh/leaf representation, LODs and controlled impostor comparison.

Evaluate geometry-vs-masked-card leaf treatments *per morphology family*: broadleaves, small fern pinnae, needled sprays and dense stems have different overdraw/triangles tradeoffs. BC5 normals and BC7 color are potential PC targets subject to engine/driver support and test. Preserve source color space and alpha mode, alpha coverage across mips, normal handedness, double-sided leaf intent and transmission approximation. Do not bake directional sunlight into base color.

**QA:** neutral diffuse/material passes, tangent seams, invalid UV/tangent/normal detection, texture paths/content hashes, silhouette continuity across LODs, shimmer in moving imagery, material/draw-call and VRAM cost in engine. Real asset quality never receives an unconditional fixed triangle count invented in advance.

## D. Hero reference and interactions: TOOL-09, TOOL-10

### TOOL-09 — Smalltrotter anatomical proxy, shared rig contract and contact clips

**Owner:** creature art/animation worker. **Depends on:** TOOL-02/03, export validator and renderer-neutral rig convention.

Build a recognizable **dwarf titanosaur proxy**, not a generic cylinder lizard:
- true anatomical juvenile versus heavier adult proportion profile;
- comparatively shaggy/sparse quill-like juvenile nape/shoulder silhouette, much sparser as adults; quills explicitly speculative;
- scattered increasing osteoderm and wrinkle/skin features, real feet/neck/tail mass, eye/head details for readability;
- a single documented skeleton/IK/animation interface with stage-specific parameters, additive neck/tail/head/eye posture and sockets for browse/drink/contact;
- test walk, rest/stand, feed, drink, idle gaze, turn, and simple collision/balance poses (clips can be rough at first but must genuinely play after export).

Supply rig/skeletal GLB, bind poses, weight verification, animation timestamps, LOD/morph method and turntable/video evidence. Preserve stage transitions without requiring full dynamic growth mechanics or detailed physiology. Nonplayer animal families later reuse the rig/animation contract where anatomically appropriate, but **do not** assume that every actor should share one body plan.

**QA:** no broken weights, toe/foot sliding in reference walks, badly deforming neck or armor; quills do not uniformly resemble porcupine spikes; actual rig and animated import supported by both engine candidates or conversion limitations declared. Performance claims require actual skin/animation benchmark.

### TOOL-10 — bending shrub / local-physical contact display contract

**Owner:** foliage interaction and renderer adapter worker. **Depends on:** Softbough geometry, collision proxies, engine test hooks.

Design engine-neutral data for **contact capsules or surface volumes**, flexible plant group weighting, bending direction/amplitude limits, recovery curve and priority when multiple bodies press through one stand. Future runtime consumes temporary contact info from local actors, not per-leaf simulated forces.

Initial implementation options to test:
1. Batched vertex-shader deformation driven by a small bounded list of nearby animal contact fields plus wind masks.
2. A few branch-bone transforms for foreground named plants, with cheap regular instancing elsewhere.
3. A hybrid with animation zones activated only around bodies.

**Bench proof:** a moving Smalltrotter proxy pushes through Softbough/ferns that bend/part/recover instead of clipping dramatically; leaves continue wind response; no detached branches; contact is local and measured against a no-contact baseline. Fallback reductions require A/B visual and frame timing evidence, not a preemptive decision to let animals ghost through shrubs.

## E. Research/provenance, QA and publication: TOOL-11, TOOL-12

### TOOL-11 — reference and usage-rights ledger

References are **source material and evidence**, not automatically redistributable textures. Required record per visual source: canonical URL/DOI where applicable, publisher/creator, capture/retrieval date, declared rights/license, allowed modification/attribution/distribution, evidence role (anatomy, botanical morphology, material, landscape mood), uncertainty, and whether original content is stored in repo.

Reference families to gather for eventual review: Main Island (Driftless/Baraboo, Wisconsin sand plain and buttes, Catskills/Appalachians, Scottish Highlands, pine barrens, selected South African terrains); Rainridge (Olympic temperate rainforest and Great Smoky Mountains humid coves); Stone Island (Yucatán/cenote and Costa Rican karst); Outer Reach (tsingy-like pinnacles and badlands). Treat these as **form/lighting references, not species or geology prescriptions**. Attach actual high-resolution originals only when reuse terms permit; otherwise store citations/links and separately authored derivative instructions.

For optional PlantFactory: record exact installer/version, test scripted batch export availability, verify provenance of every PlantCatalog-derived asset, and do not confuse permitted inclusion in a game with unrestricted asset marketplace resale. No hidden dependency on deprecated plugins or GUI-only projects. Independently modeled Blender/PlantFactory plants should be flagged distinctly from PlantCatalog variants.

**QA:** publication halts on missing legal provenance for external base meshes/textures, not on purely linked documentary references requiring no redistribution. No invented scientific sources, exact fossil claims or assumed public-domain status for modern photos.

### TOOL-12 — automated visual review and publish gate

Build repeatable cameras and comparison modes:
- orthographic silhouette atlas by life stage, scale, and fixed angles;
- neutral material/albedo/roughness/normal/depth passes;
- sun/overcast/rain-wet appearance; eye-height forest/frond views;
- wind/bending, staged animal poses, grazing/reach and rigged gait video loops;
- LOD/impostor moving-camera A/B with stable framing and sun position;
- side-by-side morphology sample sheets and nearest-neighbor visual similarity warnings;
- scene placement maps and near/far clipping/occlusion comparison.

Attach a human review rubric for anatomy, silhouette uniqueness, branch/frond credibility, skin/rock scale, lighting, ground integration, repetition, stage realism and moving-contact credibility. Automated image similarity is a triage signal, **not** a basis to decree 200 distinct species or 50 distinct animals.

**Publish gate:** schema/provenance/geometry/UV/material/rig/collision/affordance validation passed; captures and tool versions exist; operator review approved or clearly marked provisional; output hashed and promoted atomically. Only published stable bundles may be consumed by engine benchmark adapters; unreviewed experimental assets remain discoverable but not presented as production-ready.

## F. Scene and performance infrastructure interfaces

These are toolkit outputs feeding other work, not responsibilities for the botanical mesh generators.

### WORLD-01 — Splitstone exporter

A reproducible neutral terrain package: visible ravine and stream grading into open valley, outcrop/bluff or caprock remnant, mossy wet seep, mixed woodland, large boulders, believable margins and passability for juveniles. Compose striking features intentionally; do not run full geological time reconstruction. Use heightfield/terrain where sufficient and separate true 3D meshes for undercuts, caves, cliff overhangs or bank cuts.

Required sidecars: material/strata masks, precomputed moisture/sun/substrate fields, stable landmarks/instance IDs, coarse accessibility/collision data, stream surfaces and water direction, placement seeds, dense comparison patch bounds, camera routes. Document blend seams, physics contact surfaces and asset unit convention.

### BENCH-01 — comparable engine import fixtures

Import same package to isolated Flax and Wicked projects. Adapter consumes **published** toolkit neutral bundles, not author-only .blend scene assumptions. Both must identify missing/unsupported shader/rig features, apply documented substitutions and report whether visual parity survives. WISCENE and Flax-native cooked formats are **outputs** of adapters, never the sole source master.

### BENCH-02/03 — visual + frame timing

Profile after representative dense lighting/wind/foliage and hero movement exist. Preserve capture manifests, standalone build hashes, driver/API, resolution, actual CPU/GPU clocks, benchmark camera path, cold/warm distinction, PresentMon frame data where supported, RenderDoc captures and Tracy/engine CPU measurements. Show separate medians/P95/P99, low-FPS events, GPU busy, CPU cost, allocations, upload spikes, VRAM and scene parity checklist. Prefer measured frame traces over intuition about draw-call/triangle counts.

## G. Proposed command and artifact examples

These are **target interfaces for implementation and testing**, not installed commands. Define them in fixtures and execute only once implemented.

    .\tools\stalthos.ps1 doctor --json
    .\tools\stalthos.ps1 profile validate profiles/plants/jointreed.yaml
    .\tools\stalthos.ps1 build plant --profile profiles/plants/softbough.yaml --seed 42 --stage juvenile
    .\tools\stalthos.ps1 build plant --profile profiles/plants/softbough.yaml --seed 43 --stage adult
    .\tools\stalthos.ps1 build creature-proxy --profile profiles/creatures/smalltrotter.yaml --seed 42
    .\tools\stalthos.ps1 qa asset --asset-id plant.softbough --strict
    .\tools\stalthos.ps1 publish --asset-id plant.softbough --review approved
    .\tools\stalthos.ps1 batch run --manifest benchmarks/manifests/reference-pack.json

Example neutral bundle layout:

    artifacts/builds/<hash>/
      source/            # native editable master or source reference
      exchange/          # neutral geometry, textures and animations
      semantics/         # sockets, browsing, collision, bend groups
      previews/          # silhouettes, renders, motion, contact sheets
      reports/           # diagnostics, memory, provenance, metrics
      receipt.json       # inputs, versions, hash graph and status

**Filesystem rule:** scratch/build directory may be deleted/recreated; source masters, approved profiles and references must not depend on it. Publish points to complete immutable bundle IDs; latest is a reference/manifest pointer, not a mutable partially overwritten directory. Artifacts may be reused from local cache and explicitly exported to Git LFS/cloud storage later when rights/costs permit.

## H. Test ladder and quality gates

| Level | Required proof | Reject when |
|---|---|---|
| T0 contract | JSON Schema, golden known-good/bad profiles, ID/seed/units fixtures | invalid profile silently coerced; IDs collide |
| T1 deterministic build | repeat same seed/profile/tool fingerprint twice; inspect geometry, anchors and hashes | uncontrolled geometry changed, old output clobbered |
| T2 exporter round trip | origin/scale/axes, normals/tangents/UV, animation and transparency | flipped rig, detached foliage, corruption |
| T3 morphology | six botanically different reference forms and life-stage Smalltrotter | same silhouette repainted; bristles/osteoderms implausible |
| T4 visuals | neutral/outdoor turntables, full-scale near and traveling camera reels | appeal only in one render, clipping, seam/LOD pop |
| T5 contacts | visible Softbough parting/bending, grazing region depletion prop, foot/terrain contact | collision without visual response; double-consumption |
| T6 imports | same published bundle usable through both engine adapters with explicit losses | undocumented feature dropping or untracked manual repair |
| T7 hardware | equivalent dense full-scene timed traces and VRAM/CPU split on reference PC | average-only FPS, unlogged hitches or misleading density |
| T8 catalog expansion | add a structurally distinct plant and actor profile through the documented pipeline | core simulation module rewrite or license ambiguity |

T5 visible-depletion semantics can use temporary demonstration fixture values until InteractionsCore exists; don't build actual growth/population engines into the toolkit. T7 is an **experiment**, not a certification that the game meets its eventual frame goal.

## I. Recommended implementation order (concrete)

- **Pass 1, integration spine:** TOOL-01 doctor, TOOL-02 profile/common receipt schemas, TOOL-03 CLI validate/build/QA with a primitive geometric fixture, clean failure path and documented local invocation. No external texture or large asset purchase.
- **Pass 2, structural breadth:** TOOL-04 Softbough/Splitcrown, TOOL-05 Jointreed/Royal frond/Basketfern and TOOL-06 bracket fungus in parallel using frozen v0.1 schema. Each returns source, neutral export, anchors and fixed-camera previews. TOOL-08 bakes/LODs and TOOL-11 rights ledger can proceed alongside.
- **Pass 3, movement and publication:** TOOL-09 Smalltrotter proxy/animations, TOOL-10 contact bending, TOOL-12 validation montage/review and atomic publish receipts.
- **Pass 4, scene test:** WORLD-01 neutral Splitstone export, BENCH-01 consistent Flax/Wicked import; fix format losses at producer or adapter boundaries with versioned tests.
- **Pass 5, measured engine selection:** BENCH-02/03 repeatable full-scene runs and written engine decision. Only thereafter approve broad runtime implementation.

**Suggested first agent task:** implement TOOL-01 plus a one-page actual machine report and dependency pin proposal; in parallel have another agent *draft*, not land, TOOL-02 schemas and sample Softbough/Smalltrotter manifests. After the first schema approval, fan out geometry, creature, terrain and QA work. Do not ask five independent workers to choose five incompatible profile formats.

## J. Vendor verification pointers (snapshot, verify at execution)

- Blender official manual: background Python and command-line rendering supported; keep exact installed version in receipt. https://docs.blender.org/manual/en/latest/advanced/command_line/
- Flax official build/headless CLI docs (e.g. editor headless Game Cooker); confirm local source and export/import automation. https://docs.flaxengine.com/manual/editor/advanced/command-line-access.html
- Wicked official repository: Windows source build, editor and GLTF/GLB imports; test actual conversion to WISCENE. https://github.com/turanszkij/WickedEngine
- Bentley e-on/PlantFactory: perpetual editions and PlantCatalog-derived distribution limitations; verify exact FAQ. https://www.bentley.com/products/e-on-software/
- meshoptimizer: https://github.com/zeux/meshoptimizer
- glTF Transform: https://gltf-transform.dev/
- Khronos glTF Validator: https://github.com/KhronosGroup/glTF-Validator
- PresentMon: https://github.com/GameTechDev/PresentMon
- RenderDoc: https://renderdoc.org/
- Tracy: https://github.com/wolfpld/tracy

These links are leads for implementers, not proof that installed releases, license texts, exporter automation or Pascal profiler compatibility have already been tested.

## K. Definition of complete for the toolkit *experiment*

G1 may be accepted when every one of the six reference botanical assets and the Smalltrotter proxy has an editable source, pinned input manifest, neutral importable export, suitable semantic sidecar, preview/contact/animation evidence as appropriate, license provenance, structural QA result and hash-stable receipt; a clean worker can reproduce them from documented Windows commands; and important failures are diagnosable without hand editing. **Good visual quality is a separate human gate.** The *final production-grade library, engine choice, full archipelago and complete actor roster are deliberately beyond G1*.
