# Hand this to a squadron — executable toolkit task graph

This directory defines the **toolchain build**, not a new game feature list. The deliverable is an agent-operated Windows-first workshop that can author, rig, bake, validate, version, preview, publish and benchmark engine-neutral landscape/plant/creature assets.

**Canonical plan**: [toolkit-first roadmap](../docs/implementation/README.md) and [detailed toolkit spec](../docs/implementation/toolkit.md).  
**Canonical agent DAG**: [toolkit-graph.json](toolkit-graph.json) (77 detailed work nodes; sole renderer target Wicked).  
**Coordinator tool**: [taskgraph.py](../tools/taskgraph.py).  
**Status**: none of the 77 implementation tasks is complete merely because the planning files exist.

## Start in one shell

Clone or select the \`planning/toolkit-execution-graph\` branch (or its merged descendant), install **Python 3.10+**, and run from repository root:

    python tools/taskgraph.py validate
    python tools/taskgraph.py ready --max 3
    python tools/taskgraph.py packet CON-001

To ask for only jobs an environment can run:

    python tools/taskgraph.py ready --max 3 --capabilities python
    python tools/taskgraph.py ready --max 3 --capabilities python,windows,powershell,blender

Omitting \`--capabilities\` **does not check whether the worker has tools**; it displays potential jobs. \`gpu-target\` means access to **the actual reference machine** for claims of measured performance, not simply any GPU. The `wicked` capability means a tested local Wicked build; `plantfactory` means a genuinely operable installed PlantFactory edition. Neither is inferred from docs alone.

## Coordinator-owned state: never use git branches as a race-prone status database

A **single orchestrator** owns one local \`.taskgraph-state.json\`, deliberately ignored by Git. It is an ephemeral **dispatch and review journal**, not a source-of-truth substitute for accepted PRs, commit hashes and proof artifacts. Give distinct agents separate worktrees/branches. Do **not** let every worker clone its own independent state and claim tasks independently: file-based locking only coordinates processes on the same filesystem. A remote squad should use one coordinator service/process (or replace this state layer with a centrally backed transactional store) to issue unique claims.

### Actual dispatcher loop

1. Integrator checks \`validate\`, \`status\`, \`ready\` and the worker's real capabilities.
2. Integrator generates a task packet and reserves it:

       python tools/taskgraph.py packet CFG-003
       python tools/taskgraph.py claim CFG-003 --worker agent-02 --branch agent-02/cfg-003 --capabilities python

3. Worker receives complete packet, works only in assigned owned paths, and returns a PR/commit, **actually executed commands/results**, provenance and previews when relevant. Worker cannot mark its own result accepted.
4. Integrator reviews code, checks dependencies and integration tests, verifies the PR is merged to the selected integration base and its output receipt exists, then records:

       python tools/taskgraph.py accept CFG-003 --merge-commit <40-character-real-merge-SHA> --receipt <verified-receipt-path-or-URL> --reviewed-by <reviewer> --merged-and-verified

   The CLI does **not** contact GitHub to prove a merge occurred. \`--merged-and-verified\` is a human/orchestrator assertion and must only be passed after actual verification. Never invent an acceptance receipt.
5. Next \`ready\` considers this dependency satisfied. If worker fails or needs reassignment:

       python tools/taskgraph.py release CFG-003 --worker agent-02
       python tools/taskgraph.py block CFG-003 --reason "Tool missing on target workstation"
       python tools/taskgraph.py unblock CFG-003

Use \`status\` to inspect outstanding gate prerequisites and \`dot\` to export a Graphviz dependency diagram:

    python tools/taskgraph.py status
    python tools/taskgraph.py dot > tasks/toolkit-dependencies.dot
    python tools/taskgraph.py dot --gate G1 > tasks/toolkit-g1.dot

DOT exports are derived diagnostic files, not an alternate authoritative graph; typically don't commit them.

### Worker packet guarantees

Every node includes:
- stable task ID, lane, wave, qualitative effort S/M/L;
- exact \`depends_on\` list and declared task-owned write paths;
- required capabilities, objective and bounded construction steps;
- tangible deliverables and pass/fail acceptance criteria;
- common reading list, display-first/rights/engine-neutral constraints and a receipt handback checklist.

Use the CLI \`packet\` output as the full agent assignment, **not only the title**. For example:

    python tools/taskgraph.py packet PLT-003 > softbough-agent-packet.md

When agents encounter undefined shared fields, they must request an interface change; they must **not** rename schema IDs, rigs, neutral asset interchange or renderer policies in their own task branch. The integration lead owns those decisions. Changes to the DAG itself go through review.

## Wicked-first authoring paths

The active renderer path runs **RND-001 Wicked import → MAT-002 channel packing/DDS → RND-002 native smoke scene → RND-003 neutral-to-Wicked scene audit → RND-005/006/007/008 capture experiments → RND-009 hardware readiness**. Material production and scanned rocks have dedicated tasks; read [Wicked materials and PlantFactory pipeline](../docs/implementation/wicked-material-pipeline.md).

The additional work packets are **PFA-001/004/002/003/005** (PlantFactory capability discovery, agent-built native/plugin/Windows UI automation, Blender interchange, preserved branch pivots, unattended seeded export batches), **MAT-001/002/003** (procedural PBR + roughness, Wicked texture packing, thin-leaf wetness/transmission shaders), and **GEO-001** (legally sourced photogrammetry and rock/root/log cleanup). **PlantFactory automation is an explicit engineering assignment:** the absence of a packaged CLI is *not* a blocker by itself. Agents may build a supported native/plugin bridge or safe pywinauto/UIA/Win32 desktop controller, including parameter edits, save/export, screenshots, retries and resumable batches. A missing local installation blocks end-to-end verification, not the design/prototype. GUI operations must serialize per desktop session. Blender-native generation remains a separate reliable G1 fallback.

Avoid giving a shader-only worker a high-level `Wicked integration` job until the branch/core material contracts are accepted; request its specific task packet. Equivalent art coverage is checked against original Blender renders and instance manifests rather than a second renderer.

## First three assignments

With an empty status journal, the independent roots are:

| Task | Work | Tool needs |
|---|---|---|
| **CFG-001** | Inspect Windows machine/hardware/tool locations, produce read-only dependency doctor | Python, Windows, PowerShell |
| **CFG-003** | Establish cache/source/artifact layout and safe ignore/LFS policy | Python |
| **CON-001** | Freeze engine-neutral units, coordinate axes, IDs and deterministic seeds | Python |

These can be worked on independently. The next graph nodes unlock organically: CFG-002, CON-002, CLI-001 and later schemas. Don't dispatch Blender scene generation against unapproved coordinate/profile conventions just to maximize concurrent model calls.

Suggested allocation with a flash-heavy harness: up to **three active coding workers**, plus the human/orchestrator performing narrow validation/review. Model/provider selection is external to this graph. The scheduler uses stable work packets and tool-capability tags so a capable but tool-call-fragile model can receive a smaller S/M assignment rather than a broad "build the game" prompt.

## Milestone gates

- **G0 – foundation:** environment, coordinates, schemas, CLI and CI recognized; actual Windows doctor and invalid-input behavior verified.
- **G1 – asset workshop:** six distinct reference plants and juvenile/adult Smalltrotter pass source -> build -> export -> art preview -> QA -> approved bundle, with no silent license violation.
- **G2 – Wicked asset fidelity:** full neutral Splitstone terrain/plant/rig/scene material source imported into Wicked with validated placements, surface channels, pivots and observable unsupported features.
- **G3 – measured Wicked readiness:** on the GTX 1080 / first-gen Ryzen, record dense full-scene native 1080p appearance, P95/P99/hitches/VRAM, and actual shader/streaming bottlenecks. Wicked remains the planned renderer if further optimization is needed.

The **77 tasks are construction tasks**. The 50+ wildlife and 200 plant-form directions are expansion goals, not mandatory standalone full simulators or initial-toolkit release blockers. Flax integration is not scheduled; the asset masters remain neutral. No playable vertical slice is requested as part of these tasks.

## Integration and file ownership

The dispatcher selects non-overlapping \`write_paths\` among concurrently claimed tasks. This is a *best-effort* collision guard, not a Git worktree isolation substitute. Crosscutting changes (schema migration, CI-wide tweaks, version changes or shared imports) require integrator coordination even when paths differ.

Every merged task must preserve:
- compiled/parseable source, actual tests where dependencies exist;
- exact tool versions and runtime environment for generated content;
- source asset plus neutral export and diagnostic/preview evidence when relevant;
- no fake successful placeholders for unavailable optional software;
- rights/provenance, meaningful receipts and explicit blockers;
- source control hygiene: no massive caches, proprietary installers, downloaded stock photos or benchmark capture dumps in Git;
- narrow task implementation rather than unauthorized runtime ecology complexity.

The graph intentionally distinguishes **portable implementation** from **reference-PC empirical verification**. Workers without a Windows/Blender/GPU-target environment may develop code and fixtures but cannot claim hardware-specific tests passed. The coordinator should hold the task unaccepted or explicitly blocked until a compatible validator produces proof.

## Handoff to Jules / Pi / Clanker

Give the coordinator the branch and these instructions:

> Read \`tasks/README.md\`. Use \`python tools/taskgraph.py validate\`, \`ready\`, \`packet\`, \`claim\` and \`status\` to manage bounded work. Allocate no more than three simultaneous coding workers initially. Each worker receives one complete packet, its isolated branch/worktree, and only permitted write paths. Prefer independent short-to-medium work with explicit test artifacts. Do not infer capabilities, licenses, benchmark results or successful installs. Integrate only after review, merge and receipt verification; then call \`accept\` and dispatch newly ready nodes. Build Wicked as the sole active renderer; preserve neutral editable asset masters. Do not create a playable vertical slice. If tools or approval are unavailable, return exact blocker and do not manufacture success.

**No agents are launched by these files.** This repo supplies a ready-to-run orchestration interface and full construction specification; running or connecting the agents requires the user's harness.
