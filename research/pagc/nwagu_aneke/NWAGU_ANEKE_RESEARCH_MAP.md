# Nwagu Aneke Research Map

Generated: 2026-05-28

This artifact corrects course from a generic modifier atlas to the actual research object: the Nwagu Aneke script, its source trail, its symbol repertoire, and the autonomous research loops still open.

## Core Research Chain

Source -> Glyph -> Syllable -> Word -> Manuscript -> Use -> Standardization

## Current Count Landscape

| Count | Status | Meaning |
|---:|---|---|
| 26 | OBSERVED | Printed consonant rows in the audited chart, with f/v combined. |
| 27 | DERIVED | Possible phonemic count if f/v is split. |
| 164 | EXTERNAL | Ahamefula reports this as the number of actual Aneke symbols. |
| 224 | EXTERNAL | Ahamefula reports this as an ideal Igbo syllabary requirement. |
| 216 | REWRITE | Derived 27 x 8 normalization; not source-observed. |

## Claim Gate

| Label | Claim | Status | Evidence |
|---|---|---|---|
| OBSERVED | The research object is not a modifier atlas; it is the Nwagu Aneke script and archive. | READY | Repo AGENTS.md and research/pagc/WIKI.md identify PAGC as a program around Nwagu Aneke source-derived structure. |
| EXPERIMENTAL | The 27-base figure is not source-observed in the chart; it is derived only if f/v is split. | REWRITE_AS_DERIVED | EXP-0001 and corpus inventory observations INV-0001 through INV-0004. |
| EXTERNAL | Ahamefula adds a richer count problem: 224 ideal syllables vs 164 actual symbols. | NEW_RESEARCH_THREAD | USEM article lines 1134-1138; needs local archival and line-verified extraction before becoming a repo claim. |
| DERIVED | The f/v collapse is not a nuisance; it is a linguistic feature of the Umuleri-specific repertoire. | NEW_RESEARCH_THREAD | USEM article lines 1148-1152 plus EXP-0001 f/v row audit. |
| DERIVED | Logographs must be modeled as a separate inventory from CV syllabary cells. | READY | Omniglot feature list, Azuonye appendix audit, and Ahamefula logograph examples. |
| SPECULATIVE | A Unicode/repertoire proposal would require a character inventory, names, glyph sources, usage evidence, and community review. | SPECULATIVE_ONLY | Unicode status document says no encoding proposal yet; additional proposal requirements are inferred from standards practice, not proven here. |

## Autonomous Research Threads

## NA-THREAD-001: Repertoire Reconstruction

**Question:** Can we reconstruct the actual Aneke symbol repertoire from Azuonye Appendix I/II and Ahamefula's 164-symbol claim?

**Next autonomous move:** Convert Appendix I/II into structured CSV: row, vowel, glyph id, reading, duplicate/multivalent flag.

**Risk:** medium

## NA-THREAD-002: Ideal vs Actual Syllabary Space

**Question:** Why does Ahamefula say Igbo would require 224 symbols, while the Aneke syllabary has 164?

**Next autonomous move:** Model the 224 ideal space and map missing/merged/duplicate cells.

**Risk:** medium

## NA-THREAD-003: f/v Collapse

**Question:** Is f/v sharing an Umuleri phonological economy, an orthographic simplification, or a transcription artifact?

**Next autonomous move:** Compare f/v examples in Ahamefula, Azuonye Appendix II, and Igbo/Umuleri phonology sources.

**Risk:** low

## NA-THREAD-004: Logograph Lexicon

**Question:** Which whole-word symbols exist, and do they form a semantic core of the archive?

**Next autonomous move:** Create a logograph ledger from Azuonye Appendix II and Ahamefula examples.

**Risk:** medium

## NA-THREAD-005: Manuscript Corpus Access

**Question:** Where are the 100+ books/exercise books, and can usage examples be ethically studied?

**Next autonomous move:** Build a contact/provenance map: University of Nigeria, family/estate, cited project team, archives.

**Risk:** high

## NA-THREAD-006: Digitization and Unicode

**Question:** What would be required for a defensible digital repertoire, keyboard, font, or Unicode proposal?

**Next autonomous move:** Track unencoded-script status and assemble character naming, glyph variation, and evidence requirements.

**Risk:** high

## NA-THREAD-007: Comparative African Syllabaries

**Question:** How does Nwagu Aneke compare with Vai, Mende Kikakui, Loma, Bété, and Bamum in standardization path?

**Next autonomous move:** Create comparison matrix: symbol count, usage corpus, standardization, encoding, pedagogy.

**Risk:** medium


## Sources

- **NA-SRC-001 Azuonye 1992 official landing page and local PDF** (EXTERNAL+OBSERVED): Azuonye frames the work as a study of origins, features, significance, mechanics, possibilities, and problems of the Nwagu Aneke Igbo Syllabary. Locator: ScholarWorks lines 32-55; local research/pagc/primary_sources/nwagu_aneke/azuonye_1992.pdf https://scholarworks.umb.edu/africana_faculty_pubs/13/
- **NA-SRC-002 Azuonye Appendix I chart render** (OBSERVED): The rendered chart shows 26 printed consonant rows and 8 vowel columns; f/v is a combined row. Locator: experiments/EXP-0001-pagc-base-inventory-resolution/analysis.md; corpus/pagc_inventory_observations.jsonl 
- **NA-SRC-003 Omniglot Nwagu Aneke page** (EXTERNAL): Describes the script as a syllabary for Umuleri Igbo, left-to-right, with logographic symbols and no independent vowels. Locator: Omniglot lines 16-25; local omniglot_nwaguaneke.html https://www.omniglot.com/writing/nwaguaneke.htm
- **NA-SRC-004 Ahamefula 2012 USEM article** (EXTERNAL): Reports 224 ideal Igbo syllabary symbols, 164 actual Aneke symbols, around 30 multivalent characters, ten duplicate-symbol syllables, and f/v sharing. Locator: USEM PDF lines 1134-1156 and 1175-1183 https://www.usemjournal.com/pdf/volume-3.pdf
- **NA-SRC-005 Unicode L2/23-203 African scripts update** (EXTERNAL): Lists Nwagu Aneke as an unencoded syllabary with some logographic symbols, written left to right, and notes more than 100 books. Locator: Unicode PDF lines 311-315 https://www.unicode.org/L2/L2023/23203-update-african-scripts.pdf
- **NA-SRC-006 Oxford Handbook of African Languages chapter** (EXTERNAL): Places the Nwagu Aneke Igbo syllabary among recent African orthography and writing-system inventions. Locator: Oxford page line 49 https://academic.oup.com/edited-volume/38608/chapter/334730045

## Visual Artifact

Open `research/pagc/nwagu_aneke/NWAGU_ANEKE_RESEARCH_MAP.html`.
