---
type: usability_protocol
program: nwagu_aneke_frontier
status: protocol_ready_with_scorer_no_human_results
created: "2026-06-22"
goal: GOAL-FRONTIER-001
claim_ceiling: human_comprehension_signal_not_source_evidence
---

# Count-Layer Comprehension Protocol

## Purpose

This protocol checks whether a reader can use the static count-layer prototype
without confusing observation, derivation, restriction, speculation,
application, computation, contested external leads, and dropped branches.

It is not human evidence yet. It becomes evidence only after named or coded
human responses are collected, scored, stored, and reviewed under the lab's
evidence policy.

## Prototype Under Test

`research/frontier/nwagu_aneke/interfaces/count_layer_static_prototype.html`

The prototype must remain rights-safe during this test:

- no source images;
- no glyph reproductions;
- no manuscript pages;
- no Appendix II body if later recovered;
- no claims that bypass rights or authority review.

## Reader Tasks

Ask each reader to inspect the prototype for 5-8 minutes, then answer the
questions in `count_layer_comprehension_questions.csv` without opening the
fixture file or source notes.

Readers may use the layer filter and all visible text in the prototype.

## Minimum Pass Threshold

The minimum pass threshold is 80% correct across core layer-classification
questions.

Hard-stop failures require label revision even if the aggregate score passes:

- fewer than 80% classify `27/216` as derived and not source-observed;
- any reader states that `26/208` and `27/216` are two competing source facts;
- any reader treats Appendix II unrecovered status as proof that Appendix II
  does not exist;
- any reader treats PAGC speculation as a source fact;
- any reader treats computational evaluation as Nwagu source evidence.

If any hard-stop failure appears, revise labels and rerun the protocol.

## Scoring

Score each answer as:

- `correct` - answer names the expected layer and does not promote the claim;
- `partial` - answer notices uncertainty but misses the exact layer;
- `incorrect` - answer promotes, collapses, or reverses the layer.

Record the likely confusion type:

- `source_derived_collapse`
- `absence_claim_error`
- `speculation_promoted`
- `application_promoted`
- `computation_promoted`
- `count_type_collapse`
- `dropped_branch_revived`
- `other`

Then run:

```powershell
python scripts\score_count_layer_comprehension_results.py research\frontier\nwagu_aneke\interfaces\usability\responses\count_layer_results_YYYYMMDD.csv
```

Allowed scorer statuses:

- `PASS_INTERNAL_COMPREHENSION_CHECK`
- `FAIL_LABEL_REVISION_REQUIRED`
- `INVALID_READER_RUN`

The claim ceiling remains
`human_comprehension_signal_not_source_evidence` even when the internal
comprehension check passes.

## Rights And Authority

This packet does not grant source-use permission. It does not resolve authority
or community review. A good usability result only says the interface labels are
legible to readers; it does not make any research branch publishable or
externally promotable.

## Exact Next Action

Run this protocol with 3-5 human readers and record responses in
`count_layer_comprehension_results_template.csv`. Run the scorer and revise
labels if the `27/216` derived status is not correctly understood by at least
80% of readers.
