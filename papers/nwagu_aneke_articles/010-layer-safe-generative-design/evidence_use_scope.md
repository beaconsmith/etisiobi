# Evidence Use Scope

Article: `ARTICLE-NA-010`

Status: `EVIDENCE_SCOPE_DEFINED_HUMAN_SIGNOFF_BLOCKED`

## Included Evidence

The submission-review candidate may use the following evidence in its current
external-facing argument:

- `experiments/EXP-NA-010-layer-safety-tests/results.json`
- `experiments/EXP-NA-010-layer-safety-tests/expanded_results.json`
- `experiments/EXP-NA-010-layer-safety-tests/baseline_comparison.json`
- `experiments/EXP-NA-010-layer-safety-tests/analysis.md`
- `experiments/EXP-NA-010-layer-safety-tests/decision.md`
- `experiments/EXP-NA-010-layer-safety-tests/layer_non_promotion_lemma.md`
- `experiments/EXP-NA-010-layer-safety-tests/data/expanded_layer_safety_cases.csv`
- `experiments/EXP-NA-010-layer-safety-tests/data/expanded_layer_safety_cases.jsonl`
- article-local audits and gates in this directory

## Allowed Claims

Allowed for submission-review drafting, pending human source approval:

- A non-promotion invariant can reject output claims that assert a stronger
  evidence layer than the input permits.
- The expanded 24-case matrix contains 14 intentional promotion errors, all
  rejected by the layer gate.
- Provenance-only, citation-only, and no-label baselines miss promotion errors
  in the controlled matrix.
- The invariant is useful as an applied cultural-heritage computing control for
  artifact-derived generative systems.

## Excluded Evidence and Claims

Excluded unless later approved by human source and rights/authority review:

- public reproduction of source images;
- public reproduction of manuscript pages;
- public release of a glyph or claim dataset;
- claim that Nwagu Aneke source holdings have been independently reviewed;
- Unicode proposal readiness;
- glyph-shape interpretation or decipherment;
- cultural-authority decisions;
- universal compression, exceptional-math, or exact-27 theory claims;
- broad claim that the invariant solves AI safety or cultural-heritage ethics.

## Decision

The evidence package is sufficient for a text-only submission-review candidate
about layer-safe generative design. External submission remains blocked until
source, rights/authority, author, disclosure, licence/funding, and final package
sign-offs are recorded.
