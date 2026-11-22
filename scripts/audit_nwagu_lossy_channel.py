"""EXP-NA-022: source-grounded ambiguity & transcription sensitivity audit.

NOT a transliterator, corpus frequency estimator, OCR, or manuscript decoder.
Read-only, Python stdlib; prints an inspectable synthetic-prior sensitivity
analysis without turning toy assumptions into empirical uncertainty estimates.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
MICRO = ROOT / "experiments/EXP-NA-022-lossy-channel/attested_microexamples.json"
LOGOS = ROOT / "experiments/EXP-NA-004-logograph-ledger/data/logograph_leads.jsonl"
VOWELS = frozenset("aeiouịọụẹ")


def nfc(value: str) -> str:
    return unicodedata.normalize("NFC", value).strip().lower()


def begins_with_vowel(value: str) -> bool:
    value = nfc(value)
    return bool(value) and value[0] in VOWELS


def remove_initial_independent_vowel(value: str) -> str | None:
    value = nfc(value)
    return value[1:] if len(value) > 1 and begins_with_vowel(value) else None


def shannon_bits(weights: list[float]) -> float:
    if not weights or any(w < 0 or not math.isfinite(w) for w in weights):
        raise ValueError("weights must be a nonempty list of finite, nonnegative numbers")
    total = sum(weights)
    if total <= 0:
        raise ValueError("weights must have positive total")
    return -sum((w / total) * math.log2(w / total) for w in weights if w > 0)


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def audit(data: dict, chart_leads: list[dict]) -> dict:
    errors: list[str] = []
    sources = {item.get("id") for item in data.get("sources", [])}
    groups = []
    for row in data.get("ambiguous_written_readings", []):
        code = nfc(row.get("code", ""))
        candidates = row.get("candidates", [])
        names = [nfc(x.get("reading", "")) for x in candidates if isinstance(x, dict)]
        if not code or len(names) != len(candidates) or len(names) < 2 or len(set(names)) != len(names):
            errors.append(f"{code!r}: missing or duplicate candidate readings")
        if row.get("source_id") not in sources:
            errors.append(f"{code!r}: unknown source")
        for candidate in names:
            if remove_initial_independent_vowel(candidate) != code:
                errors.append(f"{code!r}: {candidate!r} is not explained by simple leading-vowel omission")
        n = len(names)
        if n:
            # Stress priors are synthetic examples, not observed frequency.
            extreme_prior = [0.7] + [0.3 / (n - 1)] * (n - 1) if n > 1 else [1.0]
            groups.append({
                "written_reading": code,
                "candidate_readings": names,
                "documented_example_count": n,
                "unconditional_unique_decoding_possible_from_code_alone": n == 1,
                "uniform_prior_entropy_bits": round(math.log2(n), 6),
                "synthetic_skew_prior_entropy_bits": round(shannon_bits(extreme_prior), 6),
                "unknown_prior_entropy_bounds_bits": {"infimum": 0.0, "supremum": round(math.log2(n), 6)},
                "not_empirical": True,
            })
    transforms = data.get("other_lossy_forms", [])
    for row in transforms:
        if row.get("source_id") not in sources:
            errors.append("lossy_form: unknown source")
        if not isinstance(row.get("input"), str) or not isinstance(row.get("reduced"), str):
            errors.append("lossy_form: invalid pair")
        elif nfc(row["input"]) == nfc(row["reduced"]):
            errors.append("lossy_form: reduction does not change the string")
    conflicts = []
    labels = [row.get("word", "") for row in chart_leads]
    for item in data.get("suspected_label_conflicts", []):
        idx = item.get("chart_position")
        if not isinstance(idx, int) or not 1 <= idx <= len(labels):
            errors.append("label conflict: invalid chart position")
            continue
        existing = nfc(item.get("repository_transcription", ""))
        scanned = nfc(item.get("printed_ahamefula_2010_chart", ""))
        if nfc(labels[idx - 1]) != existing:
            errors.append(f"label conflict: repo entry at {idx} no longer matches {existing}")
        if not scanned or scanned == existing:
            errors.append(f"label conflict: no distinct alternate reading at {idx}")
        conflicts.append({
            "chart_position": idx,
            "repo": existing,
            "candidate_scan": scanned,
            "source_prose": nfc(item.get("same_article_discussion", "")),
            "status": "requires_human_collation_not_an_approved_correction",
        })
    orig_onsets = sum(begins_with_vowel(x) for x in labels)
    candidate_labels = list(labels)
    for item in conflicts:
        candidate_labels[item["chart_position"] - 1] = item["candidate_scan"]
    candidate_onsets = sum(begins_with_vowel(x) for x in candidate_labels)
    return {
        "valid": not errors,
        "errors": errors,
        "result_type": "literature_example_ambiguity_not_manuscript_decoding",
        "attested_homography_groups": groups,
        "distinct_loss_categories_recorded": sorted({
            "omitted_independent_initial_vowel", *(x.get("type") for x in transforms)
        }),
        "other_selected_loss_examples": len(transforms),
        "chart_transcription_sensitivity": {
            "total_leads": len(labels),
            "repository_vowel_initial": orig_onsets,
            "tentative_if_scan_candidates_adjudicated": candidate_onsets,
            "unresolved_conflicts": conflicts,
            "no_population_inference": True,
        },
        "empirical_decoding_accuracy_available": False,
        "contextual_entropy_estimated_from_manuscripts": False,
        "decision": "LOSSY_CHANNEL_SUPPORTED_BY_LITERATURE_REAL_DECODER_EVALUATION_PENDING",
    }


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--micro", type=Path, default=MICRO)
    p.add_argument("--chart-leads", type=Path, default=LOGOS)
    args = p.parse_args(argv)
    try:
        data = json.loads(args.micro.read_text(encoding="utf-8"))
        result = audit(data, read_jsonl(args.chart_leads))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"valid": False, "errors": [str(exc)]}))
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
