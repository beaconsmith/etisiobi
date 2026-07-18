# Target Journal Compliance Matrix

Article: `ARTICLE-NA-005`

Candidate target venue: `ACM Journal on Computing and Cultural Heritage`

Status: `COMPLIANCE_MATRIX_COMPLETE_HUMAN_SIGNOFF_BLOCKED`

Checked against official ACM pages on 2026-07-06:

- https://dl.acm.org/journal/jocch
- https://dl.acm.org/journal/jocch/author-guidelines
- https://dl.acm.org/journal/jocch/policies

| Requirement area | Current status | Evidence | Remaining human sign-off |
|---|---|---|---|
| Venue scope | `PLAUSIBLE_FIT` | Cultural-heritage computing standards bridge for TEI, Web Annotation, and future IIIF selectors. | Author approves ACM JOCCH as target. |
| Originality | `INTERNAL_CHECK_PASS` | Repo-local 10-record selector-layer sample and article-local reviews. | Author confirms not submitted elsewhere. |
| Technical evidence | `PASS_FOR_SUBMISSION_REVIEW` | 10 annotation records, 10 TEI glyph declarations, 0 pixel-coordinate records, explicit missing-coordinate boundary. | Human author accepts partial selector-layer scope. |
| Field positioning | `PASS_FOR_SUBMISSION_REVIEW` | `selector_bridge_comparison.md` separates selector bridge from completed critical edition, public image release, and Unicode proposal. | Human source/domain reviewer approves public framing. |
| Source boundary | `TEXT_ONLY_BOUNDARY_DEFINED` | Human source review file keeps record-level and coordinate review open. | Human source review record. |
| Third-party material | `NO_REPRODUCTION_CURRENTLY_PLANNED` | No source images, glyph crops, or public IIIF canvases are required. | Rights/authority reviewer approves exact package. |
| Authorship | `MISSING_EXTERNAL_DECISION` | No external author list or contributor roles recorded. | Author/contributor approval. |
| Licence/open access/APC | `MISSING_EXTERNAL_DECISION` | ACM publication route must be selected by human author/submitter. | Licence/funding/waiver decision. |
| Conflict/AI disclosure | `MISSING_EXTERNAL_DECISION` | Repo records agent-assisted drafting and validation. | Human disclosure wording approval. |

## Decision

The remaining blockers are human author, source-review, rights/authority,
disclosure, licence/funding, and final package approval. The selector-bridge
positioning blocker has been reduced to human source and venue sign-off.
