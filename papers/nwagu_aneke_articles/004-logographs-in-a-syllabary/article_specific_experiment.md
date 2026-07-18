# Article-Specific Experiment: EXP-NA-004

## Research Question

Can visible whole-word signs in the current Nwagu Aneke chart transcription be
organized as a bounded logograph lead set without claiming a complete corpus?

## Hypothesis

If each whole-word sign is represented as a lead with source location, semantic
domain, and uncertainty status, then the article can support corpus-building
work while blocking unsupported claims about completeness, glyph review, and
public release.

## Inputs

- `experiments/EXP-NA-004-logograph-ledger/results.json`
- `experiments/EXP-NA-004-logograph-ledger/data/logograph_leads.csv`
- `experiments/EXP-NA-004-logograph-ledger/data/logograph_leads.jsonl`
- `experiments/EXP-NA-004/results.json`
- `papers/nwagu_aneke_articles/004-logographs-in-a-syllabary/logograph_leadset_comparison.md`

## Result

The audit records 30 visible chart leads, including 5 unknown or uncertain
glosses. Each row points to `research/pagc/primary_sources/nwagu_aneke/CHART_TRANSCRIPTION.md`
and carries the status `visible_chart_lead_not_reviewed_glyph`. The result is a
review queue and indexing seed, not a final inventory.

## Negative Control

A manuscript, table, figure, prompt, or interface fails the control if it calls
the lead set a complete corpus, treats unknown glosses as resolved, folds
whole-word signs into the 26 x 8 syllabic CV count, or implies reviewed glyph
shape evidence without human source review.

## Claim Ceiling

The article can support a source-limited logograph lead-set audit. It cannot
support public source-image release, a complete glyph corpus, a complete semantic
classification, Unicode readiness, or community authority approval.
