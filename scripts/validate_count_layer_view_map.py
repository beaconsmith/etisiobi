from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURE_PATH = ROOT / "research" / "frontier" / "nwagu_aneke" / "claim_layer_fixtures.jsonl"
MAP_PATH = ROOT / "research" / "frontier" / "nwagu_aneke" / "interfaces" / "count_layer_data_to_view_map.jsonl"
OUTLINE_PATH = ROOT / "research" / "frontier" / "nwagu_aneke" / "interfaces" / "count_layer_view_outline.md"

REQUIRED_FIELDS = {
    "record_id",
    "target_panel",
    "visible_label",
    "must_show",
    "must_not_show",
    "blocked_public_release_conditions",
}

LIST_FIELDS = {
    "must_show",
    "must_not_show",
    "blocked_public_release_conditions",
}


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> int:
    errors: list[str] = []

    for path in [FIXTURE_PATH, MAP_PATH, OUTLINE_PATH]:
        if not path.exists():
            errors.append(f"missing {path.relative_to(ROOT).as_posix()}")

    if not errors:
        fixtures = {record["record_id"]: record for record in load_jsonl(FIXTURE_PATH)}
        mapped: dict[str, dict] = {}

        for line_number, record in enumerate(load_jsonl(MAP_PATH), start=1):
            record_id = record.get("record_id", f"line {line_number}")
            if record_id in mapped:
                errors.append(f"{record_id}: duplicate view map record")
            mapped[str(record_id)] = record

            missing = sorted(REQUIRED_FIELDS - record.keys())
            if missing:
                errors.append(f"{record_id}: missing fields {missing}")

            for field in ["record_id", "target_panel", "visible_label"]:
                if not isinstance(record.get(field), str) or not record.get(field, "").strip():
                    errors.append(f"{record_id}: {field} must be a non-empty string")

            for field in LIST_FIELDS:
                if not isinstance(record.get(field), list) or not record.get(field):
                    errors.append(f"{record_id}: {field} must be a non-empty list")

            label = str(record.get("visible_label", ""))
            if record_id == "NA-FIX-002" and "NOT SOURCE-OBSERVED" not in label:
                errors.append("NA-FIX-002: derived f/v map must visibly mark NOT SOURCE-OBSERVED")
            if record_id == "NA-FIX-010" and "DROPPED" not in label:
                errors.append("NA-FIX-010: dropped source-observed 27/216 wording must be visibly dropped")

        missing_maps = sorted(set(fixtures) - set(mapped))
        extra_maps = sorted(set(mapped) - set(fixtures))
        if missing_maps:
            errors.append(f"missing maps for fixture records {missing_maps}")
        if extra_maps:
            errors.append(f"maps reference unknown fixture records {extra_maps}")

    if errors:
        print("COUNT_LAYER_VIEW_MAP_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        return 1

    print("COUNT_LAYER_VIEW_MAP_VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
