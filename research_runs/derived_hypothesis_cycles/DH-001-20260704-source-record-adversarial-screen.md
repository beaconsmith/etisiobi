# DH-001 Source-Record And Adversarial Screen

Date: 2026-07-04

## Milestone

DH-001 reached a decision-quality internal milestone:

```text
SOURCE_RECORD_SCREEN_PASS_ADVERSARIAL_VALUE_BLOCKED
```

This is worth celebrating inside the lab because the branch now does two things
at once:

1. It preserves reviewed source records and rejects unsafe source-promotion
   language.
2. It detects that the current positive role-recovery result is label-dependent
   and not yet a discovery-level result.

That is the lab behaving like a lab, not a PDF factory.

## Selected Experiment

- Hypothesis: `DH-001: Derived 27 x 8 Completion`
- Experiment: `EXP-DH-001-derived-completion-baseline`
- Lane: Formalization -> Experimental
- Status: `SOURCE_RECORD_SCREEN_PASS_ADVERSARIAL_VALUE_BLOCKED`

## Added Data

- `data/source_record_cases.csv`: eight reviewed source-record cases from the
  current chart transcription and source audit.
- `data/adversarial_variants.csv`: six variants that remove the role-label
  crutch or present only source-level evidence.

## Result

The derived model:

- retained toy role recovery accuracy `1.0`;
- rejected all three unsafe source-promotion counterexamples;
- preserved all eight source-record cases;
- rejected overclaiming on all six adversarial variants;
- recorded `value_beyond_label_evidence = not_demonstrated`;
- recorded `adversarial_value_status = BLOCKED_LABEL_ONLY`.

## Claim Boundary

The source-observed foundation remains:

```text
26 rows x 8 vowel/modifier columns = 208 records
```

The derived completion remains:

```text
27 rows x 8 modifier slots = 216 derived formal slots
```

The experiment does not prove historical 27 rows, 216 source records, universal
compression, external novelty, source authority, or paper readiness.

## Decision

Do not promote DH-001 toward a paper candidate. It is formally safe and useful
as a testbed for source/derived discipline, but its positive result is still
label-dependent.

## Exact Next Action

Design a non-label task with source-transcription features or park DH-001 as a
formally safe but scientifically label-dependent branch.
