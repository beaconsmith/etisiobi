# EXP-NA-021 — Contextual Encoding Topology (exploratory)

Date: 2026-11-22  
Status: **bounded source-led research; not a completed linguistic or computational result**

## Research question

Is Nwagụ Aneke best modeled as a one-to-one syllable table, or as a mixed **many-to-many sign-reading system** in which omissions, shared signs, alternative signs, vowel harmony, and full-word signs require contextual recovery?

## Inputs

- `corpus/base_modifier_cache.jsonl`: 208 **chart-slot index records**, not verified glyph shapes.
- `experiments/EXP-APP-001-count-layer-design-grammar/tokens_source_layer.jsonl`: projected source-layer design tokens.
- `experiments/EXP-NA-004-logograph-ledger/data/logograph_leads.jsonl`: 30 **unreviewed** full-word transcription leads.
- `published_full_word_examples.json`: 15 **selected** labels and author-reported counts from Ahamefula (2010), *USEM Journal* vol. 3, https://usemjournal.com/pdf/volume-3.pdf.
- Source review: `research/frontier/nwagu_aneke/source_reviews/ahamefula_2010_contextual_encoding.md`.

## Reproducible bounded audit

```bash
python3 scripts/audit_nwagu_encoding_topology.py
python3 -m unittest discover -s tests/research -p 'test_nwagu_encoding_topology.py' -v
```

The audit is read-only. It verifies chart-slot index integrity, counts currently locatable/reviewed cell evidence, measures onset patterns in two selected word lists, and keeps the 164/224 literature figures separate from 208 grid slots.

## Three claims with different ceilings

1. **Observed in repo:** 208 source-chart index entries; 208 unreviewed; zero cell regions annotated; only 26 reused row-level observation references. **This does not count historical signs.**
2. **Author-reported:** 164 distinct graphic characters, ~30 multivalent signs, ten syllables with two graphic alternatives, /f/-/v/ sharing, omitted independent vowels/nasals. **These need glyph-by-glyph independent reconciliation.**
3. **Hypothesis:** full-word symbols may partly compensate for vowel-initial spelling gaps. In current unreviewed transcription, 29/30 are vowel-initial; in the paper's selected examples, 15/15. **Neither sample is a random or matched lexical population.**

## Formal object

Define a bipartite relation `E ⊆ S × G` between syllabic readings `S` and graphic sign types `G`, plus separate full-word sign mappings and context-dependent omission/recovery operations. No fixed one-to-one correspondence is assumed.

A chart of 208 row/vowel positions can coexist with a lower count of distinct signs, **without implying that the numerical difference is a count of missing signs**. A complete reconciliation requires the actual edges `E`.

## Falsification

- If reviewed glyph annotations show nearly all signs have unique readings and no alternative signs, the many-to-many model loses its central motivation.
- If matched noun-frequency and genre controls erase the vowel-initial full-word pattern, the compensation hypothesis is not supported.
- If a contextual decoder fails to improve held-out recovery beyond a simple lexical baseline, the computational benefit is rejected.
- If rights or authority cannot be established, manuscript images remain restricted and no public training corpus is released.

## Next bounded experiment

Request permission for high-resolution scans or controlled research access to the 1978 and 1980 manuscript samples with their aligned transcriptions; construct a small reviewed `sign ↔ reading` ledger before building any decoder. Seek the Smithsonian-held research proposal to recover the earlier chart source and compare versions.
