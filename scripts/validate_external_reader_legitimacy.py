from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "research_runs" / "journal_submission_readiness" / "candidate_registry.json"
OUT_DIR = ROOT / "research_runs" / "external_reader_legitimacy"


PRIVATE_FRAMING_PATTERNS = [
    r"\bBeaconsmith Collective\b",
    r"\bEtisiobi\b",
    r"\bARTICLE-NA-\d{3}\b",
    r"\bEXP-NA-\d{3}\b",
    r"\bNA-BENCH-\d{3}\b",
    r"\bacmConference\[[^\]]*Etisiobi",
    r"\bEtisiobi Research Studio\b",
    r"\bNwagu Aneke Article Program\b",
    r"\bInternal Review\b",
    r"\bDevelopment Review\b",
    r"\bdevelopment-reviewed\b",
    r"\bdevelopment-stage\b",
    r"\boriginating lab\b",
    r"\binternal lab\b",
    r"\bresearch archive\b",
    r"\bresearch program\b",
    r"\bNwagu Aneke research program\b",
]

PACKAGE_PROCESS_PATTERNS = [
    r"\bclaim ceiling\b",
    r"\bclaim ceilings\b",
    r"\breview files\b",
    r"\breview packet\b",
    r"\breview-role\b",
    r"\brole-review\b",
    r"\breview-team\b",
    r"\breproducibility materials\b",
    r"\breproducibility packet\b",
    r"\banalysis package\b",
    r"\bsubmission-review candidate\b",
    r"\bjournal package\b",
    r"\bnot a journal submission package\b",
    r"\bnot a submission candidate\b",
    r"\bnot public-release\b",
    r"\bnot public release\b",
    r"\bnot external submission\b",
    r"\bnot a finished public submission\b",
    r"\bnot ready for submission\b",
    r"\bvalidator\b",
    r"\bgate checks\b",
    r"\bgates pass\b",
    r"\bevidence gates\b",
]

SELF_DESCRIBING_PAPER_PATTERNS = [
    r"\bThis article contributes a bounded research result\b",
    r"\bThis article develops a bounded research paper\b",
    r"\bbounded research result\b",
    r"\bIt has a result, a method\b",
    r"\bIts value is that it extends\b",
    r"\bThe article-specific result\b",
    r"\bThe present article meets\b",
    r"\bThe paper can be cited inside the lab\b",
    r"\bThis is the correct intermediate state\b",
    r"\bA weaker process would\b",
    r"\bThe stronger process\b",
]

WEAK_SCIENTIFIC_CLAIM_PATTERNS = [
    r"\buseful because it advances one research branch\b",
    r"\bnot a decorative application\b",
    r"\bthe local finding\b",
    r"\bfuture external reviewers should be asked to evaluate\b",
    r"\bwithout pretending\b",
    r"\bdoes not pretend\b",
]

REFERENCE_FILLER_PATTERNS = [
    r"\barXiv\. n\.d\.",
    r"\bSubmit TeX/LaTeX\b",
    r"\bAssociation for Computing Machinery\. n\.d\.",
    r"\bSubmissions: The Workflow and Templates\b",
]

ABSTRACT_FORBIDDEN_PATTERNS = [
    r"\bbounded\b",
    r"\barticle-specific\b",
    r"\breview packet\b",
    r"\breproducibility\b",
    r"\bclaim ceiling\b",
    r"\bdoes not claim\b",
    r"\bdoes not pretend\b",
    r"\bnot a\b",
    r"\bEtisiobi\b",
    r"\bBeaconsmith\b",
    r"\bARTICLE-NA\b",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def strip_latex_commands(text: str) -> str:
    text = re.sub(r"\\cite\{[^}]*\}", " ", text)
    text = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?(?:\{([^{}]*)\})?", r" \1 ", text)
    text = re.sub(r"[{}_$]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def abstract_text(tex: str) -> str:
    match = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", tex, flags=re.S)
    return match.group(1) if match else ""


def conclusion_text(tex: str) -> str:
    match = re.search(r"\\section\{Conclusion\}(.*?)(?:\\bibliographystyle|\\section\{)", tex, flags=re.S)
    return match.group(1) if match else ""


def match_patterns(tex: str, patterns: list[str]) -> list[str]:
    return [pattern for pattern in patterns if re.search(pattern, tex, flags=re.I)]


def candidate_dirs() -> list[tuple[str, Path]]:
    registry = json.loads(read_text(REGISTRY))
    rows: list[tuple[str, Path]] = []
    for candidate in registry.get("candidates", []):
        trace_path = ROOT / candidate["review_team_trace"]
        rows.append((candidate["article_id"], trace_path.parent))
    return rows


def validate_article(article_id: str, article_dir: Path) -> dict[str, object]:
    tex_path = article_dir / "main.tex"
    tex = read_text(tex_path) if tex_path.exists() else ""
    abstract = abstract_text(tex)
    conclusion = conclusion_text(tex)
    plain_conclusion = strip_latex_commands(conclusion)
    blockers: list[str] = []

    for label, patterns, scope in [
        ("private lab/project framing", PRIVATE_FRAMING_PATTERNS, tex),
        ("package/process prose", PACKAGE_PROCESS_PATTERNS, tex),
        ("self-describing paper prose", SELF_DESCRIBING_PAPER_PATTERNS, tex),
        ("weak non-scientific contribution phrasing", WEAK_SCIENTIFIC_CLAIM_PATTERNS, tex),
        ("template/submission reference filler", REFERENCE_FILLER_PATTERNS, tex),
    ]:
        hits = match_patterns(scope, patterns)
        if hits:
            blockers.append(f"{label}: {', '.join(hits[:8])}")

    abstract_hits = match_patterns(abstract, ABSTRACT_FORBIDDEN_PATTERNS)
    if abstract_hits:
        blockers.append(f"abstract reads like package/process note: {', '.join(abstract_hits[:8])}")

    if re.search(r"\b(has|contains|includes)\b.*\b(result|method|review|reproducibility|packet|files)\b", plain_conclusion, flags=re.I):
        blockers.append("conclusion inventories manuscript/package components instead of stating a field result")

    if len(re.findall(r"\\section\{(?:Materials and Evidence|Method|Results|Discussion|Limitations|Conclusion)\}", tex)) < 5:
        blockers.append("missing expected scientific sections")

    return {
        "article_id": article_id,
        "path": tex_path.relative_to(ROOT).as_posix(),
        "external_reader_legitimacy_pass": not blockers,
        "blockers": blockers,
    }


def build_report() -> dict[str, object]:
    articles = [validate_article(article_id, article_dir) for article_id, article_dir in candidate_dirs()]
    passed = [article for article in articles if article["external_reader_legitimacy_pass"]]
    return {
        "status": "EXTERNAL_READER_LEGITIMACY_PASS" if len(passed) == len(articles) else "EXTERNAL_READER_LEGITIMACY_FAIL",
        "passed_count": len(passed),
        "checked_count": len(articles),
        "articles": articles,
    }


def write_report(report: dict[str, object]) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "external_reader_legitimacy_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    lines = [
        "# External Reader Legitimacy Report",
        "",
        f"Status: `{report['status']}`",
        f"Passed: {report['passed_count']} / {report['checked_count']}",
        "",
        "This gate is intentionally stricter than structural arXiv quality. It rejects manuscripts that ask a reader to care about a private lab, registry, gate, packet, or process before the field contribution is legible.",
        "",
    ]
    for article in report["articles"]:  # type: ignore[index]
        lines.append(f"## {article['article_id']}")  # type: ignore[index]
        lines.append(f"Path: `{article['path']}`")  # type: ignore[index]
        if article["external_reader_legitimacy_pass"]:  # type: ignore[index]
            lines.append("- PASS")
        else:
            for blocker in article["blockers"][:12]:  # type: ignore[index]
                lines.append(f"- {blocker}")
        lines.append("")
    (OUT_DIR / "external_reader_legitimacy_report.md").write_text(
        "\n".join(lines).rstrip() + "\n",
        encoding="utf-8",
    )


def main() -> int:
    report = build_report()
    write_report(report)
    print(report["status"])
    print(f"passed={report['passed_count']}/{report['checked_count']}")
    return 0 if report["status"] == "EXTERNAL_READER_LEGITIMACY_PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
