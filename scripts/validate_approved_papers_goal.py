from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "papers" / "nwagu_aneke_articles"
TARGET = 10

REQUIRED_ROLES = {
    "research_lead",
    "domain_postdoc",
    "methods_reviewer",
    "adversarial_impact_reviewer",
    "citation_evidence_reviewer",
    "rights_authority_reviewer",
}

FORBIDDEN_OVERCLAIMS = [
    re.compile(r"27/216\s+is\s+source[- ]observed", re.I),
    re.compile(r"216\s+is\s+source[- ]observed", re.I),
    re.compile(r"proves\s+E6", re.I),
    re.compile(r"proves\s+universal\s+compression", re.I),
    re.compile(r"public\s+release\s+is\s+approved", re.I),
]

FORBIDDEN_INTERNAL_PHRASES = [
    "AI model talking to itself",
    "Impact-Journal Thesis",
    "Why The Earlier Draft Would Be Rejected",
    "IJRS",
    "Evidence-gated result for ARTICLE",
    "hostile review",
    "repo-local",
]


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path.as_posix()}:{line_number}: {exc}") from exc
        if not isinstance(row, dict):
            raise ValueError(f"{path.as_posix()}:{line_number}: row must be an object")
        rows.append(row)
    return rows


def plain_word_count(tex: str) -> int:
    stripped = re.sub(r"\\cite\{[^}]+\}", " citation ", tex)
    stripped = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?(?:\{[^}]*\})?", " ", stripped)
    return len(re.findall(r"[A-Za-z][A-Za-z0-9/-]+", stripped))


def citation_count(tex: str) -> int:
    keys: set[str] = set()
    for group in re.findall(r"\\cite\{([^}]+)\}", tex):
        keys.update(key.strip() for key in group.split(",") if key.strip())
    return len(keys)


def validate_review_trace(article_dir: Path) -> list[str]:
    trace = article_dir / "review_team_trace.jsonl"
    if not trace.exists():
        return ["missing review_team_trace.jsonl"]
    try:
        rows = read_jsonl(trace)
    except ValueError as exc:
        return [str(exc)]
    by_role = {str(row.get("role", "")): row for row in rows}
    errors: list[str] = []
    for role in sorted(REQUIRED_ROLES):
        row = by_role.get(role)
        if row is None:
            errors.append(f"review trace missing role {role}")
            continue
        if row.get("status") != "PASS":
            errors.append(f"{role} status is not PASS")
        if not str(row.get("agent_id", "")).strip():
            errors.append(f"{role} missing agent_id")
        if not row.get("files_reviewed"):
            errors.append(f"{role} missing files_reviewed")
        if row.get("blocking_issues") not in ([], None):
            errors.append(f"{role} has blocking_issues")
    return errors


def validate_article(article: dict[str, Any]) -> dict[str, Any]:
    slug = str(article.get("slug", ""))
    article_id = str(article.get("id", slug))
    article_dir = PACKAGE / slug
    tex_path = article_dir / "main.tex"
    checks: dict[str, Any] = {
        "article_id": article_id,
        "slug": slug,
        "approved": False,
        "blockers": [],
    }
    blockers: list[str] = checks["blockers"]

    required_files = {
        "main.tex": tex_path,
        "approved_paper.json": article_dir / "approved_paper.json",
        "final_submission_readiness_decision.md": article_dir / "final_submission_readiness_decision.md",
        "claim_audit.md": article_dir / "claim_audit.md",
        "novelty_audit.md": article_dir / "novelty_audit.md",
        "rights_authority_gate.md": article_dir / "rights_authority_gate.md",
        "source_review_gate.md": article_dir / "source_review_gate.md",
        "reproducibility_packet.md": article_dir / "reproducibility_packet.md",
        "review_team_trace.jsonl": article_dir / "review_team_trace.jsonl",
    }
    for label, path in required_files.items():
        if not path.exists():
            blockers.append(f"missing {label}")

    if tex_path.exists():
        tex = tex_path.read_text(encoding="utf-8", errors="replace")
        words = plain_word_count(tex)
        cites = citation_count(tex)
        checks["word_count"] = words
        checks["unique_citations"] = cites
        if words < 4500:
            blockers.append(f"manuscript too short for approved paper: {words} words")
        if cites < 20:
            blockers.append(f"too few unique citations for approved paper: {cites}")
        for pattern in FORBIDDEN_OVERCLAIMS:
            if pattern.search(tex):
                blockers.append(f"forbidden overclaim: {pattern.pattern}")
        lowered = tex.lower()
        for phrase in FORBIDDEN_INTERNAL_PHRASES:
            if phrase.lower() in lowered:
                blockers.append(f"internal/meta phrase remains: {phrase}")
        if "26 by 8" not in tex and "26 rows" not in tex:
            blockers.append("missing source-observed 26x8 foundation")
        if "derived" not in tex.lower() or "f/v" not in tex.lower():
            blockers.append("missing derived f/v layer qualifier")

    approval_path = article_dir / "approved_paper.json"
    if approval_path.exists():
        approval = read_json(approval_path)
        checks["approval_status"] = approval.get("status")
        if approval.get("status") != "APPROVED_INTERNAL_RESEARCH_PAPER":
            blockers.append("approved_paper.json status is not APPROVED_INTERNAL_RESEARCH_PAPER")
        gates = approval.get("gates", {})
        for gate in ("evidence", "citations", "source_review", "rights_authority", "review_team", "reproducibility"):
            if gates.get(gate) != "PASS":
                blockers.append(f"approval gate {gate} is not PASS")

    blockers.extend(validate_review_trace(article_dir))

    if not blockers:
        checks["approved"] = True
    return checks


def build_report() -> dict[str, Any]:
    manifest_path = PACKAGE / "manifest.json"
    if not manifest_path.exists():
        return {
            "status": "APPROVED_PAPERS_GOAL_INVALID",
            "approved_count": 0,
            "target": TARGET,
            "errors": ["missing papers/nwagu_aneke_articles/manifest.json"],
            "articles": [],
        }
    manifest = read_json(manifest_path)
    articles = [validate_article(article) for article in manifest.get("articles", [])]
    approved = [article for article in articles if article["approved"]]
    status = "APPROVED_PAPERS_GOAL_MET" if len(approved) >= TARGET else "APPROVED_PAPERS_GOAL_NOT_MET"
    return {
        "status": status,
        "target": TARGET,
        "approved_count": len(approved),
        "approved_articles": [article["article_id"] for article in approved],
        "articles": articles,
    }


def write_current(out_dir: Path, report: dict[str, Any]) -> None:
    (out_dir / "CURRENT.md").write_text(
        "\n".join(
            [
                "# Current Approved Papers Goal",
                "",
                f"- Status: `{report['status']}`",
                f"- Approved internal research papers: {report['approved_count']} / {report['target']}",
                "- External submission readiness: not claimed here",
                "- Canonical report: `research_runs/approved_papers_goal/approval_status.md`",
                "- Canonical machine state: `research_runs/approved_papers_goal/approval_status.json`",
            ]
        )
        + "\n",
        encoding="utf-8",
    )


def main() -> int:
    report = build_report()
    out_dir = ROOT / "research_runs" / "approved_papers_goal"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "approval_status.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Approved Papers Goal Status",
        "",
        f"Status: `{report['status']}`",
        f"Approved: {report['approved_count']} / {report['target']}",
        "",
        "## Article Blockers",
        "",
    ]
    for article in report.get("articles", []):
        lines.append(f"### {article['article_id']} - {article['slug']}")
        if article["approved"]:
            lines.append("- APPROVED")
        else:
            for blocker in article["blockers"][:20]:
                lines.append(f"- {blocker}")
        lines.append("")
    (out_dir / "approval_status.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    write_current(out_dir, report)

    print(report["status"])
    print(f"approved={report['approved_count']}/{report['target']}")
    return 0 if report["status"] == "APPROVED_PAPERS_GOAL_MET" else 1


if __name__ == "__main__":
    raise SystemExit(main())
