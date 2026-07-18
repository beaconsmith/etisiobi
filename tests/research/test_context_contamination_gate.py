from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


class ContextContaminationGateTest(unittest.TestCase):
    def test_hidden_evaluation_frame_patterns_are_rejected(self):
        from scripts.validate_context_contamination import (
            CONTAMINATION_PATTERNS,
            match_patterns,
        )

        contaminated = """
        This article is part of the first ten Etisiobi papers. It receives
        internal approval after validator checks and review-team trace review,
        but it is not external submission ready. The result is framed for the
        arXiv-quality gate and should satisfy the evaluation benchmark.
        """

        hits = match_patterns(contaminated, CONTAMINATION_PATTERNS)

        self.assertGreaterEqual(len(hits), 6)

    def test_current_manuscript_set_records_context_contamination(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_context_contamination.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("CONTEXT_CONTAMINATION_FAIL", result.stdout)

    def test_article_006_remains_clean_under_context_gate(self):
        from scripts.validate_context_contamination import validate_article

        article_dir = ROOT / "papers" / "nwagu_aneke_articles" / "006-unicode-readiness"
        result = validate_article(article_dir)

        self.assertTrue(result["context_contamination_pass"], result["blockers"])


if __name__ == "__main__":
    unittest.main()
