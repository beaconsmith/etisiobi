from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "papers" / "nwagu_aneke_articles"
REQUIRED_SECTIONS = [
    r"\section{Introduction}",
    r"\section{Related Work}",
    r"\section{Materials and Evidence}",
    r"\section{Method}",
    r"\section{Results}",
    r"\section{Discussion}",
    r"\section{Limitations}",
    r"\section{Reproducibility}",
    r"\section{Conclusion}",
]
FORBIDDEN_POSITIVE_PATTERNS = [
    r"proves universal compression",
    r"proves exceptional mathematics",
    r"completed glyph corpus has been reconstructed",
    r"27/216 is source[- ]observed",
]
FORBIDDEN_PUBLIC_ARTIFACTS = [
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


def bib_entry_count(text: str) -> int:
    return len(re.findall(r"@\w+\s*\{", text))


def validate_tex(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    if r"\documentclass[sigconf,nonacm]{acmart}" not in text:
        errors.append("missing acmart sigconf,nonacm documentclass")
    if r"\begin{abstract}" not in text or r"\end{abstract}" not in text:
        errors.append("missing abstract environment")
    if text.find(r"\begin{abstract}") > text.find(r"\maketitle"):
        errors.append("abstract must appear before maketitle")
    if r"\keywords{" not in text:
        errors.append("missing keywords")
    if r"\bibliographystyle{ACM-Reference-Format}" not in text:
        errors.append("missing ACM bibliography style")
    if r"\bibliography{../references}" not in text:
        errors.append("missing shared bibliography reference")
    citation_count = len(re.findall(r"\\cite\{[^}]+\}", text))
    if citation_count < 5:
        errors.append(f"too few citation groups: {citation_count}")
    for section in REQUIRED_SECTIONS:
        if section not in text:
            errors.append(f"missing section {section}")
    for pattern in FORBIDDEN_POSITIVE_PATTERNS:
        if re.search(pattern, text, flags=re.IGNORECASE):
            errors.append(f"forbidden overclaim pattern: {pattern}")
    for pattern in FORBIDDEN_PUBLIC_ARTIFACTS:
        if re.search(pattern, text, flags=re.IGNORECASE):
            errors.append(f"internal public-manuscript artifact: {pattern}")
    if "source-observed" not in text or "26 by 8" not in text:
        errors.append("missing source-observed 26-by-8 baseline")
    if "derived f/v" not in text and "derived layer" not in text:
        errors.append("missing derived f/v split qualifier")
    if "source transcription review" not in text or "rights review" not in text:
        errors.append("missing human-review limitation")
    if not any(
        phrase in text
        for phrase in (
            "The reported matrix can be reproduced",
            "The reported result can be reproduced",
            "Reproduction means checking",
            "The analysis package records",
        )
    ):
        errors.append("missing public reproducibility language")
    return errors


def main() -> int:
    errors: list[str] = []
    manifest_path = PACKAGE / "manifest.json"
    references_path = PACKAGE / "references.bib"
    readme_path = PACKAGE / "README.md"
    if not manifest_path.exists():
        errors.append("missing manifest.json")
        manifest = {"articles": []}
    else:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if not references_path.exists():
        errors.append("missing references.bib")
    else:
        reference_count = bib_entry_count(references_path.read_text(encoding="utf-8"))
        if reference_count < 20:
            errors.append(f"references.bib has too few entries: {reference_count}")
    if not readme_path.exists():
        errors.append("missing README.md")

    articles = manifest.get("articles", [])
    if len(articles) != 10:
        errors.append(f"manifest article_count mismatch: {len(articles)}")
    tex_paths = sorted(PACKAGE.glob("*/main.tex"))
    if len(tex_paths) != 10:
        errors.append(f"expected 10 main.tex files, found {len(tex_paths)}")

    seen_ids: set[str] = set()
    for article in articles:
        article_id = article.get("id", "")
        if article_id in seen_ids:
            errors.append(f"duplicate article id {article_id}")
        seen_ids.add(article_id)
        tex_path = PACKAGE / article.get("tex_path", "")
        status_path = tex_path.parent / "STATUS.md"
        if not tex_path.exists():
            errors.append(f"{article_id}: missing tex file {tex_path}")
            continue
        if not status_path.exists():
            errors.append(f"{article_id}: missing STATUS.md")
        errors.extend(f"{article_id}: {error}" for error in validate_tex(tex_path))
        if not article.get("experiment_id"):
            errors.append(f"{article_id}: manifest missing experiment_id")
        if not article.get("benchmark_task_id"):
            errors.append(f"{article_id}: manifest missing benchmark_task_id")

    if errors:
        print("NWAGU_ARTICLE_MANUSCRIPTS_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        if len(errors) > 200:
            print(f"- ... {len(errors) - 200} additional errors")
        return 1

    print("NWAGU_ARTICLE_MANUSCRIPTS_VALID")
    print(f"articles={len(articles)}")
    print(f"tex_files={len(tex_paths)}")
    print(f"references={bib_entry_count(references_path.read_text(encoding='utf-8'))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
