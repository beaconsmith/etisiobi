# DH-001 Toy Baseline Cycle

Date: 2026-07-04

## Selected Experiment

- Hypothesis: `DH-001: Derived 27 x 8 Completion`
- Experiment: `EXP-DH-001-derived-completion-baseline`
- Lane: Formalization -> Experimental
- Status: `BASELINE_TESTED_INTERNAL_TOY`

## What Ran

Command:

```powershell
python experiments\EXP-DH-001-derived-completion-baseline\run_toy_baseline.py
```

The runner generated `experiments/EXP-DH-001-derived-completion-baseline/results.json`.

## Result

The constructed role-recovery task compared:

- `source_26x8_collapsed`
- `derived_27x8_role_split`
- `shuffled_completion`

Observed toy metrics:

- `derived_27x8_role_split`: role recovery accuracy `1.0`
- `source_26x8_collapsed`: role recovery accuracy `0.0`
- `shuffled_completion`: role recovery accuracy `0.0`

## Claim Boundary

This is a toy formalization result only. It does not prove that the Nwagụ Aneke
source layer contains 27 rows, does not establish 216 source-observed records,
does not produce a paper candidate, and does not support public release.

The source-observed foundation remains:

```text
26 rows x 8 vowel/modifier columns = 208 records
```

The derived completion remains a modern formal hypothesis:

```text
27 rows x 8 modifier slots = 216 derived formal slots
```

## Blockers

- No non-toy source-transcription constraints yet.
- No counterexample set yet.
- No article-specific prior-art sweep.
- No review-team trace for any DH-001 paper branch.
- No rights or authority clearance for public claims.

## Validation Target

After this report, rerun:

```powershell
python scripts\build_retrieval_manifest.py
python scripts\validate_lab_standard.py
python scripts\validate_review_team_gate.py
python scripts\validate_continuous_research_loop.py
```

## Exact Next Action

Add a DH-001 counterexample set and non-toy source-transcription constraint file,
then rerun the toy baseline and validators. Park DH-001 if the derived split
does not survive those counterexamples without using source-observed 27 x 8
language.

## Automation

The app did not have an active automation for the old
`etisiobi-continuous-research-loop` id, so a replacement autonomous loop was
created as `etisiobi-continuous-research-loop-2`.

The loop prompt points at the exact next action above and preserves the same
submission, secrets, dependency, PDF, and readiness restrictions.
