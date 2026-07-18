# Prior-Art Scan Before Goal Creation

Generated: 2026-06-19

## Local Observations

- The repo now treats Nwagu Aneke as the seed artifact for PAGC-derived work.
  Current event state is in `spine/events/current_state.md`.
- The accepted internal count foundation is `MULTI_LAYER_COUNT_VALID`:
  source-observed `26 x 8 = 208`; derived `27 / 216` only by f/v split.
- Local primary-source folder contains Azuonye 1992 PDF, Omniglot page HTML,
  chart image, chart transcription, and source audit under
  `research/pagc/primary_sources/nwagu_aneke/`.
- Local artifact dossier contains `symbol_inventory.jsonl`, IIIF, TEI,
  structural model sketches, and transcription uncertainty notes under
  `artifacts/nwagu_aneke/`.
- The existing research map identifies open threads: repertoire reconstruction,
  ideal-vs-actual syllabary space, f/v collapse, logograph lexicon, manuscript
  corpus access, digitization/Unicode, and comparative African syllabaries.

## External Anchors Reviewed

| Source | What It Supports | Relevance |
|---|---|---|
| Azuonye 1992 ScholarWorks landing page | Confirms title, author, date, and framing of Nwagu Aneke as an Igbo syllabary with origins, features, mechanics, possibilities, and problems. | Primary academic anchor for article candidates. |
| Omniglot Nwagụ Aneke page | Describes the script as a syllabary for Umuleri Igbo with logographic symbols, left-to-right writing, and no independent vowel symbols. | Secondary public description and chart source. |
| Unicode L2/23-203 African Scripts update | Lists Nwagu Aneke as an unencoded syllabary with logographic symbols, left-to-right, and notes more than 100 books. | Supports Unicode/digitization article tracks. |
| Unicode Script Encoding Working Group guidance | Emphasizes proposal requirements and the character/glyph distinction. | Supports encoding-readiness article track. |
| Script Encoding Initiative tips | Notes value of preliminary proposals for complex scripts and use of completed proposals as models. | Supports practical Unicode-roadmap article. |
| TEI P5 character/glyph guidelines | Provides standard machinery for representing characters, glyphs, and writing modes. | Supports digital critical edition article. |
| IIIF Presentation API and IIIF annotation cookbook | Provides standards for digitized objects, canvases, and W3C Web Annotation-compatible annotations. | Supports image-to-annotation article. |

## Research Interpretation

The strongest article program should not start from "PAGC proves X." It should
start from:

```text
source artifact -> repertoire reconstruction -> uncertainty model -> digital
edition -> comparative standardization -> constrained system applications
```

## Immediate Novelty Hypotheses

1. Nwagu Aneke may be publishable as a source-critical reconstruction problem,
   independent of PAGC.
2. The count-layer problem is richer than 26/27/216: local records also preserve
   164 actual symbols and 224 ideal Igbo syllabary-space leads that require
   verification.
3. The f/v split is not just an accounting detail; it may be an orthographic,
   phonological, dialectal, or transcriptional hinge.
4. Logographs require a separate inventory and should not be collapsed into CV
   syllabary cells.
5. A Unicode-readiness paper can be valuable even before an encoding proposal,
   because it can define the evidence gaps.
6. A TEI/IIIF edition can produce reviewable research artifacts before any
   public release of sensitive source images.

## Sources

- https://scholarworks.umb.edu/africana_faculty_pubs/13/
- https://www.omniglot.com/writing/nwaguaneke.htm
- https://www.unicode.org/L2/L2023/23203-update-african-scripts.pdf
- https://sew.unicode.org/guidelines
- https://sei.berkeley.edu/tips-for-proposals/
- https://www.tei-c.org/release/doc/tei-p5-doc/en/html/WD.html
- https://iiif.io/api/presentation/3.0/
- https://iiif.io/api/cookbook/recipe/0266-full-canvas-annotation/
