# BPE Sweep Results — PAGC k=27 Hypothesis

**Date:** 2026-04-14 07:12
**Corpus:** Igbo text (7,368 test words)
**Sweep range:** k=15 to k=50
**Method:** BPE (Byte Pair Encoding) via HuggingFace `tokenizers`

## Verdict: REFUTED (inflection at k=16, not k=27)

| Metric                  | Value |
|-------------------------|-------|
| Detected inflection k   | 16 |
| k=27 fertility          | 4.7759 |
| k=27 coverage           | 0.9995 |
| Best k by fertility     | 80 |

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
| 10 | 5.1754 | 1.000 | 1.10 |
| 11 | 5.1489 | 1.000 | 1.10 |
| 12 | 5.1204 | 1.000 | 1.11 |
| 13 | 5.0949 | 1.000 | 1.12 |
| 14 | 5.0615 | 1.000 | 1.12 |
| 15 | 5.0309 | 1.000 | 1.13 |
| 16 | 5.0062 | 1.000 | 1.14 | *(inflection)*
| 17 | 4.9834 | 1.000 | 1.14 |
| 18 | 4.9604 | 1.000 | 1.15 |
| 19 | 4.9377 | 1.000 | 1.15 |
| 20 | 4.9154 | 1.000 | 1.16 |
| 21 | 4.8948 | 1.000 | 1.16 |
| 22 | 4.8711 | 1.000 | 1.17 |
| 23 | 4.8512 | 1.000 | 1.17 |
| 24 | 4.8321 | 1.000 | 1.18 |
| 25 | 4.8143 | 1.000 | 1.18 |
| 26 | 4.7942 | 1.000 | 1.19 |
| 27 | 4.7759 | 1.000 | 1.19 | **<-- PAGC**
| 28 | 4.7586 | 1.000 | 1.19 |
| 29 | 4.7408 | 1.000 | 1.20 |
| 30 | 4.725 | 1.000 | 1.20 |
| 31 | 4.7077 | 1.000 | 1.21 |
| 32 | 4.6881 | 1.000 | 1.21 |
| 33 | 4.6733 | 1.000 | 1.22 |
| 34 | 4.6581 | 1.000 | 1.22 |
| 35 | 4.6412 | 1.000 | 1.22 |
| 36 | 4.6268 | 1.000 | 1.23 |
| 37 | 4.6124 | 1.000 | 1.23 |
| 38 | 4.5987 | 1.000 | 1.24 |
| 39 | 4.5865 | 1.000 | 1.24 |
| 40 | 4.5723 | 1.000 | 1.24 |
| 41 | 4.5586 | 1.000 | 1.25 |
| 42 | 4.5444 | 1.000 | 1.25 |
| 43 | 4.5326 | 1.000 | 1.25 |
| 44 | 4.5197 | 1.000 | 1.26 |
| 45 | 4.5069 | 1.000 | 1.26 |
| 46 | 4.4952 | 1.000 | 1.26 |
| 47 | 4.4821 | 1.000 | 1.27 |
| 48 | 4.468 | 1.000 | 1.27 |
| 49 | 4.4549 | 1.000 | 1.28 |
| 50 | 4.4442 | 1.000 | 1.28 |
| 51 | 4.4312 | 1.000 | 1.28 |
| 52 | 4.4218 | 1.000 | 1.29 |
| 53 | 4.408 | 1.000 | 1.29 |
| 54 | 4.3958 | 1.000 | 1.29 |
| 55 | 4.3844 | 1.000 | 1.30 |
| 56 | 4.372 | 1.000 | 1.30 |
| 57 | 4.362 | 1.000 | 1.30 |
| 58 | 4.3519 | 1.000 | 1.31 |
| 59 | 4.3417 | 1.000 | 1.31 |
| 60 | 4.3335 | 1.000 | 1.31 |
| 61 | 4.3236 | 1.000 | 1.31 |
| 62 | 4.3139 | 1.000 | 1.32 |
| 63 | 4.304 | 1.000 | 1.32 |
| 64 | 4.2929 | 1.000 | 1.32 |
| 65 | 4.2826 | 1.000 | 1.33 |
| 66 | 4.2735 | 1.000 | 1.33 |
| 67 | 4.2644 | 1.000 | 1.33 |
| 68 | 4.2553 | 1.000 | 1.34 |
| 69 | 4.2451 | 1.000 | 1.34 |
| 70 | 4.2374 | 1.000 | 1.34 |
| 71 | 4.2291 | 1.000 | 1.34 |
| 72 | 4.2199 | 1.000 | 1.35 |
| 73 | 4.2132 | 1.000 | 1.35 |
| 74 | 4.206 | 1.000 | 1.35 |
| 75 | 4.1982 | 1.000 | 1.35 |
| 76 | 4.192 | 1.000 | 1.36 |
| 77 | 4.1832 | 1.000 | 1.36 |
| 78 | 4.1764 | 1.000 | 1.36 |
| 79 | 4.1699 | 1.000 | 1.36 |
| 80 | 4.165 | 1.000 | 1.36 |

## What Next
1. If SUPPORTS: run at scale with CC-100 Igbo corpus (~15MB)
2. If REFUTED: investigate whether the detected inflection k is meaningful
   for other tone languages (Yoruba, Ewe) — is it language-specific?
3. Compare k-optimal for English, Swahili, Yoruba, Hausa on same corpus size
4. Run MDL comparison: is PAGC 27×8=216 matrix competitive with k-optimal BPE?
