from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAP_PATH = ROOT / "research" / "frontier" / "nwagu_aneke" / "interfaces" / "count_layer_data_to_view_map.jsonl"
HTML_PATH = ROOT / "research" / "frontier" / "nwagu_aneke" / "interfaces" / "count_layer_static_prototype.html"

FORBIDDEN_SNIPPETS = [
    "<img",
    "<picture",
    "<svg",
    "27 source rows",
    "216 source cells",
    "public-ready",
    "publication-ready",
    "paper-ready",
    "ready for public release",
    "appendix ii does not exist",
    "official pdf lacks appendix ii",
    "universal compression established",
    "e6 source fact",
    "agent output as source proof",
    "benchmark score as source claim",
    "dataset available",
    "corpus complete",
    "public archive ready",
]


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value.lower()).strip()


def main() -> int:
    errors: list[str] = []

    for path in [MAP_PATH, HTML_PATH]:
        if not path.exists():
            errors.append(f"missing {path.relative_to(ROOT).as_posix()}")

    if not errors:
        html = HTML_PATH.read_text(encoding="utf-8")
        normalized_html = normalize(html)
        records = load_jsonl(MAP_PATH)

        for forbidden in FORBIDDEN_SNIPPETS:
            if normalize(forbidden) in normalized_html:
                errors.append(f"forbidden prototype text or element: {forbidden}")

        for record in records:
            record_id = record["record_id"]
            if f'data-record-id="{record_id}"' not in html:
                errors.append(f"{record_id}: missing data-record-id in prototype")

            if normalize(record["visible_label"]) not in normalized_html:
                errors.append(f"{record_id}: missing visible label {record['visible_label']!r}")

            for phrase in record["must_show"]:
                if normalize(phrase) not in normalized_html:
                    errors.append(f"{record_id}: missing required phrase {phrase!r}")

            for phrase in record["blocked_public_release_conditions"]:
                if normalize(phrase) not in normalized_html:
                    errors.append(f"{record_id}: missing blocked condition {phrase!r}")

        required_controls = [
            'data-filter="all"',
            'data-filter="source_observed"',
            'data-filter="derived_f_v"',
            'data-filter="restricted_blocked"',
            'data-filter="speculative_frontier"',
            'data-filter="applied_design"',
            'data-filter="computational_evaluation"',
            'data-filter="contested_counts"',
            'data-filter="dropped_branches"',
        ]
        for control in required_controls:
            if control not in html:
                errors.append(f"missing filter control {control}")

    if errors:
        print("COUNT_LAYER_STATIC_PROTOTYPE_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        return 1

    print("COUNT_LAYER_STATIC_PROTOTYPE_VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
