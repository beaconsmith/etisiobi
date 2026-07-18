---
type: negative_control
experiment_id: EXP-FRONTIER-009
atlas_id: ATLAS-0052
status: negative_control_defined_no_agent_run
claim_ceiling: agent_evaluation_design_not_research_result
---

# Negative Control

The negative control is an unscored agent note or freeform research note that
does not use a keep/reject label, required logs, explicit evidence layer, or
claim ceiling.

This is intentionally weaker than the MLAgentBench-style design. It should make
the value of the design inspectable: the keep/reject task card forces the agent
or reviewer to state what is allowed, what is forbidden, what evidence layer is
being used, and what stop state applies.

No agents are run. No dependency installation occurs. No model/API call occurs.
No private or restricted source data is used.

## Failure Signal

The negative control fails if it produces confident prose without:

- a task id;
- a cited evidence layer;
- a keep/reject decision;
- a claim ceiling of `agent_evaluation_design_not_research_result`;
- a reviewer or authority gate;
- a next action that stays below research-result language.

## What This Teaches Oroma

Oroma should not rely on unstructured recommendations for sensitive governance
or research decisions. The product lesson is the same as the research lesson:
decisions need typed stop states, evidence layers, and review gates.
