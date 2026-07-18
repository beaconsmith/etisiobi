---
type: preservation_decision
decision_id: PRESERVE-EXP-FRONTIER-008-001
experiment_id: EXP-FRONTIER-008
status: repo_local_internal_now
created: "2026-06-22"
claim_ceiling: preservation_route_decision_not_release
---

# Preservation Decision

## Decision

Keep the `EXP-FRONTIER-008` metadata package repo-local for now.

This is a preservation-route decision, not a release, deposit, clearance,
identifier, dataset conversion, or publication claim. The current package stays
an internal metadata package until the lab has completed rights review,
authority review, public release approval, source-image exclusion,
private-data exclusion, and dataset boundary review.

Current allowed actions are validation, checksum maintenance, and decision
trace updates. Current disallowed actions are DataLad conversion, Software
Heritage save requests, public deposit, restricted-source inclusion, and any
external submission. There is also no dependency installation in this cycle.

## Source Observations

DataLad is relevant because its official materials describe a system built on
Git and git-annex for version controlling datasets, tracking changes, capturing
provenance, and supporting reproducibility. That maps well to a future
versioned hypothesis/dataset boundary, but not to this package before the
boundary is stable.

Software Heritage is relevant because its official materials describe source
code archiving, Save Code Now, and persistent identifiers for objects present
in the Software Heritage archive. That maps well to future public source-code
preservation, but not to an internal metadata package with unresolved release
approval.

Primary sources checked:

- https://www.datalad.org/
- https://handbook.datalad.org/en/latest/book_main.html
- https://www.softwareheritage.org/
- https://docs.softwareheritage.org/devel/swh-model/persistent-identifiers.html

## Route Decisions

| Route | Current decision | Reason |
|---|---|---|
| Repo-local internal metadata package | selected now | Matches the current rights-safe package and avoids external action. |
| DataLad versioned dataset | defer until dataset boundary review | Useful later if the package becomes a versioned dataset or nested data product. |
| Software Heritage archive identifier | defer until public release or archive approval | Useful later for public code provenance, not for current internal metadata. |

## Claim Boundary

Strongest allowed claim:

`preservation_route_decision_not_release`

This packet may say the lab has selected a conservative preservation route for
now. It must not imply rights approval, authority approval, public release,
archive deposit, benchmark maturity, article maturity, or source-data
clearance.

## Exact Next Action

Define a dataset boundary review checklist for `EXP-FRONTIER-008`: what files
would enter a future versioned package, what files stay excluded, who approves
the boundary, and which validator blocks accidental inclusion of source images,
restricted manuscript material, or private data.
