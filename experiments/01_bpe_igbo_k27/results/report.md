# BPE Sweep Results — PAGC k=27 Hypothesis

**Date:** 2026-04-14 07:06
**Corpus:** Igbo text (7,368 test words)
**Sweep range:** k=15 to k=50
**Method:** BPE (Byte Pair Encoding) via HuggingFace `tokenizers`

## Verdict: REFUTED (inflection at k=15, not k=27)

| Metric                  | Value |
|-------------------------|-------|
| Detected inflection k   | 15 |
| k=27 fertility          | 5.683 |
| k=27 coverage           | 0.9995 |
| Best k by fertility     | 15 |

## Hypothesis
PAGC claims that 27 base symbols is the natural optimal vocabulary for Igbo.
If valid: the fertility curve (tokens per word) should show a **knee at k≈27**,
where diminishing returns set in — more vocabulary above 27 yields minimal gain.

## Falsification Condition
If the knee appears at k != 27 (±2), the specific PAGC k=27 claim is **refuted**
for this corpus. The broader compression argument may still hold at whatever k
the knee appears.

## Full Metrics Table

| k | Fertility | Coverage | Chars/Tok |
|---|-----------|----------|-----------|
| 15 | 5.683 | 1.000 | 1.00 | *(inflection)*
| 16 | 5.683 | 1.000 | 1.00 |
| 17 | 5.683 | 1.000 | 1.00 |
| 18 | 5.683 | 1.000 | 1.00 |
| 19 | 5.683 | 1.000 | 1.00 |
| 20 | 5.683 | 1.000 | 1.00 |
| 21 | 5.683 | 1.000 | 1.00 |
| 22 | 5.683 | 1.000 | 1.00 |
| 23 | 5.683 | 1.000 | 1.00 |
| 24 | 5.683 | 1.000 | 1.00 |
| 25 | 5.683 | 1.000 | 1.00 |
| 26 | 5.683 | 1.000 | 1.00 |
| 27 | 5.683 | 1.000 | 1.00 | **<-- PAGC**
| 28 | 5.683 | 1.000 | 1.00 |
| 29 | 5.683 | 1.000 | 1.00 |
| 30 | 5.683 | 1.000 | 1.00 |
| 31 | 5.683 | 1.000 | 1.00 |
| 32 | 5.683 | 1.000 | 1.00 |
| 33 | 5.683 | 1.000 | 1.00 |
| 34 | 5.683 | 1.000 | 1.00 |
| 35 | 5.683 | 1.000 | 1.00 |
| 36 | 5.683 | 1.000 | 1.00 |
| 37 | 5.683 | 1.000 | 1.00 |
| 38 | 5.683 | 1.000 | 1.00 |
| 39 | 5.683 | 1.000 | 1.00 |
| 40 | 5.683 | 1.000 | 1.00 |
| 41 | 5.683 | 1.000 | 1.00 |
| 42 | 5.683 | 1.000 | 1.00 |
| 43 | 5.683 | 1.000 | 1.00 |
| 44 | 5.683 | 1.000 | 1.00 |
| 45 | 5.683 | 1.000 | 1.00 |
| 46 | 5.683 | 1.000 | 1.00 |
| 47 | 5.683 | 1.000 | 1.00 |
| 48 | 5.683 | 1.000 | 1.00 |
| 49 | 5.683 | 1.000 | 1.00 |
| 50 | 5.683 | 1.000 | 1.00 |

## What Next
1. If SUPPORTS: run at scale with CC-100 Igbo corpus (~15MB)
2. If REFUTED: investigate whether the detected inflection k is meaningful
   for other tone languages (Yoruba, Ewe) — is it language-specific?
3. Compare k-optimal for English, Swahili, Yoruba, Hausa on same corpus size
4. Run MDL comparison: is PAGC 27×8=216 matrix competitive with k-optimal BPE?
