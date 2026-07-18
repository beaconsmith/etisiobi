---
type: usability_packet_index
program: nwagu_aneke_frontier
status: protocol_ready_with_scorer_no_human_results
created: "2026-06-22"
goal: GOAL-FRONTIER-001
claim_ceiling: human_comprehension_signal_not_source_evidence
prototype: research/frontier/nwagu_aneke/interfaces/count_layer_static_prototype.html
---

# Count-Layer Comprehension Packet

This packet tests whether the count-layer prototype lets a reader distinguish
`26/208` as the current source-observed Appendix I chart layer from `27/216` as
a derived f/v split. It is not human evidence yet.

## Files

- `count_layer_comprehension_protocol.md` - protocol, scoring, failure
  thresholds, and rights/authority limits.
- `count_layer_comprehension_questions.csv` - task prompts and expected
  answers.
- `count_layer_comprehension_results_template.csv` - result-capture template
  for a later human run.
- `count_layer_reader_run_sheet.md` - operator steps for a 3-5 reader run.
- `count_layer_response_scoring_guide.md` - answer scoring rules and confusion
  types.
- `responses/` - directory for future dated response CSVs without private
  contact data.
- `internal_self_audit.md` - internal preflight notes before any human review.
- `scripts/score_count_layer_comprehension_results.py` - scoring command that
  emits `PASS_INTERNAL_COMPREHENSION_CHECK`,
  `FAIL_LABEL_REVISION_REQUIRED`, or `INVALID_READER_RUN`.

## Scope

The packet checks reader comprehension only. It does not validate Nwagu Aneke
source facts, approve glyph use, recover Appendix II, resolve rights, or
substitute for authority review. There are no source images in this packet.

## Exact Next Action

Run the protocol with 3-5 human readers, save a dated response CSV under
`responses/`, then score it with:

```powershell
python scripts\score_count_layer_comprehension_results.py research\frontier\nwagu_aneke\interfaces\usability\responses\count_layer_results_YYYYMMDD.csv
```

If the scorer returns `FAIL_LABEL_REVISION_REQUIRED`, revise labels in the
prototype before any broader circulation.
