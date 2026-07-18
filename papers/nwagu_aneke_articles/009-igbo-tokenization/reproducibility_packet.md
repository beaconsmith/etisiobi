# Reproducibility Packet

Article: ARTICLE-NA-009

## Inputs

- `experiments/EXP-NA-009/results.json`
- `experiments/EXP-NA-009-tokenizer-baselines/results.json`
- `experiments/EXP-NA-009-tokenizer-baselines/analysis.md`
- `experiments/EXP-NA-009-tokenizer-baselines/decision.md`
- `experiments/EXP-NA-009-tokenizer-baselines/data/tokenizer_metrics.csv`
- `experiments/EXP-NA-009-tokenizer-baselines/data/tokenizer_metrics.jsonl`
- `experiments/EXP-NA-009-tokenizer-baselines/data/bpe_merges_200.json`
- `papers/nwagu_aneke_articles/references.bib`

## Reproduction Checks

1. Confirm source-observed 26 by 8 equals 208.
2. Confirm 27/216 appears only as derived f/v split.
3. Confirm the experiment uses 25,000 training words, 5,000 test words, and
   seed 42.
4. Confirm five tokenizers are compared: character, whitespace word, 200-merge
   BPE, source-layer CV greedy, and derived f/v CV greedy.
5. Confirm the manuscript reports tokenizer baseline metrics while excluding
   downstream NLP improvement claims.
6. Confirm the manuscript excludes public corpus release, public image-release,
   and universal-theory claims.
7. Confirm claim, novelty, rights, source, and review-role files exist.
