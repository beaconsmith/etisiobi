# Article-Specific Experiment

Article: `ARTICLE-NA-002`

Experiment: `EXP-NA-002-count-layer-ledger`

Status: `EXECUTED_WITH_REVIEW_BLOCKERS`

## Research Question

Can active Nwagu Aneke count claims be converted into a layer-labeled ledger
that prevents source-observed counts, derived counts, lead claims, and blocked
claims from being collapsed into one inventory number?

## Hypothesis

If each count claim is represented as a tuple containing quantity, value, layer,
evidence, allowed claim, blocked claim, confidence, and status, then the article
can state the 26 x 8 source-observed index and the derived 27/216 f/v split
without promoting the derived layer into a source-observed claim.

## Method

The experiment converted active count claims into a seven-row ledger:

- source rows;
- source vowels/modifier columns;
- source CV cells;
- derived rows;
- derived cells;
- visible logograph leads;
- manuscript-book claims.

Each row records the allowed claim and the blocked claim. This makes the audit
falsifiable because later source review can update a specific row rather than
forcing a rhetorical patch across the manuscript.

## Evidence Files

- `experiments/EXP-NA-002-count-layer-ledger/results.json`
- `experiments/EXP-NA-002-count-layer-ledger/analysis.md`
- `experiments/EXP-NA-002-count-layer-ledger/decision.md`
- `experiments/EXP-NA-002-count-layer-ledger/data/count_layer_ledger.csv`
- `experiments/EXP-NA-002-count-layer-ledger/data/count_layer_ledger.jsonl`

## Result

The experiment records:

- source layer: 26 rows x 8 vowels/modifier columns = 208 records;
- derived layer: 27 rows and 216 cells only if the f/v row is split;
- ready or derived records: 5;
- blocked or lead records: 2;
- decision: `COUNT_LAYERS_RECONCILED_WITH_REVIEW_BLOCKERS`.

## What This Result Allows

The article can claim that the current repo-local evidence package supports a
layer-separated count audit:

- 26 x 8 = 208 is the current source-observed index layer.
- 27/216 is a derived f/v split layer.
- visible logographs and more-than-100-book claims remain leads or secondary
  claims until source/holdings/authority review is attached.

## What This Result Does Not Allow

The experiment does not authorize:

- public source-image release;
- final Unicode repertoire claims;
- complete glyph-shape interpretation;
- a public dataset release;
- universal-compression, E6, or exact-27 theory claims;
- claims that all manuscript holdings have been reviewed.

## Remaining Blockers

1. Human source review of the chart transcription and count ledger.
2. Rights/authority clearance for external publication wording.
3. Deeper prior-art review against African script documentation and Unicode
   evidence standards.
4. Human target-output decision: full DSH article, short methods note,
   technical report, or private review packet.

## 2026-07-07 Cycle Addendum

Added `public_output_scale_audit.md` to test whether the current result supports
a public journal manuscript or only a public preprint/short-methods-note shape.
The audit keeps `ARTICLE-NA-002` at
`PUBLIC_PREPRINT_OR_SHORT_METHODS_NOTE_HUMAN_SIGNOFF_BLOCKED`: the source/derived
count result is substantive, but human source review, rights/authority review,
and author venue approval remain required before any external submission or
journal-candidate claim.
