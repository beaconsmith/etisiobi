---
type: execution_runbook
experiment_id: EXP-FRONTIER-007
status: pending_user_approval
created: "2026-06-22"
claim_ceiling: eval_harness_relevance_not_model_claim
---

# Inspect Execution Runbook

This runbook is a gate, not an execution record. There is no dependency
installation, no model/API call, no private or restricted source data, and no
paper or public-release claim in the current state.

## Preconditions

- User or lab explicitly approves a separate execution cycle.
- Dependency installation is approved for that cycle only.
- Model/API call and key handling are approved for that cycle only.
- Seed labels receive human/domain review or are kept as provisional labels.
- The run uses only non-sensitive seed cases already in this package.
- The output policy is accepted before any logs are saved.

## Intended Run Shape

1. Create a clean temporary environment or isolated project branch.
2. Install only the approved evaluation dependency set.
3. Convert `data/inspect_lpe_seed_cases.jsonl` into an executable task.
4. Run the same prompts through the manual negative control.
5. Store prompts, outputs, scores, and error logs under a dated run directory.
6. Strip secrets and private identifiers before committing any output.
7. Label the result only as `eval_harness_relevance_not_model_claim`.

## Stop Conditions

- Any prompt requires private or restricted source material.
- A dependency asks for broad system access outside the approved environment.
- A model/API key would be written to disk.
- A result is phrased as evidence that Nwagu Aneke source facts are proven.
- A result is phrased as article readiness or public release clearance.

## Exact Next Action

Review `approval_checklist.csv` and decide whether to approve or reject a
separate execution cycle.
