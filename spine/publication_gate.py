from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_claims() -> list[dict]:
    path = ROOT / "corpus" / "claim_maturity.json"
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def gate(output_name: str = "unspecified") -> dict:
    claims = load_claims()
    blockers = [c for c in claims if c.get("gate") == "negative_or_remove"]
    research_only = [c for c in claims if c.get("gate") == "research_only"]
    return {
        "output": output_name,
        "ready_for_human_review": len(blockers) == 0,
        "blocker_count": len(blockers),
        "research_only_count": len(research_only),
        "rules": [
            "Positive contribution claims must be C5+.",
            "C0-C4 claims require limitation language.",
            "CX claims may appear only as negative results.",
            "Human approval required for external release.",
        ],
    }


def main() -> None:
    result = gate()
    out = ROOT / "corpus" / "publication_gate_report.json"
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
