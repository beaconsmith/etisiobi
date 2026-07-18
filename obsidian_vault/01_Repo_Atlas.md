---
type: repo_atlas
id: "ATLAS"
status: "active"
confidence: 0.8
created: "2026-05-28"
updated: "2026-05-28"
tags: [repo_atlas]
links: []
---

# Repo Map

Generated: 2026-05-28

## OBSERVED: Top-level structure

| Entry | Kind |
|---|---|
| `.claude` | dir |
| `.gitignore` | file |
| `.obsidian` | dir |
| `AGENTS.md` | file |
| `CLAUDE.md` | file |
| `CONTRIBUTING.md` | file |
| `data` | dir |
| `ETISIOBI_KNOWLEDGE_PIPELINE.md` | file |
| `ETISIOBI_OROMA_FEED.md` | file |
| `ETISIOBI_RESEARCH_DOCTRINE.md` | file |
| `experiments` | dir |
| `library` | dir |
| `log.md` | file |
| `Makefile` | file |
| `meta` | dir |
| `NS modifier` | dir |
| `README.md` | file |
| `research` | dir |
| `scripts` | dir |
| `skills` | dir |
| `spine` | dir |

## OBSERVED: Artifact classes

| Class | Count |
|---|---:|
| config_build | 91 |
| datasets_or_metadata | 488 |
| dependency_manifest | 867 |
| license | 477 |
| model_training_or_evaluation_code | 3 |
| notes | 1558 |
| papers_drafts | 521 |
| results_logs_figures | 26 |
| scripts | 22 |
| source_code | 24139 |
| tests | 895 |
| unknown | 12276 |
| unknown_high_risk | 21 |

## OBSERVED: Major program areas

- `research/icegov/`: OGI framework wiki, sources, contradictions, and paper drafts.
- `research/pagc/`: PAGC wiki, falsification tracker, source gates, knowledge base, and paper material.
- `research/papers/`: Seven ICEGOV 2026 candidate paper harnesses with runtime manifests, evidence maps, and writing folders.
- `experiments/`: PAGC experiment code and generated results.
- `library/`: Downloaded papers, source manifests, and research pipeline scripts.
- `spine/`: Research Spine design and evidence extraction code.
- `NS modifier/`: Nested TypeScript/Next application and package workspace.

## DERIVED: Working topology

The repository is a research operating system with three layers:

1. Evidence and source acquisition: `library/`, `data/`, `research/*/sources/`, `spine/`.
2. Research control plane: `research/AGENTS.md`, `research/PORTFOLIO.md`, `research/papers/*/runtime/`, evidence maps.
3. Publication and experiment outputs: `research/*/paper/`, `research/papers/*/writing/`, `experiments/*/results/`.

## Immediate map risks

- Active and generated paper outputs are mixed with source material.
- `research/icegov_2026/` archival logs can drift from `research/papers/` active state.
- Secret-risk paths exist, including `.env`-style files; values were not printed.
