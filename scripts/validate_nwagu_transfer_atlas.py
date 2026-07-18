from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ATLAS = ROOT / "research" / "frontier" / "nwagu_transfer_atlas"

REQUIRED_FIELDS = {
    "atlas_id",
    "project",
    "source_family",
    "native_problem",
    "transferable_mechanism",
    "nwagu_research_object",
    "required_evidence",
    "experiment",
    "negative_control",
    "claim_ceiling",
    "prior_art_status",
    "rights_risk",
    "article_candidate",
    "phase_gate",
    "status",
    "source_urls",
}


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> int:
    errors: list[str] = []
    required_files = [
        ATLAS / "nwagu_research_atlas.jsonl",
        ATLAS / "summary.json",
        ATLAS / "README.md",
        ATLAS / "ATLAS_METHOD.md",
        ATLAS / "TOP_PROGRAMS.md",
    ]
    for path in required_files:
        if not path.exists():
            errors.append(f"missing {path.relative_to(ROOT).as_posix()}")

    if not errors:
        rows = read_jsonl(ATLAS / "nwagu_research_atlas.jsonl")
        summary = read_json(ATLAS / "summary.json")
        if summary.get("status") != "NWAGU_TRANSFER_ATLAS_SEEDED_NOT_PRIOR_ART_VERIFIED":
            errors.append("ATLAS must be explicitly marked seeded and not prior-art verified")
        if summary.get("frontier_claim_status") != "not_ready":
            errors.append("ATLAS must not claim frontier readiness")
        if len(rows) < 40:
            errors.append("ATLAS must seed at least 40 repo/lab transfer records")
        ids = [row.get("atlas_id") for row in rows]
        if len(ids) != len(set(ids)):
            errors.append("ATLAS IDs must be unique")
        phase_counts = Counter(row.get("phase_gate") for row in rows)
        for phase in ("begin_now", "after_reviewed_glyph_inventory", "after_authority_review"):
            if phase_counts.get(phase, 0) < 5:
                errors.append(f"ATLAS needs at least 5 records for phase gate {phase}")
        for row in rows:
            missing = REQUIRED_FIELDS.difference(row)
            if missing:
                errors.append(f"{row.get('atlas_id', 'unknown')} missing fields: {sorted(missing)}")
                continue
            if not row["required_evidence"]:
                errors.append(f"{row['atlas_id']} must list required evidence")
            if not row["negative_control"]:
                errors.append(f"{row['atlas_id']} must define a negative control")
            if not row["claim_ceiling"]:
                errors.append(f"{row['atlas_id']} must define a claim ceiling")
            if row["prior_art_status"] != "seeded_from_attachment_requires_verification":
                errors.append(f"{row['atlas_id']} must not imply verified prior art yet")
            if row["rights_risk"] not in {"low", "medium", "high"}:
                errors.append(f"{row['atlas_id']} has invalid rights risk")
            if not row["source_urls"]:
                errors.append(f"{row['atlas_id']} must include at least one source URL")

    if errors:
        print("NWAGU_TRANSFER_ATLAS_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        return 1
    print("NWAGU_TRANSFER_ATLAS_VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
