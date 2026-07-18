---
type: prior_art_note
atlas_id: ATLAS-0049
project: Inspect AI
status: verified_primary_source_relevance_not_novelty_clearance
created: "2026-06-22"
updated: "2026-06-22T18:40:23+01:00"
claim_ceiling: eval harness relevance only
rights_risk: low
---

# ATLAS-0049 Prior Art Note: Inspect AI

## 1. What Inspect AI is

Inspect AI is an open-source framework for large language model evaluations
created by the UK AI Security Institute and Meridian Labs.

Primary sources:

- Official documentation: https://inspect.aisi.org.uk/
- Official code repository: https://github.com/UKGovernmentBEIS/inspect_ai
- Inspect Evals announcement: https://www.aisi.gov.uk/blog/inspect-evals
- Inspect Evals catalogue: https://ukgovernmentbeis.github.io/inspect_evals/

The official documentation describes Inspect as a framework for frontier AI
evaluations across coding, agentic tasks, reasoning, knowledge, behavior, and
multi-modal understanding. Its core concepts include datasets, solvers/agents,
tools, scorers, logs, visualization, and sandboxed execution.

The 2026-06-22 recheck used primary sources only. No dependency was installed
and no model/API run was performed.

## 2. Relevance to LPE-Bench

Inspect AI is relevant to LPE-Bench because LPE-Bench needs exactly the kind of
structured evaluation harness that Inspect provides:

- dataset-like task samples;
- solver or agent execution;
- deterministic or model-graded scoring;
- multi-turn and tool-using agent support;
- inspectable logs and analysis outputs;
- reusable benchmark packaging.

For Etisiobi, the strongest bounded port is:

```text
LPE task sample -> Inspect dataset row
agent/model attempt -> Inspect solver output
layer-preservation judgment -> Inspect scorer
manual prompt batch -> negative control
run logs -> reproducibility trace
```

## 3. What Inspect AI does not prove

Inspect AI does not prove:

- that LPE-Bench is novel;
- that LPE-Bench is valid;
- that the Nwagu transfer atlas has verified prior art;
- that any model has or lacks layer-promotion behavior;
- that Etisiobi has a paper candidate;
- that any result is submission-ready.

It only verifies that a credible, public, actively used evaluation framework
exists and can plausibly host a bounded LPE-Bench port.

## 4. Allowed bounded port

Allowed next implementation plan:

1. Select a tiny LPE seed set from existing non-sensitive fixture records.
2. Encode each task with explicit evidence-layer labels:
   `source_observed`, `derived`, `speculative`, `forbidden_promotion`.
3. Implement an Inspect-style task definition or adapter spec.
4. Score whether the model preserves the layer boundary in its answer.
5. Compare against the manual prompt batch negative control.
6. Record every input, output, score, and decision trace.

Disallowed:

- installing dependencies during the continuous automation unless explicitly
  approved;
- downloading private data;
- using private model outputs as public evidence;
- claiming benchmark validity before a bounded run exists.

## 5. Atlas citation/source status

Recommended atlas update:

```yaml
prior_art_status: verified_primary_source_relevance_not_novelty_clearance
verified_sources:
  - https://inspect.aisi.org.uk/
  - https://github.com/UKGovernmentBEIS/inspect_ai
  - https://www.aisi.gov.uk/blog/inspect-evals
claim_ceiling: eval harness relevance only
bounded_plan: experiments/EXP-FRONTIER-007-inspect-ai-lpe-port/
next_gate: explicit_dependency_and_model_run_approval
```

## 6. Bounded Experiment Plan

The bounded no-install plan is now present at
`experiments/EXP-FRONTIER-007-inspect-ai-lpe-port/`.

It contains:

- ten non-sensitive Inspect-style LPE seed cases;
- a manual prompt negative control;
- an adapter contract for dataset, solver output, scorer, metadata, and logs;
- a manifest that blocks dependency installation, model/API access, private
  data, and unreviewed gold-label claims.

## Decision

Keep `ATLAS-0049` as the lead path for `GOAL-FRONTIER-001`.

The reason is pragmatic: Inspect AI gives the lab an externally legible
evaluation frame without requiring private data, publication PDF generation, or
premature article claims. The next useful artifact is an explicitly approved
execution run, not stronger prose.
