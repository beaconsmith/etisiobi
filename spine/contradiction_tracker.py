from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def collect() -> list[dict]:
    contradictions = []
    for claim in read_jsonl(ROOT / "corpus" / "claims.jsonl"):
        if claim.get("evidence_status") == "contradicted":
            contradictions.append(
                {
                    "kind": "claim",
                    "id": claim.get("claim_id"),
                    "text": claim.get("claim_text"),
                    "source": claim.get("source_path"),
                    "action": claim.get("needed_validation", []),
                }
            )
    for mapping in read_jsonl(ROOT / "research_lattice" / "mappings.jsonl"):
        if mapping.get("status") in {"rejected_for_now", "speculative"}:
            contradictions.append(
                {
                    "kind": "mapping",
                    "id": mapping.get("mapping_id"),
                    "text": mapping.get("claim"),
                    "source": mapping.get("source_object"),
                    "action": "Keep classified; do not promote without new evidence.",
                }
            )
    return contradictions


def main() -> None:
    rows = collect()
    out = ROOT / "corpus" / "contradiction_tracker.json"
    out.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"tracked {len(rows)} contradictions/speculative mappings -> {out}")


if __name__ == "__main__":
    main()
