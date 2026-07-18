---
type: research_goal
goal_id: GOAL-CONT-001
status: active
created: "2026-06-27T18:34:43+01:00"
updated: "2026-06-27T18:34:43+01:00"
program: nwagu_aneke_frontier
stage: RESEARCH_PROGRAM
---

# GOAL-CONT-001: Continuous Autonomous Research Loop

## Objective

Continuously convert the Nwagu transfer atlas and LPE-Bench into bounded,
validated research iterations without generating paper-looking outputs before
the evidence stage permits them.

## Current foundation

- Source-observed layer: 26 rows x 8 vowel/modifier columns = 208 records.
- 27/216 is a derived f/v split layer only.
- LPE-Bench is the current measurable failure detector.
- Nwagu Transfer ATLAS is the current experiment queue.
- Selected infrastructure prior-art verification is relevance-only and does not
  clear novelty or the whole atlas.

## Loop

1. Read canonical memory and stage gates.
2. Freeze current atlas, LPE manifest, branch, and dirty status.
3. Rank next experiments by evidence readiness, rights risk, negative control,
   reproducibility, and article potential.
4. Select a small active batch.
5. Write a run manifest and decision trace.
6. Run validators.
7. Update only research-state artifacts, never public-readiness claims.

## Stop rules

- Do not create impact-journal or arXiv-ready claims from this loop.
- Do not render new paper PDFs.
- Do not treat seeded prior art as verified.
- Do not treat selected prior-art relevance as novelty clearance.
- Do not treat AI-only labels as human/domain gold.
- Do not promote high-rights-risk artifact work without authority review.

## Success criteria

- Every run leaves a machine-readable manifest.
- Every selected experiment has a negative control and claim ceiling.
- The next action is inspectable by a human.
- `python scripts/validate_continuous_research_loop.py` passes.

## Next command

```powershell
python scripts\continuous_research_loop.py --mode cycle --max-experiments 5
```
