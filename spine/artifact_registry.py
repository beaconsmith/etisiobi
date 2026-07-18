from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_ROOTS = ["artifacts", "research", "experiments", "paper", "visual_atlas", "emitters"]


def classify(path: Path) -> str:
    parts = path.parts
    if "artifacts" in parts:
        return "artifact_dossier"
    if "experiments" in parts:
        return "experiment"
    if "paper" in parts:
        return "paper"
    if "visual_atlas" in parts:
        return "atlas"
    if "emitters" in parts:
        return "emitter"
    return "research"


def build_registry() -> list[dict]:
    rows = []
    for root_name in ARTIFACT_ROOTS:
        root = ROOT / root_name
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if path.is_file() and ".git" not in path.parts:
                rows.append(
                    {
                        "path": str(path.relative_to(ROOT)).replace("\\", "/"),
                        "kind": classify(path),
                        "suffix": path.suffix,
                        "size": path.stat().st_size,
                    }
                )
    return rows


def main() -> None:
    rows = build_registry()
    out = ROOT / "corpus" / "artifact_registry.json"
    out.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"registered {len(rows)} artifacts -> {out}")


if __name__ == "__main__":
    main()
