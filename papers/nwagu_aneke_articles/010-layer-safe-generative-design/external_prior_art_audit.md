# External Prior-Art Audit

Article: `ARTICLE-NA-010`

Status: `PRIOR_ART_AUDIT_SUBMISSION_REVIEW_PASS_HUMAN_SIGNOFF_BLOCKED`

## Article-Specific Contribution Under Audit

This article's contribution is a bounded systems result:

> a non-promotion invariant and executable gate tests that reject unsafe
> transformations from derived, speculative, or blocked evidence layers into
> source-observed claims.

The paper does not claim a new provenance standard, a new type theory, a full
trustworthy-AI framework, or a final cultural-source authority process.

## Prior-Art Areas Checked

| Area | Relevance | Boundary for This Article |
|---|---|---|
| PROV-O and provenance modeling | Tracks entities, activities, agents, and derivation chains. | Provenance can record where a claim came from; Article 010 adds a rule about what a generated output may assert. |
| RO-Crate and DataCite | Package research objects and data citation metadata. | Packaging does not by itself prevent claim-layer promotion. |
| FAIR and CARE principles | Govern data reuse and Indigenous/community authority obligations. | CARE motivates the authority boundary, but does not supply the executable non-promotion invariant. |
| Scientific claim verification and citation-grounded generation | Provides baselines for checking support between claims and evidence. | Article 010 focuses on layer preservation, not only entailment or citation presence. |
| Type systems and information-flow control | Provides the closest analogy: labels constrain allowed transformations. | The article must state this as an applied evidence-layer invariant, not a new type-system theory. |
| Cultural-heritage AI and source-critical editing | Provides ethical and editorial context for artifact-derived systems. | Needs human domain/source review before external submission. |

## Repo Evidence Anchors

- `experiments/EXP-NA-010-layer-safety-tests/results.json`
- `experiments/EXP-NA-010-layer-safety-tests/expanded_results.json`
- `experiments/EXP-NA-010-layer-safety-tests/baseline_comparison.json`
- `experiments/EXP-NA-010-layer-safety-tests/layer_non_promotion_lemma.md`
- `experiments/EXP-NA-010-layer-safety-tests/data/layer_safety_cases.csv`
- `experiments/EXP-NA-010-layer-safety-tests/data/layer_safety_cases.jsonl`
- `experiments/EXP-NA-010-layer-safety-tests/data/expanded_layer_safety_cases.csv`
- `experiments/EXP-NA-010-layer-safety-tests/data/expanded_layer_safety_cases.jsonl`
- `experiments/EXP-NA-002-count-layer-ledger/results.json`
- `research/pagc/PAGC_RESET.md`
- `research/pagc/FALSIFICATION_TRACKER.md`
- `papers/nwagu_aneke_articles/010-layer-safe-generative-design/claim_audit.md`

## Novelty-Risk Assessment

Risk: `MEDIUM`

The result is promising because it converts source/derived discipline into an
executable invariant and now compares the invariant against provenance-only,
citation-only, and no-label baselines. Novelty risk remains because provenance,
type systems, information-flow control, and claim-verification literatures are
mature. The current defensible contribution is therefore applied and bounded:
an evidence-layer preservation rule for artifact-derived generative design, not
a new provenance standard, type theory, or general AI-safety framework.

## Remaining Before External Submission

1. Human domain/source review from cultural-heritage or digital-humanities
   expertise.
2. Human author approval that the target venue accepts a synthetic controlled
   case matrix rather than live model outputs.
3. Final rights/authority review for public examples and wording.
4. Optional future expansion with live model outputs or multiple source corpora
   if requested by reviewers.

## Current Decision

The prior-art audit now supports submission-review candidate status if the
paper is framed as a bounded applied invariant and baseline comparison. It is
not ready for external submission until human source, rights/authority, author,
and final package decisions are recorded.
