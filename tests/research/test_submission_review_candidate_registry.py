import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


class SubmissionReviewCandidateRegistryTest(unittest.TestCase):
    def test_registry_validator_accepts_current_candidate_state(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_submission_review_candidate_registry.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("SUBMISSION_REVIEW_CANDIDATE_REGISTRY_VALID", result.stdout)
        self.assertIn("candidates=10/10", result.stdout)


if __name__ == "__main__":
    unittest.main()
