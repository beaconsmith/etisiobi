#!/usr/bin/env python3
"""Flag unsupported or over-strong PAGC claims in markdown files."""

from __future__ import annotations

import argparse
from pathlib import Path


RISK_PATTERNS = [
    "principia-level",
    "universal compression",
    "universal generative",
    "e6 symmetry",
    "genetic-code isomorphism",
    "genetic code isomorphism",
    "proves",
    "confirmed",
    "optimal",
    "27×8 matrix",
    "27x8 matrix",
]

ALLOW_CONTEXT = [
    "false until proven",
    "hypothesis",
    "unproven",
    "speculative",
    "falsification",
    "downgrade",
    "kill",
    "not yet prove",
]

SKIP_PARTS = {"primary_sources", "sources", "hermes_workspace"}


def is_skipped(path: Path) -> bool:
    return any(part in SKIP_PARTS for part in path.parts)


def has_allow_context(lines: list[str], index: int) -> bool:
    start = max(0, index - 2)
    end = min(len(lines), index + 3)
    window = " ".join(lines[start:end]).lower()
    return any(term in window for term in ALLOW_CONTEXT)


def scan(root: Path) -> list[tuple[Path, int, str, str]]:
    findings: list[tuple[Path, int, str, str]] = []
    for path in sorted(root.rglob("*.md")):
        if is_skipped(path):
            continue
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        for idx, line in enumerate(lines):
            lower = line.lower()
            for pattern in RISK_PATTERNS:
                if pattern in lower and not has_allow_context(lines, idx):
                    findings.append((path, idx + 1, pattern, line.strip()))
    return findings


def write_report(report_path: Path, findings: list[tuple[Path, int, str, str]], repo_root: Path) -> None:
    rows = [
        "# PAGC Unsupported Claim Gate",
        "",
        "This report flags strong PAGC language that may need source, extraction, or falsification support.",
        "",
        "| File | Line | Pattern | Text |",
        "|---|---:|---|---|",
    ]
    for path, line_no, pattern, text in findings:
        rel = path.relative_to(repo_root).as_posix()
        clean_text = text.replace("|", "\\|")
        rows.append(f"| `{rel}` | {line_no} | `{pattern}` | {clean_text} |")
    if not findings:
        rows.append("| _none_ |  |  |  |")
    rows.append("")
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(rows), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Flag unsupported PAGC claims.")
    parser.add_argument("--root", default="research/pagc", help="PAGC root to scan.")
    parser.add_argument("--report", default="research/pagc/CLAIM_GATE_REPORT.md", help="Markdown report path.")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero when findings exist.")
    args = parser.parse_args()

    repo_root = Path.cwd()
    root = (repo_root / args.root).resolve()
    report = (repo_root / args.report).resolve()
    findings = scan(root)
    write_report(report, findings, repo_root)
    print(f"Wrote {len(findings)} PAGC claim-gate findings to {report}")
    return 1 if args.strict and findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
