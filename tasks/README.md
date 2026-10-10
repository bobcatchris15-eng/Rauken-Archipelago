# Hand this to a squadron — executable toolkit task graph

This directory defines the **toolchain build**, not a new game feature list. The deliverable is an agent-operated Windows-first workshop that can author, rig, bake, validate, version, preview, publish and benchmark engine-neutral landscape/plant/creature assets.

**Canonical plan**: [toolkit-first roadmap](../docs/implementation/README.md) and [detailed toolkit spec](../docs/implementation/toolkit.md).  
**Canonical agent DAG**: [toolkit-graph.json](toolkit-graph.json) (68 detailed work nodes).  
**Coordinator tool**: [taskgraph.py](../tools/taskgraph.py).  
**Status**: none of the 68 implementation tasks is complete merely because the planning files exist.

## Start in one shell

Clone or select the \`planning/toolkit-execution-graph\` branch (or its merged descendant), install **Python 3.10+**, and run from repository root:

    python tools/taskgraph.py validate
    python tools/taskgraph.py ready --max 3
    python tools/taskgraph.py packet CON-001

To ask for only jobs an environment can run:

    python tools/taskgraph.py ready --max 3 --capabilities python
    python tools/taskgraph.py ready --max 3 --capabilities python,windows,powershell,blender

Omitting \`--capabilities\` **does not check whether the worker has tools**; it displays potential jobs. \`gpu-target\` means access to **the actual reference machine** for claims of measured performance, not simply any GPU. Flax and Wicked capabilities mean tested local engine installs.

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
- **G2 – fair renderer comparison:** neutral Splitstone scene and identical source manifests/placements/routes successfully imported into Flax and Wicked with visible loss reports.
- **G3 – evidence-based engine decision:** on the GTX 1080 / first-gen Ryzen, compare dense full-scene native 1080p appearance **and** P95/P99/hitches/VRAM; explicitly leave undecided if evidence is lacking.

The **68 tasks are construction tasks**. The 50+ wildlife and 200 plant-form directions are expansion goals, not mandatory standalone full simulators or initial-toolkit release blockers. No engine selection or playable vertical slice has been requested as part of these tasks.

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

> Read \`tasks/README.md\`. Use \`python tools/taskgraph.py validate\`, \`ready\`, \`packet\`, \`claim\` and \`status\` to manage bounded work. Allocate no more than three simultaneous coding workers initially. Each worker receives one complete packet, its isolated branch/worktree, and only permitted write paths. Prefer independent short-to-medium work with explicit test artifacts. Do not infer capabilities, licenses, benchmark results or successful installs. Integrate only after review, merge and receipt verification; then call \`accept\` and dispatch newly ready nodes. Preserve engine neutrality through G2; do not create a playable vertical slice. If tools or approval are unavailable, return exact blocker and do not manufacture success.

**No agents are launched by these files.** This repo supplies a ready-to-run orchestration interface and full construction specification; running or connecting the agents requires the user's harness.
