from __future__ import annotations

import csv
import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "score_count_layer_comprehension_results.py"
QUESTIONS = (
    ROOT
    / "research"
    / "frontier"
    / "nwagu_aneke"
    / "interfaces"
    / "usability"
    / "count_layer_comprehension_questions.csv"
)


def load_scorer():
    spec = importlib.util.spec_from_file_location("score_count_layer_comprehension_results", SCRIPT)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def write_results(path: Path, respondent_scores: dict[str, dict[str, str]]) -> None:
    fieldnames = [
        "respondent_id",
        "date",
        "role",
        "question_id",
        "answer",
        "expected_layer",
        "correct",
        "confusion_type",
        "notes",
    ]
    expected_layers = {
        "Q01": "source_observed",
        "Q02": "derived_f_v",
        "Q03": "derived_f_v",
        "Q04": "restricted_blocked",
        "Q05": "speculative_frontier",
        "Q06": "applied_design",
        "Q07": "computational_evaluation",
        "Q08": "contested_counts",
        "Q09": "dropped_branches",
        "Q10": "restricted_blocked",
    }
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for respondent_id, scores in respondent_scores.items():
            for question_id, value in scores.items():
                writer.writerow(
                    {
                        "respondent_id": respondent_id,
                        "date": "2026-06-22",
                        "role": "test_reader",
                        "question_id": question_id,
                        "answer": f"{question_id} answer",
                        "expected_layer": expected_layers[question_id],
                        "correct": value,
                        "confusion_type": "" if value == "correct" else "source_derived_collapse",
                        "notes": "",
                    }
                )


def all_correct() -> dict[str, str]:
    return {f"Q{index:02d}": "correct" for index in range(1, 11)}


class CountLayerComprehensionScoringTest(unittest.TestCase):
    def test_scores_pass_when_three_readers_preserve_source_derived_distinction(self) -> None:
        scorer = load_scorer()
        with tempfile.TemporaryDirectory() as tmpdir:
            results_path = Path(tmpdir) / "passing_results.csv"
            write_results(
                results_path,
                {
                    "R001": all_correct(),
                    "R002": all_correct(),
                    "R003": all_correct(),
                },
            )

            report = scorer.score_results(QUESTIONS, results_path)

        self.assertEqual(report["status"], "PASS_INTERNAL_COMPREHENSION_CHECK")
        self.assertEqual(report["reader_count"], 3)
        self.assertEqual(report["overall_correct_rate"], 1.0)
        self.assertEqual(report["derived_27_216_correct_rate"], 1.0)
        self.assertEqual(report["claim_ceiling"], "human_comprehension_signal_not_source_evidence")

    def test_scores_fail_when_derived_27_216_threshold_is_missed(self) -> None:
        scorer = load_scorer()
        weak_reader = all_correct()
        weak_reader["Q02"] = "incorrect"
        with tempfile.TemporaryDirectory() as tmpdir:
            results_path = Path(tmpdir) / "failing_results.csv"
            write_results(
                results_path,
                {
                    "R001": all_correct(),
                    "R002": all_correct(),
                    "R003": weak_reader,
                },
            )

            report = scorer.score_results(QUESTIONS, results_path)

        self.assertEqual(report["status"], "FAIL_LABEL_REVISION_REQUIRED")
        self.assertLess(report["derived_27_216_correct_rate"], 0.8)
        self.assertIn("27/216 derived distinction below 80%", report["blocking_issues"])

    def test_scores_reject_incomplete_reader_runs(self) -> None:
        scorer = load_scorer()
        incomplete = all_correct()
        incomplete.pop("Q10")
        with tempfile.TemporaryDirectory() as tmpdir:
            results_path = Path(tmpdir) / "incomplete_results.csv"
            write_results(
                results_path,
                {
                    "R001": all_correct(),
                    "R002": all_correct(),
                    "R003": incomplete,
                },
            )

            report = scorer.score_results(QUESTIONS, results_path)

        self.assertEqual(report["status"], "INVALID_READER_RUN")
        self.assertIn("R003 missing questions: Q10", report["blocking_issues"])


if __name__ == "__main__":
    unittest.main()
