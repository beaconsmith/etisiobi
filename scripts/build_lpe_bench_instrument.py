from __future__ import annotations

import csv
import json
import textwrap
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "instruments" / "lpe_bench"
EXP2 = ROOT / "experiments" / "EXP-FRONTIER-002-layer-promotion-expanded"
EXP3 = ROOT / "experiments" / "EXP-FRONTIER-003-blind-lpe-annotation"
EXP4 = ROOT / "experiments" / "EXP-FRONTIER-004-unicode-channel-risk-audit"
EXP5 = ROOT / "experiments" / "EXP-FRONTIER-005-real-agent-lpe-eval"
AUDIT = ROOT / "external_audits" / "elder_plinius" / "profile_code_inventory.json"


def now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(text).strip() + "\n", encoding="utf-8")


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


def top_metrics(metrics: list[dict[str, Any]]) -> list[dict[str, Any]]:
    test = [row for row in metrics if row.get("split") == "test"]
    return sorted(test, key=lambda row: (row.get("f1", 0), row.get("mcc", 0)), reverse=True)


def main() -> int:
    exp2 = read_json(EXP2 / "results.json")
    exp3 = read_json(EXP3 / "manifest.json")
    exp4 = read_json(EXP4 / "results.json")
    exp5_manifest = read_json(EXP5 / "manifest.json") if (EXP5 / "manifest.json").exists() else {}
    exp5_scores = read_json(EXP5 / "scores.json") if (EXP5 / "scores.json").exists() else {}
    exp5_agreement = read_json(EXP5 / "annotation_agreement.json") if (EXP5 / "annotation_agreement.json").exists() else {}
    metrics = read_jsonl(EXP2 / "data" / "baseline_metrics.jsonl")
    cases = read_jsonl(EXP2 / "data" / "lpe_cases.jsonl")
    audit = read_json(AUDIT) if AUDIT.exists() else {}

    leaderboard = top_metrics(metrics)
    source_counts = Counter(row["source_type"] for row in cases)
    variant_counts = Counter(row["variant_type"] for row in cases)
    split_counts = Counter(row["split"] for row in cases)

    manifest = {
        "instrument_id": "LPE-Bench",
        "title": "Layer Promotion Error Benchmark",
        "generated_at": now(),
        "status": "PUBLIC_INSTRUMENT_DRAFT_NOT_FRONTIER_PROOF",
        "research_question": "Do AI research agents promote derived, speculative, blocked, or design-layer claims into source-observed or publication-ready claims?",
        "current_case_count": exp2["case_count"],
        "blind_annotation_queue_count": exp3["case_count"],
        "best_internal_test_baseline": exp2["best_test_baseline"],
        "best_metadata_free_test_baseline": exp2["best_metadata_free_test_baseline"],
        "source_type_counts": dict(source_counts),
        "variant_type_counts": dict(variant_counts),
        "split_counts": dict(split_counts),
        "frontier_claim_status": "not_ready",
        "exp005_status": {
            "packet": exp5_manifest.get("status"),
            "annotation": exp5_agreement.get("status"),
            "score": exp5_scores.get("status"),
            "promotion_error_fleiss_kappa": exp5_agreement.get("promotion_error_fleiss_kappa"),
            "severity_fleiss_kappa": exp5_agreement.get("severity_fleiss_kappa"),
            "agent_prediction_count": exp5_scores.get("agent_prediction_count"),
            "best_overall": exp5_scores.get("best_overall"),
            "best_codex_agent": exp5_scores.get("best_codex_agent"),
        },
        "blocking_gates": [
            "independent human/domain annotation",
            "frozen gold labels",
            "real agent/model runs",
            "external non-Etisiobi cases",
            "rights/authority review for public examples",
            "statistical confidence intervals on final baselines",
        ],
        "inspiration_audit": {
            "source": "elder-plinius profile audit",
            "repos_audited": audit.get("repo_count"),
            "safe_pattern": "named instrument -> runnable artifact -> raw traces -> validation report -> paper",
        },
        "related_experiments": [
            "EXP-FRONTIER-001-layer-promotion-benchmark",
            "EXP-FRONTIER-002-layer-promotion-expanded",
            "EXP-FRONTIER-003-blind-lpe-annotation",
            "EXP-FRONTIER-004-unicode-channel-risk-audit",
        ],
    }

    write_json(OUT / "manifest.json", manifest)
    write_csv(OUT / "leaderboard_internal.csv", leaderboard)
    write_json(OUT / "leaderboard_internal.json", leaderboard)
    write_json(OUT / "data_summary.json", {
        "source_type_counts": dict(source_counts),
        "variant_type_counts": dict(variant_counts),
        "split_counts": dict(split_counts),
        "gold_positive_rate": exp2["gold_positive_rate"],
    })
    write_text(
        OUT / "README.md",
        f"""
        # LPE-Bench

        Layer Promotion Error Benchmark.

        ## Research Question

        Do AI research agents promote derived, speculative, blocked, or
        design-layer claims into source-observed or publication-ready claims?

        ## Why This Exists

        Etisiobi's Nwagu Aneke/PAGC work has one load-bearing boundary:

        ```text
        source-observed layer: 26 rows x 8 vowel/modifier columns = 208 records
        derived layer: 27 / 216 by f/v split only
        ```

        The benchmark tests whether agents preserve or violate that boundary
        when writing research claims.

        ## Current Status

        `{manifest['status']}`

        This is a named research instrument, not a paper-ready result.

        ## Current Assets

        - Internal cases: `{exp2['case_count']}`
        - Blind annotation queue: `{exp3['case_count']}`
        - Best internal typed baseline: `{exp2['best_test_baseline']['baseline']}` with F1 `{exp2['best_test_baseline']['f1']}`
        - Best metadata-free baseline: `{exp2['best_metadata_free_test_baseline']['baseline']}` with F1 `{exp2['best_metadata_free_test_baseline']['f1']}`
        - Unicode/channel audit: `{exp4['status']}`, findings `{exp4['findings']}`
        - EXP-005 annotation: `{exp5_agreement.get('status', 'missing')}`
        - EXP-005 score: `{exp5_scores.get('status', 'missing')}`
        - Best EXP-005 Codex agent: `{(exp5_scores.get('best_codex_agent') or {}).get('agent_id', 'missing')}` with F1 `{(exp5_scores.get('best_codex_agent') or {}).get('f1', 'missing')}`

        ## Public-Grade Bar

        LPE-Bench becomes a frontier candidate only after independent labels,
        frozen gold splits, real agent runs, external cases, confidence
        intervals, and a validation report that documents defects and
        corrections.

        ## Commands

        ```powershell
        python scripts\\run_frontier_lpe_benchmark_v2.py
        python scripts\\prepare_frontier_lpe_exp003_annotation_packet.py
        python scripts\\run_frontier_lpe_exp003_pilot.py
        python scripts\\audit_unicode_channel_risk.py
        python scripts\\build_lpe_bench_instrument.py
        python scripts\\validate_frontier_lab.py
        ```
        """,
    )
    write_text(
        OUT / "VALIDATION.md",
        f"""
        # LPE-Bench Validation Report

        ## Current Verdict

        `PUBLIC_INSTRUMENT_DRAFT_NOT_FRONTIER_PROOF`

        ## What Has Been Validated

        - The benchmark object is defined: Layer Promotion Error.
        - The internal expanded dataset has `{exp2['case_count']}` cases.
        - The blind annotation packet has `{exp3['case_count']}` unlabeled cases.
        - Internal baselines run and produce held-out test metrics.
        - Unicode/channel-risk audit runs as defensive publication hygiene.
        - EXP-005 can now produce independent AI-review adjudication and local
          baseline scores.

        ## What Has Not Been Validated

        - Human/domain gold labels.
        - Generalization beyond Etisiobi-local cases.
        - Real frontier-agent/model performance.
        - Statistical confidence intervals for final public claims.
        - Rights/authority approval for public examples.

        ## Current EXP-005 Result

        - Annotation status: `{exp5_agreement.get('status', 'missing')}`
        - Promotion-error Fleiss kappa: `{exp5_agreement.get('promotion_error_fleiss_kappa', 'missing')}`
        - Severity Fleiss kappa: `{exp5_agreement.get('severity_fleiss_kappa', 'missing')}`
        - Score status: `{exp5_scores.get('status', 'missing')}`
        - Agent predictions: `{exp5_scores.get('agent_prediction_count', 'missing')}`
        - Best overall run: `{(exp5_scores.get('best_overall') or {}).get('agent_id', 'missing')}` / F1 `{(exp5_scores.get('best_overall') or {}).get('f1', 'missing')}`
        - Best Codex-agent run: `{(exp5_scores.get('best_codex_agent') or {}).get('agent_id', 'missing')}` / F1 `{(exp5_scores.get('best_codex_agent') or {}).get('f1', 'missing')}`

        Interpretation: the current score is useful for internal benchmark
        development. It is not a frontier result because labels are AI-reviewer
        adjudications and the agent runs are deterministic local baselines, not
        external frontier agents.

        ## Defects / Risks

        | Risk | Status | Required Fix |
        |---|---|---|
        | Construct leakage from typed metadata | Open | Score metadata-free conditions against frozen labels. |
        | Heuristic labels | Open | Use independent annotators and adjudication. |
        | Internal-only source distribution | Open | Add external non-Etisiobi research-agent outputs. |
        | Publication rights | Open | Authority review before public examples. |
        | Overclaiming from perfect typed baseline | Controlled | Manifest blocks frontier-proof status. |

        ## Promotion Rule

        No paper may cite LPE-Bench as a frontier result until this report
        records passing independent labels, real baselines, and review-team
        approval.
        """,
    )
    write_text(
        OUT / "BENCHMARK_CARD.md",
        f"""
        # Benchmark Card: LPE-Bench

        ## Task

        Classify whether a research claim illegally promotes a weaker evidence
        layer into a stronger output claim.

        ## Labels

        - `source_observed`
        - `source_index`
        - `derived`
        - `design_hypothesis`
        - `speculative`
        - `blocked`

        ## Metrics

        - precision
        - recall
        - F1
        - MCC
        - balanced accuracy
        - severity-weighted recall

        ## Baselines

        Current internal baselines:

        - `majority_negative`
        - `rank_only_metadata`
        - `lexical_only`
        - `shacl_type_sim`
        - `metadata_free_text`
        - `hybrid_rank_lexical`

        ## Known Limitation

        The typed metadata baseline can solve the current internal task because
        the labels expose the layer transition. The real research problem is
        metadata-free or partially-observed detection on independently labeled
        agent outputs.
        """,
    )
    write_text(
        OUT / "demo.html",
        """
        <!doctype html>
        <html lang="en">
        <head>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <title>LPE-Bench</title>
          <style>
            body { font-family: Arial, sans-serif; margin: 32px; line-height: 1.45; max-width: 980px; }
            h1 { font-size: 34px; margin-bottom: 4px; }
            .status { display: inline-block; padding: 6px 10px; background: #f4d35e; color: #111; font-weight: 700; }
            .grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px; margin: 20px 0; }
            .card { border: 1px solid #ddd; padding: 14px; border-radius: 6px; }
            code { background: #f5f5f5; padding: 2px 4px; }
          </style>
        </head>
        <body>
          <h1>LPE-Bench</h1>
          <div class="status">PUBLIC INSTRUMENT DRAFT - NOT FRONTIER PROOF</div>
          <p><strong>Layer Promotion Error</strong> measures whether a research
          claim promotes derived, speculative, blocked, or design-layer evidence
          into a source-observed or publication-ready claim.</p>
          <div class="grid">
            <div class="card"><h2>Source Layer</h2><p>26 x 8 = 208 records.</p></div>
            <div class="card"><h2>Derived Layer</h2><p>27 / 216 by f/v split only.</p></div>
            <div class="card"><h2>Benchmark</h2><p>Detect invalid layer promotion.</p></div>
          </div>
          <p>The next frontier step is independent human/domain annotation and
          real agent runs against frozen labels.</p>
        </body>
        </html>
        """,
    )
    print("LPE_BENCH_INSTRUMENT_BUILT")
    print(f"status={manifest['status']}")
    print(f"cases={exp2['case_count']}")
    print(f"annotation_queue={exp3['case_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
