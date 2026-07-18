---
type: reader_run_sheet
program: nwagu_aneke_frontier
status: run_sheet_ready_no_human_results
created: "2026-06-22"
goal: GOAL-FRONTIER-001
claim_ceiling: human_comprehension_signal_not_source_evidence
---

# Count-Layer Reader Run Sheet

## Purpose

Run a small comprehension check for the count-layer prototype without converting
reader comprehension into source evidence. The target question is narrow:
can readers keep `26/208` source-observed and `27/216` derived?

## Materials

- Prototype:
  `research/frontier/nwagu_aneke/interfaces/count_layer_static_prototype.html`
- Questions:
  `research/frontier/nwagu_aneke/interfaces/usability/count_layer_comprehension_questions.csv`
- Results template:
  `research/frontier/nwagu_aneke/interfaces/usability/count_layer_comprehension_results_template.csv`
- Scoring guide:
  `research/frontier/nwagu_aneke/interfaces/usability/count_layer_response_scoring_guide.md`
- Scorer:
  `scripts/score_count_layer_comprehension_results.py`

## Reader Selection

Use 3-5 readers. Assign respondent IDs such as `R001`, `R002`, and `R003`.
Do not store private contact data in this repo. Record only the reader role
needed for interpretation, such as `researcher`, `designer`, `engineer`, or
`general_reader`.

## Procedure

1. Give the reader the prototype file only.
2. Ask the reader to inspect it for 5-8 minutes.
3. Ask the reader the ten questions in the question CSV.
4. Record answers in a copy of the results template.
5. Score each answer as `correct`, `partial`, or `incorrect` using the scoring
   guide.
6. Run the scoring script.

Example command:

```powershell
python scripts\score_count_layer_comprehension_results.py research\frontier\nwagu_aneke\interfaces\usability\responses\count_layer_results_YYYYMMDD.csv
```

## Interpretation

Allowed result labels:

- `PASS_INTERNAL_COMPREHENSION_CHECK`
- `FAIL_LABEL_REVISION_REQUIRED`
- `INVALID_READER_RUN`

The highest claim ceiling is
`human_comprehension_signal_not_source_evidence`. A passing score only says
that a small reader group understood the prototype labels. It does not validate
Nwagu source facts, rights, authority, Appendix II, PAGC, or future publication
claims.

## Exact Next Action

Create a dated response CSV under `usability/responses/` after human readers
answer the questions, then run the scoring script and record the output in the
log.
