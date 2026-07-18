# DH-003 Full Label Quality Gate

Date: 2026-07-06

## Status

`FULL_LABEL_QUALITY_GATE_COMPLETE_INTERNAL_NOT_SUBMISSION_READY`

## Selected Experiment

`experiments/EXP-FRONTIER-017-lpe-label-quality-gate`

## Result

- Full label rows routed: `360`
- Review-ready internal rows: `290`
- Needs adjudication rows: `28`
- Public-release-blocked rows: `42`
- Human/domain review packet rows: `70`
- Compared scored agent conditions: `8`
- Best overall local condition: `C0_no_layer_labels`
- Best overall local F1: `0.7692`

## Claim Ceiling

This is a full internal quality-routing result for label evidence. It is not a
paper result, public benchmark, public-release clearance, rights clearance,
source-authority approval, or journal-submission decision.

## What Changed

The old blocker "expand the 24-case pilot to the full label table" is now
resolved locally. The new blocker is independent human/domain review of the
70 unresolved rows before the label set can support a paper-candidate decision.

## Exact Next Action

Route `human_domain_review_packet.csv` through independent human/domain review,
then compare those decisions against scored agent conditions before any
paper-candidate or journal-submission decision.
