# Evidence Use Scope

Article: `ARTICLE-NA-006`

Status: `EVIDENCE_SCOPE_DEFINED_HUMAN_SIGNOFF_BLOCKED`

## Included Evidence

The submission-review candidate may use the following evidence in its current
external-facing argument:

- `experiments/EXP-NA-006-unicode-gap-matrix/results.json`
- `experiments/EXP-NA-006-unicode-gap-matrix/data/unicode_gap_matrix.csv`
- `experiments/EXP-NA-006-unicode-gap-matrix/data/unicode_gap_matrix.jsonl`
- `experiments/EXP-NA-006/results.json`
- `article_specific_experiment.md`
- `standards_status_freshness_audit.md`
- `external_prior_art_audit.md`
- `figures_tables_manifest.json`
- `reviewer2_response_plan.md`
- article-local audits and gates in this directory

## Allowed Claims

Allowed for submission-review drafting, pending human source and standards
approval:

- The experiment creates a 12-requirement Unicode-readiness gap matrix.
- The current package has 1 present, 4 partial, 3 blocked, and 4 missing
  readiness requirements.
- The matrix supports a negative readiness result: the package is suitable for
  audit discussion but not for a Unicode proposal.
- Human source review, rights/authority review, and community/standards review
  are genuine blockers that cannot be solved by formatting.
- The contribution is a reproducible readiness-audit method, not a public
  repertoire.
- A current public standards-status check may be used only to support the
  negative readiness result, pending human source/standards confirmation.

## Excluded Evidence and Claims

Excluded unless later approved by human source, standards, and rights/authority
review:

- Unicode proposal readiness;
- public codepoint assignment or code-chart language;
- complete character repertoire;
- representative public glyph chart;
- public source-image display;
- public glyph-crop release;
- manuscript corpus release;
- community-authorized standardization action;
- universal compression, exceptional-math, or broad generative-grammar claims.

## Decision

The evidence package is sufficient for a text-only submission-review candidate
about Unicode-readiness auditing. External submission remains blocked until
source/standards review, rights/authority review, author approval, disclosure,
licence/funding choice, and final package sign-offs are recorded.
