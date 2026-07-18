# DH-001 Counterexample Screen Cycle

Date: 2026-07-04

## Selected Experiment

- Hypothesis: `DH-001: Derived 27 x 8 Completion`
- Experiment: `EXP-DH-001-derived-completion-baseline`
- Lane: Formalization -> Experimental
- Status: `BASELINE_TESTED_INTERNAL_TOY_WITH_COUNTEREXAMPLE_SCREEN`

## What Changed

Added:

- `data/counterexample_cases.csv`
- `data/source_transcription_constraints.csv`
- `source_transcription_constraints.md`
- `test_toy_baseline.py`

Updated the runner so source-promotion safety is scored separately from role
recovery.

## TDD Trace

Red:

```powershell
python experiments\EXP-DH-001-derived-completion-baseline\test_toy_baseline.py
```

Failed because the runner still reported `PASS_INTERNAL_TOY_BASELINE` and did
not include counterexample or source-constraint scoring.

Green:

```powershell
python experiments\EXP-DH-001-derived-completion-baseline\test_toy_baseline.py
```

Passed after the runner included counterexample and source-constraint scoring.

## Result

The derived model:

- retained toy role recovery accuracy `1.0`;
- rejected all three unsafe source-promotion counterexamples;
- preserved the safe derived statement;
- recorded zero source-constraint violations.

The source-observed foundation remains:

```text
26 rows x 8 vowel/modifier columns = 208 records
```

The derived completion remains:

```text
27 rows x 8 modifier slots = 216 derived formal slots
```

## Blockers

- The counterexample set is still small and constructed.
- The source-transcription constraints are derived from current repo notes, not
  a new source review.
- There is no source-review trace, rights review, prior-art sweep, or paper
  candidate decision for DH-001.

## Exact Next Action

Add non-toy source-transcription cases from reviewed source records and
adversarial variants that challenge whether the f/v split adds value beyond
labels, then rerun the baseline, test, retrieval manifest, and lab validators.
