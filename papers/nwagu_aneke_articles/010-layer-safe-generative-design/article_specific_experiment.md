# Article-Specific Experiment

Article: `ARTICLE-NA-010`

Experiment: `EXP-NA-010-layer-safety-tests`

Status: `EXPANDED_SYNTHETIC_TEST_SET_WITH_BASELINE_COMPARISON`

## Research Question

Can a generative design pipeline over artifact-derived claims enforce a
non-promotion invariant so that generated outputs never assert a stronger
evidence layer than their inputs license?

## Hypothesis

If source-observed, derived, speculative, and blocked labels are treated as
ordered claim types, then a gate that rejects stronger output labels can detect
unsafe promotion errors while preserving safe source and derived claims.

## Method

The experiment defines a layer order and tests an expanded set of 24 claim
transformations:

- safe preservation cases;
- safe weakening or withholding cases;
- abstract, title, contribution, and figure-caption promotion probes;
- source/rights blocker probes;
- citation-only and provenance-only false-negative probes.

The publication gate rejects any transformation where an output claim is labeled
as stronger than the input evidence permits.

## Evidence Files

- `experiments/EXP-NA-010-layer-safety-tests/results.json`
- `experiments/EXP-NA-010-layer-safety-tests/expanded_results.json`
- `experiments/EXP-NA-010-layer-safety-tests/baseline_comparison.json`
- `experiments/EXP-NA-010-layer-safety-tests/analysis.md`
- `experiments/EXP-NA-010-layer-safety-tests/decision.md`
- `experiments/EXP-NA-010-layer-safety-tests/layer_non_promotion_lemma.md`
- `experiments/EXP-NA-010-layer-safety-tests/data/layer_safety_cases.csv`
- `experiments/EXP-NA-010-layer-safety-tests/data/layer_safety_cases.jsonl`
- `experiments/EXP-NA-010-layer-safety-tests/data/expanded_layer_safety_cases.csv`
- `experiments/EXP-NA-010-layer-safety-tests/data/expanded_layer_safety_cases.jsonl`
- `experiments/EXP-NA-010-transfer-counterexample-audit/results.json`
- `experiments/EXP-NA-010-transfer-counterexample-audit/analysis.md`
- `experiments/EXP-NA-010-transfer-counterexample-audit/data/transfer_cases.csv`

## Result

The gate detected all 14 intentional promotion errors in the expanded synthetic
test set:

- test cases: 24;
- promotion errors detected: 14;
- promotion-error detection rate on this test set: 1.0;
- provenance-only false negatives on promotion errors: 11;
- citation-only false negatives on promotion errors: 7;
- no-label gate false negatives on promotion errors: 14;
- decision: `EXPANDED_LAYER_SAFETY_BASELINE_COMPARISON_PASS`.

## What This Result Allows

The article can claim that a non-promotion invariant is executable over the
current Nwagu Aneke claim labels and can reject unsafe transformations from
derived, speculative, or blocked claims into stronger evidence layers. It may
also report that provenance-only, citation-only, and no-label baselines miss
promotion errors in this controlled case matrix.

## What This Result Does Not Allow

The experiment does not prove:

- that the invariant is complete for all cultural-heritage AI systems;
- that all Nwagu Aneke source claims are reviewed;
- that public release is authorized;
- that the invariant improves downstream model performance;
- that universal compression, E6, or exact-27 theory claims are valid.

## Remaining Blockers

1. Attach human source and rights review for external publication.
2. Add adversarial journal review of test adequacy and novelty.
3. Extend beyond the current synthetic case matrix if a target venue requires
   multiple source corpora or live model outputs.

## 2026-07-07 Cycle Addendum

Added `EXP-NA-010-transfer-counterexample-audit`, a ten-case transfer and
counterexample audit spanning Nwagu count-layer claims, digital-edition
normalization, annotation-region claims, Unicode-process claims,
cultural-heritage ML readings, and rights/authority blockers. The layer gate
rejected all six intentional cross-domain promotion errors and allowed four
layer-preserving cases. This supports a public preprint/methods-note shape, but
not a public journal-manuscript candidate claim.
