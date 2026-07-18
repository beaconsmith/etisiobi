from __future__ import annotations

import csv
import hashlib
import json
import re
import textwrap
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments" / "EXP-NA-001-source-critical-reconstruction"
LOGS = EXP / "logs"

PRIMARY = ROOT / "research" / "pagc" / "primary_sources" / "nwagu_aneke"
ARTIFACT = ROOT / "artifacts" / "nwagu_aneke"


SOURCE_FILES = [
    PRIMARY / "azuonye_1992.pdf",
    PRIMARY / "nwaguaneke_omniglot_chart.gif",
    PRIMARY / "omniglot_nwaguaneke.html",
    PRIMARY / "CHART_TRANSCRIPTION.md",
    PRIMARY / "SOURCE_AUDIT.md",
    ARTIFACT / "symbol_inventory.jsonl",
    ARTIFACT / "base_count_audit.md",
    ARTIFACT / "tei" / "nwagu_aneke_working_dossier.xml",
    ARTIFACT / "iiif" / "manifest.json",
    ROOT / "corpus" / "base_modifier_cache.jsonl",
    ROOT / "corpus" / "bmc_count_reconciliation.json",
    ROOT / "corpus" / "pagc_inventory_observations.jsonl",
]


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line in read(path).splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def find_line(path: Path, pattern: str) -> str:
    if not path.exists() or path.suffix.lower() not in {".md", ".txt", ".html", ".xml", ".json", ".jsonl"}:
        return "n/a"
    regex = re.compile(pattern, re.I)
    for idx, line in enumerate(read(path).splitlines(), start=1):
        if regex.search(line):
            return f"line {idx}"
    return "not found"


def gif_size(path: Path) -> tuple[int | None, int | None]:
    data = path.read_bytes()[:10]
    if len(data) >= 10 and data[:3] == b"GIF":
        width = data[6] + (data[7] << 8)
        height = data[8] + (data[9] << 8)
        return width, height
    return None, None


def source_file_metadata() -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for path in SOURCE_FILES:
        exists = path.exists()
        record: dict[str, Any] = {
            "path": rel(path),
            "exists": exists,
            "bytes": path.stat().st_size if exists else None,
            "sha256": sha256(path) if exists else None,
            "role": "source_or_structured_evidence",
        }
        if exists and path.suffix.lower() == ".gif":
            width, height = gif_size(path)
            record["width"] = width
            record["height"] = height
        records.append(record)
    return records


def symbol_inventory_summary() -> dict[str, Any]:
    path = ARTIFACT / "symbol_inventory.jsonl"
    rows = jsonl(path)
    by_type = Counter(row["record_type"] for row in rows)
    by_maturity = Counter(row["maturity"] for row in rows)
    row_labels = [row["label"] for row in rows if row["record_type"] == "row_label"]
    vowels = [row["label"] for row in rows if row["record_type"] == "vowel_column"]
    return {
        "record_count": len(rows),
        "by_type": dict(sorted(by_type.items())),
        "by_maturity": dict(sorted(by_maturity.items())),
        "row_labels": row_labels,
        "vowel_columns": vowels,
    }


def bmc_summary() -> dict[str, Any]:
    path = ROOT / "corpus" / "base_modifier_cache.jsonl"
    rows = jsonl(path)
    row_labels = sorted({row["row_label"] for row in rows})
    vowels = sorted({row["vowel_label"] for row in rows})
    review_status = Counter(row.get("review_status", "missing") for row in rows)
    source_region_status = Counter(row.get("source_region_status", "missing") for row in rows)
    certainty_values = [float(row["certainty"]) for row in rows if row.get("certainty") is not None]
    return {
        "record_count": len(rows),
        "row_count": len(row_labels),
        "vowel_count": len(vowels),
        "cell_count": len(rows),
        "review_status": dict(sorted(review_status.items())),
        "source_region_status": dict(sorted(source_region_status.items())),
        "certainty_min": min(certainty_values) if certainty_values else None,
        "certainty_max": max(certainty_values) if certainty_values else None,
    }


def count_model() -> dict[str, Any]:
    return json.loads(read(ROOT / "corpus" / "bmc_count_reconciliation.json"))


def evidence_rows() -> list[dict[str, Any]]:
    chart = PRIMARY / "CHART_TRANSCRIPTION.md"
    audit = PRIMARY / "SOURCE_AUDIT.md"
    base_audit = ARTIFACT / "base_count_audit.md"
    omniglot = PRIMARY / "omniglot_nwaguaneke.html"
    unicode_anchor = ROOT / "research_goals" / "nwagu_aneke_articles" / "prior_art_scan.md"
    symbol_summary = symbol_inventory_summary()
    bmc = bmc_summary()
    model = count_model()

    rows = [
        {
            "evidence_id": "NA-EV-001",
            "claim_or_observation": "Azuonye 1992 is the primary academic source anchor for Nwagu Aneke research.",
            "evidence_type": "source_file",
            "source_path": rel(PRIMARY / "azuonye_1992.pdf"),
            "locator": "local PDF present; external ScholarWorks metadata verified in prior_art_scan",
            "support_strength": "strong_metadata_medium_content",
            "reconstruction_effect": "usable_primary_anchor_but_needs_line_level_pdf_extraction",
            "limitation": "PDF text is not parsed in this experiment; appendix claims rely on prior local transcription and audits.",
        },
        {
            "evidence_id": "NA-EV-002",
            "claim_or_observation": "The local chart transcription records 26 printed consonant rows.",
            "evidence_type": "transcription",
            "source_path": rel(chart),
            "locator": find_line(chart, "Printed row count"),
            "support_strength": "strong",
            "reconstruction_effect": "source_observed_row_layer",
            "limitation": "manual transcription requires independent human review",
        },
        {
            "evidence_id": "NA-EV-003",
            "claim_or_observation": "The local chart transcription records 8 vowel columns.",
            "evidence_type": "transcription",
            "source_path": rel(chart),
            "locator": find_line(chart, r"Column count:\s*8"),
            "support_strength": "strong",
            "reconstruction_effect": "source_observed_column_layer",
            "limitation": "manual transcription requires independent human review",
        },
        {
            "evidence_id": "NA-EV-004",
            "claim_or_observation": "The f/v label is one printed row and is the source of the 26-vs-27 distinction.",
            "evidence_type": "transcription",
            "source_path": rel(chart),
            "locator": find_line(chart, "f/v"),
            "support_strength": "strong",
            "reconstruction_effect": "derived_layer_boundary",
            "limitation": "phonological interpretation requires Igbo/Umuleri review",
        },
        {
            "evidence_id": "NA-EV-005",
            "claim_or_observation": "The visible chart transcription records about 30 full-word symbols.",
            "evidence_type": "transcription",
            "source_path": rel(chart),
            "locator": find_line(chart, "Logograph count"),
            "support_strength": "moderate",
            "reconstruction_effect": "separate_logograph_inventory_needed",
            "limitation": "full logograph corpus may exceed visible chart and requires manuscript access",
        },
        {
            "evidence_id": "NA-EV-006",
            "claim_or_observation": "The source audit says the matrix may be a display convention rather than inherent grammar.",
            "evidence_type": "audit",
            "source_path": rel(audit),
            "locator": find_line(audit, "display convention"),
            "support_strength": "medium",
            "reconstruction_effect": "blocks_generative_grammar_overclaim",
            "limitation": "audit includes web-search-derived synthesis and should be rechecked against Azuonye text",
        },
        {
            "evidence_id": "NA-EV-007",
            "claim_or_observation": "Structured symbol inventory contains row labels and vowel columns, but no glyph-level cell transcription.",
            "evidence_type": "structured_inventory",
            "source_path": rel(ARTIFACT / "symbol_inventory.jsonl"),
            "locator": f"{symbol_summary['record_count']} records; by_type={symbol_summary['by_type']}",
            "support_strength": "strong_for_labels_weak_for_glyphs",
            "reconstruction_effect": "source_label_inventory_reconstructable",
            "limitation": "glyph forms and coordinates remain absent from symbol_inventory.jsonl",
        },
        {
            "evidence_id": "NA-EV-008",
            "claim_or_observation": "BMC has 208 row-vowel records, all needing human review and lacking source-region coordinates.",
            "evidence_type": "generated_structured_cache",
            "source_path": rel(ROOT / "corpus" / "base_modifier_cache.jsonl"),
            "locator": f"records={bmc['record_count']}; review={bmc['review_status']}; source_region={bmc['source_region_status']}",
            "support_strength": "strong_for_row_vowel_grid_weak_for_glyph_substrate",
            "reconstruction_effect": "source_grid_reconstructable_as_index_not_glyph_corpus",
            "limitation": "not a completed glyph transcription substrate",
        },
        {
            "evidence_id": "NA-EV-009",
            "claim_or_observation": "The count reconciliation decision is MULTI_LAYER_COUNT_VALID.",
            "evidence_type": "decision_record",
            "source_path": rel(ROOT / "corpus" / "bmc_count_reconciliation.json"),
            "locator": f"decision={model['decision']}",
            "support_strength": "strong_internal_decision",
            "reconstruction_effect": "article_must_separate_source_and_derived_counts",
            "limitation": "public article still needs independent source review",
        },
        {
            "evidence_id": "NA-EV-010",
            "claim_or_observation": "The base-count audit records 26, 8, 208, derived 27/216, and external 164/224 leads.",
            "evidence_type": "audit",
            "source_path": rel(base_audit),
            "locator": find_line(base_audit, "Count Ledger"),
            "support_strength": "strong_for_internal_taxonomy",
            "reconstruction_effect": "expands_article_from_26_27_to_count_layer_taxonomy",
            "limitation": "164/224 remain external C2 leads until locally archived and line-verified",
        },
        {
            "evidence_id": "NA-EV-011",
            "claim_or_observation": "Omniglot local HTML is available as a secondary page for syllabary/logograph features.",
            "evidence_type": "secondary_source_snapshot",
            "source_path": rel(omniglot),
            "locator": find_line(omniglot, "logographic"),
            "support_strength": "medium",
            "reconstruction_effect": "supports_public_description_but_not_primary_claims",
            "limitation": "secondary web source; should not override Azuonye/manuscript evidence",
        },
        {
            "evidence_id": "NA-EV-012",
            "claim_or_observation": "External standards review identifies Unicode, TEI, and IIIF as relevant methods for future articles.",
            "evidence_type": "prior_art_scan",
            "source_path": rel(unicode_anchor),
            "locator": find_line(unicode_anchor, "Unicode"),
            "support_strength": "medium",
            "reconstruction_effect": "supports_follow_on_digitization_and_encoding_articles",
            "limitation": "standards mapping is not evidence about Nwagu Aneke structure",
        },
    ]
    return rows


def write_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(path: Path, content: str) -> None:
    path.write_text(textwrap.dedent(content).strip() + "\n", encoding="utf-8")


def make_outputs() -> dict[str, Any]:
    EXP.mkdir(parents=True, exist_ok=True)
    LOGS.mkdir(parents=True, exist_ok=True)
    rows = evidence_rows()
    source_meta = source_file_metadata()
    symbol_summary = symbol_inventory_summary()
    bmc = bmc_summary()
    model = count_model()
    generated_at = datetime.now().astimezone().isoformat(timespec="seconds")

    write_json(EXP / "source_files.json", source_meta)
    write_jsonl(EXP / "evidence_table.jsonl", rows)
    write_csv(EXP / "evidence_table.csv", rows)

    decision = "RECONSTRUCTABLE_AS_SOURCE_LEDGER_NOT_FULL_GLYPH_CORPUS"
    results = {
        "experiment_id": "EXP-NA-001",
        "generated_at": generated_at,
        "decision": decision,
        "article_candidate": "ARTICLE-NA-001",
        "source_files_checked": len(source_meta),
        "missing_source_files": [row["path"] for row in source_meta if not row["exists"]],
        "evidence_rows": len(rows),
        "symbol_inventory": symbol_summary,
        "bmc_summary": bmc,
        "count_decision": model["decision"],
        "source_layer": {
            "rows": model["checks"]["tei_rows"],
            "vowels": model["checks"]["tei_vowels"],
            "cells": model["checks"]["expected_cells"],
        },
        "derived_layer": {
            "rows_if_f_v_split": model["checks"]["derived_split_rows_if_f_v_split"],
            "cells_if_f_v_split": model["checks"]["derived_split_cells_if_f_v_split"],
        },
        "can_claim": [
            "A source-critical article can be started from the local Nwagu Aneke dossier.",
            "The current reconstructable object is a row/vowel source ledger plus visible logograph leads.",
            "The source-observed layer must remain separate from the derived f/v split layer.",
        ],
        "cannot_claim": [
            "A completed glyph-level corpus has been reconstructed.",
            "27/216 is source-observed.",
            "The chart proves a generative grammar or universal compression theory.",
            "The visible chart proves all 100+ manuscript books or logographs are available for public analysis.",
        ],
        "next_action": "Human review of chart transcription and Azuonye appendix, then EXP-NA-002 count-layer ledger.",
    }
    write_json(EXP / "results.json", results)

    write_markdown(
        EXP / "plan.md",
        """
        # EXP-NA-001 Source-Critical Reconstruction

        ## Linked article

        `ARTICLE-NA-001: A Source-Critical Reconstruction of the Nwagu Aneke Igbo Syllabary`

        ## Question

        What can be reconstructed from the local Nwagu Aneke source package without importing PAGC assumptions?

        ## Inputs

        - `research/pagc/primary_sources/nwagu_aneke/azuonye_1992.pdf`
        - `research/pagc/primary_sources/nwagu_aneke/nwaguaneke_omniglot_chart.gif`
        - `research/pagc/primary_sources/nwagu_aneke/CHART_TRANSCRIPTION.md`
        - `research/pagc/primary_sources/nwagu_aneke/SOURCE_AUDIT.md`
        - `artifacts/nwagu_aneke/symbol_inventory.jsonl`
        - `corpus/base_modifier_cache.jsonl`
        - `corpus/bmc_count_reconciliation.json`

        ## Method

        Generate an evidence table that separates source file metadata,
        transcribed observations, structured inventory, BMC-generated row/vowel
        records, and standards/prior-art anchors.

        ## Success threshold

        The experiment must produce a table showing which claims are
        reconstructable, which are only derived, and which remain blocked.

        ## Human approval needed?

        No for local internal reconstruction. Yes before public image release,
        source reproduction, or external submission.
        """,
    )

    write_markdown(
        EXP / "commands.sh",
        """
        python scripts/run_na_source_reconstruction.py
        """,
    )

    write_markdown(
        EXP / "analysis.md",
        f"""
        # EXP-NA-001 Analysis

        Decision: `{decision}`

        ## What The Experiment Found

        The local Nwagu Aneke dossier supports a source-critical article, but
        the current reconstructable object is narrower than a finished glyph
        corpus.

        ## Reconstructable Now

        - A source file ledger with checksums and local paths.
        - A 26-row source-observed consonant-row layer.
        - An 8-column source-observed vowel/modifier layer.
        - A derived 208 source-layer cell index.
        - A derived 27/216 f/v split layer, explicitly not source-observed.
        - A visible logograph lead set of about 30 full-word symbols.
        - A 208-record BMC row/vowel index with all entries still marked for
          human review and without source-region coordinates.

        ## Not Reconstructable Yet

        - Full glyph-level cell shapes.
        - Full manuscript-corpus usage.
        - Public-rights-cleared image reproduction.
        - Verified 164 actual-symbol and 224 ideal-symbol claims.
        - Any direct historical claim that the chart itself is an inherent
          generative grammar rather than a source/pedagogical representation.

        ## Article Implication

        `ARTICLE-NA-001` is viable as a source-critical reconstruction paper if
        framed honestly: it reconstructs a ledger and uncertainty model, not a
        final digital edition.

        ## Outputs

        - `evidence_table.csv`
        - `evidence_table.jsonl`
        - `source_files.json`
        - `results.json`
        """,
    )

    write_markdown(
        EXP / "decision.md",
        f"""
        # EXP-NA-001 Decision

        Decision: `{decision}`

        ## Meaning

        The first Nwagu Aneke article can proceed as a source-critical
        reconstruction article. The evidence supports a source ledger and count
        taxonomy. It does not yet support a completed glyph corpus, public image
        release, or speculative PAGC theory claims.

        ## Active Article Status

        `ARTICLE-NA-001` remains active.

        ## Required Next Step

        Run `EXP-NA-002-count-layer-ledger` or first attach human source review
        for the chart transcription and Azuonye appendix.
        """,
    )

    (LOGS / "run_log.txt").write_text(
        f"{generated_at} generated EXP-NA-001 with {len(rows)} evidence rows and decision {decision}\n",
        encoding="utf-8",
    )
    return results


def main() -> int:
    results = make_outputs()
    print("EXP_NA_001_COMPLETE")
    print(f"decision={results['decision']}")
    print(f"evidence_rows={results['evidence_rows']}")
    print(f"source_files_checked={results['source_files_checked']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
