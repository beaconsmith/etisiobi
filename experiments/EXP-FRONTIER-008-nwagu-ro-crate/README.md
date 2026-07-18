---
type: experiment_index
experiment_id: EXP-FRONTIER-008
atlas_id: ATLAS-0039
status: DETACHED_METADATA_PACKAGE_INTERNAL_NOT_RELEASED
created: "2026-06-22"
claim_ceiling: packaging_not_clearance
---

# EXP-FRONTIER-008 Nwagu Frontier RO-Crate

This package describes a rights-safe, non-sensitive subset of the Nwagu frontier
lab using RO-Crate-style JSON-LD metadata. It is a detached metadata package:
it records file identities, checksums, roles, and blockers without copying raw
sources or restricted material into a new tree.

## What It Includes

- claim-layer fixtures and interface map;
- count-layer view outline and usability index;
- Inspect-style LPE port manifest and pending execution decision;
- preservation decision and dataset-boundary checklist;
- validators that protect claim-layer and execution-gate behavior.

## What It Excludes

- source PDFs;
- source images;
- glyph reproductions;
- restricted manuscript material;
- private data;
- human-reader results not yet collected.

## Claim Ceiling

`packaging_not_clearance`

The crate improves reproducibility and external legibility. It does not clear
rights, authority, source claims, model claims, article status, or public
release.

## Preservation Decision

The current preservation route is recorded in
`preservation_decision/PRESERVATION_DECISION.md`.

Decision: keep the package repo-local and internal for now. DataLad and
Software Heritage remain relevant later paths, but both are deferred until
dataset-boundary, release, rights, and authority gates mature.

## Dataset Boundary

The candidate/excluded-file boundary for any future versioned package is
recorded in `dataset_boundary/DATASET_BOUNDARY_CHECKLIST.md`.

Status: checklist ready for review, not approved. It lists candidate metadata
files, excluded source/private material classes, reviewer roles, and validator
behavior.

The pending review gate is recorded in
`dataset_boundary/review_gate/REVIEW_GATE.md`. It has one pending request per
required role and cannot be used as approval.

The review intake runbook is recorded in
`dataset_boundary/review_gate/intake/REVIEW_INTAKE_RUNBOOK.md`. It contains the
role-specific forms and submission schema for collecting real human review
rows.

The dispatch runbook is recorded in
`dataset_boundary/review_gate/intake/dispatch/DISPATCH_RUNBOOK.md`. It contains
unsent invitation templates and a tracker with missing reviewer contacts.

The contact approval runbook is recorded in
`dataset_boundary/review_gate/intake/dispatch/contact_approval/CONTACT_APPROVAL_RUNBOOK.md`.
It defines reviewer selection criteria, blank contact-intake rows, and a
send-approval template. It also requires no private contact data in the repo.

## Exact Next Action

Fill in reviewer identities and safe contact-handling details, obtain explicit
approval to send each invitation, then dispatch the five role-specific review
requests and collect schema-valid real human review rows.
