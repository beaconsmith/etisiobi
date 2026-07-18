from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return rows


def maturity(claim: dict) -> str:
    status = claim.get("evidence_status", "")
    confidence = float(claim.get("confidence") or 0)
    if status == "contradicted":
        return "CX"
    if status == "experiment_supported" and confidence >= 0.8:
        return "C5"
    if status == "externally_supported":
        return "C4"
    if status == "repo_supported" and confidence >= 0.85:
        return "C3"
    if claim.get("source_path"):
        return "C2"
    return "C1"


def evaluate() -> list[dict]:
    rows = []
    for claim in read_jsonl(ROOT / "corpus" / "claims.jsonl"):
        row = dict(claim)
        row["maturity"] = maturity(claim)
        if row["maturity"] in {"C5", "C6", "C7"}:
            row["gate"] = "usable_with_limits"
        elif row["maturity"] == "CX":
            row["gate"] = "negative_or_remove"
        else:
            row["gate"] = "research_only"
        rows.append(row)
    return rows


def main() -> None:
    rows = evaluate()
    out = ROOT / "corpus" / "claim_maturity.json"
    out.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"evaluated {len(rows)} claims -> {out}")


if __name__ == "__main__":
    main()
