from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURE_PATH = ROOT / "research" / "frontier" / "nwagu_aneke" / "claim_layer_fixtures.jsonl"
SCHEMA_PATH = ROOT / "research" / "frontier" / "nwagu_aneke" / "CLAIM_LAYER_SCHEMA.md"

ALLOWED_LAYERS = {
    "source_observed",
    "community_attested",
    "derived",
    "speculative",
    "computationally_generated",
    "experimentally_supported",
    "applied",
    "contested",
    "restricted",
    "dropped",
}

REQUIRED_FIELDS = {
    "record_id",
    "claim_text",
    "layer",
    "source_refs",
    "derivation_refs",
    "method_refs",
    "rights_status",
    "authority_status",
    "uncertainty",
    "contradictions",
    "promotion_status",
    "collapse_conditions",
}

LIST_FIELDS = {
    "source_refs",
    "derivation_refs",
    "method_refs",
    "contradictions",
    "collapse_conditions",
}


def main() -> int:
    errors: list[str] = []

    if not SCHEMA_PATH.exists():
        errors.append(f"missing schema: {SCHEMA_PATH.relative_to(ROOT).as_posix()}")

    if not FIXTURE_PATH.exists():
        errors.append(f"missing fixtures: {FIXTURE_PATH.relative_to(ROOT).as_posix()}")
    else:
        seen_ids: set[str] = set()
        layers_seen: set[str] = set()
        for line_number, line in enumerate(FIXTURE_PATH.read_text(encoding="utf-8").splitlines(), start=1):
            if not line.strip():
                errors.append(f"line {line_number}: blank lines are not allowed in JSONL")
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                errors.append(f"line {line_number}: invalid JSON: {exc}")
                continue

            record_id = str(record.get("record_id", f"line {line_number}"))
            if record_id in seen_ids:
                errors.append(f"{record_id}: duplicate record_id")
            seen_ids.add(record_id)

            missing = sorted(REQUIRED_FIELDS - record.keys())
            if missing:
                errors.append(f"{record_id}: missing fields {missing}")

            layer = record.get("layer")
            if layer not in ALLOWED_LAYERS:
                errors.append(f"{record_id}: invalid layer {layer!r}")
            else:
                layers_seen.add(str(layer))

            for field in LIST_FIELDS:
                if not isinstance(record.get(field), list):
                    errors.append(f"{record_id}: {field} must be a list")

            for field in ["record_id", "claim_text", "layer", "rights_status", "authority_status", "uncertainty", "promotion_status"]:
                if not isinstance(record.get(field), str) or not record.get(field, "").strip():
                    errors.append(f"{record_id}: {field} must be a non-empty string")

            if isinstance(record.get("collapse_conditions"), list) and not record["collapse_conditions"]:
                errors.append(f"{record_id}: collapse_conditions must not be empty")

            if record.get("layer") == "derived" and not record.get("derivation_refs"):
                errors.append(f"{record_id}: derived records require derivation_refs")

            if record.get("layer") in {"computationally_generated", "experimentally_supported"} and not record.get("method_refs"):
                errors.append(f"{record_id}: computational/experimental records require method_refs")

            if record.get("layer") == "applied" and not record.get("derivation_refs"):
                errors.append(f"{record_id}: applied records require source-to-abstraction derivation_refs")

        required_fixture_layers = {
            "source_observed",
            "derived",
            "restricted",
            "speculative",
            "computationally_generated",
            "applied",
            "contested",
            "dropped",
        }
        missing_layers = sorted(required_fixture_layers - layers_seen)
        if missing_layers:
            errors.append(f"fixtures missing required layer coverage: {missing_layers}")

    if errors:
        print("CLAIM_LAYER_FIXTURES_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        return 1

    print("CLAIM_LAYER_FIXTURES_VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
