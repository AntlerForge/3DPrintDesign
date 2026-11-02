"""Optional maintainer checks. Python is not required to use the skill."""

import json
from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\[[^\]]*\]\(([^\n)]+)\)")


def local_target(source, destination, root):
    destination = destination.strip().strip("<>")
    parsed = urlsplit(destination)
    if parsed.scheme or parsed.netloc or not parsed.path:
        return None
    target = (source.parent / unquote(parsed.path)).resolve()
    if not target.is_relative_to(root.resolve()):
        raise ValueError("Local link leaves the package")
    if not target.is_file():
        raise FileNotFoundError(target)
    return target


def check_graph(nodes, edges):
    ids = [node["id"] for node in nodes]
    if not ids or len(ids) != len(set(ids)):
        raise ValueError("Graph node ids must be nonempty and unique")
    adjacency = {node_id: [] for node_id in ids}
    for source, target, relation in edges:
        if source not in adjacency or target not in adjacency:
            raise ValueError("Unknown edge endpoint")
        if relation not in {"requires", "prefer_before"}:
            raise ValueError("Unknown edge relation")
        if relation == "requires":
            adjacency[source].append(target)
    visited, active = set(), set()

    def visit(node_id):
        if node_id in active:
            raise ValueError("Dependency cycle")
        if node_id in visited:
            return
        active.add(node_id)
        for target in adjacency[node_id]:
            visit(target)
        active.remove(node_id)
        visited.add(node_id)

    for node_id in ids:
        visit(node_id)


class PackageTests(unittest.TestCase):
    def test_entrypoints_exist(self):
        for name in ("SKILL.md", "README.md", "agents/openai.yaml"):
            self.assertTrue((ROOT / name).is_file(), name)

    def test_local_links_are_contained_and_resolvable(self):
        checked = 0
        for source in ROOT.rglob("*.md"):
            for match in LINK.finditer(source.read_text(encoding="utf-8")):
                target = local_target(source, match[1], ROOT)
                checked += target is not None
        self.assertGreater(checked, 0, "No local links were checked")

    def test_link_checker_rejects_escape_and_missing_files(self):
        source = ROOT / "SKILL.md"
        with self.assertRaises(ValueError):
            local_target(source, "../outside-package.md", ROOT)
        with self.assertRaises(FileNotFoundError):
            local_target(source, "missing-validation-fixture.md", ROOT)

    def test_json_is_parseable(self):
        files = list(ROOT.rglob("*.json"))
        self.assertTrue(files, "Workflow graph is missing")
        for source in files:
            self.assertIsInstance(json.loads(source.read_text()), dict)

    def test_workflow_dependencies(self):
        graph = json.loads((ROOT / "references/workflow-graph.json").read_text())
        workflows = graph["workflows"]
        ids = [workflow["id"] for workflow in workflows]
        self.assertTrue(ids)
        self.assertEqual(len(ids), len(set(ids)))
        for workflow in workflows:
            with self.subTest(workflow=workflow["id"]):
                check_graph(workflow["nodes"], workflow["edges"])
                for branch in workflow.get("branches", []):
                    if "use" in branch:
                        self.assertIn(branch["use"], ids)

    def test_dependency_checker_rejects_invalid_graphs(self):
        nodes = [{"id": "a"}, {"id": "b"}]
        with self.assertRaises(ValueError):
            check_graph(nodes, [["a", "missing", "requires"]])
        with self.assertRaises(ValueError):
            check_graph(nodes, [["a", "b", "requires"], ["b", "a", "requires"]])
        check_graph(nodes, [["a", "b", "prefer_before"], ["b", "a", "requires"]])


if __name__ == "__main__":
    unittest.main(verbosity=2)
