# EXP-0001 Analysis

## Question

Does repo-local primary evidence resolve the PAGC 26/27/28 foundation-count drift?

## Method

The audit used the archived Azuonye 1992 PDF, a `pdftotext` extraction log, the rendered appendix page, the archived Omniglot chart image, and the existing chart transcription. The decisive countable artifact is Appendix I: a chart titled "Syllabary of the Nwagu Aneke Script."

## Observations

- The chart has 26 printed consonant rows.
- The chart has 8 vowel columns.
- The `f/v` row is a combined printed row. Splitting it gives a possible derived phonemic count of 27, but that is not a separate printed row.
- The primary printed grid therefore gives 26 x 8 = 208 visible CV cells before derived normalization.
- A 27 x 8 = 216 matrix is recoverable only as a theoretical normalization after splitting `f/v`.
- The chart also has a separate full-word-symbol list of about 30 visible entries.

## Interpretation

The contradiction is not a clean RESOLVED_27 result. It is a layered-count problem: 26 source rows, 27 possible derived phonemic bases, and 216 possible derived slots. Downstream claims must state which layer they use.

## Result

Decision: MULTI_LAYER_COUNT_VALID.
