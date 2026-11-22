"""Smoke and failure-mode tests for Etisiobi's Oroma feedback harness."""
from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
NAME = "research_feedback_source_guard"
SPEC = importlib.util.spec_from_file_location(NAME, ROOT / "spine" / "research_feedback.py")
harness = importlib.util.module_from_spec(SPEC)
sys.modules[NAME] = harness
SPEC.loader.exec_module(harness)


class ResearchFeedbackSourceGuardTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.checkout = self.root / "product"
        self.output = self.root / "output"

    def create_checkout(self, vite: bool = True):
        for path, content in {
            "AGENTS.md": "# Current product instructions",
            "package.json": '{"name":"oroma-product"}',
            "apps/agents-api/src/routes/workspaces.ts": "export {}",
            "packages/db/src/schema/workspaces.ts": "export {}",
        }.items():
            dest = self.checkout / path
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(content, encoding="utf-8")
        ui = ("apps/oroma-experience/src/surfaces/Home.tsx" if vite else "frontend/app/page.tsx")
        target = self.checkout / ui
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("export default function Home(){return null}", encoding="utf-8")

    def run_harness(self):
        args = ["research_feedback.py", "--oroma", str(self.checkout), "--out", str(self.output)]
        with patch.object(sys, "argv", args):
            return harness.main()

    def test_missing_product_checkout_fails_without_reports(self):
        self.assertEqual(self.run_harness(), 2)
        self.assertFalse(self.output.exists())

    def test_incomplete_checkout_fails_without_reports(self):
        self.checkout.mkdir()
        (self.checkout / "AGENTS.md").write_text("Agent", encoding="utf-8")
        self.assertEqual(self.run_harness(), 2)
        self.assertFalse(self.output.exists())

    def test_current_vite_layout_generates_grounded_counts(self):
        self.create_checkout(vite=True)
        self.assertEqual(self.run_harness(), 0)
        self.assertEqual(harness.frontend_surface_count(self.checkout), 1)
        report = (self.output / "backend_truth_findings.md").read_text(encoding="utf-8")
        self.assertIn("Observed route files: 1; schema files: 1.", report)
        ui = (self.output / "ui_benchmark_findings.md").read_text(encoding="utf-8")
        self.assertIn("Observed 1 frontend page/surface TSX files", ui)

    def test_missing_assessment_not_reported_as_current_critical_defect(self):
        self.create_checkout()
        self.assertEqual(self.run_harness(), 0)
        report = (self.output / "engineering_risks.md").read_text(encoding="utf-8")
        self.assertIn("Backend readiness is not established by this repository scan.", report)
        self.assertIn(" | REVIEW | ", report)
        self.assertNotIn("institutional-readiness score 1/5", report)

    def test_legacy_nextjs_layout_still_supported(self):
        self.create_checkout(vite=False)
        self.assertEqual(self.run_harness(), 0)
        self.assertEqual(harness.frontend_surface_count(self.checkout), 1)

    def test_default_points_to_successor_repository(self):
        content = (ROOT / "spine/research_feedback.py").read_text(encoding="utf-8")
        self.assertIn('default="../oroma-product"', content)


if __name__ == "__main__":
    unittest.main()
