---
type: software_heritage_no_archive_identifier_decision
experiment_id: EXP-FRONTIER-011
atlas_id: ATLAS-0043
status: SOFTWARE_HERITAGE_NO_IDENTIFIER_DECISION_READY_NOT_EXECUTED
claim_ceiling: software_provenance_planning_not_archive_action
---

# Software Heritage No-Archive-Identifier Decision

## Decision

This is a no-archive-identifier decision for `ATLAS-0043` Software Heritage.

Software Heritage remains relevant to Etisiobi because its official materials
describe a universal source-code archive, source-code preservation, reference
workflows for research software, and persistent identifiers for objects present
in the archive. Those properties fit a future public software-provenance branch
for Nwagu Aneke research scripts and metadata.

The current decision is to defer all archive action. The current package remains
repo-local and internal. This cycle performed no Software Heritage request, no archive identifier claim, no repository deposit, no private data download, no
external submission, no dependency installation, and no public release claim.

## Source Observations

Primary sources checked:

- https://www.softwareheritage.org/
- https://docs.softwareheritage.org/devel/swh-model/persistent-identifiers.html
- https://www.softwareheritage.org/how-to-archive-reference-code/

Observed relevance:

- Software Heritage positions itself as a universal source-code archive.
- The site describes a workflow for triggering archiving of source-code
  repositories and for referencing research software.
- The SWHID documentation defines stable identifiers for objects already
  present in the Software Heritage archive.

Interpretation:

Software Heritage is a strong future route for software provenance, but Etisiobi
has not yet satisfied public release approval, repository boundary review,
rights review, authority review, restricted-material exclusion, license/citation
metadata review, or explicit archive approval. Therefore the strongest allowed
claim is `software_provenance_planning_not_archive_action`.

## Archive Gates

No Software Heritage archive action may occur until all of the following are
satisfied:

- public release approval;
- repository boundary review;
- rights review;
- authority review;
- restricted-material exclusion audit;
- license and citation metadata review;
- human preservation-infrastructure review;
- explicit user/lab archive approval.

## What This Teaches Oroma

For Oroma, this decision keeps software provenance subordinate to community
authority and release boundaries. A system can plan for durable references
without implying that internal code, metadata, or culturally governed research
material is ready to be deposited, cited, or externally synchronized.

## Exact Next Action

Open the provenance branch into repository-boundary review: define which
scripts, manifests, and metadata could become a future public software package,
while keeping all archive actions deferred.
