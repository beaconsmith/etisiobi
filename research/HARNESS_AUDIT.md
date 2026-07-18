# Harness Audit

> Structural repair log for the research operating system.
> Created: 2026-04-24.

## Findings Fixed

- Portfolio status now matches the local gate discipline: no candidate paper is treated as fully promoted to drafting.
- Tier A papers are marked as evidence-population / promotion candidates rather than draft-ready.
- Killed papers are explicitly dated and should remain dormant except for source redistribution.
- Missing runtime artifact types are now part of the required lab surface: `metrics.json`, `source_index.csv`, and `bib_status.csv`.

## Remaining Harness Risks

| Risk | Severity | Required fix |
|---|---:|---|
| Raw `icegov_2026` track folders and active `papers` folders can drift | High | Treat `icegov_2026` as archival; ingest useful facts into `papers/*` |
| Source registries are Markdown-first and not fully normalized | High | Keep `source_index.csv` updated for every paper |
| Bibliographic metadata is thin | High | Populate DOI/URL/read-status in `bib_status.csv` before submission |
| PAGC wiki is still a stub despite a large source base | Medium | Compile wiki and add falsification status table |
| Generated LaTeX/PDF artifacts are mixed with scripts and drafts | Medium | Later add `build/` or `.gitignore` cleanup; do not delete current artifacts without human approval |

## Definition Of Harness Done

- `PORTFOLIO.md`, `run_manifest.yaml`, and `promote_gate.yaml` agree.
- Active papers have populated evidence files.
- Killed papers are inert but searchable.
- Runtime JSON/CSV files provide machine-readable status.
- Reviewer attack surfaces are active, not placeholders.
- Every claim in a draft has a trace to `claim_map.md` and `source_registry.md`.
