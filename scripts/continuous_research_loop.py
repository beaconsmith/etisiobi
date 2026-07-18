from __future__ import annotations

import argparse
import csv
import hashlib
import json
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
LOOP_ROOT = ROOT / "research" / "frontier" / "continuous_research_loop"
RUNS_ROOT = ROOT / "research_runs" / "continuous"
ATLAS_PATH = ROOT / "research" / "frontier" / "nwagu_transfer_atlas" / "nwagu_research_atlas.jsonl"
PRIOR_ART_VERIFICATION_PATH = (
    ROOT
    / "research"
    / "frontier"
    / "nwagu_transfer_atlas"
    / "prior_art_verification"
    / "verification_manifest.json"
)
LPE_MANIFEST_PATH = ROOT / "instruments" / "lpe_bench" / "manifest.json"
LAB_GATES_PATH = ROOT / "research" / "LAB_STAGE_GATES.json"
GOAL_PATH = ROOT / "research_goals" / "continuous_autoresearch" / "GOAL-CONT-001.md"


def now_local() -> datetime:
    return datetime.now().astimezone().replace(microsecond=0)


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def selected_prior_art_records() -> dict[str, dict[str, Any]]:
    if not PRIOR_ART_VERIFICATION_PATH.exists():
        return {}
    manifest = read_json(PRIOR_ART_VERIFICATION_PATH)
    return {
        str(record.get("atlas_id")): record
        for record in manifest.get("selected_records", [])
        if isinstance(record, dict) and record.get("atlas_id")
    }


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = sorted({key for row in rows for key in row})
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def git_output(*args: str) -> str:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        return (result.stdout or result.stderr).strip()
    except OSError:
        return "git unavailable"


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def score_record(row: dict[str, Any]) -> tuple[float, list[str]]:
    reasons: list[str] = []
    score = 0.0

    phase_gate = row.get("phase_gate", "")
    phase_scores = {
        "begin_now": 30,
        "after_authority_review": 6,
        "after_reviewed_glyph_inventory": 8,
        "after_repertoire_stability": 10,
        "after_logograph_review": 7,
        "after_manuscript_access": 4,
    }
    score += phase_scores.get(phase_gate, 0)
    reasons.append(f"phase_gate={phase_gate}:{phase_scores.get(phase_gate, 0)}")

    rights = row.get("rights_risk", "")
    rights_scores = {"low": 22, "medium": 10, "high": -8}
    score += rights_scores.get(rights, 0)
    reasons.append(f"rights_risk={rights}:{rights_scores.get(rights, 0)}")

    if row.get("negative_control"):
        score += 12
        reasons.append("negative_control_present:12")
    if row.get("claim_ceiling"):
        score += 12
        reasons.append("claim_ceiling_present:12")
    if row.get("article_candidate"):
        score += 6
        reasons.append("article_candidate_present:6")
    if row.get("experiment"):
        score += 8
        reasons.append("experiment_defined:8")

    required = row.get("required_evidence", [])
    if isinstance(required, list):
        if len(required) <= 3:
            score += 5
            reasons.append("bounded_required_evidence:5")
        else:
            score -= 3
            reasons.append("large_required_evidence:-3")

    source_family = str(row.get("source_family", "")).lower()
    if any(token in source_family for token in ["benchmark", "evaluation", "model evaluation", "language model"]):
        score += 8
        reasons.append("benchmark_or_eval_family:8")
    if any(token in source_family for token in ["research object", "data versioning", "software preservation"]):
        score += 6
        reasons.append("reproducibility_family:6")

    if row.get("prior_art_status") != "verified":
        score -= 6
        reasons.append("prior_art_unverified:-6")

    return round(score, 2), reasons


def build_ranked_queue() -> list[dict[str, Any]]:
    atlas = read_jsonl(ATLAS_PATH)
    selected_prior_art = selected_prior_art_records()
    ranked: list[dict[str, Any]] = []
    for row in atlas:
        score, reasons = score_record(row)
        atlas_id = str(row.get("atlas_id"))
        prior_record = selected_prior_art.get(atlas_id, {})
        ranked.append(
            {
                "atlas_id": atlas_id,
                "project": row.get("project"),
                "source_family": row.get("source_family"),
                "phase_gate": row.get("phase_gate"),
                "rights_risk": row.get("rights_risk"),
                "prior_art_status": row.get("prior_art_status"),
                "selected_prior_art_status": prior_record.get("verified_status", "not_selected_for_verification"),
                "selected_prior_art_claim_ceiling": prior_record.get("claim_ceiling", ""),
                "selected_prior_art_next_action": prior_record.get("bounded_next_action", ""),
                "experiment": row.get("experiment"),
                "negative_control": row.get("negative_control"),
                "claim_ceiling": row.get("claim_ceiling"),
                "article_candidate": row.get("article_candidate"),
                "frontier_loop_score": score,
                "score_reasons": "; ".join(reasons),
            }
        )
    return sorted(ranked, key=lambda item: (-float(item["frontier_loop_score"]), str(item["atlas_id"])))


def write_goal(timestamp: str) -> None:
    write_text(
        GOAL_PATH,
        f"""---
type: research_goal
goal_id: GOAL-CONT-001
status: active
created: "{timestamp}"
updated: "{timestamp}"
program: nwagu_aneke_frontier
stage: RESEARCH_PROGRAM
---

# GOAL-CONT-001: Continuous Autonomous Research Loop

## Objective

Continuously convert the Nwagu transfer atlas and LPE-Bench into bounded,
validated research iterations without generating paper-looking outputs before
the evidence stage permits them.

## Current foundation

- Source-observed layer: 26 rows x 8 vowel/modifier columns = 208 records.
- 27/216 is a derived f/v split layer only.
- LPE-Bench is the current measurable failure detector.
- Nwagu Transfer ATLAS is the current experiment queue.
- Selected infrastructure prior-art verification is relevance-only and does not
  clear novelty or the whole atlas.

## Loop

1. Read canonical memory and stage gates.
2. Freeze current atlas, LPE manifest, branch, and dirty status.
3. Rank next experiments by evidence readiness, rights risk, negative control,
   reproducibility, and article potential.
4. Select a small active batch.
5. Write a run manifest and decision trace.
6. Run validators.
7. Update only research-state artifacts, never public-readiness claims.

## Stop rules

- Do not create impact-journal or arXiv-ready claims from this loop.
- Do not render new paper PDFs.
- Do not treat seeded prior art as verified.
- Do not treat selected prior-art relevance as novelty clearance.
- Do not treat AI-only labels as human/domain gold.
- Do not promote high-rights-risk artifact work without authority review.

## Success criteria

- Every run leaves a machine-readable manifest.
- Every selected experiment has a negative control and claim ceiling.
- The next action is inspectable by a human.
- `python scripts/validate_continuous_research_loop.py` passes.

## Next command

```powershell
python scripts\\continuous_research_loop.py --mode cycle --max-experiments 5
```
""",
    )


def write_operating_doc(timestamp: str) -> None:
    write_text(
        LOOP_ROOT / "README.md",
        f"""# Continuous Research Loop

Generated: {timestamp}

This is the controlled autonomous loop for Etisiobi frontier research.

It is intentionally narrower than `scripts/research_loop.py`. The older loop can
regenerate broad scaffolding. This loop only:

1. reads canonical stage gates;
2. reads LPE-Bench and the Nwagu Transfer ATLAS;
3. ranks experiments;
4. writes a run trace;
5. blocks paper/readiness promotion.

## Current Research Object

Layer Promotion Error (LPE): an AI or research workflow promotes a claim from a
weaker evidence layer into a stronger one, for example treating a derived
27/216 f/v split as source-observed.

## Continuous Loop Command

```powershell
python scripts\\continuous_research_loop.py --mode cycle --max-experiments 5
python scripts\\validate_continuous_research_loop.py
```

## Promotion Rule

The loop may select experiments. It may not declare a paper complete. Paper
readiness remains governed by `research/LAB_STAGE_GATES.json`,
`research/A_PLUS_LAB_STANDARD.md`, and the review-team trace gate.
""",
    )


def write_run(max_experiments: int) -> dict[str, Any]:
    timestamp = now_local()
    stamp = timestamp.strftime("%Y%m%d-%H%M%S")
    run_id = f"RUN-CONT-{stamp}"
    run_dir = RUNS_ROOT / run_id
    ranked = build_ranked_queue()
    selected = ranked[:max_experiments]

    atlas_summary = read_json(ROOT / "research" / "frontier" / "nwagu_transfer_atlas" / "summary.json")
    prior_art_manifest = read_json(PRIOR_ART_VERIFICATION_PATH) if PRIOR_ART_VERIFICATION_PATH.exists() else {}
    lpe_manifest = read_json(LPE_MANIFEST_PATH)
    gates = read_json(LAB_GATES_PATH)
    status = "RUN_CREATED_RESEARCH_SELECTION_ONLY_NOT_FRONTIER_PROOF"

    manifest = {
        "run_id": run_id,
        "generated_at": timestamp.isoformat(),
        "status": status,
        "goal": "GOAL-CONT-001",
        "git": {
            "branch": git_output("branch", "--show-current"),
            "commit": git_output("rev-parse", "--short", "HEAD"),
            "status_short_hash": hashlib.sha256(git_output("status", "--short").encode("utf-8")).hexdigest(),
        },
        "inputs": {
            "atlas_path": str(ATLAS_PATH.relative_to(ROOT)).replace("\\", "/"),
            "atlas_sha256": file_sha256(ATLAS_PATH),
            "lpe_manifest_path": str(LPE_MANIFEST_PATH.relative_to(ROOT)).replace("\\", "/"),
            "lpe_manifest_sha256": file_sha256(LPE_MANIFEST_PATH),
            "stage_gates_path": str(LAB_GATES_PATH.relative_to(ROOT)).replace("\\", "/"),
            "stage_gates_sha256": file_sha256(LAB_GATES_PATH),
        },
        "foundation": {
            "source_observed_layer": "26 rows x 8 vowel/modifier columns = 208 records",
            "derived_layer": "derived 27/216 by f/v split only",
            "forbidden_promotion": "27/216 must not be described as source-observed",
        },
        "source_state": {
            "atlas_status": atlas_summary.get("status"),
            "atlas_record_count": atlas_summary.get("record_count"),
            "atlas_frontier_claim_status": atlas_summary.get("frontier_claim_status"),
            "selected_prior_art_verification": {
                "verification_id": prior_art_manifest.get("verification_id"),
                "status": prior_art_manifest.get("status"),
                "path": str(PRIOR_ART_VERIFICATION_PATH.relative_to(ROOT)).replace("\\", "/"),
                "selected_record_count": len(prior_art_manifest.get("selected_records", [])),
                "whole_atlas_prior_art_status": prior_art_manifest.get("whole_atlas_prior_art_status"),
                "claim_ceiling": prior_art_manifest.get("claim_ceiling"),
            },
            "lpe_status": lpe_manifest.get("status"),
            "lpe_frontier_claim_status": lpe_manifest.get("frontier_claim_status"),
            "stage_count": len(gates.get("stages", [])),
        },
        "selected_experiments": selected,
        "blocked_promotions": [
            "no paper-ready status",
            "no public release status",
            "no source-observed 27/216 claim",
            "no AI-only gold-label frontier claim",
        ],
        "next_command": "python scripts\\continuous_research_loop.py --mode cycle --max-experiments 5",
    }

    write_json(run_dir / "run_manifest.json", manifest)
    write_csv(run_dir / "ranked_queue.csv", ranked)
    write_json(run_dir / "ranked_queue.json", ranked)
    write_text(
        run_dir / "selected_experiments.md",
        "# Selected Experiments\n\n"
        + "\n".join(
            f"## {idx}. {item['atlas_id']} - {item['project']}\n\n"
            f"- Score: {item['frontier_loop_score']}\n"
            f"- Experiment: {item['experiment']}\n"
            f"- Negative control: {item['negative_control']}\n"
            f"- Claim ceiling: {item['claim_ceiling']}\n"
            f"- Rights risk: {item['rights_risk']}\n"
            f"- Atlas prior art: {item['prior_art_status']}\n"
            f"- Selected prior-art verification: {item['selected_prior_art_status']}\n"
            f"- Selected prior-art boundary: {item['selected_prior_art_claim_ceiling']}\n"
            for idx, item in enumerate(selected, start=1)
        ),
    )
    write_text(
        run_dir / "decision_trace.md",
        f"""# Decision Trace

Run: `{run_id}`

Decision: `KEEP_AS_RESEARCH_SELECTION_RUN_NOT_PAPER_PROMOTION`

Why:

- The repo already has a seeded transfer atlas and LPE instrument.
- The next autonomous action should select bounded experiments, not create papers.
- Selected records have explicit negative controls and claim ceilings.
- The selected infrastructure prior-art packet verifies primary-source relevance
  for this batch only.
- The whole transfer atlas remains not prior-art verified, so no frontier or
  novelty claim is promoted.

Main blocker:

- Human/domain validation, broader atlas verification, and branch-specific
  execution or review gates are still required before any result can become a
  paper candidate.
""",
    )

    def next_action_line(idx: int, item: dict[str, Any]) -> str:
        action = item.get("selected_prior_art_next_action")
        if not action:
            action = f"Verify prior art for `{item['project']}` before planning `{item['atlas_id']}`."
        return f"{idx}. {action}"

    write_text(
        run_dir / "next_actions.md",
        "# Next Actions\n\n"
        + "\n".join(
            next_action_line(idx, item)
            for idx, item in enumerate(selected, start=1)
        )
        + "\n",
    )

    write_json(
        LOOP_ROOT / "loop_state.json",
        {
            "updated_at": timestamp.isoformat(),
            "status": status,
            "active_goal": "GOAL-CONT-001",
            "latest_run": str(run_dir.relative_to(ROOT)).replace("\\", "/"),
            "latest_run_id": run_id,
            "selected_count": len(selected),
            "frontier_claim_status": "not_ready",
            "next_command": manifest["next_command"],
        },
    )
    write_text(
        RUNS_ROOT / "CURRENT.md",
        f"""# Current Continuous Research Run

- Run: `{run_id}`
- Status: `{status}`
- Manifest: `{run_dir.relative_to(ROOT).as_posix()}/run_manifest.json`
- Selected experiments: `{run_dir.relative_to(ROOT).as_posix()}/selected_experiments.md`
- Next command: `{manifest['next_command']}`
""",
    )
    return manifest


def append_log(manifest: dict[str, Any]) -> None:
    log_path = ROOT / "log.md"
    entry = f"""

## [{manifest['generated_at'][:10]}] frontier | continuous-research-loop | {manifest['run_id']}

Initialized controlled continuous research loop.

- Goal: `GOAL-CONT-001`
- Status: `{manifest['status']}`
- Selected experiments: {len(manifest['selected_experiments'])}
- Frontier claim status: `not_ready`
- Rule: source-observed layer remains 26x8=208; 27/216 is derived only.
- Next: `{manifest['next_command']}`
"""
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(entry)


def run_cycle(max_experiments: int) -> None:
    timestamp = now_local().isoformat()
    write_goal(timestamp)
    write_operating_doc(timestamp)
    manifest = write_run(max_experiments=max_experiments)
    append_log(manifest)
    print("CONTINUOUS_RESEARCH_LOOP_RUN_CREATED")
    print(f"run_id={manifest['run_id']}")
    print(f"selected={len(manifest['selected_experiments'])}")
    print("status=RUN_CREATED_RESEARCH_SELECTION_ONLY_NOT_FRONTIER_PROOF")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["cycle", "state-only"], default="cycle")
    parser.add_argument("--max-experiments", type=int, default=5)
    args = parser.parse_args()

    if args.max_experiments < 1:
        raise SystemExit("--max-experiments must be >= 1")

    write_goal(now_local().isoformat())
    write_operating_doc(now_local().isoformat())
    if args.mode == "cycle":
        run_cycle(max_experiments=args.max_experiments)
    else:
        print("CONTINUOUS_RESEARCH_LOOP_STATE_WRITTEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
