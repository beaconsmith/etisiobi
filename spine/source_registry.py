from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "corpus" / "source_registry.json"


def load_sources() -> list[dict]:
    if REGISTRY_PATH.exists():
        return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    sources = []
    for path in [ROOT / "corpus" / "sources.jsonl", ROOT / "corpus" / "nwagu_aneke_research_threads.json"]:
        if not path.exists():
            continue
        if path.suffix == ".jsonl":
            for line in path.read_text(encoding="utf-8").splitlines():
                if line.strip():
                    sources.append(json.loads(line))
        else:
            data = json.loads(path.read_text(encoding="utf-8"))
            sources.extend(data.get("sources", []))
    return sources


def save_sources(sources: list[dict]) -> None:
    REGISTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    REGISTRY_PATH.write_text(json.dumps(sources, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    sources = load_sources()
    save_sources(sources)
    print(f"registered {len(sources)} sources -> {REGISTRY_PATH}")


if __name__ == "__main__":
    main()
