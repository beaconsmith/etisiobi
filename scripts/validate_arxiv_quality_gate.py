from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "research_runs" / "arxiv_quality_reset"

PACKAGES = [
    ROOT / "papers" / "nwagu_aneke_articles",
    ROOT / "papers" / "nwagu_aneke_articles_cycle2",
]

FORBIDDEN_EXTERNAL_READY = re.compile(
    r"\bREADY_FOR_HUMAN_ARXIV_REVIEW\b|\bREADY_FOR_SUBMISSION\b|\bSUBMISSION_READY\b",
    re.I,
)

AI_TO_AI_MARKERS = [
    "internal approval",
    "internally approved",
    "this article is part of",
    "first ten etisiobi papers",
    "second cycle",
    "review-team trace",
    "validator checks",
    "approved internal",
    "not external submission",
    "paper receives internal approval",
    "the article is also designed to produce a cleaner reviewer packet",
    "reproduce the internal approval decision",
]

WEAK_RESULT_MARKERS = [
    "perspective trace",
    "outline-quality audit",
    "red-herring audit",
    "bounded question compiler",
    "converts the first-cycle ledger",
    "better research surface",
    "sharper research question",
]

REQUIRED_ARXIV_EVIDENCE_FILES = [
    "arxiv_quality_candidate.json",
    "external_prior_art_audit.md",
    "article_specific_experiment.md",
    "figures_tables_manifest.json",
    "human_source_review.md",
    "rights_submission_clearance.md",
    "reviewer2_response_plan.md",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(read_text(path))


def article_dirs(package: Path) -> list[Path]:
    if not package.exists():
        return []
    return sorted(path for path in package.iterdir() if path.is_dir() and re.match(r"^\d{3}-", path.name))


def tex_word_count(tex: str) -> int:
    stripped = re.sub(r"\\cite\{[^}]+\}", " citation ", tex)
    stripped = re.sub(r"\\begin\{verbatim\}.*?\\end\{verbatim\}", " ", stripped, flags=re.S)
    stripped = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?(?:\{[^}]*\})?", " ", stripped)
    return len(re.findall(r"[A-Za-z][A-Za-z0-9/-]+", stripped))


def citations(tex: str) -> set[str]:
    keys: set[str] = set()
    for group in re.findall(r"\\cite\{([^}]+)\}", tex):
        keys.update(key.strip() for key in group.split(",") if key.strip())
    return keys


def experiment_is_substantive(article_dir: Path) -> tuple[bool, str]:
    approved_path = article_dir / "approved_paper.json"
    if not approved_path.exists():
        return False, "missing approved_paper.json"
    try:
        approval = read_json(approved_path)
    except json.JSONDecodeError:
        return False, "approved_paper.json is invalid JSON"
    article_id = str(approval.get("article_id", ""))
    exp_ids: list[str] = []
    manifest_path = article_dir.parent / "manifest.json"
    if manifest_path.exists():
        manifest = read_json(manifest_path)
        for row in manifest.get("articles", []):
            if row.get("id") == article_id:
                exp_ids.append(str(row.get("experiment_id", "")))
    exp_ids.extend(str(value) for value in approval.get("experiment_ids", []) if value)
    exp_ids = [item for item in dict.fromkeys(exp_ids) if item]
    if not exp_ids:
        return False, "missing linked experiment id"

    weak_decisions = []
    for exp_id in exp_ids:
        result_path = ROOT / "experiments" / exp_id / "results.json"
        if not result_path.exists():
            return False, f"missing experiment result {exp_id}"
        result = read_json(result_path)
        text = json.dumps(result, ensure_ascii=False).lower()
        if any(marker in text for marker in ("approved_internal", "prewrite", "outline", "question compiler", "better research surface")):
            weak_decisions.append(exp_id)
    if weak_decisions:
        return False, "linked experiments are prewriting/approval artifacts, not substantive research results: " + ", ".join(weak_decisions)
    return True, "linked experiment looks substantive"


def validate_article(article_dir: Path) -> dict[str, Any]:
    blockers: list[str] = []
    tex_path = article_dir / "main.tex"
    tex = read_text(tex_path) if tex_path.exists() else ""
    lowered = tex.lower()
    if not tex:
        blockers.append("missing main.tex")
    else:
        word_count = tex_word_count(tex)
        cite_count = len(citations(tex))
        if word_count < 5000:
            blockers.append(f"manuscript below arXiv-quality depth threshold: {word_count} validator words")
        if cite_count < 25:
            blockers.append(f"too few unique citations for arXiv-quality candidate: {cite_count}")
        found_ai = [marker for marker in AI_TO_AI_MARKERS if marker in lowered]
        if found_ai:
            blockers.append("AI-to-AI/internal process language remains: " + ", ".join(found_ai[:6]))
        found_weak = [marker for marker in WEAK_RESULT_MARKERS if marker in lowered]
        if found_weak:
            blockers.append("result is framed as process/prewriting rather than discovery: " + ", ".join(found_weak[:6]))
        if "research question" not in lowered or "hypothesis" not in lowered:
            blockers.append("missing explicit research question and hypothesis pair")
        if "limitations" not in lowered:
            blockers.append("missing limitations section")
        if FORBIDDEN_EXTERNAL_READY.search(tex):
            blockers.append("contains external submission readiness claim")

    for file_name in REQUIRED_ARXIV_EVIDENCE_FILES:
        if not (article_dir / file_name).exists():
            blockers.append(f"missing arXiv-quality evidence file: {file_name}")

    substantive, reason = experiment_is_substantive(article_dir)
    if not substantive:
        blockers.append(reason)

    decision_path = article_dir / "final_submission_readiness_decision.md"
    if decision_path.exists():
        decision = read_text(decision_path).lower()
        if "not arxiv-ready" in decision or "not journal-submission-ready" in decision:
            blockers.append("own readiness decision says not arXiv/journal-submission ready")

    return {
        "article": article_dir.name,
        "package": article_dir.parent.name,
        "arxiv_quality_pass": not blockers,
        "blockers": blockers,
    }


def quality_gate_status(passed_count: int, checked_count: int) -> str:
    if checked_count > 0 and passed_count == checked_count:
        return "ARXIV_QUALITY_GATE_PASS"
    if passed_count > 0:
        return "ARXIV_QUALITY_GATE_PARTIAL"
    return "ARXIV_QUALITY_GATE_FAIL"


def build_report() -> dict[str, Any]:
    articles = [validate_article(article_dir) for package in PACKAGES for article_dir in article_dirs(package)]
    passed = [row for row in articles if row["arxiv_quality_pass"]]
    status = quality_gate_status(len(passed), len(articles))
    return {
        "status": status,
        "passed_count": len(passed),
        "checked_count": len(articles),
        "passed_articles": [row["article"] for row in passed],
        "articles": articles,
    }


def write_report(report: dict[str, Any]) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "arxiv_quality_gate_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    lines = [
        "# arXiv Quality Gate Report",
        "",
        f"Status: `{report['status']}`",
        f"Passed: {report['passed_count']} / {report['checked_count']}",
        "",
        "This gate is stricter than internal approval. It rejects manuscripts that read like an AI-to-AI lab process document, lack a substantive article-specific result, or carry their own not-ready decision.",
        "",
        "## Article Findings",
        "",
    ]
    for article in report["articles"]:
        lines.append(f"### {article['package']}/{article['article']}")
        if article["arxiv_quality_pass"]:
            lines.append("- PASS")
        else:
            for blocker in article["blockers"][:12]:
                lines.append(f"- {blocker}")
        lines.append("")
    (OUT_DIR / "arxiv_quality_gate_report.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    report = build_report()
    write_report(report)
    print(report["status"])
    print(f"passed={report['passed_count']}/{report['checked_count']}")
    return 0 if report["status"] == "ARXIV_QUALITY_GATE_PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
