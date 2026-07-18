from __future__ import annotations

import argparse
from pathlib import Path

import project_research_events


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVENTS = ROOT / "spine" / "events" / "research_events.jsonl"


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Etisiobi research event stream.")
    parser.add_argument("--events", default=str(DEFAULT_EVENTS), help="Event JSONL path.")
    args = parser.parse_args()
    events_path = Path(args.events)
    if not events_path.is_absolute():
        events_path = ROOT / events_path
    events = project_research_events.load_events(events_path)
    errors = project_research_events.validate_events(events)
    if errors:
        print("RESEARCH_EVENTS_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        if len(errors) > 200:
            print(f"- ... {len(errors) - 200} additional errors")
        return 1
    print("RESEARCH_EVENTS_VALID")
    print(f"events={len(events)}")
    print(f"last_event_id={events[-1]['event_id'] if events else 'none'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
