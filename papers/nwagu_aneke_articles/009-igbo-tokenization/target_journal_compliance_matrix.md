# Target Journal Compliance Matrix

Article: `ARTICLE-NA-009`

Candidate target venue: `Language Resources and Evaluation (Springer Nature)`

Status: `COMPLIANCE_MATRIX_COMPLETE_HUMAN_SIGNOFF_BLOCKED`

Checked against official Springer pages on 2026-07-06:

- https://link.springer.com/journal/10579
- https://link.springer.com/journal/10579/submission-guidelines

| Requirement area | Current status | Evidence | Remaining human sign-off |
|---|---|---|---|
| Venue scope | `PLAUSIBLE_FIT` | Tokenizer baseline for a less-resourced-language setting, with language-resource evaluation framing. | Author approves LRE as target. |
| Originality | `INTERNAL_CHECK_PASS` | Repo-local five-tokenizer baseline and article-local prior-art audit. | Author confirms not submitted elsewhere. |
| Technical evidence | `PASS_FOR_SUBMISSION_REVIEW` | 25,000 train words, 5,000 test words, seed 42, five tokenizer conditions, metrics and confidence intervals. | Human source/NLP reviewer accepts the metrics and public wording. |
| Field positioning | `PASS_FOR_SUBMISSION_REVIEW` | Article frames the result as baseline evaluation, not downstream task improvement. | Human NLP/domain reviewer approves framing. |
| Source boundary | `TEXT_ONLY_BOUNDARY_DEFINED` | Human source review file keeps corpus and source/derived review open. | Human source/NLP review record. |
| Third-party material | `NO_REPRODUCTION_CURRENTLY_PLANNED` | No source images, glyph crops, public corpus sample, or task dataset is required. | Rights/authority reviewer approves exact package. |
| Authorship | `MISSING_EXTERNAL_DECISION` | No external author list or contributor roles recorded. | Author/contributor approval. |
| Licence/open access/APC | `MISSING_EXTERNAL_DECISION` | Springer publication route must be selected by human author/submitter. | Licence/funding/waiver decision. |
| Conflict/AI disclosure | `MISSING_EXTERNAL_DECISION` | Repo records agent-assisted drafting and validation. | Human disclosure wording approval. |

## Decision

The remaining blockers are human author, source/NLP-review, rights/authority,
disclosure, licence/funding, and final package approval. The tokenizer-baseline
blocker has been reduced to human source/NLP and venue sign-off.
