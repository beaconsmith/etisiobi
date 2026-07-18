# DH-001: Derived 27 x 8 Completion

id: DH-001
title: Derived 27 x 8 Completion
lane: Formalization -> Experimental
source inputs: Nwagụ Aneke source-observed layer recorded by the current lab as 26 rows x 8 vowel/modifier columns = 208 records.
invented/derived step: Split the ambiguous f/v row into two formal roles for a derived completion model, yielding a 27 x 8 construction only inside the derived hypothesis lane.
formal object: A role-indexed matrix model with one source-observed 26-row view and one derived 27-row view. The source view preserves the observed count; the derived view introduces two role labels where the source view keeps one collapsed row.
research question: Does the derived role split improve any measurable formal task over the source-observed collapsed view and trivial completion baselines?
hypothesis: The derived f/v split improves role-recovery consistency in a toy role-labeled benchmark while preserving the source/derived boundary.
baseline: Source-observed 26 x 8 collapsed view; deterministic shuffled f/v completion.
test: Run `experiments/EXP-DH-001-derived-completion-baseline/run_toy_baseline.py` against the bounded toy cases and compare role-recovery accuracy, collision count, and source-claim safety.
kill condition: Park the hypothesis if the derived split does not beat the collapsed and shuffled baselines on role recovery, or if any useful result requires saying that 27 rows are source-observed.
allowed wording: "The 27 x 8 completion is a derived formal hypothesis that can be tested against baselines."
forbidden wording: "The source shows 27 rows", "216 records are source-observed", "PAGC proves universal compression", "DH-001 is paper-ready."
stage: PARKED_BY_GLOBAL_BENCHMARK_GATE
next action: Leave DH-001 parked unless a future source or corpus-usage event supplies non-label evidence for the f/v split.

## Decision

DH-001 is parked as an internally useful, source-safe toy formalization. It is
not a source claim, not a historical claim, not a linguistic result, and not a
paper candidate.

The current experiment asks only whether a derived role split can solve a task
that a collapsed source-row view cannot solve by construction. That is useful as
a sanity check for the formal lane, but it does not establish external novelty
or cultural authority.

The adversarial screen now adds the important negative finding: when role labels
are masked or when only the reviewed source record is available, DH-001 has not
yet demonstrated value beyond the f/v labels. This is a real milestone because
it prevents the branch from mistaking label consistency for discovery.

The 2026-07-06 source-feature screen adds the smallest non-label task: printed
row count, combined f/v row status, absence of standalone vowels, absence of
tone marking, and matrix-as-representation status. These features preserve the
source transcription but provide zero positive support for the derived f/v
split. The branch should therefore be parked as formally safe but scientifically
label-dependent.

The global benchmark gate makes the park decision explicit. DH-001 passes
reproducibility, documented data, baseline, adversarial, transparent-metric, and
source-boundary criteria, but fails non-label generalization.

## Evidence Packet

- Experiment: `experiments/EXP-DH-001-derived-completion-baseline/`
- Dataset: `experiments/EXP-DH-001-derived-completion-baseline/data/toy_completion_cases.csv`
- Counterexamples: `experiments/EXP-DH-001-derived-completion-baseline/data/counterexample_cases.csv`
- Source constraints: `experiments/EXP-DH-001-derived-completion-baseline/data/source_transcription_constraints.csv`
- Source records: `experiments/EXP-DH-001-derived-completion-baseline/data/source_record_cases.csv`
- Adversarial variants: `experiments/EXP-DH-001-derived-completion-baseline/data/adversarial_variants.csv`
- Source-feature task: `experiments/EXP-DH-001-derived-completion-baseline/data/source_feature_task_cases.csv`
- Global benchmark criteria: `experiments/EXP-DH-001-derived-completion-baseline/data/global_benchmark_criteria.csv`
- Global benchmark gate: `experiments/EXP-DH-001-derived-completion-baseline/run_global_benchmark_gate.py`
- Global gate results: `experiments/EXP-DH-001-derived-completion-baseline/global_benchmark_gate_results.json`
- Test: `experiments/EXP-DH-001-derived-completion-baseline/test_toy_baseline.py`
- Global gate test: `experiments/EXP-DH-001-derived-completion-baseline/test_global_benchmark_gate.py`
- Runner: `experiments/EXP-DH-001-derived-completion-baseline/run_toy_baseline.py`
- Results: `experiments/EXP-DH-001-derived-completion-baseline/results.json`
- Decision: `experiments/EXP-DH-001-derived-completion-baseline/decision.md`

## Claim Ceiling

Strongest allowed claim:

```text
DH-001 has a bounded toy baseline result showing that an explicitly derived f/v
role split can improve role recovery in a constructed formal task, reject a
small set of unsafe source-promotion counterexamples, preserve reviewed
source-record cases, and pass a five-case source-feature screen that finds no
positive non-label support for the split, while keeping the source-observed
layer fixed at 26 x 8 = 208. Its current positive result remains
label-dependent.
```

Global benchmark decision:

```text
GLOBAL_BENCHMARK_NEGATIVE_BREAKTHROUGH_PARK_DH001
```

This is a negative breakthrough: the lab has enough benchmark evidence to stop
promoting DH-001 and keep it parked until new non-label evidence exists.

Disallowed claim:

```text
The experiment proves that the Nwagụ Aneke source layer has 27 rows or 216
source-observed records.
```
