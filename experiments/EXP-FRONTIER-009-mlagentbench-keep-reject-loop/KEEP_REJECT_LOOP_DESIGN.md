---
type: bounded_experiment_design
experiment_id: EXP-FRONTIER-009
atlas_id: ATLAS-0052
status: MLAGENTBENCH_KEEP_REJECT_DESIGN_READY_NO_AGENT_RUN
created: "2026-06-23"
claim_ceiling: agent_evaluation_design_not_research_result
---

# MLAgentBench-Style Keep/Reject Loop Design

This packet converts `ATLAS-0052` into a no-run design for deciding whether
future AI-agent research tasks should be kept, revised, rejected, or blocked.
No agents are run. No dependency installation occurs. No model/API call occurs.
No private or restricted source data is used.

## Primary-Source Basis

MLAgentBench is useful prior art because it treats agent work as a sequence of
goal-directed experimentation tasks with actions, logs, metrics, and final
evaluation. The Etisiobi transfer is not about machine-learning accuracy. The
transferable mechanism is the keep/reject loop: define a goal, constrain
allowed actions, record logs, score against a bounded metric, and reject outputs
that promote claims beyond their evidence layer.

Primary sources:

- https://arxiv.org/abs/2310.03302
- https://github.com/snap-stanford/MLAgentBench

## Design Principle

The Etisiobi version keeps the MLAgentBench discipline but changes the research
object:

- MLAgentBench native object: machine-learning experimentation by agents.
- Etisiobi object: layer-safe research behavior around LPE and Nwagu glyph/count
  boundaries.
- Claim ceiling: `agent_evaluation_design_not_research_result`.

The design can say that the task cards are plausible evaluation designs. It
cannot say an agent performed well, that LPE is solved, that Nwagu source facts
are validated, or that any article is mature.

## Keep/Reject Labels

| Label | Meaning |
|---|---|
| `keep_for_review` | The task is bounded, non-sensitive, and worth human/domain review before any run. |
| `revise_before_run` | The task is promising but its prompt, metric, or logs are not yet sharp enough. |
| `reject_as_overclaim` | The task would reward evidence-layer promotion or model-result overclaiming. |
| `blocked_missing_authority` | The task needs source, rights, cultural authority, or reviewer approval first. |

## Required Logs For Any Future Run

- task card id and version;
- exact prompt or instruction;
- local files exposed to the agent;
- allowed and forbidden actions;
- all agent edits and tool calls;
- metric inputs and outputs;
- keep/reject decision;
- reviewer notes before any external citation.

## What This Teaches Oroma

Oroma-facing governance and research tools need explicit stop states, not just
success states. A good agent loop should know when to keep an idea for review,
revise it, reject it as an overclaim, or block it because authority is missing.
That pattern transfers cleanly from research integrity into product governance:
claims and decisions should move only when the right evidence and authority are
present.

## Exact Next Action

Review the four task cards for source-layer and rights/authority safety. Do not
run agents until explicit approval and human/domain review are recorded.
