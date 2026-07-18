from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "papers" / "nwagu_aneke_articles_cycle2"
FIRST_STATUS = ROOT / "research_runs" / "approved_papers_goal" / "approval_status.json"
OUT_DIR = ROOT / "research_runs" / "storm_acceleration_cycle2"
TARGET = 10
MIN_WORDS = 4800
MIN_CITES = 22

REQUIRED_ROLES = {
    "research_lead",
    "domain_postdoc",
    "methods_reviewer",
    "adversarial_impact_reviewer",
    "citation_evidence_reviewer",
    "rights_authority_reviewer",
}

REQUIRED_FILES = [
    "main.tex",
    "main.pdf",
    "approved_paper.json",
    "final_submission_readiness_decision.md",
    "claim_audit.md",
    "novelty_audit.md",
    "rights_authority_gate.md",
    "source_review_gate.md",
    "reproducibility_packet.md",
    "review_team_trace.jsonl",
    "storm_prewrite_trace.json",
    "perspective_questions.md",
    "outline_quality_audit.md",
    "red_herring_audit.md",
    "acceleration_trace.json",
    "package_manifest.json",
]

FORBIDDEN_PATTERNS = [
    re.compile(r"27/216\s+is\s+source[- ]observed", re.I),
    re.compile(r"216\s+is\s+source[- ]observed", re.I),
    re.compile(r"proves\s+E6", re.I),
    re.compile(r"proves\s+universal\s+compression", re.I),
    re.compile(r"public\s+release\s+is\s+approved", re.I),
    re.compile(r"arxiv[- ]ready", re.I),
    re.compile(r"journal[- ]submission[- ]ready", re.I),
]

FORBIDDEN_PHRASES = [
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
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path.as_posix()}:{line_number}: {exc}") from exc
        if not isinstance(value, dict):
            raise ValueError(f"{path.as_posix()}:{line_number}: JSONL row must be an object")
        rows.append(value)
    return rows


def plain_word_count(tex: str) -> int:
    stripped = re.sub(r"\\cite\{[^}]+\}", " citation ", tex)
    stripped = re.sub(r"\\begin\{verbatim\}.*?\\end\{verbatim\}", " ", stripped, flags=re.S)
    stripped = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?(?:\{[^}]*\})?", " ", stripped)
    return len(re.findall(r"[A-Za-z][A-Za-z0-9/-]+", stripped))


def citation_keys(tex: str) -> set[str]:
    keys: set[str] = set()
    for group in re.findall(r"\\cite\{([^}]+)\}", tex):
        keys.update(key.strip() for key in group.split(",") if key.strip())
    return keys


def bib_keys(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return set(re.findall(r"@\w+\{([^,\s]+)", path.read_text(encoding="utf-8", errors="replace")))


def first_cycle_approved() -> set[str]:
    if not FIRST_STATUS.exists():
        return set()
    status = read_json(FIRST_STATUS)
    if status.get("status") != "APPROVED_PAPERS_GOAL_MET":
        return set()
    return set(status.get("approved_articles", []))


def validate_review_trace(article_dir: Path) -> list[str]:
    trace_path = article_dir / "review_team_trace.jsonl"
    errors: list[str] = []
    try:
        rows = read_jsonl(trace_path)
    except ValueError as exc:
        return [str(exc)]
    by_role = {str(row.get("role", "")): row for row in rows}
    for role in sorted(REQUIRED_ROLES):
        row = by_role.get(role)
        if row is None:
            errors.append(f"review trace missing role {role}")
            continue
        if row.get("status") != "PASS":
            errors.append(f"{role} status is not PASS")
        if not str(row.get("agent_id", "")).strip():
            errors.append(f"{role} missing agent_id")
        summary = str(row.get("summary", "")).strip()
        if len(summary.split()) < 8:
            errors.append(f"{role} summary too thin")
        files = row.get("files_reviewed", [])
        if not isinstance(files, list) or len(files) < 3:
            errors.append(f"{role} must review at least three files")
        else:
            for file_path in files:
                if not (ROOT / str(file_path)).exists():
                    errors.append(f"{role} reviewed missing file {file_path}")
        if row.get("blocking_issues") not in ([], None):
            errors.append(f"{role} has blocking issues")
    return errors


def validate_article(article: dict[str, Any], approved_first: set[str], known_bib: set[str]) -> dict[str, Any]:
    slug = str(article.get("slug", ""))
    article_id = str(article.get("id", slug))
    article_dir = PACKAGE / slug
    blockers: list[str] = []
    result: dict[str, Any] = {
        "article_id": article_id,
        "slug": slug,
        "approved": False,
        "blockers": blockers,
    }

    for file_name in REQUIRED_FILES:
        if not (article_dir / file_name).exists():
            blockers.append(f"missing {file_name}")

    tex_path = article_dir / "main.tex"
    if tex_path.exists():
        tex = tex_path.read_text(encoding="utf-8", errors="replace")
        words = plain_word_count(tex)
        cites = citation_keys(tex)
        result["word_count"] = words
        result["unique_citations"] = len(cites)
        if words < MIN_WORDS:
            blockers.append(f"manuscript too short for cycle-two paper: {words} words")
        if len(cites) < MIN_CITES:
            blockers.append(f"too few unique citations for cycle-two paper: {len(cites)}")
        missing_cites = sorted(cites - known_bib)
        if missing_cites:
            blockers.append("unresolved citation keys: " + ", ".join(missing_cites[:8]))
        for pattern in FORBIDDEN_PATTERNS:
            if pattern.search(tex):
                blockers.append(f"forbidden overclaim: {pattern.pattern}")
        lowered = tex.lower()
        for phrase in FORBIDDEN_PHRASES:
            if phrase.lower() in lowered:
                blockers.append(f"forbidden internal/meta phrase remains: {phrase}")
        required_text = ["26 by 8", "derived", "f/v", "STORM", "perspective", "red-herring"]
        for token in required_text:
            if token.lower() not in lowered:
                blockers.append(f"missing required manuscript concept: {token}")

    approval_path = article_dir / "approved_paper.json"
    if approval_path.exists():
        approval = read_json(approval_path)
        if approval.get("status") != "APPROVED_INTERNAL_RESEARCH_PAPER_CYCLE2":
            blockers.append("approved_paper.json status is not APPROVED_INTERNAL_RESEARCH_PAPER_CYCLE2")
        gates = approval.get("gates", {})
        for gate in (
            "evidence",
            "citations",
            "source_review",
            "rights_authority",
            "review_team",
            "reproducibility",
            "storm_prewrite",
            "recursion",
        ):
            if gates.get(gate) != "PASS":
                blockers.append(f"approval gate {gate} is not PASS")
        builds_on = set(approval.get("builds_on", []))
        if not builds_on:
            blockers.append("approval missing recursive builds_on list")
        elif not builds_on.issubset(approved_first | {item.get("id") for item in read_json(PACKAGE / "manifest.json").get("articles", [])}):
            blockers.append("approval builds_on includes unknown or unapproved articles")

    storm_path = article_dir / "storm_prewrite_trace.json"
    if storm_path.exists():
        storm = read_json(storm_path)
        perspectives = storm.get("perspectives", [])
        if len(perspectives) < 6:
            blockers.append("STORM trace has fewer than six perspectives")
        if not storm.get("source_urls") or len(storm.get("source_urls", [])) < 3:
            blockers.append("STORM trace missing source URLs")

    acceleration_path = article_dir / "acceleration_trace.json"
    if acceleration_path.exists():
        acceleration = read_json(acceleration_path)
        if acceleration.get("cycle") != 2:
            blockers.append("acceleration trace cycle is not 2")
        if not acceleration.get("builds_on"):
            blockers.append("acceleration trace missing builds_on")
        if not acceleration.get("new_research_operation"):
            blockers.append("acceleration trace missing new_research_operation")

    exp_id = str(article.get("experiment_id", ""))
    exp_result = ROOT / "experiments" / exp_id / "results.json"
    if not exp_result.exists():
        blockers.append(f"missing experiment result {exp_result.relative_to(ROOT).as_posix()}")
    else:
        exp = read_json(exp_result)
        if exp.get("article_id") != article_id:
            blockers.append("experiment result article_id mismatch")
        if exp.get("status") != "PASS":
            blockers.append("experiment result status is not PASS")

    pdf_path = article_dir / "main.pdf"
    if pdf_path.exists() and pdf_path.stat().st_size < 10000:
        blockers.append("main.pdf exists but is unexpectedly small")

    blockers.extend(validate_review_trace(article_dir))

    if not blockers:
        result["approved"] = True
    return result


def build_report() -> dict[str, Any]:
    errors: list[str] = []
    manifest_path = PACKAGE / "manifest.json"
    if not manifest_path.exists():
        return {
            "status": "NWAGU_CYCLE2_INVALID",
            "approved_count": 0,
            "target": TARGET,
            "errors": ["missing papers/nwagu_aneke_articles_cycle2/manifest.json"],
            "articles": [],
        }
    manifest = read_json(manifest_path)
    if manifest.get("cycle") != 2:
        errors.append("manifest cycle is not 2")
    approved_first = first_cycle_approved()
    if len(approved_first) < 10:
        errors.append("first-cycle approved status is missing or incomplete")
    known_bib = bib_keys(PACKAGE / "references.bib")
    if "shao2024storm" not in known_bib or "jiang2024costorm" not in known_bib:
        errors.append("cycle-two bibliography missing STORM or Co-STORM sources")
    articles = [validate_article(article, approved_first, known_bib) for article in manifest.get("articles", [])]
    direct_first_cycle: set[str] = set()
    for article in manifest.get("articles", []):
        for parent in article.get("builds_on", []):
            parent_text = str(parent)
            if re.match(r"ARTICLE-NA-0(0[1-9]|10)$", parent_text):
                direct_first_cycle.add(parent_text)
    missing_first_cycle = sorted(approved_first - direct_first_cycle)
    if missing_first_cycle:
        errors.append("cycle-two manifest does not directly build on first-cycle articles: " + ", ".join(missing_first_cycle))
    approved = [article for article in articles if article["approved"]]
    status = "NWAGU_CYCLE2_APPROVED_GOAL_MET" if not errors and len(approved) >= TARGET else "NWAGU_CYCLE2_APPROVED_GOAL_NOT_MET"
    return {
        "status": status,
        "target": TARGET,
        "approved_count": len(approved),
        "approved_articles": [article["article_id"] for article in approved],
        "errors": errors,
        "articles": articles,
    }


def main() -> int:
    report = build_report()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "cycle2_approval_status.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Cycle-Two Approved Papers Status",
        "",
        f"Status: `{report['status']}`",
        f"Approved: {report['approved_count']} / {report['target']}",
        "",
    ]
    if report.get("errors"):
        lines.append("## Global Errors")
        lines.extend(f"- {error}" for error in report["errors"])
        lines.append("")
    lines.append("## Article Blockers")
    lines.append("")
    for article in report.get("articles", []):
        lines.append(f"### {article['article_id']} - {article['slug']}")
        if article["approved"]:
            lines.append("- APPROVED")
        else:
            for blocker in article["blockers"][:30]:
                lines.append(f"- {blocker}")
        lines.append("")
    (OUT_DIR / "cycle2_approval_status.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(report["status"])
    print(f"approved={report['approved_count']}/{report['target']}")
    return 0 if report["status"] == "NWAGU_CYCLE2_APPROVED_GOAL_MET" else 1


if __name__ == "__main__":
    raise SystemExit(main())
