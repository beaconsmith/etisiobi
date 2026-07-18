# Nwagu Aneke Character-Glyph Distinction Matrix

Status: `CHARACTER_GLYPH_REVIEW_REQUIRED`

Do not submit this matrix as a Unicode character-glyph decision.

Unicode proposal work requires deciding which observed signs are abstract
characters, which are glyph variants, which are sequences, and which are
editorial or derived analysis artifacts. The current repo can state the review
questions, but cannot yet answer them for a full repertoire.

| Candidate object | Current evidence | Unicode question | Current decision |
|---|---|---|---|
| 26 row labels | Source-observed chart labels | Are these consonant bases, row headings, or character classes? | Review required |
| 8 vowel/modifier columns | Source-observed chart labels | Are these dependent signs, inherent-vowel modifiers, or table axes only? | Review required |
| 208 source table cells | Source-observed grid model | Are cells atomic syllabic characters, sequences, or glyph forms? | Review required |
| f/v split | Derived analytical operation | Does Unicode need one source row, two characters, or sequences? | Derived only until reviewed |
| About 30 whole-word signs | Aggregate source observation | Are these logographs, abbreviations, words, or non-encoded symbols? | Source extraction required |
| 164 actual-symbol lead | Ahamefula/Mbah external lead | Does this supersede, refine, or describe a different count type? | External source extraction required |
| 224 ideal-space lead | Ahamefula/Mbah external lead | Is this an ideal syllable space rather than an encoded repertoire? | External source extraction required |

## Required Review Output

A proposal-ready character-glyph matrix must include:

- proposed character identifier;
- representative glyph or source example;
- source citation and locator;
- decision: character, glyph variant, sequence, punctuation, number, symbol,
  logograph, or not encoded;
- reason for rejecting existing Unicode equivalents or sequences;
- rights status for any example;
- reviewer name/date or accountable review record.

Current decision:

`DO_NOT_USE_AS_REPERTOIRE_PROPOSAL`
