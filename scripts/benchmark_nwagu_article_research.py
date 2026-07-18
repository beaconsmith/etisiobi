from __future__ import annotations

import csv
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
BENCH = ROOT / "benchmarks" / "nwagu_article_research"
PACKAGE = ROOT / "papers" / "nwagu_aneke_articles"
SUMMARY = ROOT / "experiments" / "nwagu_aneke_article_experiments" / "results.json"
TASKS = BENCH / "benchmark_tasks.jsonl"
HISTORY = BENCH / "score_history.jsonl"

ARTICLE_SLUGS = [
    "001-source-critical-reconstruction",
    "002-count-layer-drift",
    "003-f-v-hinge",
    "004-logographs-in-a-syllabary",
    "005-tei-iiif-critical-edition",
    "006-unicode-readiness",
    "007-manuscript-corpus-provenance",
    "008-comparative-standardization",
    "009-igbo-tokenization",
    "010-layer-safe-generative-design",
]

META_NOTE_PATTERNS = [
    "Why The Earlier Draft Would Be Rejected",
    "Impact-Journal Thesis",
    "What Was Fixed In This Revision",
    "A formatted PDF is not a publishable paper",
    "move from a formatted note",
    "AI model",
]

REQUIRED_ARTICLE_SECTIONS = [
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


def now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def read_json(path: Path, default: Any = None) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def append_jsonl(path: Path, row: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    keys: list[str] = []
    for row in rows:
        for key in row:
            if key not in keys:
                keys.append(key)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(rows)


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def word_count(tex: str) -> int:
    cleaned = re.sub(r"\\cite\{[^}]+\}", " citation ", tex)
    cleaned = re.sub(r"\\[A-Za-z]+\*?(?:\[[^\]]*\])?(?:\{[^}]*\})?", " ", cleaned)
    cleaned = re.sub(r"[{}\\_$]", " ", cleaned)
    return len(re.findall(r"[A-Za-z][A-Za-z0-9/-]+", cleaned))


def citation_count(tex: str) -> int:
    keys: set[str] = set()
    for group in re.findall(r"\\cite\{([^}]+)\}", tex):
        keys.update(key.strip() for key in group.split(",") if key.strip())
    return len(keys)


def tex_files() -> dict[str, str]:
    return {
        slug: (PACKAGE / slug / "main.tex").read_text(encoding="utf-8")
        if (PACKAGE / slug / "main.tex").exists()
        else ""
        for slug in ARTICLE_SLUGS
    }


def meta_note_hits(tex: str) -> list[str]:
    lower = tex.lower()
    return [pattern for pattern in META_NOTE_PATTERNS if pattern.lower() in lower]


def forbidden_overclaim_hits(tex: str) -> list[str]:
    patterns = [
        r"27/216\s+is\s+source[- ]observed",
        r"216\s+is\s+source[- ]observed",
        r"proves\s+universal\s+compression",
        r"proves\s+E6",
        r"E6\s+is\s+proven",
        r"completed\s+glyph[- ]level\s+corpus",
        r"public\s+release\s+is\s+approved",
        r"downstream\s+NLP\s+improvement\s+is\s+shown",
    ]
    hits: list[str] = []
    for pattern in patterns:
        if re.search(pattern, tex, flags=re.IGNORECASE):
            hits.append(pattern)
    return hits


def article_quality(tex_by_slug: dict[str, str]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for slug, tex in tex_by_slug.items():
        words = word_count(tex)
        cites = citation_count(tex)
        sections_present = [section for section in REQUIRED_ARTICLE_SECTIONS if section in tex]
        meta_hits = meta_note_hits(tex)
        overclaim_hits = forbidden_overclaim_hits(tex)
        has_exp = "EXP-NA-" in tex
        has_table = r"\begin{table}" in tex or r"\begin{table*}" in tex
        raw_score = (
            0.18 * clamp(words / 2500)
            + 0.12 * clamp(cites / 12)
            + 0.18 * clamp(len(sections_present) / len(REQUIRED_ARTICLE_SECTIONS))
            + 0.14 * float(has_exp)
            + 0.10 * float(has_table)
            + 0.14 * float("source-observed 26" in tex or "26 by 8" in tex)
            + 0.14 * float("derived f/v" in tex or "derived layer" in tex)
            - 0.35 * clamp(len(meta_hits) / max(1, len(META_NOTE_PATTERNS)))
            - 0.50 * float(bool(overclaim_hits))
        )
        score = clamp(raw_score)
        if words < 3000:
            score = min(score, 0.65)
        elif words < 4500:
            score = min(score, 0.78)
        rows.append(
            {
                "article": slug,
                "words": words,
                "unique_citations": cites,
                "sections_present": len(sections_present),
                "has_experiment_reference": has_exp,
                "has_result_table": has_table,
                "meta_note_hits": "; ".join(meta_hits),
                "overclaim_hits": "; ".join(overclaim_hits),
                "article_quality_score": round(score, 4),
            }
        )
    return rows


def experiment_score(summary: dict[str, Any]) -> dict[str, float]:
    exps = summary.get("experiments", {})
    exp009 = exps.get("EXP-NA-009", {})
    exp010 = exps.get("EXP-NA-010", {})
    exp006 = exps.get("EXP-NA-006", {})
    exp005 = exps.get("EXP-NA-005", {})
    return {
        "count_layer": 1.0 if exps.get("EXP-NA-002", {}).get("source_layer", {}).get("records") == 208 else 0.0,
        "fv_hinge": 1.0 if exps.get("EXP-NA-003", {}).get("delta_records") == 8 else 0.0,
        "logograph": clamp(exps.get("EXP-NA-004", {}).get("lead_count", 0) / 30),
        "tei_iiif": 0.75 if exp005.get("annotation_records", 0) >= 10 else 0.0,
        "unicode_gap": clamp(1.0 - 0.05 * exp006.get("status_counts", {}).get("missing", 0)),
        "provenance": clamp(exps.get("EXP-NA-007", {}).get("ledger_records", 0) / 4),
        "comparative": clamp(exps.get("EXP-NA-008", {}).get("scripts_compared", 0) / 8),
        "tokenizer_baseline": (
            0.75
            if exp009.get("test_words_used", 0) >= 1000 and len(exp009.get("metrics", [])) >= 5
            else 0.0
        ),
        "tokenizer_downstream": 0.0,
        "layer_safety": exp010.get("promotion_error_detection_rate", 0.0),
    }


def task_scores(tasks: list[dict[str, Any]], summary: dict[str, Any], tex_by_slug: dict[str, str]) -> list[dict[str, Any]]:
    exp = experiment_score(summary)
    quality_rows = article_quality(tex_by_slug)
    avg_quality = sum(row["article_quality_score"] for row in quality_rows) / max(1, len(quality_rows))
    all_tex = "\n".join(tex_by_slug.values())
    all_meta_hits = sum(len(meta_note_hits(tex)) for tex in tex_by_slug.values())
    all_overclaim_hits = sum(len(forbidden_overclaim_hits(tex)) for tex in tex_by_slug.values())

    source_discipline = 1.0 if all_overclaim_hits == 0 else 0.0
    evidence_ledger = (exp["count_layer"] + exp["fv_hinge"] + exp["provenance"]) / 3
    result_strength = (
        exp["count_layer"]
        + exp["fv_hinge"]
        + exp["logograph"]
        + exp["tei_iiif"]
        + exp["unicode_gap"]
        + exp["provenance"]
        + exp["comparative"]
        + exp["tokenizer_baseline"]
        + exp["layer_safety"]
    ) / 9
    novelty = 0.72
    reproducibility = 0.90 if summary.get("input_checksums") else 0.70
    reviewer_burndown = 0.84 if all_meta_hits == 0 else 0.55
    rights_authority = 0.55
    coherence = avg_quality
    reusable_value = 0.88
    comparability = 1.0 if TASKS.exists() and SUMMARY.exists() else 0.5

    metric_by_task = {
        "NA-BENCH-001": source_discipline,
        "NA-BENCH-002": evidence_ledger,
        "NA-BENCH-003": result_strength,
        "NA-BENCH-004": novelty,
        "NA-BENCH-005": reproducibility,
        "NA-BENCH-006": reviewer_burndown,
        "NA-BENCH-007": rights_authority,
        "NA-BENCH-008": coherence,
        "NA-BENCH-009": reusable_value,
        "NA-BENCH-010": comparability,
    }

    rows: list[dict[str, Any]] = []
    for task in tasks:
        score = clamp(metric_by_task.get(task["task_id"], 0.0))
        rows.append(
            {
                **task,
                "score_0_1": round(score, 4),
                "evidence_points": round(score * float(task["evidence_weight"]), 4),
                "ijrs_points": round(score * float(task["ijrs_weight"]), 2),
                "passes_threshold": score * float(task["ijrs_weight"]) >= float(task["pass_threshold"]),
            }
        )
    return rows


def status_for_ijrs(ijrs: float, hard_gate_failures: list[str], applied_caps: list[str]) -> str:
    if hard_gate_failures:
        return "BENCHMARK_HARD_GATE_FAILED"
    if ijrs < 65:
        return "WORKING_PAPER_SET_NOT_IMPACT_READY"
    if ijrs >= 85 and not applied_caps:
        return "IMPACT_JOURNAL_CANDIDATE"
    if ijrs >= 75:
        return "STRONG_JOURNAL_TRACK_DRAFT_NOT_SUBMISSION_READY"
    if ijrs >= 65:
        return "INTERNAL_RESEARCH_DRAFT_BLOCKERS_DOMINATE"
    if ijrs >= 50:
        return "REDESIGN_OR_DOWNGRADE"
    return "REJECT_OR_FREEZE"


def render_markdown(scoreboard: dict[str, Any]) -> str:
    lines = [
        "# Nwagu Aneke Article Research Benchmark",
        "",
        f"Generated: `{scoreboard['generated_at']}`",
        "",
        "This benchmark is the anti-whack-a-mole control plane for the ten-article program.",
        "It follows the Karpathy autoresearch pattern of fixed inputs, fixed evaluator,",
        "one headline score, visible sub-scores, and keep/reject decisions. The metric",
        "is adapted to research: lower research loss means fewer evidence, claim,",
        "citation, reproducibility, and manuscript-readiness failures.",
        "",
        f"- Evidence completion score: `{scoreboard['evidence_completion_score']}`",
        f"- Impact-journal readiness score (IJRS): `{scoreboard['impact_journal_readiness_score']}` / 100",
        f"- Research loss: `{scoreboard['research_loss_lower_is_better']}`",
        f"- Status: `{scoreboard['status']}`",
        "",
        "## Hard Gates",
        "",
    ]
    if scoreboard["hard_gate_failures"]:
        lines.extend(f"- FAIL: {failure}" for failure in scoreboard["hard_gate_failures"])
    else:
        lines.append("- PASS: no source/derived, citation, or forbidden-overclaim hard gate failed.")
    lines.extend(["", "## Caps", ""])
    if scoreboard["applied_caps"]:
        lines.extend(f"- {cap}" for cap in scoreboard["applied_caps"])
    else:
        lines.append("- No caps applied.")
    lines.extend(
        [
            "",
            "## Task Scores",
            "",
            "| Task | Score | Evidence points | IJRS points | Pass |",
            "|---|---:|---:|---:|---|",
        ]
    )
    for row in scoreboard["task_scores"]:
        lines.append(
            f"| {row['task']} | {row['score_0_1']} | {row['evidence_points']} | "
            f"{row['ijrs_points']} | `{row['passes_threshold']}` |"
        )
    lines.extend(
        [
            "",
            "## Article Quality",
            "",
            "| Article | Words | Citations | Sections | Meta-note hits | Overclaim hits | Score |",
            "|---|---:|---:|---:|---|---|---:|",
        ]
    )
    for row in scoreboard["article_quality"]:
        lines.append(
            f"| `{row['article']}` | {row['words']} | {row['unique_citations']} | "
            f"{row['sections_present']} | {row['meta_note_hits'] or '-'} | "
            f"{row['overclaim_hits'] or '-'} | {row['article_quality_score']} |"
        )
    lines.extend(
        [
            "",
            "## Keep/Reject Rule",
            "",
            "Keep a manuscript revision only if it raises IJRS by at least five points,",
            "removes a hard gate, or removes a cap without increasing overclaim risk.",
            "Reject revisions that improve prose while weakening source-layer discipline.",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    tasks = read_jsonl(TASKS)
    summary = read_json(SUMMARY, {})
    tex_by_slug = tex_files()
    article_rows = article_quality(tex_by_slug)
    rows = task_scores(tasks, summary, tex_by_slug)
    evidence_completion = sum(row["evidence_points"] for row in rows) / max(0.0001, sum(float(row["evidence_weight"]) for row in rows))
    ijrs_raw = sum(row["ijrs_points"] for row in rows)

    hard_gate_failures: list[str] = []
    if any(row["overclaim_hits"] for row in article_rows):
        hard_gate_failures.append("forbidden overclaim appears in article body")
    if not all("source-observed" in tex or "26 by 8" in tex for tex in tex_by_slug.values()):
        hard_gate_failures.append("one or more articles omit the 26-by-8 source-layer control")
    unsafe_downstream_patterns = [
        r"shows\s+downstream\s+NLP\s+improvement",
        r"demonstrates\s+downstream\s+NLP\s+improvement",
        r"improves\s+downstream\s+NLP",
    ]
    if any(
        any(re.search(pattern, tex, flags=re.IGNORECASE) for pattern in unsafe_downstream_patterns)
        for tex in tex_by_slug.values()
    ):
        hard_gate_failures.append("Article 9 may imply downstream NLP improvement without downstream task result")

    applied_caps: list[str] = []
    if hard_gate_failures:
        ijrs = min(ijrs_raw, 49.0)
    else:
        ijrs = ijrs_raw
    if any(meta_note_hits(tex) for tex in tex_by_slug.values()):
        ijrs = min(ijrs, 64.0)
        applied_caps.append("Meta-note prose remains in manuscript bodies; cap IJRS at 64.")
    if summary.get("experiments", {}).get("EXP-NA-009", {}).get("decision") == "TOKENIZER_BASELINES_RAN_NO_DOWNSTREAM_TASK_RESULT":
        applied_caps.append("Article 9 cannot exceed bounded-baseline status without downstream NLP task result.")
    if rows and next((row for row in rows if row["task_id"] == "NA-BENCH-004"), {}).get("passes_threshold") is False:
        ijrs = min(ijrs, 64.0)
        applied_caps.append("Article-specific novelty/prior-art gate failed; cap IJRS below impact-readiness.")
    if rows and next((row for row in rows if row["task_id"] == "NA-BENCH-007"), {}).get("score_0_1", 0) < 0.75:
        ijrs = min(ijrs, 59.0)
        applied_caps.append("Rights/authority unresolved; cap IJRS below impact-readiness.")
    if any(row["article_quality_score"] < 0.70 for row in article_rows):
        ijrs = min(ijrs, 59.0)
        applied_caps.append("Manuscripts are short working-paper drafts, not full impact-journal articles; cap IJRS below impact-readiness.")

    ijrs = round(ijrs, 2)
    evidence_completion = round(evidence_completion, 4)
    status = status_for_ijrs(ijrs, hard_gate_failures, applied_caps)
    scoreboard = {
        "generated_at": now(),
        "benchmark_name": "Nwagu Aneke Article Research Benchmark",
        "sota_design_basis": [
            "Karpathy/autoresearch: fixed budget, one metric, compare/keep/reject loop",
            "ScienceAgentBench/PaperBench style task/rubric decomposition",
            "SciFact/ALCE style claim and citation verification",
            "RO-Crate style provenance packaging",
        ],
        "accepted_foundation": {
            "source_observed_layer": "26 rows x 8 vowel/modifier columns = 208 records",
            "derived_layer": "27/216 only as derived f/v split layer",
        },
        "evidence_completion_score": evidence_completion,
        "impact_journal_readiness_score": ijrs,
        "research_loss_lower_is_better": round(1.0 - evidence_completion, 4),
        "status": status,
        "hard_gate_failures": hard_gate_failures,
        "applied_caps": applied_caps,
        "task_scores": rows,
        "article_quality": article_rows,
    }
    write_json(BENCH / "scoreboard.json", scoreboard)
    write_csv(BENCH / "task_scores.csv", rows)
    write_csv(BENCH / "article_quality.csv", article_rows)
    write_text(BENCH / "BENCHMARK.md", render_markdown(scoreboard))
    append_jsonl(
        HISTORY,
        {
            "generated_at": scoreboard["generated_at"],
            "evidence_completion_score": evidence_completion,
            "impact_journal_readiness_score": ijrs,
            "status": status,
            "hard_gate_failures": hard_gate_failures,
            "applied_caps": applied_caps,
        },
    )
    print("NWAGU_ARTICLE_RESEARCH_BENCHMARK_COMPLETE")
    print(f"evidence_completion_score={evidence_completion}")
    print(f"impact_journal_readiness_score={ijrs}")
    print(f"status={status}")
    return 1 if hard_gate_failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
