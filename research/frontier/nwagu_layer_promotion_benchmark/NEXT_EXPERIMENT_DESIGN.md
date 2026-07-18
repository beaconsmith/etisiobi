# Next Experiment Design

## Status

`FRONTIER_BENCHMARK_SEEDED_NOT_PAPER_READY`

## Why The Current Result Is Not Enough

`EXP-FRONTIER-001` proved only that the lab can operationalize Layer Promotion
Error. `EXP-FRONTIER-002` improves this by expanding to 510 cases, adding
cross-program cases, external-prior-art controls, locked splits, hard cases, and
multiple baselines.

It still does not prove detector generalization because labels are heuristic and
not blind-reviewed. The strongest typed baselines use metadata fields that would
not always be available in a real claim-audit scenario. The important open
research problem is metadata-free or weak-metadata detection.

`EXP-FRONTIER-003` now provides a 360-case blind annotation queue and a synthetic
three-reviewer pilot. The pilot validates the annotation harness but does not
replace independent human/domain labels.

## Publication-Grade Experiment

Create `EXP-FRONTIER-004` with:

- blind annotation by at least three reviewers;
- inter-annotator agreement before adjudication;
- locked train/dev/test splits;
- baselines:
  - majority class;
  - rank-only;
  - lexical trigger;
  - SHACL/type-style constraints;
  - LLM zero-shot judge;
  - LLM with evidence-layer rubric;
  - hybrid detector;
- metadata-free evaluation;
- confidence intervals;
- false-positive and false-negative taxonomy;
- severity-weighted scoring.

Unlike `EXP-FRONTIER-002`, labels must be written independently of the detector
and frozen before model or rule tuning. Unlike the `EXP-FRONTIER-003` pilot,
labels must come from independent human/domain reviewers or separately run
agents whose instructions and outputs are archived outside the detector script.

## Minimum Metrics

- precision, recall, F1;
- balanced accuracy;
- Matthews correlation coefficient;
- confidence intervals;
- per-transition confusion matrix;
- inter-annotator agreement;
- performance by source type;
- robustness/paraphrase delta;
- severity-weighted recall for blocking errors.

## Frontier Gate

Do not call this frontier until the detector or protocol identifies
layer-promotion failures in real, previously unseen artifact-derived research
outputs, outperforms credible baselines, survives domain and rights review, and
changes what claims the lab or another project is allowed to publish.

## Harness Port Gate

`EXP-FRONTIER-007` now defines a no-install Inspect-style adapter plan for
LPE-Bench. It is useful only as an execution path:

- dataset sample shape;
- solver-output slot;
- scorer semantics;
- manual prompt negative control;
- log/provenance contract.

It does not replace blind annotation, human/domain review, or rights review. The
next step is explicit approval for dependency installation and model/API access
in a separate run.
