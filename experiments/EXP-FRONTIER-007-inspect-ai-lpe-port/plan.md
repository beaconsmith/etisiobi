---
type: bounded_experiment_plan
experiment_id: EXP-FRONTIER-007
atlas_id: ATLAS-0049
status: INSPECT_LPE_PORT_PLAN_READY_EXECUTION_GATE_PENDING
created: "2026-06-22"
updated: "2026-06-22T18:45:09+01:00"
claim_ceiling: eval_harness_relevance_not_model_claim
---

# Inspect-Style LPE-Bench Port Plan

## Question

Can LPE-Bench be expressed in the same evaluation shape used by Inspect AI:
dataset samples, a solver or agent attempt, a scorer, and inspectable logs?

## Primary-Source Basis

The official Inspect documentation describes a frontier AI evaluation framework
with datasets, agents, tools, scorers, logs, analysis views, and sandboxing. The
GitHub repository identifies the framework as open source and points to the
same documentation. The tutorial shows tasks as a dataset plus solver plus
scorer, including custom scorers and tool-using agent tasks.

Primary sources checked:

- https://inspect.aisi.org.uk/
- https://github.com/UKGovernmentBEIS/inspect_ai
- https://www.aisi.gov.uk/blog/inspect-evals
- https://inspect.aisi.org.uk/tutorial.html

## Method

1. Keep this run no-install and no-model-run.
2. Encode ten non-sensitive LPE cases in an Inspect-style sample shape.
3. Include both promotion-error and non-promotion-error labels.
4. Include Nwagu count-layer, speculation-boundary, computational-evaluation,
   and external-prior-art-control cases.
5. Define a manual prompt batch as negative control.
6. Require later human/domain review before seed labels can be treated as gold
   labels.
7. Require explicit dependency and API approval before any executable Inspect
   run.

## Expected Learning

This plan should show whether LPE-Bench has a clean bridge into a recognized
evaluation framework without weakening claim-layer discipline.

## Failure Conditions

- The seed cases require private or restricted source data.
- The adapter collapses source-observed, derived, speculative, and applied
  layers.
- The scorer treats an evaluation harness as proof of Nwagu source facts.
- The plan depends on dependency installation during the continuous loop.
- The negative control is not defined.

## Allowed Statuses

- `INSPECT_LPE_PORT_PLAN_READY_NO_DEPENDENCY_INSTALL`
- `INSPECT_LPE_PORT_EXECUTION_APPROVED_NOT_RUN`
- `INSPECT_LPE_PORT_RUN_COMPLETE_NOT_SOURCE_EVIDENCE`
- `INSPECT_LPE_PORT_REJECTED`

## Blockers

- explicit dependency approval;
- model/API key approval;
- human/domain review of seed labels;
- no private or restricted source data;
- execution gate pending user approval.

## Execution Gate

The approval packet now lives under `execution_gate/`.

It keeps the execution decision at `pending_user_approval` and records:

- required approval gates;
- forbidden actions in the current state;
- run isolation expectations;
- secret/output handling rules;
- claim ceiling for any future output.

The reviewed gate packet is
`execution_gate/review/EXECUTION_GATE_REVIEW.md`. It keeps execution blocked
and records that explicit user/lab approval or rejection is still required.

## Exact Next Action

Record explicit user/lab approval or rejection for a separate Inspect execution
cycle. Without approval, continue to the `ATLAS-0052` design-only loop.
