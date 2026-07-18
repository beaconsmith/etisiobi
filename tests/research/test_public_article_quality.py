from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PACKAGE = ROOT / "papers" / "nwagu_aneke_articles"

FORBIDDEN_PUBLIC_TEX = [
    r"\bEXP-NA-\d{3}\b",
    r"\bNA-BENCH-\d{3}\b",
    r"\bIJRS\b",
    r"Benchmark task",
    r"Evidence score",
    r"Evidence-gated result for ARTICLE",
    r"\bBMC\b",
    r"repo-local",
    r"experiments/",
    r"benchmarks/",
    r"impact-journal readiness score",
    r"hostile review",
    r"publication gate",
    r"claim gate",
    r"claim-gated",
    r"claim gating",
]


def main_tex_files() -> list[Path]:
    return sorted(PACKAGE.glob("*/main.tex"))


def test_public_manuscripts_do_not_expose_internal_benchmark_artifacts() -> None:
    offenders: list[str] = []
    for tex_path in main_tex_files():
        text = tex_path.read_text(encoding="utf-8")
        for pattern in FORBIDDEN_PUBLIC_TEX:
            if re.search(pattern, text, flags=re.IGNORECASE):
                offenders.append(f"{tex_path.relative_to(ROOT).as_posix()}: {pattern}")
    assert offenders == []


def test_public_manuscripts_keep_reproducibility_without_repo_paths() -> None:
    offenders: list[str] = []
    for tex_path in main_tex_files():
        text = tex_path.read_text(encoding="utf-8")
        if r"\section{Reproducibility}" not in text:
            offenders.append(f"{tex_path.relative_to(ROOT).as_posix()}: missing reproducibility section")
        if re.search(r"\b(experiments|benchmarks|research_runs|scripts)/", text, flags=re.IGNORECASE):
            offenders.append(f"{tex_path.relative_to(ROOT).as_posix()}: exposes repo-local path in manuscript")
    assert offenders == []


def test_compiled_public_articles_have_no_overfull_horizontal_boxes() -> None:
    log_dir = PACKAGE / "compile_logs"
    offenders: list[str] = []
    for log_path in sorted(log_dir.glob("*.log")):
        text = log_path.read_text(encoding="utf-8", errors="replace")
        if "Overfull \\hbox" in text:
            offenders.append(log_path.relative_to(ROOT).as_posix())
    assert offenders == []


if __name__ == "__main__":
    test_public_manuscripts_do_not_expose_internal_benchmark_artifacts()
    test_public_manuscripts_keep_reproducibility_without_repo_paths()
    test_compiled_public_articles_have_no_overfull_horizontal_boxes()
    print("PUBLIC_ARTICLE_QUALITY_TEST_PASS")
