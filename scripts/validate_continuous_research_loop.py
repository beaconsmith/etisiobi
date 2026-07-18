from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
READY_RE = re.compile(r"\bREADY_FOR_HUMAN_ARXIV_REVIEW\b|\bSUBMISSION_READY\b|\bPUBLIC_RELEASE_READY\b")


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def main() -> int:
    errors: list[str] = []
    required = [
        ROOT / "research_goals" / "continuous_autoresearch" / "GOAL-CONT-001.md",
        ROOT / "research" / "frontier" / "continuous_research_loop" / "README.md",
        ROOT / "research" / "frontier" / "continuous_research_loop" / "loop_state.json",
        ROOT / "research_runs" / "continuous" / "CURRENT.md",
    ]
    for path in required:
        if not path.exists():
            errors.append(f"missing {path.relative_to(ROOT).as_posix()}")

    state_path = ROOT / "research" / "frontier" / "continuous_research_loop" / "loop_state.json"
    if state_path.exists():
        state = read_json(state_path)
        if state.get("active_goal") != "GOAL-CONT-001":
            errors.append("loop_state active_goal must be GOAL-CONT-001")
        if state.get("frontier_claim_status") != "not_ready":
            errors.append("continuous loop must keep frontier_claim_status=not_ready")
        latest = state.get("latest_run")
        if not latest:
            errors.append("loop_state must point to latest_run")
        else:
            run_dir = ROOT / latest
            manifest_path = run_dir / "run_manifest.json"
            selected_path = run_dir / "selected_experiments.md"
            queue_path = run_dir / "ranked_queue.csv"
            for path in [manifest_path, selected_path, queue_path, run_dir / "decision_trace.md", run_dir / "next_actions.md"]:
                if not path.exists():
                    errors.append(f"missing latest-run artifact: {path.relative_to(ROOT).as_posix()}")
            if manifest_path.exists():
                manifest = read_json(manifest_path)
                status = str(manifest.get("status", ""))
                if "NOT_FRONTIER_PROOF" not in status:
                    errors.append("run status must explicitly block frontier proof")
                foundation = manifest.get("foundation", {})
                if "26 rows x 8" not in foundation.get("source_observed_layer", ""):
                    errors.append("manifest must preserve 26x8 source-observed foundation")
                if "derived" not in foundation.get("derived_layer", "").lower():
                    errors.append("manifest must mark 27/216 as derived")
                selected = manifest.get("selected_experiments", [])
                if not selected:
                    errors.append("latest run must select at least one experiment")
                source_state = manifest.get("source_state", {})
                prior_packet = source_state.get("selected_prior_art_verification", {})
                if prior_packet.get("status") != "selected_primary_source_relevance_verified_not_novelty_clearance":
                    errors.append("manifest must surface selected prior-art verification status")
                if prior_packet.get("whole_atlas_prior_art_status") != "not_verified":
                    errors.append("manifest must keep whole atlas prior art not verified")
                for item in selected:
                    if not item.get("negative_control"):
                        errors.append(f"{item.get('atlas_id')} missing negative control")
                    if not item.get("claim_ceiling"):
                        errors.append(f"{item.get('atlas_id')} missing claim ceiling")
                    if item.get("selected_prior_art_status") != "primary_source_relevance_verified_not_novelty_clearance":
                        errors.append(f"{item.get('atlas_id')} missing selected prior-art relevance verification")
                    if item.get("selected_prior_art_claim_ceiling") != "prior_art_relevance_not_frontier_claim":
                        errors.append(f"{item.get('atlas_id')} selected prior-art claim ceiling must block frontier claims")
                    if item.get("prior_art_status") == "verified":
                        continue
                    if "requires_verification" not in str(item.get("prior_art_status", "")):
                        errors.append(f"{item.get('atlas_id')} prior_art_status must remain explicit")
                rendered = json.dumps(manifest, ensure_ascii=False)
                if READY_RE.search(rendered):
                    errors.append("manifest contains forbidden readiness language")

    for path in required:
        if path.exists() and READY_RE.search(read_text(path)):
            errors.append(f"forbidden readiness language in {path.relative_to(ROOT).as_posix()}")

    if errors:
        print("CONTINUOUS_RESEARCH_LOOP_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        return 1
    print("CONTINUOUS_RESEARCH_LOOP_VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
