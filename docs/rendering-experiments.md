# Rendering architecture experiments

**Domain:** Wicked Engine visual fidelity, shader and performance experiments. **Status:** Wicked is the active renderer choice after user local testing; full-scene benchmarks remain planned/unmeasured.

## Hardware and objective

Reference target: **NVIDIA GTX 1080 8 GB (Pascal)**, **first-generation Ryzen** (exact CPU/RAM/storage to inspect). Windows-first packaged application. Target native **1920×1080** initially. **30 FPS floor**, with strong preference for 45–60+ FPS.

30 FPS is 33.33 ms/frame; 60 FPS 16.67 ms. Average FPS is insufficient: measure median, P95/P99, 1% lows, >33 ms spikes, streaming hitches, GPU busy time, CPU game/render time, memory and clocks. Any below-30 events must be logged rather than averaged away.

No hardware ray tracing, path tracing or frame generation as the baseline. Software GI, foliage upscaling and modern GPU-driven techniques must earn a measured visual/performance benefit.

## Where the frame budget goes

**Give the pixels the budget; starve the invisible simulation.** The 33.3 ms/frame 30 FPS objective is an *entire-scene* measurement including the Hero Beast, visible fauna, dense plant silhouettes, wind, terrain, shadows, water, weather and scene preparation. A candidate rendering feature is evaluated by visual improvement **per unit of measured frame time and memory**, not purely by geometric sophistication.

Break profiling into CPU main/submit, GPU shading/overdraw, visibility and draw dispatch, foliage wind/shadows, character skinning/IK, local physics/contact, streaming/asset uploads and scene-activation spikes. Test steady as well as camera-turn, sudden reveal and chunk-crossing frames. Measure VRAM and memory traffic; a cheap shader with too much transparent foliage may still be expensive. Minimize CPU per-object update/draw overhead with batched instancing and caches; move structural work to offline generation or bounded background preparation.

**Staged fidelity:** current player motion/contact is prompt; on-screen or potentially revealed fauna use only the animation/behavior sophistication needed to read correctly; obscured nearby fauna may maintain cheap poses/activities without full physics/IK; remote regions are visual proxies and density records. Purely decorative plants have zero individual biology ticks and usually no runtime colliders. Never sacrifice near-view silhouettes/lighting before proving that a cheaper approach cannot preserve them.

Require A/B captures *and* frame-time traces for any quality compromise. Do not encode a blanket low-poly/no-shadow decision based on assumptions; optimize the actual dominant costs.

## Active engine and deferred alternatives

**Wicked Engine is the only active implementation target.** Do not author a Flax adapter or spend this phase running two-engine competitive benchmarks. Maintain authored neutral Blender/PlantFactory geometry, material recipes and GLB interchange independently of Wicked.

The user's local Wicked test provides directional confidence, **not measured proof** that the planned dense woodland, animal contact and full water/weather effects meet the reference-PC frame target. Reopen a second engine only after an explicit decision and a concrete Wicked blocker. The current task graph owns native Wicked import, roughness/alpha packing, foliage/wetness shaders, visual reviews and frame traces.

## Common test bed

Build one neutral reference scene with identical frozen source heightmap/meshes, plant positions/coverage, materials, weather inputs and scripted camera routes on each **Wicked test iteration**. Compare to authored Blender/reference image and manifests. A Wicked optimization must not look faster by quietly reducing density, shadow quality or creature animation.

Proposed benchmark data:
- Detailed terrain patch around 512×512 m and distant lower-detail surrounding views; include a 1×1 km walkable geography test independently.
- Canopy conifers, shrubs, tall detailed ferns, dense low stems, ground litter, boulders, stream and rock interface.
- One fully animated sauropod proxy, plus several animated distant animals.
- Dense woodland, exposed floodplain, stream/cliff interface, animal gathering and storm/wet-scene routes.
- Repeated camera paths at juvenile viewpoint, including sudden turns and fast traversal.

Counts are subject to visually equivalent screen coverage. Preserve a geometry-only, then foliage, then wind, then shadows, then animals, then weather progression.

## Bench protocol

- Record exact engine commit/version, driver, graphics API, GPU settings, scene manifest/hash, executable and reference hardware.
- Standalone release builds; native 1080p baseline; no VSync or framerate cap for throughput capture.
- Warm and cold-streaming tests separately; 3+ steady trials, identical camera route and randomness.
- Use PresentMon for external frame timing/GPU Busy if supported; Tracy or engine instruments for CPU; RenderDoc for frame breakdown. Nsight compatibility on Pascal must be verified; do not assume its newest GPU profilers work.
- Measure GPU vs CPU bottleneck, not just total draw count. Don't sum overlapping processing intervals as sequential.
- Use diagnostic modes to isolate overdraw, shadows, foliage deformation, animation/IK, water and streaming.
- Keep raw captures and scripts, not only summarized screenshots.

**Experimental pass:** P99 <=33.3 ms under representative full-render workload with no recurring severe hitches; a meaningful margin for future ecology/AI is preferable. This *provisional experiment gate* isn't a guarantee that every frame of the eventual game passes. Report actual failing frames.

## Required experiments

**V1 Native foliage:** standard engine instancing/streaming. Record draw calls, visible instances, shader cost and cache invalidation.

**V2 Geometry vs masked cards:** compare equivalent leaf silhouettes, opacity coverage and overdraw. Test broad leaves, fern fronds and dense stems separately.

**V3 GPU grass and patch generation:** deterministic seeds/compact instance streams, vertex deformation, spatial culling and indirect drawing where hardware/API supports them; CPU alternative baseline.

**V4 LOD:** indexed mesh reduction, dithered transitions, clustered leaves, multiview impostors; preserve near and far crown shape with motion.

**V5 Wind:** hierarchical trunk/branch/leaf response plus local animal bending; simplify distant wind; quantify shadow update effects.

**V6 Light:** main sun, restrained ambient/shadow approximation, thin-leaf transmission, contact shadow selection, no costly default GI assumption.

**V7 Water/weather:** normals/flow, riverbank depth blend, wetness and local interaction; no full-world fluid GPU simulation.

**V8 Creatures:** skeletal GPU/CPU cost, foot IK, skin/osteoderm/quill render cost, reduced distant update rates, age morph changes.

**V9 Display-level ecology bridge:** visible browsing, seasonal foliage and wetness update only affected patches; conspicuous saved changes survive reload. Chunk loading requests cheap seeded/seasonal FloraSim appearance plus StalthosState exceptions, not comprehensive individual plant biology.

**V9b Staging/visual decoupling:** **HeroSim/FaunaSim** keep simple active behavior beyond camera visibility with shared cheap BeastCore rules. **InteractionsCore** updates visible contacts; weather/wetness draws from StalthosSim current state. Benchmark chunk reload and long-absence reentry without hidden ecological reconstruction.

**V10 Streaming:** camera route across cell boundaries at varying speeds; monitor stalls, pops, resource residence and distant transition quality.

## Outcome/reporting

Deliver Wicked source revision/build steps, immutable neutral source scene and repeated Wicked benchmark paths, raw timing results, corresponding source/Wicked still and moving captures, shader/material fidelity audits, optimization deltas and explicit release-readiness blockers.

Score both *visual quality* and *frametime/headroom* in Wicked. If Wicked misses either gate, identify specific shader, alpha coverage, LOD, instancing, source geometry or memory bottlenecks and conduct **targeted experiments** instead of guessing. No second engine build or full game implementation authorized here.

## Useful technical leads

- Wicked Engine: https://github.com/turanszkij/WickedEngine
- PresentMon: https://github.com/GameTechDev/PresentMon
- RenderDoc: https://renderdoc.org/
- Tracy: https://github.com/wolfpld/tracy
- meshoptimizer: https://meshoptimizer.org/

For Wicked, verify whether batch instance-buffer updates and local contact shader data can avoid rebuilding whole foliage groups after every browsing event; benchmark rather than assume any particular engine API.

See [Visual direction](visual-direction.md) for appearance requirements and [Asset toolkit](asset-toolkit.md) for reproducible content.

## HeroView and simulation buffer benchmarks

Test orbit-follow without automatic heading recentering, body-relative WASD at every camera heading, local free-camera flight to a soft/hard tether, returning to the animal, collision handling, and tether correction when the animal walks away.

Critically, **SimCore simulation activation must buffer beyond the full local free-camera envelope**. Benchmark flora bulk instantiation, fauna cohort instantiation/retirement, and rendering together while flying the camera over an occluding hill. Animals should already be resting/browsing before revealed, not spawned by renderer visibility. Check CPU spikes, delayed geometry, known-animal duplication and visible popping, and the ability to draw camera-visible creatures Smalltrotter has not perceived. See [Spatial activation](spatial-activation.md).
