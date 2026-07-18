# Continuous Research Loop

Generated: 2026-06-27T18:34:43+01:00

This is the controlled autonomous loop for Etisiobi frontier research.

It is intentionally narrower than `scripts/research_loop.py`. The older loop can
regenerate broad scaffolding. This loop only:

1. reads canonical stage gates;
2. reads LPE-Bench and the Nwagu Transfer ATLAS;
3. ranks experiments;
4. writes a run trace;
5. blocks paper/readiness promotion.

## Current Research Object

Layer Promotion Error (LPE): an AI or research workflow promotes a claim from a
weaker evidence layer into a stronger one, for example treating a derived
27/216 f/v split as source-observed.

## Continuous Loop Command

```powershell
python scripts\continuous_research_loop.py --mode cycle --max-experiments 5
python scripts\validate_continuous_research_loop.py
```

## Promotion Rule

The loop may select experiments. It may not declare a paper complete. Paper
readiness remains governed by `research/LAB_STAGE_GATES.json`,
`research/A_PLUS_LAB_STANDARD.md`, and the review-team trace gate.
