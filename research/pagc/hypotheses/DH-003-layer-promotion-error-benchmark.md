# DH-003: Layer-Promotion Error Benchmark

id: DH-003
title: Layer-Promotion Error Benchmark
lane: Experimental
source inputs: repo-local claim records, LPE benchmark cases, label-gate pilot,
and layer-safety proof outputs
invented/derived step: treating claim-layer promotion as a measurable benchmark
task
formal object: evidence-layer transition record with input layer, output layer,
promotion-error label, severity, split, and quality-gate status
research question: Can autonomous research agents be evaluated on whether they
promote derived, speculative, source-index, rights-blocked, or paper-blocked
claims into stronger evidence layers?
hypothesis: Layer-promotion error is benchmarkable and can produce reusable
research-safety knowledge when labels, baselines, and review gates are explicit.
baseline: lexical-only detector; metadata-aware layer rank detector; ungated
labels
test: consolidate repo-local LPE evidence into ten bounded knowledge units and
verify each unit against explicit evidence signals
kill condition: fewer than ten units pass, signals are not traceable, or labels
are treated as paper evidence before quality routing and blind review
allowed wording: "DH-003 produced ten internal benchmark-design knowledge
units"; "this is an internal research-safety milestone"
forbidden wording: "DH-003 is globally novel"; "DH-003 is public benchmark
ready"; "DH-003 proves PAGC source claims"; "DH-003 is paper-ready"
stage: INTERNAL_KNOWLEDGE_BREAKTHROUGH
next action: expand the LPE label quality gate from pilot sample to the full
label set, then compare quality-gate status against scored agent conditions

## Current Evidence

- `experiments/EXP-DH-003-layer-promotion-knowledge-benchmark/results.json`
- `experiments/EXP-FRONTIER-002-layer-promotion-expanded/results.json`
- `experiments/EXP-FRONTIER-017-lpe-label-quality-gate/pilot_results.json`
- `experiments/EXP-APP-003-layer-safety-proof/verification_report.json`
- `experiments/EXP-DH-001-derived-completion-baseline/global_benchmark_gate_results.json`

## Current Decision

`SIGNIFICANT_INTERNAL_KNOWLEDGE_BREAKTHROUGH_DH003`

DH-003 is now the strongest next branch for controlled research-loop work
because it produced ten traceable internal knowledge units without weakening
the source/derived boundary or claiming public readiness.

