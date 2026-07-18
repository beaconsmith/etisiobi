---
type: repository_boundary_review
experiment_id: EXP-FRONTIER-012
atlas_id: ATLAS-0043
status: REPOSITORY_BOUNDARY_REVIEW_OPEN_NOT_APPROVED
claim_ceiling: repository_boundary_review_not_public_release
---

# Repository-Boundary Review

## Decision

This packet opens a repository-boundary review for future public software
provenance around `ATLAS-0043` Software Heritage. It does not create an export,
release package, archive request, or archive identifier.

The current inventory is candidate internal review only. It separates repo
assets that might someday become a public software-provenance package from
excluded repository paths that must stay out of any package unless a later
human review and approval record changes their status.

Current claim ceiling: `repository_boundary_review_not_public_release`.

## Review Scope

The review asks a narrow question: which scripts, validators, manifests, status
surfaces, and non-sensitive metadata are even eligible for future release or
archival consideration?

It does not answer whether release should happen. It does not answer whether
Software Heritage should be contacted. It does not approve any branch, dataset,
paper, or product-facing claim.

## Excluded Repository Paths

The exclusion table blocks raw source material, primary-source folders,
publication PDFs, image files, private data, contact records, secrets, and
human-reader response data from the candidate package. The table is deliberately
conservative because a public software package must not smuggle source,
authority, or privacy decisions through infrastructure work.

## Required Reviews

The review cannot become a release or archive decision until these roles answer
their questions:

- repository boundary reviewer;
- rights authority reviewer;
- source dossier reviewer;
- preservation infrastructure reviewer;
- data protection reviewer.

## No Archive Action

This packet records no archive action. It records no dependency installation,
private data download, repository export, Software Heritage request, archive
identifier claim, repository deposit, public release claim, or public package
approval.

## What This Teaches Oroma

For Oroma, this turns infrastructure ambition into visible boundary discipline:
a system can become externally legible without quietly converting internal
records into public artifacts. Provenance should make governance clearer, not
override authority, consent, privacy, or source-layer uncertainty.

## Exact Next Action

Assign repository-boundary reviewers and adjudicate the candidate and excluded
path inventory before any export, archive request, or public release.
