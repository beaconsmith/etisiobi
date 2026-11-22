# EXP-NA-022 — Recoverability, underdetermination, and source-collation test

Date: 2026-11-22  
Status: **literature-attested microexperiment; no empirical manuscript-decoding result**  
Program: Nwagụ Aneke Frontier Lab  
Predecessor: EXP-NA-021 (contextual encoding topology)

## What changed

The 1992 Azuonye paper gives direct ambiguity examples:

- One written `bi` sign can express **obi, ubi, ibi or ebi**, in different contexts.
- One written `ma` sign can express **oma, ama, or uma**, among other forms.

Full reference: https://scholarworks.umb.edu/africana_faculty_pubs/13/ ; readable transcription https://paperzz.com/doc/9320092/the-nwagu-aneke-igbo-script---scholarworks-at-umass-boston , section on vowel-less syllables, text lines ~224-243. Azuonye says context or memory is needed to recover the original word.

The full 2010 Ahamefula article https://usemjournal.com/pdf/volume-3.pdf , **printed p.39 / PDF page index 38**, independently describes omitted syllabic nasals, vowel assimilation and absence of written word/sentence boundaries. The fixture `attested_microexamples.json` records *four selected short transformations* as author-reported examples, not as a general historical grammar or a fully reconstructed encoder.

**Important:** these are examples of **potential phonological/readback collapse**. They do not authorize treating the short printed Latin transcription as a validated machine-readable Aneke glyph or a one-to-one source mapping.

## Strong negative result: no context-free inverse

A deterministic map that omits the first independent vowel maps four listed words to the same `bi` written reading and three to `ma`. Therefore the inverse is **non-unique** even if the written syllable is recognized perfectly.

This is a small and valid deductive result about the **reported examples**, not a new global theorem or a measured reconstruction rate. Any software that silently returns one word from `bi` or `ma` has added an assumption.

For `k` listed candidate words, a **hypothetical uniform prior** yields `H(W | written form) = log2(k)`. Thus for these illustrative *candidate lists*, the conditional entropy is:

- `bi`: 2 bits with four equally likely candidates.
- `ma`: approximately 1.585 bits with three equally likely candidates.

But this is **not** observed uncertainty. Without corpus frequencies and compatible candidate coverage, the entropy is underdetermined: it can approach zero with a dominant candidate or approach `log2(k)` if candidates are equally likely. The audit prints both uniform and **synthetic skew-prior** scenarios to expose this dependency.

## Additional source-collation finding

The existing `CHART_TRANSCRIPTION.md` and its 30-record logograph lead list spell the **second full-word label `uche`**, vowel-initial. The image of the chart reproduced in the 2010 paper (**Appendix II, PDF zero-index page 42**) appears to spell that label **`nche`**, consonant-initial. The prose of the same paper (printed p.39, PDF page 38) instead spells **`uche`**.

This could reflect poor scan legibility, scribal variation, an editorial error, different signs, or an erroneous original transcription. **Do not silently correct `uche` to `nche`.** Obtain human source collation, and preferably compare the 1992 Azuonye chart and earlier proposal before deciding.

The previous EXP-NA-021's **29/30 vowel-initial** figure is therefore robust as a *property of the existing repo list*, but **not yet a verified source census**. If the page-42 reading `nche` is adjudicated, the same list would have **28/30** vowel-initial labels. Neither result is an enrichment or causal estimate because the sample is selective and Igbo nominal forms often begin with vowels.

## Computation

```bash
python3 scripts/audit_nwagu_lossy_channel.py
python3 -m unittest discover -s tests/research -p 'test_nwagu_lossy_channel.py' -v
```

The script is intentionally **read-only** and returns:
- two source-attested ambiguous-readback groups;
- explicit theoretical entropy bounds, labeled non-empirical;
- four distinct source-attested short transformation examples;
- a sensitivity report for the unadjudicated chart/prose conflict;
- no fabricated decoder accuracy, language-model score, alignment, or source authentication.

## Research opening: reversible, abstention-first manuscript reading

The data supports an important **design requirement**, not a validated product:

1. Start from a rights-cleared image location and a *human-confirmed glyph identity*.
2. Link it to candidate syllables and possible word-level readings rather than overwrite the image with one chosen transliteration.
3. Record which transforms could explain each candidate (vowel omission, nasal omission, assimilation, missing boundary, shared f/v), along with language/genre evidence.
4. Return multiple candidates or **abstain** when no validated context establishes a unique reading.
5. Evaluate on *held-out, independently annotated* authentic passages. Report candidate coverage, abstention, word error and calibration; compare against a simple lexical baseline.
6. Review editorial corrections and historical reading rights through cultural/linguistic authorities.

Potential downstream outputs: reversible manuscript transcription, uncertainty-linked critical editions, digitization pedagogy, and bounded language-technology experiments. None has been demonstrated at runtime.

## Stop conditions

Do not claim contextual entropy reduction, original historical intent, historical logograph selection mechanism, universal compression, `164 = 208` reconciliation, Unicode-ready codepoints, or glyph-identification accuracy from this experiment.

**Next decisive source dependency:** independent collation of the Appendix II label, then one rights-cleared *glyph/Latin reading/meaning* alignment from the published 1978 or 1980 sample and an independent held-out comparison.
