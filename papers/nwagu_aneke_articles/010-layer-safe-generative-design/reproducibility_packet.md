# Reproducibility Packet

Article: ARTICLE-NA-010

## Inputs

- `experiments/EXP-NA-002-count-layer-ledger/results.json`
- `experiments/EXP-NA-002-count-layer-ledger/analysis.md`
- `experiments/EXP-NA-002-count-layer-ledger/decision.md`
- `experiments/EXP-NA-010-layer-safety-tests/results.json`
- `experiments/EXP-NA-010-layer-safety-tests/expanded_results.json`
- `experiments/EXP-NA-010-layer-safety-tests/baseline_comparison.json`
- `experiments/EXP-NA-010-layer-safety-tests/layer_non_promotion_lemma.md`
- `experiments/EXP-NA-010-layer-safety-tests/data/expanded_layer_safety_cases.csv`
- `experiments/EXP-NA-010-layer-safety-tests/run_layer_safety_analysis.py`
- `experiments/EXP-NA-010-transfer-counterexample-audit/results.json`
- `experiments/EXP-NA-010-transfer-counterexample-audit/analysis.md`
- `experiments/EXP-NA-010-transfer-counterexample-audit/data/transfer_cases.csv`
- `transfer_counterexample_audit.md`
- `papers/nwagu_aneke_articles/references.bib`

## Reproduction Checks

1. Confirm source-observed 26 by 8 equals 208.
2. Confirm 27/216 appears only as derived f/v split.
3. Confirm the manuscript excludes public image-release and universal-theory claims.
4. Confirm claim, novelty, rights, source, and review-team files exist.
5. Run `python experiments/EXP-NA-010-layer-safety-tests/run_layer_safety_analysis.py`.
6. Confirm the expanded gate catches all intentional promotion errors and that
   provenance-only, citation-only, and no-label baselines have false negatives.
7. Confirm the transfer/counterexample audit rejects all six cross-domain
   promotion errors while allowing four layer-preserving cases.
