from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "papers" / "nwagu_aneke_articles"
BENCHMARK = ROOT / "benchmarks" / "nwagu_article_research" / "scoreboard.json"

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

FORBIDDEN_META_PHRASES = [
    "Why The Earlier Draft Would Be Rejected",
    "Impact-Journal Thesis",
    "What Was Fixed In This Revision",
    "A formatted PDF is not a publishable paper",
    "move from a formatted note",
    "AI model talking to itself",
]

FORBIDDEN_OVERCLAIMS = [
    r"27/216\s+is\s+source[- ]observed",
    r"216\s+is\s+source[- ]observed",
    r"proves\s+universal\s+compression",
    r"proves\s+E6",
    r"completed\s+glyph[- ]level\s+corpus",
    r"public\s+release\s+is\s+approved",
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


def plain_words(tex: str) -> list[str]:
    stripped = re.sub(r"\\cite\{[^}]+\}", " citation ", tex)
    stripped = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?(?:\{[^}]*\})?", " ", stripped)
    stripped = re.sub(r"[{}\\_$]", " ", stripped)
    return re.findall(r"[A-Za-z][A-Za-z0-9/-]+", stripped)


def citation_keys(tex: str) -> set[str]:
    keys: set[str] = set()
    for group in re.findall(r"\\cite\{([^}]+)\}", tex):
        keys.update(key.strip() for key in group.split(",") if key.strip())
    return keys


def validate_article(tex_path: Path, article: dict[str, object]) -> list[str]:
    text = tex_path.read_text(encoding="utf-8")
    errors: list[str] = []
    words = plain_words(text)
    cites = citation_keys(text)
    if len(words) < 1400:
        errors.append(f"too short for research-article draft: {len(words)} words")
    if len(cites) < 10:
        errors.append(f"too few unique citation keys: {len(cites)}")
    for section in REQUIRED_SECTIONS:
        if section not in text:
            errors.append(f"missing section {section}")
    for phrase in FORBIDDEN_META_PHRASES:
        if phrase.lower() in text.lower():
            errors.append(f"contains internal process/meta phrase: {phrase}")
    for pattern in FORBIDDEN_OVERCLAIMS:
        if re.search(pattern, text, flags=re.IGNORECASE):
            errors.append(f"contains forbidden overclaim: {pattern}")
    for pattern in FORBIDDEN_PUBLIC_ARTIFACTS:
        if re.search(pattern, text, flags=re.IGNORECASE):
            errors.append(f"contains internal public-manuscript artifact: {pattern}")
    if r"\begin{abstract}" not in text or text.find(r"\begin{abstract}") > text.find(r"\maketitle"):
        errors.append("missing top-matter abstract before maketitle")
    if text.count(r"\begin{table}") + text.count(r"\begin{table*}") < 1:
        errors.append("missing evidence/result table")
    if "source-observed 26" not in text and "26 by 8" not in text:
        errors.append("missing source-observed 26-by-8 control")
    if "derived f/v" not in text and "derived layer" not in text:
        errors.append("missing derived f/v layer qualifier")
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
    if "source transcription review" not in text or "rights review" not in text:
        errors.append("missing explicit human review blockers")
    return errors


def main() -> int:
    errors: list[str] = []
    manifest_path = PACKAGE / "manifest.json"
    audit_path = PACKAGE / "impact_readiness_audit.md"
    if not manifest_path.exists():
        errors.append("missing manifest.json")
        manifest = {}
    else:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("status") != "TARGETED_HUMAN_REVIEW_DRAFTS_NOT_SUBMISSION_READY":
        errors.append("manifest status should be TARGETED_HUMAN_REVIEW_DRAFTS_NOT_SUBMISSION_READY")
    if not audit_path.exists():
        errors.append("missing impact_readiness_audit.md")
    if not BENCHMARK.exists():
        errors.append("missing benchmark scoreboard")
    articles = manifest.get("articles", [])
    if len(articles) != 10:
        errors.append(f"expected 10 articles in manifest, found {len(articles)}")
    for article in articles:
        article_id = article.get("id", "")
        tex_path = PACKAGE / str(article.get("tex_path", ""))
        status_path = tex_path.parent / "STATUS.md"
        if not tex_path.exists():
            errors.append(f"{article_id}: missing main.tex")
            continue
        if not status_path.exists():
            errors.append(f"{article_id}: missing STATUS.md")
        else:
            status_text = status_path.read_text(encoding="utf-8")
            if "TARGETED_HUMAN_REVIEW_DRAFT_NOT_SUBMISSION_READY" not in status_text:
                errors.append(f"{article_id}: status file missing targeted human-review status")
        for error in validate_article(tex_path, article):
            errors.append(f"{article_id}: {error}")

    if errors:
        print("NWAGU_ARTICLE_WORKING_DRAFT_STRUCTURE_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        if len(errors) > 200:
            print(f"- ... {len(errors) - 200} additional errors")
        return 1
    print("NWAGU_ARTICLE_WORKING_DRAFT_STRUCTURE_VALID")
    print(f"articles={len(articles)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
