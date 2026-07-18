# Target Journal Compliance Matrix

Article: `ARTICLE-NA-010`

Candidate target venue: `ACM Journal on Computing and Cultural Heritage`

Status: `COMPLIANCE_MATRIX_COMPLETE_HUMAN_SIGNOFF_BLOCKED`

Checked against official ACM pages on 2026-07-06:

- https://dl.acm.org/journal/jocch
- https://dl.acm.org/journal/jocch/author-guidelines
- https://dl.acm.org/journal/jocch/policies

| Requirement area | Current status | Evidence | Remaining human sign-off |
|---|---|---|---|
| Venue scope | `PLAUSIBLE_FIT` | Cultural-heritage computing paper about evidence-layer preservation in artifact-derived generation. | Author approves JOCCH as target. |
| Originality | `INTERNAL_CHECK_PASS` | Expanded experiment and article-local audits are repo-local. | Author confirms not submitted elsewhere. |
| Technical evidence | `PASS_FOR_SUBMISSION_REVIEW` | 24-case layer-safety evaluation, 14/14 promotions rejected, shallow baselines have false negatives. | Human author accepts synthetic case-matrix scope. |
| Source boundary | `TEXT_ONLY_BOUNDARY_DEFINED` | Paper depends on source/derived labels, not public source images or glyph corpus release. | Human source reviewer approves public wording. |
| Third-party material | `NO_REPRODUCTION_CURRENTLY_PLANNED` | No source images or manuscript pages are required. | Rights/authority reviewer approves exact package. |
| Ethics and authority | `HUMAN_REVIEW_REQUIRED` | Current package treats authority as a blocker, not an automated decision. | Human rights/source authority approval. |
| Authorship | `MISSING_EXTERNAL_DECISION` | No final external author list or contributor roles are recorded. | Author/contributor approval. |
| Licence/open access | `MISSING_EXTERNAL_DECISION` | ACM publication route must be selected by the human author/submitter. | Licence/funding/waiver decision. |
| Conflict/AI disclosure | `MISSING_EXTERNAL_DECISION` | Repo records agent-assisted drafting and validation. | Human disclosure wording approval. |

## Decision

The target-journal compliance blockers are reduced to human author, source,
rights/authority, disclosure, licence/funding, and final package approval. The
technical blocker listed in the earlier prior-art audit has been addressed by
the expanded baseline comparison, but reviewers may still request future
extension with live model outputs or additional source corpora.
