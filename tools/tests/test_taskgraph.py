"""Tests for the independent stdlib toolkit task DAG dispatcher.

Run: python -m unittest discover -s tools/tests -v
"""
import contextlib
import copy
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("rauken_taskgraph", ROOT / "tools" / "taskgraph.py")
tg = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tg)


class TaskGraphTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph = tg.read_json(ROOT / "tasks" / "toolkit-graph.json")
        cls.by_id, cls.order = tg.validate_graph(cls.graph)

    def test_real_graph_is_acyclic_complete_and_bounded(self):
        self.assertEqual(len(self.by_id), 68)
        self.assertEqual(len(self.order), 68)
        self.assertEqual([g["id"] for g in self.graph["gates"]], ["G0", "G1", "G2", "G3"])
        self.assertEqual(
            [t["id"] for t in tg.ready(self.graph, self.by_id, tg.empty_state(), 3, None)],
            ["CFG-001", "CFG-003", "CON-001"],
        )

    def test_reference_capabilities_exclude_win_tasks(self):
        selected = tg.ready(self.graph, self.by_id, tg.empty_state(), 3, {"python"})
        self.assertEqual([t["id"] for t in selected], ["CFG-003", "CON-001"])
        all_caps = {"python", "windows", "powershell"}
        self.assertEqual(len(tg.ready(self.graph, self.by_id, tg.empty_state(), 3, all_caps)), 3)

    def test_bad_dependency_and_cycle_fail(self):
        g = copy.deepcopy(self.graph)
        g["tasks"][0]["depends_on"] = ["NOT-999"]
        with self.assertRaisesRegex(tg.GraphError, "missing or self"):
            tg.validate_graph(g)
        g = copy.deepcopy(self.graph)
        g["tasks"][0]["depends_on"] = ["CFG-002"]
        with self.assertRaisesRegex(tg.GraphError, "cycle"):
            tg.validate_graph(g)

    def test_claimed_slots_and_path_overlap(self):
        state = tg.empty_state()
        for tid in ("CFG-001", "CFG-003", "CON-001"):
            state["claimed"][tid] = {"worker": "unit", "branch": "unit/branch"}
        self.assertEqual(tg.ready(self.graph, self.by_id, state, 3, None), [])
        self.assertTrue(tg.paths_overlap("toolkit/cli", "toolkit/cli/main.py"))
        self.assertFalse(tg.paths_overlap("toolkit/cli", "toolkit/qa"))
        self.assertTrue(tg.tasks_conflict({"write_paths": ["a/b"]}, {"write_paths": ["a/b/c"]}))

    def test_malformed_accepted_state_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            state_path = Path(directory) / "state.json"
            state = tg.empty_state()
            state["accepted"]["CLI-007"] = {"commit": "a" * 40, "receipt": "fake", "reviewed_by": "unit"}
            tg.write_json(state_path, state)
            with self.assertRaisesRegex(tg.GraphError, "prerequisite"):
                tg.load_state(state_path, self.by_id)

    def test_packet_is_self_contained_and_printable(self):
        item = self.by_id["PLT-003"]
        packet = tg.task_packet(item, self.graph, False)
        for value in ("PLT-003", "Softbough", "docs/asset-toolkit.md", "deliverables", "integrator"):
            self.assertIn(value.lower(), packet.lower())
        structured = json.loads(tg.task_packet(item, self.graph, True))
        self.assertEqual(structured["task"]["id"], "PLT-003")

    def test_coordinator_claim_release_and_accept_transitions(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "state.json"
            def run(*args):
                with contextlib.redirect_stdout(io.StringIO()) as sink:
                    result = tg.main(["--state", str(path), *args])
                self.assertEqual(result, 0)
                return sink.getvalue()
            claim = json.loads(run("claim", "CFG-003", "--worker", "worker-01",
                                   "--branch", "worker-01/cfg-003", "--capabilities", "python"))
            self.assertEqual(claim["action"], "claim")
            self.assertIn("CFG-003", tg.load_state(path, self.by_id)["claimed"])
            run("release", "CFG-003", "--worker", "worker-01")
            self.assertNotIn("CFG-003", tg.load_state(path, self.by_id)["claimed"])
            run("claim", "CFG-003", "--worker", "worker-01", "--branch", "worker-01/cfg-003")
            run("accept", "CFG-003", "--merge-commit", "a" * 40,
                "--receipt", "test-only-synthetic-receipt", "--reviewed-by", "test-reviewer",
                "--merged-and-verified")
            state = tg.load_state(path, self.by_id)
            self.assertIn("CFG-003", state["accepted"])
            self.assertNotIn("CFG-003", state["claimed"])
            self.assertEqual(tg.show_status(self.graph, self.by_id, state)["counts"]["accepted"], 1)
            self.assertFalse((path.parent / (path.name + ".lock")).exists())

    def test_writer_collision_guard_with_simulated_claims(self):
        state = tg.empty_state()
        state["claimed"]["CFG-003"] = {"worker": "a", "branch": "a"}
        # Force an overlapping write prefix in an otherwise-independent root to test dispatcher guard.
        graph = copy.deepcopy(self.graph)
        by_id, _ = tg.validate_graph(graph)
        by_id["CON-001"]["write_paths"] = ["tools/workspace.py"]
        selection = tg.ready(graph, by_id, state, 3, None)
        self.assertNotIn("CON-001", [t["id"] for t in selection])


if __name__ == "__main__":
    unittest.main()
