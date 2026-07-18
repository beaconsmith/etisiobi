# Next Experiment: EXP-FRONTIER-005

The next benchmark step is not another manuscript draft. It is independent
annotation plus real agent evaluation.

## Blocking Question

Does LPE-Bench detect a real failure mode in AI research agents, or only a
heuristic artifact of Etisiobi's current labels?

## Immediate Work

1. Freeze `annotation_queue.csv`.
2. Collect three independent annotation passes.
3. Adjudicate labels into `gold_labels.csv`.
4. Run at least three research-agent conditions.
5. Score LPE rates and confidence intervals.
6. Update `VALIDATION.md`.

## Paper Trigger

Only after EXP-FRONTIER-005 has real labels and real agent runs should Etisiobi
draft the paper:

```text
Layer Promotion Error: Measuring Source/Derived Claim Drift in AI Research Agents
```

Until then, LPE-Bench remains `PUBLIC_INSTRUMENT_DRAFT_NOT_FRONTIER_PROOF`.

