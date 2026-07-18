from __future__ import annotations

import argparse
import json
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any

from validate_approved_papers_goal import build_report


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "papers" / "nwagu_aneke_articles"
RUN_ROOT = ROOT / "research_runs" / "approved_papers_goal"
TARGET = 10


def now() -> str:
    return datetime.now().astimezone().replace(microsecond=0).isoformat()


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def git_output(*args: str) -> str:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        return (result.stdout or result.stderr).strip()
    except OSError:
        return "git unavailable"


def load_manifest() -> dict[str, Any]:
    return json.loads((PACKAGE / "manifest.json").read_text(encoding="utf-8"))


def score_candidate(article: dict[str, Any], current_report: dict[str, Any]) -> tuple[float, list[str]]:
    article_id = article.get("id")
    slug = article.get("slug")
    report_by_id = {row["article_id"]: row for row in current_report.get("articles", [])}
    blockers = report_by_id.get(article_id, {}).get("blockers", [])
    score = 0.0
    reasons: list[str] = []

    priority_bonus = {
        "ARTICLE-NA-002": 40,
        "ARTICLE-NA-010": 38,
        "ARTICLE-NA-005": 24,
        "ARTICLE-NA-009": 22,
        "ARTICLE-NA-001": 20,
        "ARTICLE-NA-006": 18,
        "ARTICLE-NA-003": 16,
        "ARTICLE-NA-004": 14,
        "ARTICLE-NA-008": 12,
        "ARTICLE-NA-007": 10,
    }.get(str(article_id), 0)
    score += priority_bonus
    reasons.append(f"portfolio_priority:{priority_bonus}")

    if blockers:
        score += max(0, 40 - len(blockers) * 2)
        reasons.append(f"blocker_count_adjusted:{max(0, 40 - len(blockers) * 2)}")
    else:
        score += 50
        reasons.append("no_blockers_detected:50")

    if slug in {"002-count-layer-drift", "010-layer-safe-generative-design"}:
        score += 15
        reasons.append("A_plus_active_hardening_branch:15")

    return score, reasons


def select_batch(max_active: int, report: dict[str, Any]) -> list[dict[str, Any]]:
    manifest = load_manifest()
    approved = set(report.get("approved_articles", []))
    candidates: list[dict[str, Any]] = []
    for article in manifest.get("articles", []):
        if article.get("id") in approved:
            continue
        score, reasons = score_candidate(article, report)
        enriched = dict(article)
        enriched["approval_loop_score"] = round(score, 2)
        enriched["score_reasons"] = reasons
        candidates.append(enriched)
    return sorted(candidates, key=lambda row: (-row["approval_loop_score"], row["id"]))[:max_active]


def write_goal_doc(report: dict[str, Any], batch: list[dict[str, Any]]) -> None:
    write_text(
        RUN_ROOT / "GOAL-10-APPROVED-PAPERS.md",
        f"""# Goal: 10 Approved Etisiobi Papers

Updated: {now()}

Status: `{report['status']}`

Approved count: {report['approved_count']} / {TARGET}

## Counting Rule

A paper counts only when:

- `approved_paper.json` says `APPROVED_INTERNAL_RESEARCH_PAPER`;
- all approval gates are `PASS`;
- `review_team_trace.jsonl` contains PASS reviews from all required roles;
- source, rights, citation, evidence, reproducibility, and review gates are clear;
- manuscript does not contain internal benchmark/progress-note language;
- manuscript preserves the 26x8 source layer and derived-only 27/216 invariant.

## Active Hardening Batch

{chr(10).join(f"- `{row['id']}`: {row['title']} (`{row['slug']}`)" for row in batch)}

## Stop Rule

Continue approved-paper loops until approved count is 10 / 10. Do not count
working drafts, formatted notes, review-blocked manuscripts, or papers with
rights/source/citation blockers.
""",
    )


def write_run(report: dict[str, Any], batch: list[dict[str, Any]]) -> dict[str, Any]:
    run_id = "RUN-APPROVED-" + datetime.now().astimezone().strftime("%Y%m%d-%H%M%S")
    run_dir = RUN_ROOT / run_id
    manifest = {
        "run_id": run_id,
        "generated_at": now(),
        "status": "APPROVED_PAPER_LOOP_CONTINUE" if report["approved_count"] < TARGET else "APPROVED_PAPER_LOOP_STOP",
        "approved_count": report["approved_count"],
        "target": TARGET,
        "git": {
            "branch": git_output("branch", "--show-current"),
            "commit": git_output("rev-parse", "--short", "HEAD"),
        },
        "selected_batch": batch,
        "next_action": "harden selected batch; do not mark approved until validator passes",
    }
    write_json(run_dir / "run_manifest.json", manifest)
    write_text(
        run_dir / "selected_batch.md",
        "# Selected Paper Hardening Batch\n\n"
        + "\n".join(
            f"## {idx}. {row['id']} - {row['title']}\n\n"
            f"- Slug: `{row['slug']}`\n"
            f"- Score: {row['approval_loop_score']}\n"
            f"- Reasons: {'; '.join(row['score_reasons'])}\n"
            f"- Current status: not approved until `scripts/validate_approved_papers_goal.py` passes.\n"
            for idx, row in enumerate(batch, start=1)
        ),
    )
    write_text(
        RUN_ROOT / "CURRENT.md",
        f"""# Current Approved Papers Loop

- Run: `{run_id}`
- Approved: {report['approved_count']} / {TARGET}
- Status: `{manifest['status']}`
- Manifest: `{run_dir.relative_to(ROOT).as_posix()}/run_manifest.json`
- Selected batch: `{run_dir.relative_to(ROOT).as_posix()}/selected_batch.md`
""",
    )
    return manifest


def append_log(manifest: dict[str, Any]) -> None:
    with (ROOT / "log.md").open("a", encoding="utf-8") as handle:
        handle.write(
            f"""

## [{manifest['generated_at'][:10]}] papers | approved-paper-loop | {manifest['run_id']}

- Approved count: {manifest['approved_count']} / {manifest['target']}
- Status: `{manifest['status']}`
- Selected batch: {', '.join(row['id'] for row in manifest['selected_batch'])}
- Rule: no paper counts without PASS review trace and clear source/rights/citation/evidence gates.
"""
        )


def run_once(max_active: int) -> dict[str, Any]:
    report = build_report()
    batch = select_batch(max_active=max_active, report=report)
    write_goal_doc(report, batch)
    write_json(RUN_ROOT / "approval_status.json", report)
    manifest = write_run(report, batch)
    append_log(manifest)
    print(manifest["status"])
    print(f"approved={manifest['approved_count']}/{manifest['target']}")
    print("selected=" + ",".join(row["id"] for row in batch))
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-active", type=int, default=2)
    args = parser.parse_args()
    if args.max_active < 1:
        raise SystemExit("--max-active must be >= 1")
    run_once(max_active=args.max_active)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
