# Wicked-first materials, vegetation and visual asset pipeline

**Decision (2026-10-10):** use **Wicked Engine as the single active renderer/runtime implementation target**. The user's local testing favors Wicked. Do not construct or benchmark a Flax adapter as a prerequisite to any current task. This is a *production-direction decision*, **not** a claim that a full dense Rauken scene currently hits the 30 FPS goal.

**Preserve reversibility:** Blender and PlantFactory native masters, neutral GLB/FBX geometry, PBR texture recipes and semantic manifests remain independent of Wicked. WISCENE/compiled shaders/DDS and GPU-ready foliage attributes are derived. Switching engines later must not require recreating source assets.

**Canonical executable task IDs:** `tasks/toolkit-graph.json` (RND-001 through RND-009, PFA-001 through PFA-003, MAT-001 through MAT-003, GEO-001). This document describes contract and art decisions, not alternative scheduling.

## 1. Practical tool priorities

| Category | Default | Optional branch | What agents must prove |
|---|---|---|---|
| Plants, bark structure, leaf topology | Blender Python/Geometry Nodes | **PlantFactory** versioned source+export | Exports preserve scale, identifiable branch groups, UV/alpha intent, editable masters and licenses |
| Materials | Blender nodes + **Material Maker** recipe evaluation | InstaMAT where license/automation allows | Roughness, normal, color, occlusion and thickness are distinguishable, deterministic and legally sourced |
| Surface flaws and masks | Krita/GIMP, Blender texture paint | ArmorPaint if installed/licensed | Editable original layers and true texture-space masks |
| Scanned rock/root/log | Own photos or **Poly Haven** CC0 sources with rights receipt | RealityScan/RealityCapture or another licensed photogrammetry tool | Correct meter scale, UV seams, low-poly bake, origin metadata and permissible reuse |
| Tangents, GLB, LOD | Blender glTF exporter, meshoptimizer/gltfpack with protection | glTF Transform/validator | LODs keep leaf and branch pivot semantics; optimization can't silently strip sidecars |
| Runtime textures | Engine-verified DDS/BC formats, tested Compressonator/NVIDIA tools | KTX or fallback as supported | Wicked-supported channel packing, alpha/mip, normal orientation and real memory footprint |
| Native GPU proof | Wicked standalone, PresentMon/RenderDoc/Tracy where supported | other evidence-gathering utilities | Measured on exact GTX 1080 / first-gen Ryzen; no speculative performance or Pascal-only nonexistent counters |

**External-tool rule:** an option is evaluated, not silently treated as a required dependency. Do not invent PlantFactory command-line flags, Unreal Pivot Painter compatibility, Material Maker APIs, compression settings or scanner export paths. First probe installed version and executable behavior; if an operation is GUI-only, label it manual and offer a Blender-native fallback. Never force users to buy software or approve a third-party license just to pass G0.

## 2. PlantFactory -> Blender -> Wicked

1. **Audit** PlantFactory edition and native source/export format. Bentley's sunset/perpetual versions and separate PlantCatalog distribution constraints need exact version-specific license evidence before any assets are redistributed. PlantCatalog-derived and fully custom PlantFactory assets receive different provenance tags.
2. **Author** credible woody plants with structured trunks, branches, needles/leaves and age variants. Preserve editable PlantFactory project where licensing permits, plus exported branch/submesh hierarchy.
3. **Normalize** meter scale, pivots, axes, UVs, opacity, double-sided surface intent and material IDs via Blender. Keep sidecar source-to-derived IDs.
4. **Retain wind semantics**: root influence, parent branch IDs, local bend pivots/axes, mass/stiffness, leaf tip/fold regions, wind masks and mouth/browse collision regions. Treat Pivot Painter-style attributes as a *data design*, not an expectation that an Unreal exporter runs in Wicked.
5. **Optimize carefully**: after meshoptimizer/gltfpack/LOD generation, compare custom attributes and branch IDs against source. If unsupported attribute data is stripped, store and verify the exact remap/sidecar. Reject or explicitly flag irrecoverable pivot loss.
6. **Consume in Wicked**: GPU instancing, shader vertex bending and a local animal contact field; avoid a physics body per leaf. Camera proximity by itself must never bend leaves or stage an animal.

**G1 fallback:** Native Blender botanical generators are the guaranteed implementation path for all six reference plants. An absent or GUI-only PlantFactory cannot prevent publishing those bundles. PlantFactory adapters may remain blocked awaiting local installation without stopping the backbone.

## 3. Material semantics, not a generic texture pile

Every authored family provides an engine-neutral recipe/profile declaring:
- `base_color` **sRGB**, `normal` **tangent-space linear**, `roughness` **linear**, metallic (normally 0 for biological nonmetals), AO, and optional height/thickness/transmission;
- color and texel scale per material, e.g. waxy upper leaf, matte lighter underside, irregular bark, porous stone, wet sediment, damp moss, skin scales and osteoderms;
- alpha cutout, double-sided or thickness/shadow intent, mip alpha-coverage correction and foliage normal treatment;
- source license, authorship, procedural seed/graph version, hash, output resolution and compression plan;
- dry/wet response and optional cavity/substrate wetness mask.

**Wicked adapter owns final GPU layout:** inspect the **pinned engine commit's material and shader definitions**, then explicitly map neutral sources into that revision's channel packing and DDS formats. Do not assume the packing in a third-party Unreal texture preset matches Wicked. Produce material-channel debug output, calibrated texture-swatch screenshots, and **before/after** compression comparisons. Validate BC5/BC7 support and alpha behavior on target hardware.

For roughness: image-derived \"roughness\" is an estimate, not a measurement. Evaluate under fixed neutral HDRI, overcast, forest shade, low sun and backlight. A consistent specular highlight shape and texture scale matter more than a high-resolution photograph.

## 4. Wicked shader families to implement and measure

### Thin vegetation
- Thick stem/root bark: opaque microsurface, world-/UV-aligned detail as appropriate, crevice ambient response.
- Broadleaf/fern pinna: two-sided thin foliage material with controlled normal bias, distinct face/underside, optional transmission from thickness and sun-facing orientation, cutout/mip treatment.
- Conifer needle spray: geometry-versus-masked-foliage comparisons at fixed silhouette/coverage; anisotropic-looking highlights only if measured useful.
- Fungi/moss: damp cavity normals, subtle roughness shifts and soft rim/transmission only where physically sensible.

### Surface wetness
- Leaf cuticle: roughness/specular changes with discrete droplets/accumulation only at visible scales.
- Bark: nonuniform darkening and cavity moisture; avoid making every trunk uniformly glossy.
- Porous rock/soil: microdetail contrast, dark wet patches, crevice pooling and oriented runoff masks.
- Mud/moss: distinct saturated material response and soft diffuse microstructure.
- Transition/water contact: wet bank overlays and persistent puddle masks as **display state**, not full surface fluid transport.

### Deformation and density
- Local wind via plant hierarchy and branch stiffness, separate small-leaf flutter.
- Animal-local contact field/capsule impacts; branches bow around Smalltrotter and return smoothly; mouths reach actual browse groups.
- Close juvenile-height moving views, geometry vs alpha overdraw, double-sided shading cost, shimmer and shadow stability.
- Defer advanced GI, volumetric effects and higher-cost contact approaches until reference-PC captures show where time is going.

## 5. Measurable gates

**Source/rights:** native source path and checksums + cited/license-confirmed reused bytes, correct original-vs-catalog designation, no huge third-party caches committed.

**Geometry:** meter-calibrated bbox, validated glTF, UV/tangents/normals, growth/stage distinction, rig sockets, alpha coverage, semantic branch pivots and collision/browse groups.

**Material:** base/color-space separation, inspected normal handedness, packed roughness/metal/AO mapping, visual wet/dry/reverse-lit evidence, compressed size and measured load/cost.

**Scene:** neutral Splitstone manifests/positions/routes imported to Wicked in full; neutral-vs-Wicked screenshots identify lost features, not a Flax-vs-Wicked contest.

**Target machine:** actual GTX 1080 8 GB + early Ryzen, native 1920x1080, repeated route captures; record frametime P50/P95/P99, below-30 events, VRAM and CPU/GPU bottlenecks. P99 <= 33.3 ms remains a *goal*, not a claimed result. Every material and foliage optimization requires side-by-side moving evidence and measured time.

**Engine contingency:** only revisit other engines if a measured Wicked integration/quality/performance blocker justifies it and the user requests new comparison work.

## 6. Repo-backed working contracts

- `profiles/materials/` and `reference/materials/` — procedural source and rights metadata, not downloaded unlicensed photography.
- `toolkit/adapters/plantfactory/` — opt-in source exporter/importer, wind pivot semantics and actual feature probes.
- `toolkit/materials/` and `toolkit/adapters/wicked/materials/` — neutral recipe and tested derived packing.
- `toolkit/adapters/wicked/shaders/foliage/`, `shaders/wetness/`, `shaders/contact/` — authored Wicked shader variants, only when tested.
- `toolkit/adapters/photogrammetry/` — scanned rock/roots/logs with CC0/self-authored provenance, plus Blender fallback.
- `benchmarks/wicked/` — compiler/build fixtures, import quality and reference-PC metrics.
- `assets-source/`, `artifacts/`, local `cache/` — source masters and regenerable outputs kept separate.

These are planned implementation paths; the presence of this document does not assert the tools, plugins, engines or assets have been installed or generated.
