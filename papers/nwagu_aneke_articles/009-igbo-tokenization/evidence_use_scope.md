# Evidence Use Scope

Article: `ARTICLE-NA-009`

Status: `EVIDENCE_SCOPE_DEFINED_HUMAN_SIGNOFF_BLOCKED`

## Included Evidence

The submission-review candidate may use the following evidence in its current
external-facing argument:

- `experiments/EXP-NA-009/results.json`
- `experiments/EXP-NA-009-tokenizer-baselines/results.json`
- `experiments/EXP-NA-009-tokenizer-baselines/data/tokenizer_metrics.csv`
- `experiments/EXP-NA-009-tokenizer-baselines/data/tokenizer_metrics.jsonl`
- `experiments/EXP-NA-009-tokenizer-baselines/data/bpe_merges_200.json`
- `experiments/EXP-NA-009-tokenizer-baselines/analysis.md`
- `experiments/EXP-NA-009-tokenizer-baselines/decision.md`
- `article_specific_experiment.md`
- `external_prior_art_audit.md`
- `figures_tables_manifest.json`
- `reviewer2_response_plan.md`
- article-local audits and gates in this directory

## Allowed Claims

Allowed for submission-review drafting, pending human source/NLP approval:

- The experiment compares five tokenizer conditions on a 25,000-word training
  and 5,000-word test setup with seed 42.
- The source-layer and derived f/v CV greedy tokenizers produced 3.6708 mean
  tokens per word and 0.6746 CV character coverage in this run.
- BPE with 200 merges produced 3.6164 mean tokens per word in this run.
- The experiment supports tokenizer baseline reporting and future task design.
- The contribution is a bounded language-resource evaluation result, not a
  downstream NLP improvement claim.

## Excluded Evidence and Claims

Excluded unless later approved by human source/NLP and rights/authority review:

- public corpus release;
- public source-image display;
- public glyph-crop release;
- downstream NLP improvement;
- tokenizer superiority on task performance;
- source-observed status for the derived f/v layer;
- Unicode proposal readiness;
- community-authorized data-release decisions;
- universal compression, exceptional-math, or broad generative-grammar claims.

## Decision

The evidence package is sufficient for a text-only and metric-only
submission-review candidate about tokenizer baselines. External submission
remains blocked until source/NLP review, rights/authority review, author
approval, disclosure, licence/funding choice, and final package sign-offs are
recorded.
