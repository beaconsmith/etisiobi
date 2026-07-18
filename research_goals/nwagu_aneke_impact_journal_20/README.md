# Nwagu Aneke All-20 Impact-Journal Hardening Control Room

Status: `ALL_20_HARDENING_PLANNED_NOT_IMPACT_READY`

This folder records the human portfolio decision to pursue all 20 Nwagu Aneke
articles toward impact-journal acceptance. It does not mark any article ready
for external submission.

## Current Count

- External accepted papers: 0.
- Internal research papers: 20.
- arXiv quality gate pass count: 6 / 20.
- Strongest first hardening targets: `ARTICLE-NA-001`, `ARTICLE-NA-002`, `ARTICLE-NA-003`, `ARTICLE-NA-004`, `ARTICLE-NA-005`, and `ARTICLE-NA-010`.

## Operating Rule

All 20 articles may be developed, but each article must independently pass:

1. Article-specific prior-art audit.
2. Human source review.
3. Rights and source-authority clearance.
4. Article-specific experiment or source-critical result.
5. Figures/tables manifest.
6. Reviewer 2 response plan.
7. Manuscript rewrite that removes internal lab-process framing.
8. `python scripts\validate_arxiv_quality_gate.py`.
9. `python scripts\validate_lab_standard.py`.
10. `python scripts\validate_review_team_gate.py`.

No article may be called impact-journal ready before these gates pass.

## Lanes

| Lane | Articles | Current Use |
|---|---|---|
| A | `ARTICLE-NA-002`, `ARTICLE-NA-010` | First serious hardening pass. |
| B | `ARTICLE-NA-001`, `ARTICLE-NA-003` to `ARTICLE-NA-009` | Upgrade working drafts into article candidates. |
| C | `ARTICLE-NA-011` to `ARTICLE-NA-020` | Rebuild quarantined process traces into substantive methods/result papers. |

## Exact Next Action

Continue with `ARTICLE-NA-006`: `ARTICLE-NA-001`, `ARTICLE-NA-002`,
`ARTICLE-NA-003`, `ARTICLE-NA-004`, `ARTICLE-NA-005`, and `ARTICLE-NA-010`
now pass the repo arXiv-quality validator, but human source review,
rights/submission clearance, adversarial journal review, and venue decisions
remain missing. The next repo-local action is to harden the Unicode-readiness
paper with an evidence gap matrix, article-specific evidence pack, manuscript
rewrite, and explicit rights/source blockers.
