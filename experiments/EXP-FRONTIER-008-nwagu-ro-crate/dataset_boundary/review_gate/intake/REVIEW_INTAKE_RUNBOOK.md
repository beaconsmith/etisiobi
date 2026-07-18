---
type: dataset_boundary_review_intake
intake_id: BOUNDARY-REVIEW-INTAKE-EXP-FRONTIER-008-001
gate_id: BOUNDARY-REVIEW-GATE-EXP-FRONTIER-008-001
status: intake_ready_no_reviews_collected
created: "2026-06-22"
claim_ceiling: review_intake_ready_not_human_review
---

# Review Intake Runbook

## Purpose

This review intake packet turns the pending dataset-boundary review gate into a
usable review collection process. It provides one role-specific form per
required reviewer and a schema for future real human review rows.

Status: no real human review rows collected yet.

Agent may not approve the boundary. Agent-generated forms, templates, or
summaries are not review evidence and are not approval.

## Review Packet

Each reviewer should inspect:

- `../../DATASET_BOUNDARY_CHECKLIST.md`
- `../../candidate_files.csv`
- `../../excluded_files.csv`
- `../../reviewer_roles.csv`
- `../../validator_controls.json`
- `../REVIEW_GATE.md`
- `../review_requests.csv`

## Role-Specific Form

Use the matching role-specific form in `role_forms/`. Each form requires one of
`PASS`, `REJECT`, or `REVISE`, a summary, reviewed files, blocking issues, and
an attestation.

## Submission Schema

Future review rows must conform to `review_submission_schema.json`.

The schema records real human review rows. It does not make any single review
row a final boundary approval. A separate decision record is still required.

## Collected Reviews

Future review rows should be stored under `collected_reviews/` as JSONL only
after real reviewer input exists. Do not add agent-generated approvals.

## Claim Ceiling

`review_intake_ready_not_human_review`

This packet says review intake is ready. It does not say review happened.

## Exact Next Action

Send the five role-specific forms to the corresponding reviewers and collect
real human review rows that conform to `review_submission_schema.json`.
