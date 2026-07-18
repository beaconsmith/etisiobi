---
type: dataset_boundary_review_gate
gate_id: BOUNDARY-REVIEW-GATE-EXP-FRONTIER-008-001
boundary_id: BOUNDARY-EXP-FRONTIER-008-001
experiment_id: EXP-FRONTIER-008
status: pending_human_review
created: "2026-06-22"
claim_ceiling: review_gate_pending_not_boundary_approval
---

# Dataset Boundary Review Gate

## Purpose

This review gate prepares the `EXP-FRONTIER-008` dataset boundary for human
review. It is not an approval record, release record, DataLad conversion,
Software Heritage request, public deposit, or archive action.

Status: pending human review.

Agent may not approve the boundary. A future approval or rejection requires
human review rows from every required role and a separate decision record.

## Review Packet

Reviewers should inspect:

- `../DATASET_BOUNDARY_CHECKLIST.md`
- `../candidate_files.csv`
- `../excluded_files.csv`
- `../reviewer_roles.csv`
- `../validator_controls.json`

Gate operators should use:

- `review_trace_template.jsonl` as the review trace template;
- `decision_record_template.json` as the decision record template.
- `intake/REVIEW_INTAKE_RUNBOOK.md` as the review intake runbook for sending
  role-specific forms.

## Required Roles

- `rights_authority_reviewer`
- `community_authority_reviewer`
- `source_dossier_reviewer`
- `preservation_infrastructure_reviewer`
- `data_protection_reviewer`

## Required Output

Each reviewer must return one of:

- `PASS`
- `REJECT`
- `REVISE`

Every non-`PASS` review must include blockers. A final decision record must not
be created from this template unless every required role has a real human row.

## Current Claim Boundary

`review_gate_pending_not_boundary_approval`

The gate says the review process is ready to use. It does not say the dataset
boundary is approved.

## Exact Next Action

Collect real review rows from all five required roles, then create a separate
decision record marked `PASS`, `REJECT`, or `REVISE`.
