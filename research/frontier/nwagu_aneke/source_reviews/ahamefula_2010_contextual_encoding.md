---
type: source_review_and_hypothesis_note
program: nwagu_aneke_frontier
status: external_fulltext_reviewed_in_browser_local_archival_pending
date: 2026-11-22
claim_ceiling: sourced_linguistic_report_and_exploratory_hypothesis
---

# Nwagụ Aneke: recoverable contextual encoding, not a flat 208-sign alphabet

## New external source located

**Ndubuisi Ogbonna Ahamefula**, "West African Indigenous Writing Systems: Focus on the Nwagu Aneke’s Syllabary", *USEM Journal of Languages, Linguistics and Literature*, vol. 3 (2010), article 4, printed pp. ~35–42 with appendices. Full journal PDF: https://usemjournal.com/pdf/volume-3.pdf.

This is **not** the separately cited Ahamefula and Mbah (2011), JILL 3:95–103 paper. The 2011 paper remains a distinct bibliographic lead. The 2010 full text is now available for human review and rights-aware source acquisition. The original 2010 source PDF has **not** been copied into the repository.

### Direct observations in the available article

- PDF text around article section 3 reports **164 graphic characters** versus a theoretical **224-symbol** coverage figure; it describes about **30 characters that each serve multiple syllables** and **10 syllables that each have two graphic representations**. These are **author-reported counts**, not independently reconstructed measurements.
- The source says the /f/ and /v/ syllables share representations, mentions missing independent vowel and syllabic nasal signs, vowel assimilation, and unmarked word/sentence boundaries.
- The paper's **Appendix II** (PDF page index 42) reproduces a chart with 26 printed rows, eight columns, and full-word symbols. This Appendix II is **not** the missing Appendix II alphabetical list from **Azuonye 1992**; the two appendices must not be conflated.
- **Appendix III** (PDF page index 43) includes a June 1978 script sample with Umuleri transcription and English translation, attributed to *Nwagụ Aneke Research Project Proposal*, p. 9.
- **Appendix IV** (PDF page index 44) reproduces a sample from an August 1980 testimony with a transcription of the first eight lines and English translation in the adjacent text.
- Bibliographic/editorial caveat: the article appears to print `28 x 28 (224)` in a discussion of an ideal 28-consonant/8-vowel syllabary. This is an **arithmetic typo** (28×28 ≠ 224); do not silently treat it as a source calculation.

These samples make an **aligned-image / transcription / translation** research path possible, subject to rights review and expert alignment. They do **not** establish a machine-readable glyph corpus or permission to republish the images.

### Source URLs and anchors

- Journal PDF: https://usemjournal.com/pdf/volume-3.pdf
- Azuonye 1992 official citation: https://scholarworks.umb.edu/africana_faculty_pubs/13/
- Published text discussion: journal article section 3, approximately PDF text lines 1153–1203.
- Chart and manuscript samples: PDF page indices 42, 43, 44 (zero-indexed).

## New empirical question: What is the *encoding topology*?

The current 26×8 = 208 dataset is a **row/vowel grid-slot index**, not a validated inventory of 208 distinct graphic signs.

The in-repo `corpus/base_modifier_cache.jsonl` contains 208 slots, but:
- 208/208 have `source_region_status=not_annotated` and `source_region=null`;
- 208/208 have `review_status=human_review_needed` and `status=unreviewed`;
- the 208 records refer to only 26 distinct `glyph_observation_id` values, each identifying a **row-level** annotation, not an independently observed cell glyph.

The fact that 208 slot records are internally well formed does **not** imply 208 observed glyphs. Treat `source_observed` on those design tokens as shorthand for a **source-grounded grid coordinate**, not a per-glyph observation.

The 2010 paper describes a different mathematical object: a **many-to-many bipartite mapping** `E ⊆ S × G`, where `S` is syllabic readings and `G` is graphic sign types.

- Some signs have multiple readings (`degree_G > 1`).
- Some readings have alternative signs (`degree_S > 1`).
- Some initial vowel/nasal segments are omitted or assimilated and must be recovered contextually.
- Full-word signs form a distinct path to meaning.

Consequently, **208 - 164 = 44 is not evidence of 44 missing characters**. The two numbers describe different things, from different studies, with unverified reconciliation. A subtraction alone is not a glyph-census method.

## Complementary, narrower test: phonologically structured polyphony

The 2010 article also reports that multivalent signs often encode syllables within the same vowel-harmony group. A separate test is now preregistered in `research/frontier/nwagu_aneke/results/EXP-NA-022-harmony-constrained-polyphony.md`. Its `scripts/nwagu_multivalence_probe.py` requires **human-adjudicated sign↔reading edges with source locators** and compares the within-sign same-harmony pair rate against a degree-preserving class-permutation null; no authentic edges are claimed or supplied yet.

In the repository's own analytic f/v split, **eight combined f/v chart positions become sixteen derived reading records**, sharing eight source-parent IDs. The extra eight records are analytical **reading distinctions, not demonstrated additional historical graphic signs**. This is checked by `tests/research/test_nwagu_fv_reconciliation.py`.

## Testable lead: vowel-initial full-word signs

Etisiobi's existing, unreviewed chart transcription lists 30 full-word labels; **29 begin with a vowel**, with `nga` the only exception. This is a reproducible property of that **transcription**, not a confirmed property of all historical logographs.

The independent 2010 paper gives 15 illustrative full-word labels, all vowel-initial in its printed spelling:

`ụbọsi, uche, afọ, ọgụ, ogbenye, ọgbọ, ụka, ili, akwụkwọ, asa, asatọ, ụwa, ụzọ, izu, ana`.

**Hypothesis:** full-word signs may be disproportionately used for lexemes whose vowel-initial forms are incompletely representable in a CV-only sign inventory. This is **not proven**: Igbo nouns often begin with vowel prefixes, and both lists are selected, nonrandom examples. It is also possible that semantic importance, word frequency, genre, or later editorial selection explains the pattern.

**Discriminating test:** compare logograph use against a **matched set of vowel-initial and consonant-initial nouns of similar frequency/genre**, then align actual sign occurrences with manuscript transcriptions. The hypothesis weakens if the enrichment disappears under noun-class matching, or if full-word signs are rarely used where vowel omission would otherwise occur.

## Stronger test: ambiguity recovery in authentic text

1. Obtain rights-cleared high-resolution scans and expert alignment for the published 1978 and 1980 examples; retain source and manuscript provenance.
2. Create a **many-to-many sign-reading ledger**, recording ambiguous signs, alternative allographs, omissions and vowel-harmony restrictions.
3. Compare three decoders on **held-out manuscript segments**: (A) one-sign/one-syllable lookup; (B) sign→candidate readings + phonological/vowel-harmony constraints; (C) B + word and discourse context. Measure character/word error and uncertainty calibration.
4. Evaluate with **real sign annotations**, not generated 208 grid labels. Reject the hypothesis if contextual modeling offers no gain over a well-designed dictionary baseline, or if the apparent gain is merely train/test text leakage.
5. Do not equate success of a modern decoder with a claim about Aneke's conscious design intentions.

This is a substantive linguistic-computational research lane, **not** a proof of PAGC, historical matrix generation, general AI memory, or global novelty.

## Source acquisition: verified catalogue lead

The Smithsonian Libraries catalogue has a bibliographic record for **The Nwagu Aneke Research Project proposal**, listed as 11 pages, `[Nsukka: University of Nigeria, 1983–89?]`, project director D. I. Nwoga, call number `PL8021.N5 N93 1983 quarto African Art`, barcode `39088008864084`, with a two-page Azuonye letter noted as inserted in the copy.

Catalog record (legacy URL): https://siris-libraries.si.edu/ipac20/ipac.jsp?booklistformat=&profile=liball&session=DC6205453H395.776069&uri=full%3D3100001~%21553317~%210

This is a **catalogue holding lead**, not confirmation that an accessible scan or current circulation request exists. Ask the Smithsonian library for a holding/scan/permissions check before claiming the proposal has been recovered. The catalogue information is stronger than the prior generic "ask UNN" lead.

## Immediate decision

**Advance:** bounded encoding-topology hypothesis and source recovery of 1978/1980 paired samples.

**Do not advance:** glyph corpus completion, 208 unique historical signs, full 164/224 reconciliation, source-authorized logograph selection mechanism, or a paper-quality computational result.
