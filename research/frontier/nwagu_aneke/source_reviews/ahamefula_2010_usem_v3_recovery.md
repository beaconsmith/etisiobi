---
type: external_source_review
program: nwagu_aneke_frontier
source_id: NA-EXT-USEM-2010-01
status: externally_read_but_glyph_inventory_not_extracted
review_date: "2026-11-22"
claim_ceiling: source_attributed_secondary_analysis_not_verified_repertoire
---

# Source recovery: Ahamefula (2010), USEM Volume 3

## Bibliographic identity (verified against journal cover and article heading)

**Author:** Ndubuisi Ogbonna Ahamefula (single author).  
**Title:** *West African Indigenous Writing Systems: Focus on the Nwagu Aneke's Syllabary*.  
**Venue:** *USEM Journal of Languages, Linguistics and Literature*, **volume 3 (2010)**, Department of Linguistics and Nigerian Languages, University of Uyo.  
**Official publicly accessible source:** https://usemjournal.com/pdf/volume-3.pdf  
**Article span:** printed journal pp. 35–45 (PDF pages 35–45; 1-based).  
**Inspection:** direct PDF text cross-checked against rendered journal pp. 1, 35, 36, 38, 39, 43, 44, 45 on 2026-11-22.

**Do not conflate** with the *different* Ahamefula & Mbah (2011), *Linguistic Analysis of the Nwagu Aneke Indigenous Igbo Syllabary*, which remains an unacquired bibliographic lead. This 2010 paper can be cited in its own right, but is not a recovered copy of the 2011 study.

## Material findings (attributed claims; not independently counted glyphs)

| Journal location | What the author reports | What Etisiobi can responsibly say |
|---|---|---|
| p. 38 | The script has **up to 164 graphic signs** | Published inventory estimate from this article; per-sign list and counting scope not independently verified here |
| p. 38 | **About 30 signs** can stand for more than one syllable, often in the same vowel-harmony group | Published polyphony assertion, pending sign→reading mapping extraction and independent review |
| pp. 38–39 | **Ten syllables** are each represented by two signs | Published allography assertion, pending review of actual pairs |
| pp. 36, 38 | **224** as an idealized CV target for a wider Igbo consonant inventory | The printed p. 36 expression is **28 × 28 (224)**, an arithmetical inconsistency; 28 × 8 = 224 is the arithmetically consistent interpretation, not an amended historical quote |
| p. 39 | **f/v** sounds share graphic representation; bare vowels and syllabic nasals lack dedicated signs; tone and word boundaries not consistently encoded | Evidence that a cell-to-character-only transliterator loses context and will need uncertainty-preserving encoding |
| p. 39 | Some words have independent full-word signs | Logographic channel must be modeled separately from CV signs |

### Recovered page-level evidence previously absent from source plan

- **Appendix II, journal p. 43:** chart with printed CV row/column labels, visible handwritten signs and full-word signs; this is **not** Donatus Nwoga's missing *Appendix II alphabetical list* from Azuonye (1992).
- **Appendix III, journal p. 44:** published handwriting sample reproduced alongside Umuleri-Igbo Roman-script transcription and an English translation; attributed on the page to *Nwagu Aneke Project Proposal*, p. 9. A **parallel-script/reading/translation sample exists** for future reviewed alignment.
- **Appendix IV, journal p. 45:** photographed sample page labeled an August 1980 testimony by Nwagu Aneke, without equivalent full parallel transcription on that page.

No image, transcript, or translation has been copied into this repo. External access and *permission to reproduce or publish a derived dataset* are separate questions.

## Essential reconciliation of counting units

Etisiobi's **26 × 8 = 208** describes *printed chart cell positions* in its currently reconstructed source-chart index, not independently established **208 distinct graphemes**.

The **27 × 8 = 216** data structure is an analytical f/v-split representation, not another historical manuscript inventory; its implementation contains 200 carried-through derived objects and 16 explicit f/v-split variants.

The **up-to-164** quantity is a published estimate of **graphic signs** from a different analytical scope; its exact comparability to the chart is **unknown** until sign identity is reviewed.

### A precise f/v implication, verified in Etisiobi's own derived ledger

The local EXP-APP-001 source data contains **eight** combined `f/v` positions (one per vowel column). Its derived data expands each to `-f` and `-v` reading objects, **16 variant records replacing eight source positions**, while preserving the same `source_bmc_id` parent in each pair. None has a reviewed source `glyph_id`.

The 2010 author (journal p. 39) explicitly describes shared signs for /f/ and /v/ syllables. Therefore the derived 216-record layer's additional eight distinctions are **analytical readings/objects, not demonstrated additional historical graphic signs**. A Unicode or transliteration system must not treat `-f` and `-v` as distinct characters merely because their derived record IDs differ.

This is a bounded reconciliation of **source position → possible readings**, not a claim that the exact underlying glyph has already been independently identified for each cell.

The **224** quantity concerns an idealized broader CV inventory, and should never be treated as a corpus count.

**Do not compute `208 - 164 = 44 missing signs`, claim 44 distinct glyph collisions, or derive exact compression ratios.** Those calculations silently assume comparable, complete, independently verified inventories. We do not possess that evidence.

## New archival route to the underlying project proposal (catalogue verified, item not read)

The Smithsonian Libraries and Archives catalogue lists *The Nwagu Aneke Research Project proposal* (University of Nigeria, undated circa 1983–89), 11 illustrated pages, **African Art** collection, **PL8021.N5 N93 1983 quarto**, barcode **39088008864084**, OCLC **40642457**. The catalogue notes a two-page Azuonye letter inserted in this copy. Its historical physical contents were **not** inspected in this review.

Catalogue record: https://siris-libraries.si.edu/ipac20/ipac.jsp?booklistformat=&profile=liball&session=DC6205453H395.776069&uri=full%3D3100001~%21553317~%210

This is an actionable possible route to the proposal page 5 chart and page 9 sample cited in Azuonye and Ahamefula. The Smithsonian item is *not* evidence that the missing **1991 Donatus Nwoga alphabetical list** is included. Confirm holding and permissions through the [African Art library](https://library.si.edu/libraries/african-art) or [Smithsonian access guidance](https://library.si.edu/departments/special-collections/accessing) before seeking reproduction. See `SOURCE_ACQUISITION_LEADS.md` / `LEAD-SI-001`.

## What this changes scientifically

A one-to-one mapping `CV_cell ↔ unique_glyph` is **not currently justified**. The independently reported polyphonic and allographic properties call for an ambiguity-preserving relation, conceptually:

```text
Sign  <--attested at SourceLocator-->  Reading(s)
Sign  <--used in Occurrence-->        Context
Reading <--alternative forms-->       Sign(s)
```

The working hypothesis is **phonologically constrained polyphony**: multiple syllabic readings of a sign may cluster within vowel-harmony classes, reducing some ambiguity in context. The paper *reports* such a tendency; Etisiobi has **not** measured it from reviewed sign→reading mappings.

## Next falsification experiment

Use Appendix II as *candidate* sign inventory and Appendix III as an *attested text sample*, following rights/authority review. Have two qualified readers independently assign stable sign IDs and candidate readings with image coordinates, variants, degree of certainty, and source locators. Adjudicate disagreements rather than forcing one reading. Only then:

1. Build sign↔syllable bipartite incidence edges, including alternate forms.
2. Verify or refute the reported ~30 multivalent signs and 10 double-graphic syllables **for the scope that the paper actually counted**.
3. Test vowel-harmony clustering against a degree- and inventory-preserving null. Register vowel categories and dialect-specific treatment of /a/ *before* looking at results.
4. Apply to the sample with parallel Umuleri transcription: measure unresolved reading alternatives, explicit vowel/nasal deletions, and word-boundary ambiguity. Report inter-reviewer agreement and unresolved cases.
5. Stop if glyph identity, rights, or sample alignment are too weak to support a count. Do not invent mapping edges.

## Boundaries

This is a verified **source recovery and problem-reframing result**, not an original finding that the actual unique-character count is 164, not a claim of new Unicode repertoire, not a proven compression method, and not permission to publish scans. Azuonye (1992) Appendix II remains unrecovered. The 2011 joint study also remains unrecovered.
