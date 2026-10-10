# Rendering architecture experiments

**Domain:** Evidence-based engine and renderer selection. **Status:** Planned trials only; no measurements yet.

## Hardware and objective

Reference target: **NVIDIA GTX 1080 8 GB (Pascal)**, **first-generation Ryzen** (exact CPU/RAM/storage to inspect). Windows-first packaged application. Target native **1920×1080** initially. **30 FPS floor**, with strong preference for 45–60+ FPS.

30 FPS is 33.33 ms/frame; 60 FPS 16.67 ms. Average FPS is insufficient: measure median, P95/P99, 1% lows, >33 ms spikes, streaming hitches, GPU busy time, CPU game/render time, memory and clocks. Any below-30 events must be logged rather than averaged away.

No hardware ray tracing, path tracing or frame generation as the baseline. Software GI, foliage upscaling and modern GPU-driven techniques must earn a measured visual/performance benefit.

## Shortlist

1. **Flax Engine** — favored for existing terrain, quadtree foliage, animation and native source access. Watch cluster rebuild cost for frequent plant edits.
2. **Wicked Engine** — favored for source-level rendering modifications, custom vegetation and engine-neutral data flow; watch custom toolchain/terrain integration burden.
3. **UNIGINE** — optional third control with mature environmental systems and proprietary constraints. Retain only if access/license/automation meet experiment needs.
4. Other alternatives (Godot, Unity URP, Unreal without expensive defaults, Bevy) may enter after evidence-based screening, not uncontrolled multiplication of demos.

No benchmark-based winner has been selected. The user currently leans Flax or Wicked.

## Common test bed

Build one shared reference scene with identical source heightmap/meshes, plant positions/coverage, materials, weather inputs and scripted camera routes. A candidate must not 'win' by quietly reducing density, shadow quality or creature animation.

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

**V9 Ecology bridge:** plant consumption/growth and channel wetness changes rebuild only affected spatial patches; persistent IDs survive unload/reload. Chunk loading requests **FloraSim** bulk snapshots from persistent **RaukenState** identities; no per-rendered-plant biology polling.

**V9b Simulation/visual decoupling:** **HeroSim/FaunaSim** biology continues at suitable active rates regardless of visibility, with shared **BeastCore** formulas. **InteractionsCore** changes update the affected visuals; weather/wetness rendering reads **RaukenSim** current state. Benchmark chunk unload/reload and catch-up spikes.

**V10 Streaming:** camera route across cell boundaries at varying speeds; monitor stalls, pops, resource residence and distant transition quality.

## Outcome/reporting

Deliver source and build steps for each engine, identical manifests/benchmark paths, a raw results set, corresponding still/moving captures, optimization deltas, license notes and an explicit recommendation.

Score both *visual quality* and *frametime/headroom*. Prefer a clear practical winner; if neither meets the quality+performance gate, diagnose top costs and conduct **targeted renderer experiments** instead of guessing. No full game implementation authorized here.

## Useful technical leads

- Flax foliage: https://docs.flaxengine.com/manual/foliage/index.html
- Flax programmatic foliage: https://docs.flaxengine.com/manual/foliage/tutorials/foliage-from-code.html
- Wicked Engine: https://github.com/turanszkij/WickedEngine
- PresentMon: https://github.com/GameTechDev/PresentMon
- RenderDoc: https://renderdoc.org/
- Tracy: https://github.com/wolfpld/tracy
- meshoptimizer: https://meshoptimizer.org/

Important: Flax documentation notes that after programmatic foliage changes clusters should be rebuilt in batches. Plant bite events must not rebuild a huge actor on every action.

See [Visual direction](visual-direction.md) for appearance requirements and [Asset toolkit](asset-toolkit.md) for reproducible content.

## HeroView and simulation buffer benchmarks

Test orbit-follow without automatic heading recentering, body-relative WASD at every camera heading, local free-camera flight to a soft/hard tether, returning to the animal, collision handling, and tether correction when the animal walks away.

Critically, **SimCore simulation activation must buffer beyond the full local free-camera envelope**. Benchmark flora bulk instantiation, fauna cohort instantiation/retirement, and rendering together while flying the camera over an occluding hill. Animals should already be resting/browsing before revealed, not spawned by renderer visibility. Check CPU spikes, delayed geometry, repeated count conservation, and the ability to draw camera-visible creatures Smalltrotter has not perceived. See [Spatial activation](spatial-activation.md).
