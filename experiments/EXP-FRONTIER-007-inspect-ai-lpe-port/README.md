---
type: experiment_index
experiment_id: EXP-FRONTIER-007
atlas_id: ATLAS-0049
status: INSPECT_LPE_PORT_PLAN_READY_EXECUTION_GATE_PENDING
created: "2026-06-22"
updated: "2026-06-22T18:45:09+01:00"
claim_ceiling: eval_harness_relevance_not_model_claim
---

# EXP-FRONTIER-007 Inspect-Style LPE Port

This experiment turns `ATLAS-0049` into a bounded adapter plan for LPE-Bench.
It does not install Inspect AI, run models, call external APIs, or validate any
Nwagu Aneke source claim.

## Contents

- `manifest.json` - status, sources, blockers, and claim ceiling.
- `plan.md` - bounded experiment design.
- `inspect_adapter_contract.md` - mapping from LPE records into an Inspect-style
  task shape.
- `data/inspect_lpe_seed_cases.jsonl` - ten non-sensitive seed samples.
- `data/manual_prompt_negative_control.jsonl` - manual-prompt control shape.
- `execution_gate/` - pending approval checklist, runbook, risk register, and
  output handling policy.
- `execution_gate/review/` - reviewed decision packet that keeps execution
  blocked pending explicit user/lab approval.

## Current Interpretation

Inspect AI is useful prior art for an externally legible evaluation harness.
This package only says that LPE-Bench can be mapped onto the same style of
dataset, solver, scorer, and log separation. It does not show model behavior.

## Exact Next Action

Record explicit user/lab approval or rejection for a separate Inspect execution
cycle. Until that decision changes, no dependency installation, model/API call,
or output claim is allowed; without approval, continue to the `ATLAS-0052`
design-only loop.
