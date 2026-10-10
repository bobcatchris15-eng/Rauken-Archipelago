# Stalthos asset-production toolkit

**Domain:** Agent-facing software inventory, offline generation, optimization, validation and reproducibility. **Status:** Production tooling plan — independent of engine and species design.

## Mission

Create a scriptable **Windows-first digital natural-history workshop**. Agents should be able to research, generate, inspect, optimize, import and benchmark an organism through stable tool contracts—without depending on manual GUI clicking for every asset. Source masters remain editable; runtime assets are derived and reproducible.

Prioritize **free/open source and no paid recurring API rates**. Paid/legacy tools may be evaluated but not made hard dependencies without approval.

## Tool inventory

### Essential
- **Blender + Python/bpy**: anatomical master meshes, sculpting, procedural Geometry Nodes, branch/fern generators, rigs, bake passes, headless renders and exports.
- **Python/PowerShell**: orchestration; scientific geometry/data tools, manifests, batch export, QA and reporting.
- **Visual Studio C++ build tools and tested Windows SDK** for the selected Wicked Engine source/build configuration; determine actual required components from the installed version.
- **Wicked Engine** source/editor/standalone build tooling as the sole active renderer. Derived WISCENE and shader outputs must not replace authored neutral masters.
- **Git and Git LFS**: text specs and scripts in ordinary Git; version heavyweight source assets deliberately, with provenance.
- **meshoptimizer / gltfpack**: optimize and simplify static meshes and process glTF with rig/animation checks.
- **AMD Compressonator**: BC texture compression with proper format selection (e.g., BC5 normals, BC7 color where suitable).
- **RenderDoc, PresentMon, Tracy and native profilers**: visual/frametime validation.

### Strong optional candidates
- **PlantFactory** (discontinued perpetual Bentley edition) for procedural trees/plants **when a real installed exporter works**. Probe actual automation, preserve source and branch pivot metadata; PlantCatalog-derived assets have distinct licensing/resale constraints. Blender remains mandatory fallback.
- **Material Maker** or Blender-node recipes for procedural PBR bark, foliage, stone, moss, fungi and skin materials. Include editable roughness, albedo, tangent-space normals, AO and leaf thickness/transmission intent.
- **Krita / GIMP**, optionally **ArmorPaint**, for mask painting, texture corrections, composites and photo processing.
- **Inkscape** for vector diagrams and user-interface artwork.
- **QGIS / GDAL** for terrain GIS data and drainage inspection.
- **Gaea** for terrain experiment reference where licensing/export tiers permit. **RealityScan or other photogrammetry** can produce rock/root/log scans if image rights and local license permit; use CC0 Poly Haven data or own photos otherwise.
- **ImageMagick, FFmpeg** for deterministic image/video postprocessing and render comparisons.
- **glTF Transform, Khronos validators, KTX-Software** where target engine and data formats support them.

Do not confuse asset visualization software (VUE/PlantFactory) with a runtime game engine. The active renderer is Wicked; keep every source profile and editable geometry/material independent of it.

**Machine work packets:** [Wicked PlantFactory/material pipeline](implementation/wicked-material-pipeline.md) and [75-node execution graph](../tasks/README.md). Implement actual version probes, shader/roughness channel mappings and pivot-preservation QA before declaring external authoring automation complete.

## Proposed command-line tool contract

A self-contained 'Stalthos Asset Toolkit' should eventually expose operations such as:
- research_species
- generate_plant
- generate_plant_variants
- build_creature
- rig_creature
- bake_materials
- generate_lods
- render_turntable
- render_growth_stages
- validate_asset
- benchmark_asset
- publish_asset

These are **planned interfaces**, not claims that tools are implemented. Implement them as documented CLI wrappers with deterministic seed and input config. Outputs should be standard JSON status, asset paths, logs, hashes and metrics. Consistent exit codes and actionable errors are more important than a fancy UI.

Example conceptual invocation: generate plant from a YAML species definition, seed 42 and juvenile growth stage, then produce canonical source geometry, optimized exports, neutral render, validation report and metadata. Do not create this CLI during the planning-only repo setup.

## Canonical pipeline

1. **Source/research:** anatomical and botanical literature, labeled living comparators, reference images, usage rights and uncertainty tier.
2. **Parameterization:** species design file (morphology, development, materials, variation, functional interaction points).
3. **High-resolution generation:** Blender / applicable procedural authoring; preserve native source and authored rigs.
4. **Texture/material creation:** scientifically motivated roughness, color, normal, thickness; baking of multiscale structure; avoid baking directional lighting into albedo.
5. **Variants/stages:** seeded individual variations, age proportions, dead/damaged forms and plant phenology where necessary.
6. **Optimization:** geometry reduction and impostors, texture packing/compression, skeleton/update LOD, collision proxy, streaming memory cost.
7. **Interchange:** glTF/GLB where practical, engine-specific conversions only downstream; retain source versions and importer settings.
8. **Quality assurance:** geometry, normals, UVs, skeletal rig and morph targets, surface artifacts, shadow/alpha checks, visual renders and frame-time cost.
9. **Publish:** versioned, validated runtime assets referenced by manifest; generate reproducible build receipt.

## Data and provenance

Every produced asset should have:
- Stable logical ID, species/morphology ID, source version, generation seed, age/stage and individual variant.
- Tool versions, input hashes, licensed references and source/baked file relationships.
- Anatomical/growth parameters and ecological affordance metadata (e.g., edible foliage targets, plant contact bounds).
- Mesh/texture/memory/LOD counts and measured benchmark profile.
- Validation outcome; preview images and automation logs.
- License provenance and redistribution notes (especially PlantCatalog and downloaded references).

Avoid proprietary binary-only source state where agent-controlled serialization is feasible. Keep Blender project files for high-detail editing and declarative configs for reproducibility.

## Breadth-scale production — catalogs are data, not fifty or two hundred separate engines

Plan for **~50 recognizable non-Hero Beast fauna actor profiles and ~200 distinct visual botanical profiles**, with no fixed upper cap. Agents should create and maintain machine-readable manifests, reference images/source metadata, procedural morphology parameters and review sheets. Adding a favorite creature or plant should normally entail adding a profile/assets and habitat tags, not modifying SimCore, FaunaSim or FloraSim.

**Batch tools to support:** silhouette montages at controlled scale; animal pose/walk/rest/feeding/contact reels; plant foliage silhouette and leaf/venation atlases; near/far/wet/dry/season comparisons; procedural variety/duplicate detection; ecological placement previews by island/terrain; per-family shared rig/generator exports. Count forms only when distinguishable by shape/motion, not texture swaps.

**Prioritize generator coverage of genuinely different structures:** quadrupeds, birdlike bipeds, snakes, small mammals, crocodyliforms, flying pterosaurs/birds and conspicuous invertebrates; plant crowns, branching shrubs, ferns with true pinnae, rosettes, jointed stems, vines and aquatics. Share tooling and generic behaviors while protecting each actor's appearance and characteristic movement.

Keep the original six flora reference builds and flagship animal as **pipeline verification only**. They are neither the final vegetation roster nor a reason to restrict subsequent species additions. See [Fauna actor catalog](fauna-actor-catalog.md) and [Plant visual catalog](plant-visual-catalog.md).

## Special plant production

Create branch-aware trees, true rachis/pinna ferns, segmented horsetails, stiff cycads, broadleaf shrubs, moss/lichen surfaces and fruiting fungi as different morphology generators sharing a common export contract. Batch plant instances spatially. For interactive shrubs, retain usable branch/leaf resource targets; for tiny grasses use ecological density patches rather than many individually scripted game objects.

A plant family should yield morphological variants with identifiable species traits; don't randomize so widely that forms stop resembling one lineage.

The asset generator should reconstruct recognizable prominent trees from stable seeds plus compact appearance and **saved conspicuous damage**; no exact identity for every ordinary branch or leaf is required. The renderer receives state snapshots and InteractionsCore change events, never drives biological ticking.

## Special creature production

A rigged anatomical source for the flagship titanosaur with stage-dependent proportions; osteoderm and bristle zones attached to skeleton, underlying scale patterns, pose wrinkle regions, material masks, multiple growth stages and animation contacts. **BeastCore** shared development curves inform appearance from HeroSim/FaunaSim life state. Export validated neutral poses, gait loops, grazing/drinking and head/neck ranges. No animation budget estimates based solely on triangle count.

## Visual review

Automate turntables at fixed angles, closeup skin/frond crops, moving-camera tests, neutral light and sun/overcast/wet lighting, near-to-far LOD comparisons. Review anatomy against actual research references; generated pictures are mood boards, not paleontological proof. Capture before/after images when optimizing.

## Acceptance and failure handling

- Deterministic repeatability from manifest + seed.
- Valid materials/normals/UVs; no inverted/torn meshes.
- Skinning, skeleton hierarchy, bone weights, morph targets and collision correct at all stages.
- LOD preserves silhouette at relevant screen coverage; measure shimmer/ghosting in motion.
- Generated geometry has measured GPU/CPU/memory cost on GTX 1080; report, don't infer.
- Asset generator can fail gracefully with logs; partial exports not published.
- Every external image, scan, library asset and tool license recorded.
- Pipeline can run unattended from a Windows PowerShell entrypoint.

## Initial tool-building experiment

Build the six reference plants from [Flora](flora.md) and the sauropod anatomical proxy from [Creatures](creatures.md). Run generation, bake, **Wicked native import**, turntables, LOD, material shader checks, and target-PC benchmark. This is an **asset/rendering experiment**, not a playable game.

## Vendor/source leads

- Blender: https://www.blender.org/
- PlantFactory/VUE: https://www.bentley.com/products/e-on-software/
- Material Maker: https://materialmaker.org/
- meshoptimizer: https://meshoptimizer.org/
- glTF Transform: https://gltf-transform.dev/
- Compressonator: https://github.com/GPUOpen-Tools/compressonator
- Poly Haven CC0: https://polyhaven.com/
- Smithsonian Open Access: https://www.si.edu/openaccess
- PresentMon: https://github.com/GameTechDev/PresentMon
- RenderDoc: https://renderdoc.org/
- Tracy: https://github.com/wolfpld/tracy

## Stable biological appearance inputs

**Produce a stable visual result with the smallest source description that works.** For most plants and animals, retain identity/seed, morphology variant, age/stage and seasonal appearance parameters. A browsed patch can use a local foliage-density mask or damaged variant, not immutable addresses for all branches and bites.

For a **conspicuous or frequently observed tree**, save missing-limb/death/fall exceptions or optional stable segment IDs so recognizable damage persists. Fine anatomical segment graphs are justified only by a demonstrated close-camera benefit; ordinary branches and leaves need none.

**Acceptance:** browse a recognizable shrub, leave and return to plausible depletion/recovery; topple a landmark tree and reload to find it still fallen. No exact branch-resource accounting, climate-interval replay or invisible historic damage reconstruction. Dense cover uses seeded/patched display variants.
## Camera and activation diagnostics

Asset tests should support active biological chunks prepared before camera visibility, with stable tree-state reconstruction, lightweight creature rest/browse/gaze animations and a HeroView capture path showing body-relative steering, screen-space follow/pan and bounded near-hill camera flight. This is an experimental authoring/render benchmark, **not** a required playable vertical slice. See [Spatial activation](spatial-activation.md).
