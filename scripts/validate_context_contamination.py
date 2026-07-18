from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PACKAGES = [
    ROOT / "papers" / "nwagu_aneke_articles",
    ROOT / "papers" / "nwagu_aneke_articles_cycle2",
]
OUT_DIR = ROOT / "research_runs" / "context_contamination"
OUT_JSON = OUT_DIR / "context_contamination_report.json"
OUT_MD = OUT_DIR / "context_contamination_report.md"


CONTAMINATION_PATTERNS = [
    r"\bEtisiobi\b",
    r"\bBeaconsmith Collective\b",
    r"\bfirst ten Etisiobi papers\b",
    r"\bsecond cycle\b",
    r"\bARTICLE-NA-\d{3}\b",
    r"\bEXP-NA-\d{3}\b",
    r"\breview-team trace\b",
    r"\breview team trace\b",
    r"\breview packet\b",
    r"\breproducibility packet\b",
    r"\bsubmission sign[- ]off packet\b",
    r"\bvalidator checks?\b",
    r"\bvalidator\b",
    r"\bgate checks?\b",
    r"\bgate\b",
    r"\barXiv-quality gate\b",
    r"\barXiv-quality candidate\b",
    r"\barXiv-ready\b",
    r"\bnot arXiv-ready\b",
    r"\bnot journal-submission-ready\b",
    r"\bnot external submission\b",
    r"\bexternal submission readiness\b",
    r"\bsubmission-review candidate\b",
    r"\bjournal-submission-ready\b",
    r"\bimpact-journal\b",
    r"\bapproved internal\b",
    r"\binternal approval\b",
    r"\binternally approved\b",
    r"\bThe article is also designed to produce\b",
    r"\bThis article is part of\b",
    r"\bpaper receives internal approval\b",
    r"\breproduce the internal approval decision\b",
    r"\bown readiness decision\b",
    r"\bshould satisfy the evaluation benchmark\b",
    r"\bbeing tested\b",
    r"\bbeing evaluated\b",
    r"\bevaluation benchmark\b",
    r"\bevaluation awareness\b",
    r"\bfake scenario\b",
]

WEAK_BENCHMARK_SHAPING_PATTERNS = [
    r"\bbetter research surface\b",
    r"\bsharper research question\b",
    r"\bbounded question compiler\b",
    r"\boutline-quality audit\b",
    r"\bred-herring audit\b",
    r"\bperspective trace\b",
    r"\bconverts the first-cycle ledger\b",
]

SAFE_CONTEXT_PATTERNS = [
    r"\bUnicode-readiness\b",
    r"\breadiness audit\b",
    r"\bUnicode proposal\b",
    r"\bproposal framing\b",
    r"\bproposal dossier\b",
    r"\bUnicode roadmaps\b",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def article_dirs() -> list[Path]:
    rows: list[Path] = []
    for package in PACKAGES:
        if package.exists():
            rows.extend(sorted(path for path in package.iterdir() if path.is_dir() and re.match(r"^\d{3}-", path.name)))
    return rows


def match_patterns(text: str, patterns: list[str]) -> list[str]:
    return [pattern for pattern in patterns if re.search(pattern, text, flags=re.I)]


def strip_safe_context(text: str) -> str:
    stripped = text
    for pattern in SAFE_CONTEXT_PATTERNS:
        stripped = re.sub(pattern, " ", stripped, flags=re.I)
    return stripped


def validate_article(article_dir: Path) -> dict[str, Any]:
    tex_path = article_dir / "main.tex"
    tex = read_text(tex_path) if tex_path.exists() else ""
    scan_text = strip_safe_context(tex)
    blockers: list[str] = []

    contamination_hits = match_patterns(scan_text, CONTAMINATION_PATTERNS)
    if contamination_hits:
        blockers.append(
            "visible evaluation/status/lab-frame residue: "
            + ", ".join(contamination_hits[:12])
        )

    weak_hits = match_patterns(scan_text, WEAK_BENCHMARK_SHAPING_PATTERNS)
    if weak_hits:
        blockers.append(
            "manuscript appears shaped by benchmark/prewriting task language: "
            + ", ".join(weak_hits[:12])
        )

    if re.search(r"\b(this|the present)\s+(article|paper)\s+(contributes|develops)\s+a\s+bounded\b", scan_text, flags=re.I):
        blockers.append("self-describes contribution as a bounded package rather than reporting a field result")

    if re.search(r"\bnot\s+(a\s+)?(public release|journal submission|external submission|arXiv)\b", scan_text, flags=re.I):
        blockers.append("manuscript carries negative readiness/status disclaimer in public prose")

    return {
        "article": article_dir.name,
        "package": article_dir.parent.name,
        "path": tex_path.relative_to(ROOT).as_posix(),
        "context_contamination_pass": not blockers,
        "blockers": blockers,
    }


def build_report() -> dict[str, Any]:
    articles = [validate_article(article_dir) for article_dir in article_dirs()]
    passed = [article for article in articles if article["context_contamination_pass"]]
    status = "CONTEXT_CONTAMINATION_PASS" if len(passed) == len(articles) else "CONTEXT_CONTAMINATION_FAIL"
    return {
        "status": status,
        "passed_count": len(passed),
        "checked_count": len(articles),
        "passed_articles": [article["article"] for article in passed],
        "interpretation": (
            "This gate catches visible traces of hidden evaluation-frame contamination: lab status vocabulary, "
            "validator/gate language, packet prose, and benchmark-shaped manuscript framing. It is inspired by "
            "global-workspace evidence that task context can affect model behavior without appearing as ordinary output content."
        ),
        "articles": articles,
    }


def write_report(report: dict[str, Any]) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Context Contamination Report",
        "",
        f"Status: `{report['status']}`",
        f"Passed: {report['passed_count']} / {report['checked_count']}",
        "",
        str(report["interpretation"]),
        "",
        "## Article Findings",
        "",
    ]
    for article in report["articles"]:
        lines.append(f"### {article['package']}/{article['article']}")
        if article["context_contamination_pass"]:
            lines.append("- PASS")
        else:
            for blocker in article["blockers"][:8]:
                lines.append(f"- {blocker}")
        lines.append("")
    OUT_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    report = build_report()
    write_report(report)
    print(report["status"])
    print(f"passed={report['passed_count']}/{report['checked_count']}")
    return 0 if report["status"] == "CONTEXT_CONTAMINATION_PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
