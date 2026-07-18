---
type: source_note
program: nwagu_aneke_frontier
experiment_id: EXP-NA-002
backlog_id: EXP-BL-001
status: source_review_completed_with_appendix_ii_gap
created: "2026-06-22"
updated: "2026-06-22T11:34:04+01:00"
goal: GOAL-FRONTIER-001
claim_ceiling: source-critical note only
---

# EXP-NA-002 Source Note: Azuonye 1992

## Question

Does Azuonye 1992 confirm, revise, or weaken the current 26/208
source-observed and 27/216 derived count-layer audit?

## Short Decision

Azuonye 1992 strengthens the current source-layer audit for Appendix I:

```text
26 printed consonant rows x 8 printed vowel columns = 208 source-layer cells
```

The source does not show a separate printed `f` row and `v` row in Appendix I.
The row is printed as a combined `f/v` row, so:

```text
27 rows / 216 cells remains a derived f/v split layer.
```

This note does not make the result paper-ready. It does not settle the full
manuscript corpus, the complete character inventory, phonological analysis, or
community authority questions.

## Source Used

| Field | Record |
|---|---|
| Source | Chukwuma Azuonye, "The Nwagu Aneke Igbo Script: Its Origins, Features and Potentials as a Medium of Alternative Literacy in African Languages" |
| Publication date | 1992 |
| Repository landing page | https://scholarworks.umb.edu/africana_faculty_pubs/13/ |
| Local PDF | `research/pagc/primary_sources/nwagu_aneke/azuonye_1992.pdf` |
| Local text extraction | `experiments/EXP-0001-pagc-base-inventory-resolution/logs/azuonye_1992_pdftotext.txt` |
| Local rendered Appendix I page | `experiments/EXP-0001-pagc-base-inventory-resolution/figures/azuonye_1992_page_16.png` |
| Prior local audit | `artifacts/nwagu_aneke/azuonye_1992_audit.md` |
| Chart transcription | `research/pagc/primary_sources/nwagu_aneke/CHART_TRANSCRIPTION.md` |
| Appendix II recovery audit | `research/frontier/nwagu_aneke/source_reviews/azuonye_1992_appendix_ii_recovery.md` |
| Source-acquisition leads | `research/frontier/nwagu_aneke/source_reviews/SOURCE_ACQUISITION_LEADS.md` |

The ScholarWorks landing page identifies the work as an article by Chukwuma
Azuonye, dated January 1992, and provides the preferred repository citation.

## Count-Relevant Evidence

| Item | Evidence from reviewed local source trail | Classification |
|---|---|---|
| Script type | Azuonye describes the script as syllabic and discusses it as a writing system for the Umuleri dialect of Igbo. | `[SRC]` |
| Appendix placement | The PDF text says the syllabary is contained in Appendix I and an alphabetical list in Appendix II. | `[SRC]` |
| Vowel handling | The PDF text says the script has no standalone vowel characters and no place for V syllables. | `[SRC]` |
| Logographs | The PDF text states that some complete-word or morpheme characters exist and points to the Appendix I box. | `[SRC]` |
| Vowel/modifier columns | Rendered Appendix I shows 8 printed vowel columns. | `[OBS]` |
| Printed rows | Rendered Appendix I shows 26 printed consonant rows. | `[OBS]` |
| f/v hinge | Rendered Appendix I prints `f/v` as one combined row, not two separate rows. | `[OBS]` |
| Source-layer cells | 26 printed rows x 8 printed columns = 208 source-layer cells. | `[DERIVED]` from `[OBS]` counts |
| Derived f/v split | Splitting `f/v` into separate `f` and `v` rows yields 27 x 8 = 216 cells. | `[DERIVED]` |
| Appendix II | The local PDF names Appendix II, but the rendered/text-extracted local copy does not expose its character-list content beyond the appendix title leaf. | `[NEG]` / blocker |

## Matrix Status

The matrix is observed as a representation in Appendix I of the local Azuonye
PDF. It should be described as an Appendix I chart or printed source display.

The evidence reviewed here does not prove that the matrix is:

- Aneke's original working structure;
- the complete manuscript inventory;
- a generative grammar;
- a mathematically exact symbolic system;
- or a 27-row source structure.

Current classification:

```text
matrix-as-printed-source-display: supported
matrix-as-underlying historical/generative structure: unresolved
```

## Rights and Quotation Limits

The repository makes the PDF downloadable, but this is not a license to
republish figures, appendix images, or long extracts. Until rights review is
complete:

- use citation, metadata, short paraphrase, and internal audit references;
- do not reproduce Appendix I in public-facing outputs;
- do not render new publication PDFs using the chart image;
- keep figure use internal to source review;
- preserve the local PDF as a source artifact, not as reusable design material.

## Effect on Current Count-Layer Audit

| Current audit claim | Effect of Azuonye review | Status |
|---|---|---|
| 26 source-observed rows | Strengthened for Appendix I printed row count. | Supported within chart layer |
| 8 source-observed columns | Strengthened for Appendix I printed column count. | Supported within chart layer |
| 208 source-layer cells | Strengthened as a count derived from Appendix I printed rows and columns. | Supported within chart layer |
| 27 source-observed rows | Not supported by Appendix I. | Rejected for source layer |
| 216 source-observed cells | Not supported by Appendix I. | Rejected for source layer |
| 27/216 derived layer | Still allowed only as an explicit f/v split transformation. | Supported as derived |
| Complete inventory claim | Not supported, because Appendix II content and manuscript corpus review remain incomplete. | Blocked |

## Blockers

1. Appendix II is named but not available in usable content from the local PDF
   extraction/render set. The alphabetical character list still needs recovery
   or alternate copy review. The dedicated recovery audit is
   `research/frontier/nwagu_aneke/source_reviews/azuonye_1992_appendix_ii_recovery.md`.
2. The 100-plus exercise-book manuscript corpus remains unreviewed and
   rights/authority constrained.
3. Human/domain transcription review is still required before any paper
   candidate can treat the count layer as externally hardened.
4. Public use of appendix imagery remains blocked by rights review.

## Dossier Update Rule

The count-layer dossier may cite this note as strengthening the current
Appendix I count layer. It must not use this note to claim:

- paper readiness;
- complete reconstruction;
- Unicode repertoire readiness;
- manuscript-corpus completeness;
- or source-observed 27/216.

## Exact Next Action

Human-review the unsent ScholarWorks request draft at
`research/frontier/nwagu_aneke/source_reviews/request_drafts/scholarworks_appendix_ii_request.md`,
then decide whether to send it through the public repository support route.
