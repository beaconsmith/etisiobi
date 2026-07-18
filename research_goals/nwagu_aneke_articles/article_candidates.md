# Ten Research Article Candidates Derived From Nwagu Aneke

Generated: 2026-06-19

Each title is a novelty hypothesis, not a novelty claim.

## Active Candidates

### ARTICLE-NA-001: A Source-Critical Reconstruction of the Nwagu Aneke Igbo Syllabary

Research question: what exactly can be reconstructed from Azuonye, the chart,
Omniglot, and local transcription files without importing PAGC assumptions?

Novelty hypothesis: a disciplined critical reconstruction of Nwagu Aneke as a
source artifact may be more publishable than speculative PAGC theory.

First experiment: align Azuonye appendix, local chart transcription,
`symbol_inventory.jsonl`, and Omniglot chart into one evidence table.

Current result: `EXP-NA-001-source-critical-reconstruction` produced
`RECONSTRUCTABLE_AS_SOURCE_LEDGER_NOT_FULL_GLYPH_CORPUS`. The article can
proceed as a source-critical ledger paper. It cannot yet claim a completed
glyph-level corpus, public image release, or 27/216 as source-observed.

Falsification condition: if the local sources cannot support a stable
reconstructable inventory, the article becomes a negative-result source audit.

Blockers: rights to reproduce chart/manuscript images; human source review.

### ARTICLE-NA-002: Count-Layer Drift in Nwagu Aneke: 26x8, 27/216, 164, and 224

Research question: can all known Nwagu Aneke count claims be reconciled as
different abstraction layers?

Novelty hypothesis: the strongest early result is a layer-specific count
taxonomy, not a single magic count.

First experiment: create a count ledger covering printed rows, vowel columns,
CV cells, f/v derived split, actual symbols, ideal syllable space, and logographs.

Falsification condition: if 164/224 cannot be source-verified, they remain leads
and cannot enter the article as results.

Blockers: line-verified access to Ahamefula/Mbah and primary manuscript corpus.

### ARTICLE-NA-003: The f/v Hinge: Orthographic Economy and Dialect-Specific Design in Nwagu Aneke

Research question: is the f/v row a dialectal feature, an orthographic economy,
or a transcription artifact?

Novelty hypothesis: f/v is the hinge that explains why source-layer and
derived-layer counts diverge.

First experiment: compare f/v examples across Azuonye appendix readings, local
chart transcription, Umuleri/Igbo phonology sources, and the BMC row labels.

Falsification condition: if f/v evidence is too sparse or inconsistent, the
article becomes an uncertainty note rather than a linguistic claim.

Blockers: domain linguist review; stronger Umuleri phonology sources.

## Pending Candidates

### ARTICLE-NA-004: Logographs in a Syllabary: Separating Whole-Word Signs From CV Cells

Question: which Nwagu Aneke signs are logographic, and how should they be
modeled separately from syllabary cells?

Method: build a logograph ledger with source locator, reading, semantic domain,
and relationship to CV signs.

First experiment: extract every locally observed whole-word sign into
`artifacts/nwagu_aneke/logograph_inventory.jsonl`.

### ARTICLE-NA-005: Toward a TEI/IIIF Critical Edition of an Unencoded African Syllabary

Question: can Nwagu Aneke be represented as a standards-compatible digital
critical edition before Unicode encoding?

Method: map local chart/manuscript references to IIIF canvases, TEI character
and glyph declarations, uncertainty records, and annotation selectors.

First experiment: validate a minimal TEI + IIIF + Web Annotation bundle for ten
representative symbols.

### ARTICLE-NA-006: Unicode Readiness for Nwagu Aneke: Character, Glyph, Evidence, and Community Review

Question: what evidence would a future Unicode proposal for Nwagu Aneke need?

Method: compare Unicode/SEI proposal expectations against local repertoire
evidence, glyph variation, usage examples, names, directionality, and community
authority.

First experiment: create a Unicode-readiness gap matrix from local files.

### ARTICLE-NA-007: Manuscript Corpus Provenance: Locating and Ethically Studying the 100+ Nwagu Aneke Books

Question: where are the manuscripts, who has authority over them, and what can
be studied or published?

Method: provenance/contact map plus CARE-style authority gate.

First experiment: build a source-owner/holding-institution ledger without
publishing sensitive material.

### ARTICLE-NA-008: Comparative Standardization Paths for African Syllabaries

Question: how does Nwagu Aneke compare with Vai, Bamum, Mende Kikakui, Loma,
Kpelle, Nsibidi, and Ndebe in corpus, teaching, encoding, and community use?

Method: comparative matrix over repertoire size, usage corpus, digital tools,
Unicode status, community authority, and educational adoption.

First experiment: create `systematic_reviews/nwagu_aneke_comparative_scripts/`.

### ARTICLE-NA-009: Igbo Tokenization From a Source-Grounded Syllabary Layer

Question: can a tokenizer informed by Nwagu Aneke source-layer structure improve
Igbo representation without overclaiming universal compression?

Method: compare standard BPE/Unigram baselines to source-layer and derived-layer
tokenizers on local Igbo corpora.

First experiment: rerun the k-sweep with frozen dependencies, confidence
intervals, corpus card, and source/derived layer labels.

### ARTICLE-NA-010: Layer-Safe Generative Design Systems From Nwagu Aneke

Question: can systems use derived symbolic layers without allowing them to
become false source claims?

Method: formalize source, derived, speculative, and authority labels as system
types; test the Layer-Safety Theorem against design workflows.

First experiment: turn `experiments/EXP-APP-003-layer-safety-proof/` into a
reviewable theorem + test suite article.

## Recommended Activation Order

1. `ARTICLE-NA-001`
2. `ARTICLE-NA-002`
3. `ARTICLE-NA-003`

Reason: these three determine the source, count, and f/v foundation. Articles
004-010 become stronger after those foundations survive review.
