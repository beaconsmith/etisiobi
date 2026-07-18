from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCOREBOARD = ROOT / "benchmarks" / "nwagu_article_research" / "scoreboard.json"


def test_failed_novelty_or_rights_blocks_impact_readiness() -> None:
    scoreboard = json.loads(SCOREBOARD.read_text(encoding="utf-8"))
    failed = {
        row["task_id"]
        for row in scoreboard["task_scores"]
        if row.get("passes_threshold") is False
    }

    assert {"NA-BENCH-004", "NA-BENCH-007"} & failed
    assert scoreboard["impact_journal_readiness_score"] < 65
    assert scoreboard["status"] == "WORKING_PAPER_SET_NOT_IMPACT_READY"


def test_article_quality_scores_do_not_reward_short_skeletons_as_impact_articles() -> None:
    scoreboard = json.loads(SCOREBOARD.read_text(encoding="utf-8"))
    short_articles = [
        row
        for row in scoreboard["article_quality"]
        if row["words"] < 3000
    ]

    assert len(short_articles) == 10
    assert max(row["article_quality_score"] for row in short_articles) <= 0.65


if __name__ == "__main__":
    test_failed_novelty_or_rights_blocks_impact_readiness()
    test_article_quality_scores_do_not_reward_short_skeletons_as_impact_articles()
    print("LAB_QUALITY_BAR_TEST_PASS")
