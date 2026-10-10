# Parallel agent work packages and integration rules

**Status:** Ready-to-assign specifications, **not dispatched agent executions**.
**Execution interface:** [Toolkit task graph](../../tasks/README.md) is the detailed machine-readable dependency queue and worker packet generator; these lane guidelines govern review and cross-domain integration.  
**Parent:** [Roadmap](README.md); [Toolkit breakdown](toolkit.md).  
**First integration rule:** one worker owns v0.1 interface decisions; other workers may prototype in parallel but cannot silently invent contradictory production contracts.

## Working model

Use one integration lead and a bounded set of specialist worktrees or isolated branches. Workers return **pull requests or inspectable patches**, artifact receipts, tests, screenshots/motion captures and any necessary decision proposal. Do not allow five workers to push to main or simultaneously edit the same generated scene file. Work should be small enough to review and merge individually but large enough to provide an actual working artifact, not empty scaffolding.

Three concurrent *active implementers* plus a lightweight review/test lane is a reasonable **initial proposal**, not a model limit or performance requirement. Increase concurrency when interfaces stabilize. Agents may use different model/providers; the canonical instruction packet and artifacts matter more than their model identity.

### Worktree ownership

| Lane | Branch suggestion | Owns | Must not edit without contract review |
|---|---|---|---|
| A integration/tooling | work/toolkit-core | tools/stalthos.ps1, toolkit/cli, toolkit/schemas, toolkit/tests, conventions | fauna/flora spec authority; engine decision |
| B botanical geometry | work/plant-families | toolkit/generators/plants, plant profiles and source/preview fixtures | CLI/schemas, game biology |
| C creature and animation | work/smalltrotter-proxy | toolkit/generators/creatures, creature rig profiles/fixtures | HeroSim intent, shared schema without approval |
| D landscape and references | work/splitstone-neutral | scenes/splitstone, terrain/export and placement packages, reference metadata | living ecology scheduler, renderer-specific source |
| E Wicked adapters/benchmark | work/wicked-visuals | benchmarks/wicked, toolkit/adapters/wicked | common source profiles, source art and biological save rules |
| G authoring/material adapters | work/authoring-pbr | toolkit/adapters/plantfactory, toolkit/materials, toolkit/adapters/photogrammetry | common geometry/export and license schemas; Wicked import internals |
| F QA/provenance | work/visual-qa | toolkit/qa, reference/index, golden visual rubric | schema versions without change proposal |

**Parallelism:** A begins first; while A freezes contract v0.1, B/C/D/F can research and make disposable sketches from agreed example profiles. B/C/D/E can implement on accepted v0.1 in parallel; E needs enough published geometry to run honest Wicked visual and frame-timing tests. F continues throughout. Do not pretend a prototype with manually imported files is a completed CLI or quality gate.

## Global agent packet — prepend to every assignment

> You are implementing a bounded piece of The Stalthosian Archipelago (repository historically named Rauken-Archipelago). Read docs/README.md, docs/vision-and-principles.md, docs/research-register.md, docs/asset-toolkit.md, docs/visual-direction.md, and the two docs/implementation plans before editing. Preserve display-first/cheap-invisible-ecology priorities, agent-accessible Windows-first workflow, no forced playable vertical slice, Wicked as the single current renderer, with neutral source masters, reference GTX 1080 / first-gen Ryzen 1080p target, no invented scientific evidence and no hidden paid API dependency. Work only within your declared file ownership or submit an interface-change request. Include commands actually executed, source/test receipts, known limitations, and visual proof when appearance matters. Do not claim benchmarks ran if the reference hardware or tools were unavailable.

This packet intentionally does not select a programming language for the game runtime or settle tool versions before TOOL-01 measurement.

## Packet A0 — bootstrap and schema freeze

**Start immediately. Priority: blocking.** Covers TOOL-01, then TOOL-02 and a minimal TOOL-03 entrypoint.

**Deliver:** a functioning Windows dependency doctor; build environment documentation and per-tool capability statuses; pinned Python/test environment; v0.1 asset/profile/provenance/receipt schemas with sample Softbough, Royal frond and Smalltrotter profiles; validators; a wrapper CLI which can validate these and report JSON/exit codes; good/bad golden fixtures.

**Mandatory proof:** run doctor on a real Windows box, run schema validation in fresh checkout, show missing-Blender and malformed-profile errors, confirm no optional installer download, create one deterministic primitive export only after the schema contract is accepted.

**Handoff:** publish v0.1 schema package and fixture manifest. Explicitly signal frozen fields/axis conventions to B-F and publish changes through versioned migration, not ad hoc edits.

**Review questions:** does any field require game-engine classes? Can a species be added by data? Does a failed build leave no published asset? Can agent infer next action from errors alone?

## Packet B1 — botany: six reference morphologies

**Start after schema v0.1, sketches sooner.** Covers TOOL-04/05/06/07 for the six [Flora](../flora.md) references.

**Deliver:** distinct branch-tree, shrub, fern/frond, segmented-stem and attached-fungus construction paths; source master files; seeded variants and juvenile/adult appearance where useful; stable contact/forage group names; neutral exports plus generation/turntable scripts; branch/frond/ground-integration comparison sheets.

**Acceptance:** Splitcrown, Softbough, Jointreed, Royal frond, Basketfern and bracket fungus are genuinely different in silhouette and structure. Two chosen seeds repeat shapes; 3–5 other seeds give species-preserving variation. Tool/rights/asset metadata passes A0 schema and F1 QA. No 200-species rush, no deep plant simulation.

**Integration:** consume A0 CLI/schemas unchanged; request new sidecar fields through an explicit fixture proposal; provide flexible groups for E2 contact deformation rather than performing plant physics in generators.

## Packet C1 — Smalltrotter anatomical/rig proxy

**Start after schema v0.1, reference research sooner.** Covers TOOL-09.

**Deliver:** a body-proportion and anatomy reference/evidence sheet; juvenile-to-adult source mesh and rig/LOD; nape bristle/osteoderm zones; named mouth/foot/head/neck/tail attachments and basic move/rest/browse/drink motion; export to neutral interchange plus stage turntables and gait reel.

**Acceptance:** juvenile looks distinctively shaggy at nape/shoulders but not mammalian or fully spiked; adult heavier and more pebbled/wrinkled with relatively sparse bristles and stronger osteoderms; foot plant and contact look coherent in motion; rigs import with validated binding. Document all fictional anatomy honestly. A cube with a long neck is a temporary test fixture, not a successful anatomical output.

**Integration:** renderer adapters can consume C1 without changing rig bone names ad hoc. Future HeroSim/BeastCore consumes semantic bones and age parameters but does not own the art generator.

## Packet D1 — neutral Splitstone environment

**Research/layout may start immediately; final build waits for v0.1 format.** Covers WORLD-01.

**Deliver:** terrain/rock/stream generators or composable authored files; neutral material masks and geology/suitability sidecars; a ~512 m dense rendering exercise and a separate ~1 km traversable geography case; authored camera routes at Smalltrotter juvenile height; instance-placement seed list; landmark IDs; collision and weather/wetness visualization inputs.

**Acceptance:** a physically plausible downhill stream crosses a fractured ravine toward a valley, a bluff/resistant outcrop reads strongly, shade/wet hollow/root/rock seams make sense, an ordinary forest stretch separates prominent features, alternatives and impassable routes both exist. Above/under-cut geometry uses meshes where a heightfield cannot express it. No mandated ten-stage geological history simulation or gameplay attraction map.

**Integration:** geometry and placement exports are engine neutral. Keep flora generation and renderer shader assumptions external. Connect to B1 botanical publish IDs, not unversioned local .blend file paths.

## Packet E1 — Wicked import, shaders and benchmark scaffold

**Can scaffold against primitive fixtures after A0; representative full-scene benchmarks wait for B/C/D.** Covers RND-001 through RND-009 and MAT-002/003 as their prerequisites allow.

**Deliver:** Wicked source build/import recipe and neutral-to-Wicked scene conversion, material packing/DDS and shaders with traceable version/channel mappings, camera/lighting route, captured runtime/driver/binary hashes, comparison to neutral Blender reference frames, basic capture automation and raw timing report. Measure on the actual GTX 1080/Ryzen target where accessible.

**Acceptance:** Wicked consumes core fixtures at correct scale with verified roughness/normal/alpha mapping; unsupported material/rig/plant-pivot features are reported; repeated runs preserve conditions. Reports include CPU/GPU/VRAM, P95/P99 and hitches rather than just average FPS. No unsupported claim of Pascal profiler compatibility.

**Integration:** E1 consumes A0/B1/C1/D1 artifacts as immutable bundles. Wicked-specific WISCENE/shader/DDS assets remain derived copies. For engine issues, file a minimal reproducer with screenshot, raw timing and exact import settings.


## Packet G1 — PlantFactory and procedural surface tools

**Can start with capability/version/rights audits after CFG-001; automated import requires actual installed exporters and the approved neutral schema.** Covers PFA-001/002/003, MAT-001 and GEO-001. Collaborates with E1 for MAT-002/003. Never claim that discontinued PlantFactory offers a batch CLI unless discovered and demonstrated locally.

**Deliver:** PlantFactory export capability and PlantCatalog provenance matrix, source-to-Blender asset conversion with optional branch/wind/pivot sidecars, Material Maker or Blender-node PBR graphs for leaf/bark/rock/skin and correctly tagged roughness/thickness/normal channels, scanned-rock cleanup and rights records.

**Acceptance:** actual source fixtures preserve UV/scale/leaves/branch-group data or disclose losses; material swatches show controlled lighting comparisons; optimization cannot silently discard interaction attributes. Absent PlantFactory is a documented optional blocked adapter, not a reason to stop six-reference-plant work.

**Ownership:** G1 uses its own worktree and only the PFA/MAT/GEO paths listed by the machine graph. E1 owns Wicked shader conversion and target-PC measurement; shared interfaces are versioned through A0/INT review.

## Packet F1 — reference/provenance and visual QC

**Can start immediately; links to every lane.** Covers TOOL-11/12.

**Deliver:** source reference ledger/rights template, no-assumed-license policy, batch preview recipes, neutral-light and field-light turntables, silhouette/leaf atlas, locomotion/contact video template, LOD shimmer comparison and rubric for manual acceptance. Start catalog reference scouting across the four islands using the landscape leads in docs/research-register.md.

**Acceptance:** a reviewer can decide if two morphologies are genuinely distinct without texture colors, whether a skeleton moves credibly, whether an asset is licensed for intended distribution and whether a renderer 'optimization' degraded quality. A missing PlantCatalog redistribution flag or rights record blocks only the relevant publish, not the entire workshop doctor.

**Integration:** add test requirements via fixtures/validator adapters rather than redefining all profile fields. Return both pass/fail machine reports and **explicit human-art-review needed** status.

## Packet E2 — vegetation contact A/B

**Starts once Softbough and creature contact fixture exist.** Covers TOOL-10 and relevant V5 tests.

**Deliver:** bounded contact-field schema, two cheap rendering implementations or one plus a documented baseline, moving animal + Softbough scene, side-by-side video and measured cost. The shader should deflect branches/ferns near a moving animal while ordinary wind stays active. Persisted browse depletion can be a fixture override until InteractionsCore exists.

**Acceptance:** visible movement around the animal, recovery after passage, no unbounded per-branch physics, measured impact of each option. Avoid fake 'contact' animations that fire only on camera visibility or require the player animal to cross specified stage points.

## Packet INT — integration lead / reviewer

At each merge:
1. Rebase on accepted contract; reject silent profile/schema drift.
2. Run schema and deterministic fixture tests.
3. Verify source master, neutral bundle, preview, right-to-use record, commit/test receipt.
4. Reject blanket geometry/foliage compromises without visual A/B evidence.
5. Reproduce cleanly on Windows; note missing hardware/tool blockers separately from code failures.
6. Update docs/implementation state and decisions, not prose-only percentage claims.
7. Merge bounded packages when acceptance passes. Do not merge five unreviewed agents' arbitrary scene/script changes at once.

## Change requests and conflict strategy

**Allowed normal changes:** file-local procedural parameters, visual variants and previews, generator-private internals, QA annotations.  
**Requires shared-contract review:** axes, schema_version, logical identity representation, rig sockets/bones, neutral exporter structure, output receipt shape, publish atomicity, scene placement IDs, parser license rule, rendering cost reporting.  
**Never silently changed:** engine remains undecided before benchmarks; screen-space direct movement and separated camera/animal perception; no requirement for full ecology; legal provenance and no paid API hard dependency.

When two agents disagree, create a *small representative fixture* that reveals the disagreement (e.g. 1 m cube coordinate test, two-stage skeleton import or 50-instance shrub test) instead of holding a broad design meeting or building two full incompatible pipelines.

## First execution sprint — integration order

| Order | Parallel lanes | Required output to pass |
|---|---|---|
| 0 | A0, F1 plus B/C/D reference research | doctor + draft schemas; provenance template; research packets |
| 1 | A0 finalizes schema v0.1 and primitive export | approved fixture contract and receipts |
| 2 | B1, C1, D1, E1 and F1 (isolated branches) | six botanical forms, animal proxy, terrain, import/scaffold, review tools |
| 3 | B1 + C1 refinements, E2, TOOL-08 optimization | bending/contact reel, optimized exports, moving silhouette captures |
| 4 | INT + E1 Wicked fidelity/benchmark | neutral-to-Wicked import proof; measured visual/frametime regressions and targeted fixes |

Do not require artificial weekly deadlines or fixed asset polygon/texture budgets before benchmark data. Track **blocked by contract**, **in progress**, **fixture passed**, **visual review passed**, **measured** separately.

## Handoff report template

    Work package:
    Branch/commit:
    Parent schema version:
    Implemented commands:
    Local OS/tool versions:
    Input fixtures and seeds:
    Output artifacts/hashes:
    Tests executed, exact result:
    Visual review links or local capture paths:
    Rights/evidence sources:
    Benchmark hardware and measurements (if any):
    Known regressions, unknowns and missing dependencies:
    Contract changes requested:
    Safe next work item:

**Dispatch status as of this document:** no coding subagents have been launched. These packets are intended for a future Jules/Pi/Clanker/Codex or human delegation workflow with actual execution capabilities. Parallel *inspection* and independent branch development are structurally supported; asynchronous execution must be supplied by the chosen agent harness.
