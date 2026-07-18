# Nwagu Aneke Article Research Benchmark

Generated: `2026-06-21T02:46:40+01:00`

This benchmark is the anti-whack-a-mole control plane for the ten-article program.
It follows the Karpathy autoresearch pattern of fixed inputs, fixed evaluator,
one headline score, visible sub-scores, and keep/reject decisions. The metric
is adapted to research: lower research loss means fewer evidence, claim,
citation, reproducibility, and manuscript-readiness failures.

- Evidence completion score: `0.8582`
- Impact-journal readiness score (IJRS): `59.0` / 100
- Research loss: `0.1418`
- Status: `WORKING_PAPER_SET_NOT_IMPACT_READY`

## Hard Gates

- PASS: no source/derived, citation, or forbidden-overclaim hard gate failed.

## Caps

- Article 9 cannot exceed bounded-baseline status without downstream NLP task result.
- Article-specific novelty/prior-art gate failed; cap IJRS below impact-readiness.
- Rights/authority unresolved; cap IJRS below impact-readiness.
- Manuscripts are short working-paper drafts, not full impact-journal articles; cap IJRS below impact-readiness.

## Task Scores

| Task | Score | Evidence points | IJRS points | Pass |
|---|---:|---:|---:|---|
| Source-layer discipline and claim safety | 1.0 | 0.1 | 15.0 | `True` |
| Evidence ledger and citation reliability | 1.0 | 0.1 | 12.0 | `True` |
| Article-specific result strength | 0.9222 | 0.166 | 16.6 | `True` |
| Novelty against prior art | 0.72 | 0.0576 | 8.64 | `False` |
| Reproducible method/data/code | 0.9 | 0.108 | 9.0 | `True` |
| Reviewer attack-surface burn-down | 0.84 | 0.0672 | 8.4 | `True` |
| Rights, authority, CARE/community ethics | 0.55 | 0.044 | 4.4 | `False` |
| Manuscript coherence and venue fit | 0.65 | 0.065 | 5.2 | `False` |
| Field impact and reusable artifact value | 0.88 | 0.0704 | 6.16 | `True` |
| Benchmark comparability and keep/reject ledger | 1.0 | 0.08 | 0.0 | `True` |

## Article Quality

| Article | Words | Citations | Sections | Meta-note hits | Overclaim hits | Score |
|---|---:|---:|---:|---|---|---:|
| `001-source-critical-reconstruction` | 1425 | 14 | 9 | - | - | 0.65 |
| `002-count-layer-drift` | 1452 | 14 | 9 | - | - | 0.65 |
| `003-f-v-hinge` | 1438 | 13 | 9 | - | - | 0.65 |
| `004-logographs-in-a-syllabary` | 1439 | 15 | 9 | - | - | 0.65 |
| `005-tei-iiif-critical-edition` | 1451 | 15 | 9 | - | - | 0.65 |
| `006-unicode-readiness` | 1422 | 16 | 9 | - | - | 0.65 |
| `007-manuscript-corpus-provenance` | 1434 | 16 | 9 | - | - | 0.65 |
| `008-comparative-standardization` | 1432 | 16 | 9 | - | - | 0.65 |
| `009-igbo-tokenization` | 1466 | 18 | 9 | - | - | 0.65 |
| `010-layer-safe-generative-design` | 1439 | 14 | 9 | - | - | 0.65 |

## Keep/Reject Rule

Keep a manuscript revision only if it raises IJRS by at least five points,
removes a hard gate, or removes a cap without increasing overclaim risk.
Reject revisions that improve prose while weakening source-layer discipline.
