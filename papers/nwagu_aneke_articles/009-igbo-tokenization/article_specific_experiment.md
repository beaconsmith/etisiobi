# Article-Specific Experiment

Article: `ARTICLE-NA-009`

Experiment: `EXP-NA-009-tokenizer-baselines`

Status: `SUBSTANTIVE_EXPERIMENT_COMPLETE_HUMAN_REVIEW_BLOCKED`

## Research Question

Can source-layer and derived-layer Nwagu Aneke representations be used to run a
bounded Igbo tokenizer baseline without claiming downstream NLP improvement?

## Hypothesis

If character, whitespace, BPE, source-layer CV, and derived f/v CV tokenizers
are compared on the same local Igbo sample, the result will produce useful
segmentation and coverage measurements while keeping downstream task claims
blocked.

## Inputs

- `experiments/EXP-NA-009-tokenizer-baselines/results.json`
- `experiments/EXP-NA-009-tokenizer-baselines/data/tokenizer_metrics.csv`
- `experiments/EXP-NA-009-tokenizer-baselines/data/tokenizer_metrics.jsonl`
- `experiments/EXP-NA-009-tokenizer-baselines/data/bpe_merges_200.json`
- `experiments/EXP-NA-009-tokenizer-baselines/analysis.md`
- `experiments/EXP-NA-009-tokenizer-baselines/decision.md`

## Result

The run used 25,000 training words, 5,000 test words, and seed 42. It compared
five tokenizers: character, whitespace word, BPE with 200 merges, source-layer
CV greedy, and derived f/v CV greedy. The source-layer and derived f/v CV
tokenizers both produced 3.6708 mean tokens per word and 0.6746
source-or-derived CV character coverage. BPE produced 3.6164 mean tokens per
word. The experiment therefore supports a tokenizer baseline paper, but not a
downstream NLP improvement claim.

## Negative Control

The article fails if it claims task improvement, public corpus release, source
validation of the derived f/v layer, or superiority for any tokenizer without a
downstream evaluation dataset.

## Claim Ceiling

The experiment supports a bounded language-resource baseline. It does not
support sentiment, translation, retrieval, language-modeling, OCR, or benchmark
performance claims.
