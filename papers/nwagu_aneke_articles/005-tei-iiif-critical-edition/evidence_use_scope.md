# Evidence Use Scope

Article: `ARTICLE-NA-005`

Status: `EVIDENCE_SCOPE_DEFINED_HUMAN_SIGNOFF_BLOCKED`

## Included Evidence

The submission-review candidate may use the following evidence in its current
external-facing argument:

- `experiments/EXP-NA-005-tei-iiif-selectors/results.json`
- `experiments/EXP-NA-005-tei-iiif-selectors/analysis.md`
- `experiments/EXP-NA-005-tei-iiif-selectors/decision.md`
- `experiments/EXP-NA-005-tei-iiif-selectors/data/tei_glyph_declarations.jsonl`
- `experiments/EXP-NA-005-tei-iiif-selectors/data/web_annotation_sample.jsonld`
- `experiments/EXP-NA-005/results.json`
- `selector_bridge_comparison.md`
- article-local audits and gates in this directory

## Allowed Claims

Allowed for submission-review drafting, pending human source approval:

- The experiment creates a 10-record TEI glyph declaration sample.
- The experiment creates a 10-record Web Annotation sample.
- The current sample has 0 pixel-coordinate source selectors.
- TEI locators and Web Annotation TextQuoteSelector values can function as
  non-image selector leads.
- The contribution is a selector-layer bridge and missing-coordinate boundary,
  not a completed IIIF critical edition.

## Excluded Evidence and Claims

Excluded unless later approved by human source and rights/authority review:

- public source-image display;
- public glyph-crop release;
- pixel-level source annotation;
- complete IIIF critical edition;
- reviewed glyph corpus;
- public IIIF canvas release;
- Unicode proposal readiness;
- public cultural-authority decisions;
- universal compression, exceptional-math, or broad generative-grammar claims.

## Decision

The evidence package is sufficient for a text-only submission-review candidate
about a TEI/Web Annotation selector-layer bridge. External submission remains
blocked until source, rights/authority, author, disclosure, licence/funding, and
final package sign-offs are recorded.
