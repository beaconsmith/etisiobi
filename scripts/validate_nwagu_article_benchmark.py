from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BENCH = ROOT / "benchmarks" / "nwagu_article_research"
PACKAGE = ROOT / "papers" / "nwagu_aneke_articles"


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> int:
    errors: list[str] = []
    required = [
        BENCH / "benchmark_tasks.jsonl",
        BENCH / "baseline.json",
        BENCH / "scoreboard.json",
        BENCH / "score_history.jsonl",
        BENCH / "task_scores.csv",
        BENCH / "article_quality.csv",
        BENCH / "BENCHMARK.md",
    ]
    for path in required:
        if not path.exists():
            errors.append(f"missing {path.relative_to(ROOT).as_posix()}")

    if not errors:
        tasks = read_jsonl(BENCH / "benchmark_tasks.jsonl")
        scoreboard = read_json(BENCH / "scoreboard.json")
        history = read_jsonl(BENCH / "score_history.jsonl")
        manifest = read_json(PACKAGE / "manifest.json")

        if len(tasks) != 10:
            errors.append(f"expected 10 benchmark tasks, found {len(tasks)}")
        if abs(sum(float(task["evidence_weight"]) for task in tasks) - 1.0) > 0.0001:
            errors.append("benchmark evidence weights must sum to 1.0")
        if sum(float(task["ijrs_weight"]) for task in tasks) != 100:
            errors.append("benchmark IJRS weights must sum to 100")
        if scoreboard.get("hard_gate_failures"):
            errors.append("scoreboard has hard gate failures")
        if scoreboard.get("status") not in {
            "WORKING_PAPER_SET_NOT_IMPACT_READY",
            "IMPACT_JOURNAL_CANDIDATE",
            "STRONG_JOURNAL_TRACK_DRAFT_NOT_SUBMISSION_READY",
            "INTERNAL_RESEARCH_DRAFT_BLOCKERS_DOMINATE",
            "REDESIGN_OR_DOWNGRADE",
            "REJECT_OR_FREEZE",
        }:
            errors.append(f"unknown benchmark status {scoreboard.get('status')}")
        if scoreboard.get("impact_journal_readiness_score", 0) >= 65 and scoreboard.get("status") == "WORKING_PAPER_SET_NOT_IMPACT_READY":
            errors.append("working-paper status cannot have IJRS >= 65")
        if scoreboard.get("impact_journal_readiness_score", 0) < 65 and scoreboard.get("status") != "WORKING_PAPER_SET_NOT_IMPACT_READY":
            errors.append("IJRS below impact threshold must use WORKING_PAPER_SET_NOT_IMPACT_READY")
        if not history:
            errors.append("score history is empty")
        if manifest.get("status") != "TARGETED_HUMAN_REVIEW_DRAFTS_NOT_SUBMISSION_READY":
            errors.append("article manifest has unexpected status")
        for article in manifest.get("articles", []):
            tex = PACKAGE / article["tex_path"]
            pdf = tex.with_suffix(".pdf")
            if not tex.exists():
                errors.append(f"missing article source {tex.relative_to(ROOT).as_posix()}")
            if not pdf.exists():
                errors.append(f"missing article PDF {pdf.relative_to(ROOT).as_posix()}")
            if not article.get("experiment_id") or not article.get("benchmark_task_id"):
                errors.append(f"{article.get('id')}: missing experiment_id or benchmark_task_id")

    if errors:
        print("NWAGU_ARTICLE_BENCHMARK_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        return 1
    print("NWAGU_ARTICLE_BENCHMARK_VALID")
    print("tasks=10")
    print(f"ijrs={read_json(BENCH / 'scoreboard.json')['impact_journal_readiness_score']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
