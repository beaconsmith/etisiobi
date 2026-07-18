# Frontier Sprint: Layer Promotion Error Benchmark

## Research Question

Can an evidence-layer gate detect when an AI-assisted research or design system
promotes a non-source claim into a source-observed claim?

## Thesis

Artifact-derived systems need a layer-safety benchmark because standards such as
TEI, IIIF, PROV-O, RO-Crate, Web Annotation, and CIDOC CRM can record evidence,
but they do not by themselves reject the specific failure where a derived,
speculative, blocked, or design-layer claim is rewritten as source-observed.

## Accepted Foundation

```text
source-observed Nwagu Aneke layer = 26 rows x 8 vowel/modifier columns = 208 records
derived layer = 27 / 216 only if f/v is split
```

## Benchmark Name

`LPE-BENCH-001`: Layer Promotion Error Benchmark for Nwagu Aneke-derived claims.

## What Counts As A Layer Promotion Error

A layer promotion error occurs when:

```text
rank(output_layer) < rank(input_layer)
```

where stronger evidence has lower rank:

```text
source_observed < source_index < derived < design_hypothesis < speculative < blocked
```

Examples:

- derived `27/216` described as source-observed;
- speculative E6 mapping described as a result;
- rights-blocked glyph corpus described as publicly releasable;
- design grammar described as historical fact.

## Experiment

Run:

```powershell
python scripts\run_frontier_layer_promotion_benchmark.py
```

Outputs:

- `experiments/EXP-FRONTIER-001-layer-promotion-benchmark/results.json`
- `experiments/EXP-FRONTIER-002-layer-promotion-expanded/results.json`
- `experiments/EXP-FRONTIER-003-blind-lpe-annotation/manifest.json`
- `experiments/EXP-FRONTIER-003-blind-lpe-annotation/pilot_results.json`
- `experiments/EXP-FRONTIER-001-layer-promotion-benchmark/data/lpe_cases.jsonl`
- `experiments/EXP-FRONTIER-002-layer-promotion-expanded/data/lpe_cases.jsonl`
- `experiments/EXP-FRONTIER-001-layer-promotion-benchmark/data/lpe_predictions.jsonl`
- `experiments/EXP-FRONTIER-002-layer-promotion-expanded/data/baseline_metrics.csv`
- `experiments/EXP-FRONTIER-003-blind-lpe-annotation/annotation_queue.jsonl`
- `experiments/EXP-FRONTIER-001-layer-promotion-benchmark/analysis.md`
- `benchmarks/layer_promotion_error/BENCHMARK.md`
- `benchmarks/layer_promotion_error/EXPANDED_BENCHMARK.md`
- `benchmarks/layer_promotion_error/scoreboard.json`
- `benchmarks/layer_promotion_error/expanded_scoreboard.json`

## Blind Annotation Packet

`EXP-FRONTIER-003` prepares the next-stage benchmark packet:

- 360 unlabeled cases;
- 130 real agent/research-output cases;
- 90 cross-program cases;
- 30 external-prior-art controls;
- locked train/dev/test splits;
- no gold labels in model-visible fields.
- synthetic pilot annotations from three reviewer profiles.

Current status:

```text
BLIND_ANNOTATION_PACKET_READY_UNLABELED
```

Pilot status:

```text
SYNTHETIC_PILOT_LABELS_CREATED_NOT_HUMAN_REVIEW
```

The pilot is useful for testing the annotation harness and surfacing reviewer
disagreement, especially around rights/authority. It is not human annotation and
must not be used as frontier proof.

## Current Expanded Result

`EXP-FRONTIER-002` expands the seed into 510 cases using repo-derived claims,
cross-program claims, external-prior-art controls, and adversarial hard cases.

The result is scientifically more useful than the seed because it shows the
difference between typed and untyped detection:

- metadata/rank baselines solve the typed task;
- metadata-free text baselines make false-positive and false-negative errors;
- therefore the publication-grade problem is not "can we compare two labels?"
  but "can we infer or preserve evidence layers in real generated outputs?"

Current status:

```text
EXPANDED_BENCHMARK_INTERNAL_NOT_FRONTIER_PROOF
```

## Promotion Gate

This branch can become a `PAPER_CANDIDATE` only when:

- benchmark has at least 50 cases;
- precision and recall are reported;
- baseline rules are compared against at least one alternative detector;
- external prior art is written for claim verification, provenance, type systems, and artifact criticism;
- a domain postdoc confirms that the examples do not distort the Nwagu Aneke foundation.

## Publication-Grade Upgrade

The current benchmark is still not enough for a paper because the labels are
heuristic, synthetic, or not independently human-reviewed. To become
publication-grade, the next sprint must add:

- at least 150 cases from real manuscripts, generated drafts, source notes, and
  adversarially rewritten claims;
- blind labels from at least two reviewers;
- inter-annotator agreement;
- detector baselines: rank-only, lexical-only, LLM judge, and hybrid;
- held-out test split;
- failure analysis by evidence layer;
- cross-domain cases beyond Nwagu Aneke, for example OGI/governance claims and
  another cultural-heritage artifact;
- explicit comparison to fact verification, claim verification, provenance, and
  type-system literature.

Until then the correct status is:

```text
FRONTIER_BENCHMARK_SEEDED_NOT_PAPER_READY
```
