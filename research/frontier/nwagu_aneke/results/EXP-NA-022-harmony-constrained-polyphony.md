# EXP-NA-022 — Test whether Nwagụ Aneke sign ambiguity respects vowel harmony

Status: `SOURCE_LEAD_RECOVERED / TEST_PREREGISTERED / NO GLYPH_LEVEL_RESULT`

## New opening

Ahamefula's **2010 sole-authored** USEM Volume 3 paper (journal pp. 38–39; official PDF at https://usemjournal.com/pdf/volume-3.pdf) reports that some signs serve multiple syllables, often in the same vowel-harmony group. It also reports alternate signs for some syllables and a parallel manuscript/reading/translation sample (Appendix III, journal p. 44). See `research/frontier/nwagu_aneke/source_reviews/ahamefula_2010_contextual_encoding.md`.

The theoretical object is **not** a 26×8 array of unique glyphs. It is a candidate *many-to-many sign-reading relation with attested context*.

## Central falsifiable question

**H1:** Reviewed signs with multiple syllabic readings show a higher rate of same-harmony reading pairs than expected under a null that preserves sign-reading connections and the number of reading classes.

**H0:** The observed within-sign harmony rate is not greater than that null.

There is **no experiment result yet**: the repo lacks the necessary expert-reviewed sign identities and reading edges. The author's textual assertion is a research lead, not adjudicated edge data.

## Minimum reviewed edge

```json
{
  "sign_id": "STABLE_REVIEWED_SIGN_ID",
  "reading_id": "ADJUDICATED_UMULERI_CV_READING",
  "harmony_class": null,
  "source_locator": "USEM-v3-2010:p43:<reviewed-region-or-folio>",
  "review_status": "human_adjudicated"
}
```

This is a **schema example only**, not an observed glyph/sign assignment. Do not use artificial sign IDs from a grid position to pretend unique graphic identities were observed.

## Extraction and evaluation gates

1. Obtain rights/authority guidance for making derivative graphic descriptions. Do not copy source scans or full transcriptions to the repo without approval.
2. Have at least two domain-competent readers independently identify graphic signs, possible readings, and coordinates, first from the 2010 published chart (Appendix II) and its aligned text sample (Appendix III). Record disagreements and whether a drawn form is a variant, a different sign, or uncertain.
3. Establish a dialect-aware harmony classification, including how to handle /a/ and uncertain vowels **before** inspecting candidate outcomes. Unknown must remain unknown.
4. Export reviewed `sign_id ↔ reading_id` pairs with stable locators. Do not count uncertain/AI-guessed pairs as adjudicated.
5. Run: `python scripts/nwagu_multivalence_probe.py --edges path/to/reviewed_edges.jsonl --permutations 9999 --seed 42`.
6. Report total reviewed sign/readings, sign degrees (polyphony), reading degrees (allography), eligible within-sign pairs, same-class pair fraction, permutation null distribution, and uncertainty. Compare the author's ~30 and 10 *only when both inventory scopes and sign equivalence are defined*. An incomplete sample does not estimate full inventory frequency.
7. Independently inspect the text sample for cases that a graph without syllable/word boundaries cannot resolve. Report actual error cases; don't equate a symbolic sign overlap with a demonstrated comprehension failure.

## Why the test is worth running

If the harmony effect is independently replicated, the syllabary may employ a **phonologically constrained many-to-many code**, and its decoder should rank alternate readings using dialectal phonological context rather than discard alternatives or force an exact one-to-one glyph table. This could be a meaningful computational insight for indigenous script restoration and low-resource transliteration.

If the effect is not supported, keep multivalence, abandon the harmony-specific explanation, and retain explicit alternatives.

## Probe limits

The included Python probe evaluates an *externally supplied adjudicated edge list*. Tests use **synthetic fixtures only**. Its null shuffles reading-class assignments over the fixed graph; it preserves sign and reading degrees and overall class counts, but **does not preserve lexical frequency or phonotactic co-occurrence constraints**. A significant exploratory result would need independent review, robustness checks and a better linguistic null before any general claim.

No experiment, source-rights, paper-ready, dataset-ready, Unicode-ready or historical-novelty promotion is authorized by this note.
