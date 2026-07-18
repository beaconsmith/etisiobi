from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    claims = load_json(ROOT / "corpus" / "claim_maturity.json", [])
    artifacts = load_json(ROOT / "corpus" / "artifact_registry.json", [])
    contradictions = load_json(ROOT / "corpus" / "contradiction_tracker.json", [])
    maturity_counts = Counter(c.get("maturity", "unknown") for c in claims)
    artifact_counts = Counter(a.get("kind", "unknown") for a in artifacts)
    dashboard = {
        "claim_count": len(claims),
        "artifact_count": len(artifacts),
        "contradiction_count": len(contradictions),
        "maturity_counts": dict(maturity_counts),
        "artifact_counts": dict(artifact_counts),
        "top_paths": [a.get("path") for a in artifacts[:20]],
    }
    out = ROOT / "visual_atlas" / "lab_dashboard_data.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(dashboard, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(dashboard, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
