#!/usr/bin/env python3
"""Stdlib-only queue and validator for tasks/toolkit-graph.json.

This is a LOCAL coordinator-side dispatcher, not a distributed locking service or
an executor. It never runs agents, installs packages, merges PRs, or certifies tests.
Use a single coordinator/state file per squad; independent clones require an
external shared coordinator.
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import sys
import tempfile

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_GRAPH = ROOT / "tasks" / "toolkit-graph.json"
DEFAULT_STATE = ROOT / ".taskgraph-state.json"
VALID_CAPABILITIES = {
    "python", "powershell", "windows", "blender", "github-actions",
    "flax", "wicked", "gpu-target",
}
VALID_LANES = {
    "integration", "contracts", "assets", "research", "quality",
    "plants", "creatures", "world", "renderer",
}
VALID_SIZES = {"S", "M", "L"}


class GraphError(ValueError):
    """Bad graph, task state, or requested coordinator operation."""


def read_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as source:
        obj = json.load(source)
    if not isinstance(obj, dict):
        raise GraphError(f"{path}: expected JSON object")
    return obj


def write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as sink:
            json.dump(value, sink, indent=2, ensure_ascii=False)
            sink.write("\n")
            sink.flush()
            os.fsync(sink.fileno())
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


@contextmanager
def locked_state(path: Path):
    """Exclusive single-filesystem writer; stale locks need human inspection."""
    path.parent.mkdir(parents=True, exist_ok=True)
    lock = path.with_name(path.name + ".lock")
    try:
        fd = os.open(str(lock), os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as exc:
        raise GraphError(f"coordinator lock exists: {lock}; inspect owner before removing") from exc
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            stream.write(f"pid={os.getpid()}\n")
        yield
    finally:
        lock.unlink(missing_ok=True)


def validate_graph(graph: dict) -> tuple[dict, list[str]]:
    if graph.get("schema_version") != "1.0.0":
        raise GraphError("graph schema_version must be 1.0.0")
    tasks = graph.get("tasks")
    if not isinstance(tasks, list) or not tasks:
        raise GraphError("graph.tasks must be nonempty list")
    by_id = {}
    required = {
        "id", "title", "lane", "wave", "size", "depends_on", "write_paths",
        "capabilities", "objective", "steps", "deliverables", "acceptance",
    }
    for item in tasks:
        if not isinstance(item, dict) or not required.issubset(item):
            raise GraphError(f"task lacks required fields: {item!r}")
        tid = item["id"]
        if not isinstance(tid, str) or not re.fullmatch(r"[A-Z]{2,3}-[0-9]{3}", tid):
            raise GraphError(f"invalid task id: {tid!r}")
        if tid in by_id:
            raise GraphError(f"duplicate task {tid}")
        if item["lane"] not in VALID_LANES or item["size"] not in VALID_SIZES:
            raise GraphError(f"{tid}: invalid lane or size")
        if not isinstance(item["wave"], int) or item["wave"] < 0:
            raise GraphError(f"{tid}: invalid wave")
        for field in ("title", "objective"):
            if not isinstance(item[field], str) or not item[field].strip():
                raise GraphError(f"{tid}: empty {field}")
        for field in ("depends_on", "write_paths", "capabilities", "steps", "deliverables", "acceptance"):
            value = item[field]
            if not isinstance(value, list) or (field not in ("depends_on", "capabilities") and not value):
                raise GraphError(f"{tid}: {field} must be list; nonempty where required")
            if any(not isinstance(x, str) or not x.strip() for x in value):
                raise GraphError(f"{tid}: invalid {field} entry")
            if len(set(value)) != len(value):
                raise GraphError(f"{tid}: duplicate in {field}")
        if not set(item["capabilities"]) <= VALID_CAPABILITIES:
            raise GraphError(f"{tid}: unknown capabilities")
        for path in item["write_paths"]:
            normalized = path.replace("\\", "/")
            if normalized.startswith("/") or "/../" in f"/{normalized}/" or normalized.startswith(".."):
                raise GraphError(f"{tid}: write path escapes repository: {path}")
        by_id[tid] = item

    for tid, item in by_id.items():
        for dep in item["depends_on"]:
            if dep not in by_id or dep == tid:
                raise GraphError(f"{tid}: missing or self dependency {dep}")
            if by_id[dep]["wave"] > item["wave"]:
                raise GraphError(f"{tid}: depends on later-wave task {dep}")

    visiting, visited, topological = set(), set(), []

    def visit(tid: str) -> None:
        if tid in visiting:
            raise GraphError(f"dependency cycle involving {tid}")
        if tid in visited:
            return
        visiting.add(tid)
        for dep in by_id[tid]["depends_on"]:
            visit(dep)
        visiting.remove(tid)
        visited.add(tid)
        topological.append(tid)

    for tid in by_id:
        visit(tid)

    seen_gates = set()
    for gate in graph.get("gates", []):
        gid = gate.get("id")
        if gid in seen_gates or not gid:
            raise GraphError(f"invalid/duplicate gate {gid}")
        seen_gates.add(gid)
        for tid in gate.get("requires", []):
            if tid not in by_id:
                raise GraphError(f"gate {gid}: missing task {tid}")
    if not isinstance(graph.get("conventions"), dict):
        raise GraphError("conventions must be object")
    return by_id, topological


def empty_state() -> dict:
    return {"schema_version": "1.0.0", "accepted": {}, "claimed": {}, "blocked": {}}


def load_state(path: Path, by_id: dict) -> dict:
    state = read_json(path) if path.exists() else empty_state()
    if state.get("schema_version") != "1.0.0":
        raise GraphError("task state schema_version must be 1.0.0")
    for key in ("accepted", "claimed", "blocked"):
        if not isinstance(state.get(key), dict):
            raise GraphError(f"state.{key} must be object")
        unknown = set(state[key]) - set(by_id)
        if unknown:
            raise GraphError(f"state.{key} references unknown tasks: {sorted(unknown)}")
    categories = [set(state[x]) for x in ("accepted", "claimed", "blocked")]
    if any(categories[i] & categories[j] for i in range(3) for j in range(i + 1, 3)):
        raise GraphError("a task cannot be accepted, claimed and/or blocked simultaneously")
    for tid, proof in state["accepted"].items():
        if not isinstance(proof, dict) or not all(proof.get(k) for k in ("commit", "receipt", "reviewed_by")):
            raise GraphError(f"{tid}: accepted entry missing commit, receipt or reviewed_by")
        for dep in by_id[tid]["depends_on"]:
            if dep not in state["accepted"]:
                raise GraphError(f"{tid}: accepted before prerequisite {dep}")
    for tid, claim in state["claimed"].items():
        if not isinstance(claim, dict) or not claim.get("worker") or not claim.get("branch"):
            raise GraphError(f"{tid}: claimed entry missing worker or branch")
        for dep in by_id[tid]["depends_on"]:
            if dep not in state["accepted"]:
                raise GraphError(f"{tid}: claimed before prerequisite {dep}")
    for tid, reason in state["blocked"].items():
        if not isinstance(reason, str) or not reason:
            raise GraphError(f"{tid}: block reason required")
    return state


def paths_overlap(a: str, b: str) -> bool:
    x, y = a.strip("/"), b.strip("/")
    return x == y or x.startswith(y + "/") or y.startswith(x + "/")


def tasks_conflict(a: dict, b: dict) -> bool:
    return any(paths_overlap(p, q) for p in a["write_paths"] for q in b["write_paths"])


def ready(graph: dict, by_id: dict, state: dict, limit: int | None,
          capabilities: set[str] | None, lane: str | None = None) -> list[dict]:
    accepted = set(state["accepted"])
    unavailable = set(state["claimed"]) | set(state["blocked"]) | accepted
    claimed_jobs = [by_id[tid] for tid in state["claimed"]]
    available_slots = max(0, graph["conventions"].get("default_max_workers", 3) - len(claimed_jobs))
    if limit is not None:
        available_slots = min(available_slots, limit)
    if available_slots == 0:
        return []
    selection = []
    for item in sorted(by_id.values(), key=lambda x: (x["wave"], x["id"])):
        if item["id"] in unavailable or lane and item["lane"] != lane:
            continue
        if not all(dep in accepted for dep in item["depends_on"]):
            continue
        if capabilities is not None and not set(item["capabilities"]) <= capabilities:
            continue
        if any(tasks_conflict(item, other) for other in claimed_jobs + selection):
            continue
        selection.append(item)
        if len(selection) >= available_slots:
            break
    return selection


def task_packet(item: dict, graph: dict, json_format: bool) -> str:
    if json_format:
        return json.dumps({"policy": graph["conventions"], "task": item}, indent=2)
    lines = [
        f"# Agent work order — {item['id']}: {item['title']}",
        "",
        f"Lane: {item['lane']} | Wave: {item['wave']} | Size: {item['size']}",
        f"Dependencies: {', '.join(item['depends_on']) or 'none'}",
        f"Required capabilities: {', '.join(item['capabilities']) or 'none'}",
        "",
        "## Binding instructions",
        graph["conventions"]["agent_policy"],
        "",
        "This is a real implementation assignment, not a request for a new roadmap or an empty scaffold.",
        "Deliver a concrete working change and executable tests where tools are available.",
        "If required hardware/software is absent, make only portable code/fixtures, report exact blocker and do not claim empirical completion.",
        "Maintain all source masters in editable form. Do not download/commit unlicensed references or paid model/API dependencies.",
        "No vertical slice, game engine election without measured parity, or deep hidden ecological simulation.",
        "",
        "Read before work:",
    ]
    lines.extend("- " + d for d in graph["conventions"]["required_instruction_docs"])
    lines += ["", "## Goal", item["objective"], "", "## Implementation steps"]
    lines.extend(f"{i}. {s}" for i, s in enumerate(item["steps"], 1))
    lines += ["", "## Owned write paths"]
    lines.extend("- " + path for path in item["write_paths"])
    lines += ["", "## Required deliverables"]
    lines.extend("- " + output for output in item["deliverables"])
    lines += ["", "## Acceptance criteria"]
    lines.extend("- " + check for check in item["acceptance"])
    lines += [
        "", "## Required return packet",
        "Return: task ID; worker; branch/PR; parent schema version; files changed;",
        "commands actually run and exit codes; test receipts; authored asset/source hashes;",
        "visual or motion proof when relevant; rights/reference sources; observed hardware;",
        "missing prerequisites/known defects; exact integration review request.",
        "Do not call the task accepted until the integration lead verifies and merges it."
    ]
    return "\n".join(lines) + "\n"


def show_status(graph: dict, by_id: dict, state: dict) -> dict:
    counts = {"accepted": len(state["accepted"]), "claimed": len(state["claimed"]),
              "blocked": len(state["blocked"]), "total": len(by_id)}
    counts["pending"] = counts["total"] - counts["accepted"] - counts["claimed"] - counts["blocked"]
    gates = [
        {"id": gate["id"], "name": gate["name"],
         "remaining": [tid for tid in gate["requires"] if tid not in state["accepted"]]}
        for gate in graph.get("gates", [])
    ]
    return {"counts": counts, "gates": gates, "claimed": state["claimed"], "blocked": state["blocked"]}


def parsed_caps(args) -> set[str] | None:
    if args.capabilities is None:
        return None
    caps = {v.strip() for v in args.capabilities.split(",") if v.strip()}
    if not caps <= VALID_CAPABILITIES:
        raise GraphError(f"unknown capabilities: {sorted(caps - VALID_CAPABILITIES)}")
    return caps


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Local coordinator for the Stalthos asset toolkit task DAG")
    ap.add_argument("--graph", type=Path, default=DEFAULT_GRAPH)
    ap.add_argument("--state", type=Path, default=DEFAULT_STATE)
    subs = ap.add_subparsers(dest="command", required=True)
    subs.add_parser("validate", help="validate canonical DAG and local state if provided")
    ready_cmd = subs.add_parser("ready", help="show unclaimed prerequisite-complete, non-conflicting jobs")
    ready_cmd.add_argument("--max", type=int, default=None)
    ready_cmd.add_argument("--capabilities", help="comma-separated available capabilities; omitted means no filtering")
    ready_cmd.add_argument("--lane", choices=sorted(VALID_LANES))
    packet = subs.add_parser("packet", help="print complete worker handoff for one task")
    packet.add_argument("task")
    packet.add_argument("--json", action="store_true")
    claim = subs.add_parser("claim", help="claim one ready task with a single coordinator state file")
    claim.add_argument("task")
    claim.add_argument("--worker", required=True)
    claim.add_argument("--branch", required=True)
    claim.add_argument("--capabilities", help="comma-separated local worker capabilities")
    release = subs.add_parser("release", help="release a claimed task")
    release.add_argument("task")
    release.add_argument("--worker", required=True)
    block = subs.add_parser("block", help="mark unclaimed task blocked with reason")
    block.add_argument("task")
    block.add_argument("--reason", required=True)
    unblock = subs.add_parser("unblock", help="clear blocked task")
    unblock.add_argument("task")
    accept = subs.add_parser("accept", help="record reviewed and merged work; never auto-certifies code")
    accept.add_argument("task")
    accept.add_argument("--merge-commit", required=True)
    accept.add_argument("--receipt", required=True)
    accept.add_argument("--reviewed-by", required=True)
    accept.add_argument("--merged-and-verified", action="store_true", required=True)
    subs.add_parser("status", help="show completed/pending/claimed/blockers and gate status")
    dot = subs.add_parser("dot", help="print Graphviz DOT dependency graph")
    dot.add_argument("--gate", help="filter to ancestors of a named gate")

    args = ap.parse_args(argv)
    graph = read_json(args.graph)
    by_id, order = validate_graph(graph)
    state = load_state(args.state, by_id)

    if args.command == "validate":
        print(json.dumps({"valid": True, "nodes": len(by_id), "edges": sum(len(x["depends_on"]) for x in by_id.values()),
                          "root_tasks": [t for t in order if not by_id[t]["depends_on"]],
                          "gates": [g["id"] for g in graph["gates"]]}, indent=2))
    elif args.command == "ready":
        if args.max is not None and args.max < 1:
            raise GraphError("--max must be positive")
        selection = ready(graph, by_id, state, args.max, parsed_caps(args), args.lane)
        print(json.dumps([{"id": t["id"], "title": t["title"], "lane": t["lane"],
                           "capabilities": t["capabilities"], "size": t["size"],
                           "write_paths": t["write_paths"]} for t in selection], indent=2))
    elif args.command == "packet":
        if args.task not in by_id:
            raise GraphError(f"unknown task: {args.task}")
        print(task_packet(by_id[args.task], graph, args.json), end="\n" if args.json else "")
    elif args.command == "status":
        print(json.dumps(show_status(graph, by_id, state), indent=2))
    elif args.command == "dot":
        selected = set(by_id)
        if args.gate:
            gates = {g["id"]: g for g in graph.get("gates", [])}
            if args.gate not in gates:
                raise GraphError(f"unknown gate {args.gate}")
            selected = set()
            def mark(tid):
                if tid in selected:
                    return
                selected.add(tid)
                for dep in by_id[tid]["depends_on"]:
                    mark(dep)
            for tid in gates[args.gate]["requires"]:
                mark(tid)
        print("digraph toolkit {")
        print('  rankdir="LR";')
        for tid in order:
            if tid not in selected:
                continue
            item = by_id[tid]
            print(f'  "{tid}" [label="{tid}\\n{item["title"]}", group="{item["lane"]}"];')
            for dep in item["depends_on"]:
                if dep in selected:
                    print(f'  "{dep}" -> "{tid}";')
        print("}")
    elif args.command in {"claim", "release", "block", "unblock", "accept"}:
        tid = args.task
        if tid not in by_id:
            raise GraphError(f"unknown task: {tid}")
        with locked_state(args.state):
            state = load_state(args.state, by_id)
            if args.command == "claim":
                possible = ready(graph, by_id, state, None, parsed_caps(args))
                if tid not in {t["id"] for t in possible}:
                    raise GraphError(f"{tid}: unavailable, missing prerequisites/capabilities, no slots, or file ownership conflict")
                state["claimed"][tid] = {"worker": args.worker, "branch": args.branch, "claimed_at": now_utc()}
            elif args.command == "release":
                claim_record = state["claimed"].get(tid)
                if not claim_record or claim_record["worker"] != args.worker:
                    raise GraphError(f"{tid}: not claimed by {args.worker}")
                del state["claimed"][tid]
            elif args.command == "block":
                if tid in state["claimed"] or tid in state["accepted"]:
                    raise GraphError(f"{tid}: release claimed job before blocking; accepted tasks cannot be blocked")
                state["blocked"][tid] = args.reason
            elif args.command == "unblock":
                if tid not in state["blocked"]:
                    raise GraphError(f"{tid}: not blocked")
                del state["blocked"][tid]
            elif args.command == "accept":
                if not args.merged_and_verified:
                    raise GraphError("accept requires explicit --merged-and-verified")
                if tid not in state["claimed"]:
                    raise GraphError(f"{tid}: must be claimed before recording acceptance")
                if not re.fullmatch(r"[0-9a-fA-F]{40}", args.merge_commit):
                    raise GraphError("accept requires full 40-character merged commit SHA")
                state["accepted"][tid] = {
                    "commit": args.merge_commit,
                    "receipt": args.receipt,
                    "reviewed_by": args.reviewed_by,
                    "accepted_at": now_utc(),
                    "worker": state["claimed"][tid]["worker"],
                }
                del state["claimed"][tid]
            validate_state_object(state, by_id)
            write_json(args.state, state)
        print(json.dumps({"ok": True, "action": args.command, "task": tid, "state": str(args.state)}))
    return 0


def validate_state_object(state: dict, by_id: dict) -> bool:
    """Re-use load_state validation for in-memory modified coordinator state."""
    accepted = set(state["accepted"])
    claimed = set(state["claimed"])
    blocked = set(state["blocked"])
    if (accepted & claimed) or (accepted & blocked) or (claimed & blocked):
        raise GraphError("task status overlap")
    for tid in accepted | claimed:
        for dep in by_id[tid]["depends_on"]:
            if dep not in accepted:
                raise GraphError(f"{tid}: unsatisfied prerequisite {dep}")
    return True


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (GraphError, FileNotFoundError, json.JSONDecodeError, OSError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}), file=sys.stderr)
        raise SystemExit(2)
