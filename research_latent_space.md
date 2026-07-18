# Latent Research Space

## Axis 1: Problem formulation

- Current formulation: evidence-first research operating system for OGI/ICegov and PAGC.
- Alternative formulations: paper factory, source verification engine, product-research telemetry spine, falsification lab.
- What changes if the objective changes? Paper throughput optimizes drafting; falsification optimizes truth preservation; product spine optimizes computability.

## Axis 2: Representation

- Current representation: Markdown, LaTeX, YAML, JSON, CSV, PDFs, images.
- Alternative representations: unified claim graph, source database, typed evidence schema.
- Compression/abstraction opportunities: normalize source registries and claim maps into JSONL.

## Axis 3: Mechanism / algorithm

- Current mechanism: autoresearch loop plus paper-specific gates and human-readable evidence files.
- Replaceable modules: claim extraction, citation verification, goal scoring, experiment runner.
- Search space: source acquisition, contradiction mining, baseline experiments, reviewer attack-surface reduction.

## Axis 4: Evaluation

- Current metrics: paper gate status, evidence counts, BPE metrics, falsification decisions.
- Missing metrics: citation faithfulness, claim coverage, reproducibility score, blinding leakage score.
- Adversarial metrics: unsupported claim rate, stale citation rate, circularity risk.
- Human-centered metrics: community benefit, local grounding, CARE-aligned evidence handling.

## Axis 5: Data / environment

- Current data: Igbo corpus files, downloaded PDFs, OGI source registers, product feedback notes.
- Data gaps: larger documented Igbo corpora, T1 regional recordkeeping sources, product event fixtures.
- Synthetic data possibilities: non-production Research Spine fixtures.
- Stress tests: source-count disagreement, citation audit, null-model experiments.

## Axis 6: Scaling / efficiency

- Bottlenecks: source metadata normalization, PDF reading, claim-to-evidence linking.
- Complexity: multi-paper state drift across Markdown/YAML/LaTeX.
- Cost model: cheap scans first; external downloads, cloud, APIs, and production data require approval.
- Approximation opportunities: path-level scans, dry-run loops, sampled citation audits.

## Axis 7: Robustness / safety / security

- Failure modes: prompt injection, secret leakage, malicious scripts, circular experiments, false citations.
- Attack surface: repo text, notebooks, .env files, package scripts, PDFs, generated papers.
- Misuse risks: premature submission, private data exposure, fabricated novelty.
- Defensive controls: human gates, path-only secret scans, validation scripts, claim labels.

## Axis 8: Theory

- Informal principles: source-first, evidence over vibes, user sovereignty, community sovereignty.
- Formalizable assumptions: every claim maps to source/evidence; every goal has a minimal test.
- Testable predictions: stronger gate alignment reduces reviewer attack surface.
- Counterexamples: PAGC k=27 and RL circularity already show why falsification matters.

## Axis 9: Systems architecture

- Current pipeline: source/library -> evidence maps -> runtime gates -> drafts -> submission checks.
- Interfaces: Research Spine, paper harnesses, experiments, Obsidian vault, Makefile targets.
- Observability: repo_index, claims/evidence JSONL, research_state, reflection log.
- Reproducibility: experiment plan directories, commands, environment notes.

## Axis 10: Paper potential

- Novelty: highest where product-research computability and source-first falsification are explicit.
- Clarity: strongest when claims remain separated by OBSERVED/DERIVED/EXPERIMENTAL/EXTERNAL/SPECULATIVE.
- Evidence needed: source metadata, primary-source audits, reproducible experiment logs.
- Venue fit: ICEGOV for governance papers; arXiv or methods note for research-system tooling.
