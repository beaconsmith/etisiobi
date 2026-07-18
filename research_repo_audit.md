# Research Repo Audit

Generated: 2026-05-28

## Scope

This is a Phase 0-4 read-only-informed audit plus generated bootstrap overlay. No experiments were executed, no dependencies were installed, no data was uploaded, and no submissions were attempted.

## OBSERVED: Git state

```text
## research-hyperloop/bootstrap
 M .claude/settings.local.json
 M .gitignore
 M .obsidian/graph.json
 M .obsidian/workspace.json
 D "216, k, d.md"
 M README.md
 D RESEARCH_SPINE.md
 M log.md
 D research/icegov/CONTRADICTIONS.md
 M research/icegov/INDEX.md
 M research/icegov/WIKI.md
 M research/icegov/WORKSPACE.md
 M research/icegov/paper/OGI_PAPER_DRAFT_v5.md
 M research/icegov/paper/autoresearch-v6.md
 M research/pagc/INDEX.md
 M research/pagc/WIKI.md
 M research/pagc/paper/kb/nwagu_aneke_syllabary.md
 D sources/download_manifest.jsonl
 D sources/full_missing_sources_list.md
 D sources/missing_report_metadata.json
 D sources/research_pipeline/__pycache__/data_filters.cpython-314.pyc
 D sources/research_pipeline/data_filters.py
 D sources/research_pipeline/gather_frontier.py
 D sources/research_pipeline/gather_sources.py
 D sources/research_pipeline/paper_downloader.py
 D sources/research_pipeline/retry_failed.py
 D sources/research_pipeline/retry_unpaywall.py
 D sources/retry_failed.log
 D sources/retry_unpaywall.log
 D sources/session_02_downloads.md
 D sources/sort_sources.py
?? AGENTS.md
?? CONTRIBUTING.md
?? ETISIOBI_KNOWLEDGE_PIPELINE.md
?? ETISIOBI_OROMA_FEED.md
?? ETISIOBI_RESEARCH_DOCTRINE.md
?? Makefile
?? "NS modifier/"
?? data/
?? library/
?? research/AGENTS.md
?? research/CHIEF_OF_STAFF.md
?? research/CITATION_POLICY.md
?? research/EVIDENCE_POLICY.md
?? research/HARNESS_AUDIT.md
?? research/KILL_CRITERIA.md
?? research/LAB_DASHBOARD.md
?? research/PORTFOLIO.md
?? research/QUALITY_BAR.md
?? research/RESEARCH_ORG.md
?? research/SUBMISSION_RULES.md
?? research/icegov/RESEARCH_CONTRADICTIONS.md
?? research/icegov/paper/CDGI_ARXIV_NAMED.tex
?? research/icegov/paper/CDGI_GIQ_ANONYMOUS.tex
?? research/icegov/paper/CDGI_ICEGOV2026_Submission.tex
?? research/icegov/paper/CDGI_ICEGOV2026_Submission_package.zip
?? research/icegov/paper/GIQ_Author_Biography.txt
?? research/icegov/paper/GIQ_Cover_Letter.tex
?? research/icegov/paper/GIQ_Highlights.txt
?? research/icegov/paper/GIQ_Submission_Drafts.md
?? research/icegov/paper/GIQ_Title_Page.tex
?? research/icegov/paper/OGI_ARXIV_NAMED.tex
?? research/icegov/paper/OGI_ICEGOV_SUBMISSION_v2.tex
?? research/icegov/paper/OGI_ICIS2026_DOUBLEBLIND.tex
?? research/icegov/paper/OGI_PAPER_DRAFT_v6.md
?? research/icegov/paper/OGI_PAPER_DRAFT_v7.md
?? research/icegov/paper/OGI_PAPER_DRAFT_v8.md
?? research/icegov/paper/OGI_PAPER_SUBMISSION_CANONICAL.md
?? research/icegov/paper/OGI_PAPER_SUBMISSION_CANONICAL.tex
?? research/icegov_2026/
?? research/pagc/BMCG_SPEC_V0_1.md
?? research/pagc/CLAIM_GATE_REPORT.md
?? research/pagc/FALSIFICATION_TRACKER.md
?? research/pagc/PAGC_RESET.md
?? research/pagc/primary_sources/
?? research/pagc/schema/
?? research/papers/
?? research/product_feedback/
?? scripts/
?? spine/ARCHITECTURE.md
?? spine/pagc_claim_gate.py
?? spine/research_feedback.py
```

## OBSERVED: Repo structure

- Markdown dominates the repository: 1661 `.md` files.
- Python appears in experiment, spine, and research pipeline code.
- TypeScript/Next code appears under `NS modifier/`.
- LaTeX drafts already exist under `research/icegov/`, `research/icegov_2026/`, and `research/papers/*/writing/`.
- Data and metadata include CSV, JSON, JSONL, YAML, PDFs, images, a gzipped corpus, and result logs.

## OBSERVED: Existing research harness

- `research/PORTFOLIO.md` identifies active ICEGOV 2026 papers and killed/parked tracks.
- `research/papers/*/runtime/` contains `run_manifest.yaml`, `promote_gate.yaml`, `metrics.json`, `source_index.csv`, and `bib_status.csv` for all seven paper folders.
- `research/QUALITY_BAR.md`, `research/EVIDENCE_POLICY.md`, and `research/CITATION_POLICY.md` define promotion and citation standards.

## OBSERVED: Code paths

- `spine/extractor.py` is the evidence extraction engine surface.
- `library/research_pipeline/*.py` contains source download and filtering utilities.
- `experiments/01_bpe_igbo_k27/train_bpe_sweep.py` is the BPE sweep path.
- `experiments/05_sovereign_memory_rl/run_simulation.py` is the memory simulation path.
- `NS modifier/` contains a separate TypeScript application workspace.

## OBSERVED: Datasets and results

- `data/igbo_corpus/` contains train, validation, test, merged, and raw files.
- `experiments/01_bpe_igbo_k27/results/` contains metrics, figure, and report output.
- `experiments/05_sovereign_memory_rl/results/` contains an output figure.
- `library/papers/` contains a large PDF corpus with topical subdirectories.

## OBSERVED: Tests and CI

- Tests exist under `NS modifier/packages/*/test/` and `NS modifier/apps/dashboard/test/`.
- No `.github/` CI files were detected in the current file list.
- No project tests were executed in this bootstrap pass.

## OBSERVED: Secret-risk scan

Values were not printed. Path-level risk hits:

| Path | Match count |
|---|---:|
| `NS modifier/node_modules/next/dist/compiled/babel/bundle.js` | 838 |
| `NS modifier/node_modules/eslint/lib/rules/indent.js` | 812 |
| `NS modifier/node_modules/viem/_types/tempo/actions/token.d.ts` | 754 |
| `NS modifier/node_modules/hermes-estree/dist/generated/predicates.js` | 682 |
| `NS modifier/node_modules/viem/tempo/actions/token.ts` | 676 |
| `NS modifier/node_modules/typescript/lib/typescript.d.ts` | 670 |
| `NS modifier/node_modules/markdown-it/dist/markdown-it.js` | 663 |
| `NS modifier/node_modules/markdown-it/dist/index.cjs.js` | 662 |
| `NS modifier/node_modules/@babel/parser/lib/index.js` | 622 |
| `NS modifier/node_modules/next/dist/compiled/@vercel/og/index.edge.js` | 585 |
| `NS modifier/node_modules/next/dist/compiled/@vercel/og/index.node.js` | 585 |
| `NS modifier/node_modules/viem/tempo/Decorator.ts` | 576 |
| `NS modifier/node_modules/viem/_types/tempo/Decorator.d.ts` | 521 |
| `NS modifier/node_modules/viem/_esm/tempo/actions/token.js` | 489 |
| `NS modifier/node_modules/eslint/lib/rules/utils/ast-utils.js` | 422 |
| `NS modifier/node_modules/next/dist/compiled/terser/bundle.min.js` | 380 |
| `NS modifier/node_modules/@eslint-community/eslint-utils/index.js` | 328 |
| `NS modifier/node_modules/@eslint-community/eslint-utils/index.mjs` | 306 |
| `NS modifier/node_modules/eslint/lib/languages/js/source-code/token-store/index.js` | 306 |
| `NS modifier/node_modules/next/dist/compiled/comment-json/index.js` | 303 |
| `NS modifier/node_modules/@types/node/crypto.d.ts` | 290 |
| `NS modifier/node_modules/eslint/lib/rules/keyword-spacing.js` | 286 |
| `NS modifier/node_modules/@shikijs/vscode-textmate/dist/index.js` | 269 |
| `NS modifier/node_modules/ox/tempo/e2e.test.ts` | 265 |
| `library/download_manifest.jsonl` | 263 |
| `NS modifier/node_modules/viem/_types/tempo/actions/dex.d.ts` | 260 |
| `NS modifier/node_modules/doctrine/lib/typed.js` | 244 |
| `NS modifier/node_modules/lunr/lunr.js` | 243 |
| `NS modifier/.next/build/chunks/node_modules_13sb.px._.js` | 242 |
| `NS modifier/apps/dashboard/.next/build/chunks/node_modules_13sb.px._.js` | 242 |
| `NS modifier/apps/dashboard/.next/dev/build/chunks/node_modules_13sb.px._.js` | 242 |
| `library/missing_report_metadata.json` | 240 |
| `NS modifier/node_modules/abitype/dist/types/generated.d.ts` | 236 |
| `NS modifier/node_modules/abitype/src/generated.ts` | 236 |
| `NS modifier/node_modules/acorn/dist/acorn.js` | 235 |
| `NS modifier/node_modules/viem/_types/tempo/actions/amm.d.ts` | 235 |
| `NS modifier/node_modules/viem/tempo/actions/amm.ts` | 233 |
| `NS modifier/node_modules/acorn/dist/acorn.mjs` | 232 |
| `NS modifier/node_modules/postcss/lib/parser.js` | 210 |
| `NS modifier/node_modules/next/node_modules/postcss/lib/parser.js` | 203 |

## DERIVED: Main research object

The repo studies and operationalizes community-led digital governance evidence systems and a separate PAGC falsification program. It is not a single-paper repo; it is a portfolio-oriented research lab with code, source corpora, paper harnesses, and experiment outputs.

## Immediate risks

- Deadline drift: internal files disagree between April 24, 2026 and May 8, 2026 for ICEGOV-related work.
- Format drift: the repo submission rules specify ACM `sigconf`, while the requested bootstrap prompt asks for `manuscript`.
- PAGC core number drift: the falsification tracker records 26-28 observed base rows while other files use 27.
- Citation metadata remains a known risk where downloaded PDFs and Markdown source registries are not fully normalized.
- `.env.local` and `.env.production` style files exist under `NS modifier/`; they require redaction review before publication or sharing.

## Missing pieces

- A unified machine-readable claim ledger across all papers.
- A repo-level citation audit that connects paper claims to source registry rows.
- A clean separation between generated paper outputs and editable source artifacts.
- A dry-run research loop that updates corpus, goals, vault, and paper scaffold without running compute.
