from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)


def main() -> int:
    validation = run(["python", "scripts/validate_research_events.py"])
    if validation.returncode != 0:
        print(validation.stdout)
        print(validation.stderr)
        return validation.returncode

    projection = run(["python", "scripts/project_research_events.py"])
    if projection.returncode != 0:
        print(projection.stdout)
        print(projection.stderr)
        return projection.returncode

    state_path = ROOT / "spine" / "events" / "current_state.json"
    index_path = ROOT / "spine" / "events" / "artifact_event_index.json"
    state = json.loads(state_path.read_text(encoding="utf-8"))
    index = json.loads(index_path.read_text(encoding="utf-8"))

    assert state["last_event_id"] == "REVT-0021", "event trace should include the Nwagu article benchmark result"
    assert "pagc_nwagu_aneke_count_layer_foundation" in state["latest_by_scope"], "count-layer foundation must project"
    assert state["gate_status"]["retrieval_firewall"]["status"] == "pass", "retrieval firewall gate must project as pass"
    assert state["gate_status"]["vendor_neutrality"]["status"] == "pass", "vendor-neutrality gate must project as pass"
    assert "research/pagc/INDEX.md" in state["superseded_artifacts"], "stale PAGC index must be superseded in state"
    assert "spine/retrieval_manifest.yaml" in index, "retrieval manifest must be indexed to source events"

    manifest = (ROOT / "spine" / "retrieval_manifest.yaml").read_text(encoding="utf-8")
    assert "source_event_id: \"REVT-" in manifest, "retrieval manifest must carry event provenance where available"

    print("RESEARCH_EVENT_TRACE_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
