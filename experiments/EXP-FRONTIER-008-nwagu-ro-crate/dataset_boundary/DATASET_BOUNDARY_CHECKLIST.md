---
type: dataset_boundary_checklist
boundary_id: BOUNDARY-EXP-FRONTIER-008-001
experiment_id: EXP-FRONTIER-008
status: checklist_ready_for_review_not_approved
created: "2026-06-22"
claim_ceiling: dataset_boundary_checklist_not_dataset_release
---

# Dataset Boundary Checklist

## Purpose

This checklist defines the review boundary for a possible future versioned
metadata package derived from `EXP-FRONTIER-008`.

It is not a DataLad dataset, Software Heritage request, public deposit,
publication package, rights decision, authority decision, or release approval.
There is no external submission from this packet.

## Candidate Files

Candidate files are listed in `candidate_files.csv`.

Current candidate rule:

```text
non-sensitive metadata and validators only
```

Candidate files may include claim-layer fixtures, interface maps, usability
protocol indexes, Inspect execution metadata, preservation decisions, boundary
records, and validators. They may not include raw sources, source images, glyph
reproductions, restricted manuscript material, private data, or identifiable
human-reader responses.

## Excluded Files

Excluded files are listed in `excluded_files.csv`.

The exclusion list is intentionally broader than the current crate. It blocks
classes of material that would make a versioned package look more mature than
its evidence and rights status.

## Reviewer Roles

Reviewer roles are listed in `reviewer_roles.csv`.

Every role is currently marked `not_reviewed`. No role may approve a current
public release from this checklist alone. The checklist only prepares a review
surface.

## Validator Behavior

Validator controls are listed in `validator_controls.json`.

The validator must reject candidate records that include source paths, image
formats, glyph reproduction folders, restricted-material markers, private-data
markers, or human-reader response folders. It must also require candidate,
excluded, reviewer, and control records before the boundary can pass.

## Promotion Rule

Strongest allowed claim:

`dataset_boundary_checklist_not_dataset_release`

Promotion beyond this status requires rights review, authority review, dataset
boundary approval, public release approval, and a restricted-material exclusion
audit.

## Exact Next Action

Run the checklist through human review roles. If the roles approve the boundary,
create a separate approval record before any DataLad conversion, Software
Heritage request, public deposit, or archive identifier work.
