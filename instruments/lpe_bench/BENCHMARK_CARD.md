# Benchmark Card: LPE-Bench

## Task

Classify whether a research claim illegally promotes a weaker evidence
layer into a stronger output claim.

## Labels

- `source_observed`
- `source_index`
- `derived`
- `design_hypothesis`
- `speculative`
- `blocked`

## Metrics

- precision
- recall
- F1
- MCC
- balanced accuracy
- severity-weighted recall

## Baselines

Current internal baselines:

- `majority_negative`
- `rank_only_metadata`
- `lexical_only`
- `shacl_type_sim`
- `metadata_free_text`
- `hybrid_rank_lexical`

## Known Limitation

The typed metadata baseline can solve the current internal task because
the labels expose the layer transition. The real research problem is
metadata-free or partially-observed detection on independently labeled
agent outputs.
