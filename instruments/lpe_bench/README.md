# LPE-Bench

Layer Promotion Error Benchmark.

## Research Question

Do AI research agents promote derived, speculative, blocked, or
design-layer claims into source-observed or publication-ready claims?

## Why This Exists

Etisiobi's Nwagu Aneke/PAGC work has one load-bearing boundary:

```text
source-observed layer: 26 rows x 8 vowel/modifier columns = 208 records
derived layer: 27 / 216 by f/v split only
```

The benchmark tests whether agents preserve or violate that boundary
when writing research claims.

## Current Status

`PUBLIC_INSTRUMENT_DRAFT_NOT_FRONTIER_PROOF`

This is a named research instrument, not a paper-ready result.

## Current Assets

- Internal cases: `510`
- Blind annotation queue: `360`
- Best internal typed baseline: `rank_only_metadata` with F1 `1.0`
- Best metadata-free baseline: `lexical_only` with F1 `0.8`
- Unicode/channel audit: `UNICODE_CHANNEL_AUDIT_COMPLETE_NOT_PUBLICATION_BLOCKING`, findings `2`
- EXP-005 annotation: `ANNOTATION_ADJUDICATED_GOLD_CREATED_AI_REVIEW_NOT_HUMAN_FRONTIER_READY`
- EXP-005 score: `SCORED_NOT_VALIDATED_FOR_FRONTIER_CLAIM`
- Best EXP-005 Codex agent: `codex_C0_no_layer_labels` with F1 `0.7692`

## Public-Grade Bar

LPE-Bench becomes a frontier candidate only after independent labels,
frozen gold splits, real agent runs, external cases, confidence
intervals, and a validation report that documents defects and
corrections.

## Commands

```powershell
python scripts\run_frontier_lpe_benchmark_v2.py
python scripts\prepare_frontier_lpe_exp003_annotation_packet.py
python scripts\run_frontier_lpe_exp003_pilot.py
python scripts\audit_unicode_channel_risk.py
python scripts\build_lpe_bench_instrument.py
python scripts\validate_frontier_lab.py
```
