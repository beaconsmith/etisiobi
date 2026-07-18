---
type: safe_role_assignment_recorder
experiment_id: EXP-FRONTIER-014
atlas_id: ATLAS-0043
status: SAFE_ROLE_ASSIGNMENT_RECORDER_READY_NO_ASSIGNMENTS_RECORDED
claim_ceiling: safe_role_assignment_recorder_not_assignment_completion
---

# Safe Role-Assignment Recorder

## Decision

This packet creates a safe role-assignment recorder for the `ATLAS-0043`
repository-boundary review. It defines the format for future approved role
records without storing real reviewer identities, private contact data,
invitations, reviews, or adjudication outcomes.

Current claim ceiling: `safe_role_assignment_recorder_not_assignment_completion`.

## Current State

No assignments recorded. No reviewer identities recorded. No private contact data.
The assignment log remains empty until human selections and approval records
exist outside the repo.

## Recording Rule

Future assignment rows must use pseudonymous reviewer references, role labels,
selection basis, and approval-record references. They must not include real
names, contact details, review text, invitation status, release decisions, or
archive decisions.

## Pseudonymous Reviewer References

Use stable pseudonymous reviewer references such as `RB-REVIEWER-001`, paired
with an external approval-record reference. The external approval record may
remain outside the repository if it contains private or identifying details.

## What This Teaches Oroma

For Oroma, this creates a clean separation between governance evidence and
personal data. A system can record that a role was approved without exposing
the person behind that role or turning assignment logistics into a public
release claim.

## Exact Next Action

When human selections exist outside the repo, add only non-private approved
role-assignment rows to `approved_role_assignments.jsonl` using pseudonymous
reviewer references.
