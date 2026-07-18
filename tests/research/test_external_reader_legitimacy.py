from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


class ExternalReaderLegitimacyTest(unittest.TestCase):
    def test_bad_package_prose_is_rejected_by_patterns(self):
        from scripts.validate_external_reader_legitimacy import (
            PACKAGE_PROCESS_PATTERNS,
            SELF_DESCRIBING_PAPER_PATTERNS,
            WEAK_SCIENTIFIC_CLAIM_PATTERNS,
            match_patterns,
        )

        bad_prose = """
        This article contributes a bounded research result for digital editions,
        annotation standards, and cultural-heritage interoperability. It has a
        result, a method, a claim ceiling, review files, and reproducibility
        materials, but it is not a journal submission package. Its value is that
        it extends the Nwagu Aneke research program without promoting derived,
        speculative, or blocked claims into primary source claims.
        References
        [1] Simon Ager. n.d.. Nwagu Aneke Syllabary. Omniglot.
        [2] arXiv. n.d.. Submit TeX/LaTeX.
        [3] Association for Computing Machinery. n.d.. Submissions: The Workflow
        and Templates.
        """

        hits = (
            match_patterns(bad_prose, PACKAGE_PROCESS_PATTERNS)
            + match_patterns(bad_prose, SELF_DESCRIBING_PAPER_PATTERNS)
            + match_patterns(bad_prose, WEAK_SCIENTIFIC_CLAIM_PATTERNS)
        )

        self.assertGreaterEqual(len(hits), 5)

    def test_current_candidate_set_fails_until_delabbed(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_external_reader_legitimacy.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("EXTERNAL_READER_LEGITIMACY_FAIL", result.stdout)


if __name__ == "__main__":
    unittest.main()
