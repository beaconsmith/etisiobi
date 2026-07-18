# First-Principles Model

## Observed primitives

- Repo files, papers, source registries, runtime manifests, experiment scripts, datasets, figures, logs, and policies.
- Research programs: OGI/ICegov and PAGC.
- Control files: portfolio, quality bar, evidence policy, citation policy, submission rules, falsification tracker.
- Product-research interface: Research Spine design around Oroma domain events.

## Derived objects

- A research claim is a statement that must map to evidence or be explicitly marked speculative.
- A paper candidate is a folder with scope, thesis, evidence maps, runtime state, and writing artifacts.
- A falsification target is a claim with a minimal test that can lower confidence.
- A research loop is a bounded update to claims, goals, evidence, vault notes, and paper scaffold.

## State variables

- Claim evidence status
- Citation verification status
- Paper gate status
- Experiment status
- Source read/verification status
- Deadline/venue format status
- Secret/provenance risk status

## Operations / transformations

- Scan repo to classify artifacts.
- Extract claims and evidence links.
- Generate goals from contradictions and weak signals.
- Plan isolated experiments.
- Update Obsidian notes and paper audit tables.
- Validate generated state.

## Objective functions

- Maximize evidence-backed claim density.
- Maximize expected information gain per experiment.
- Minimize unsupported claims, stale citations, and reviewer attack surface.
- Preserve negative results and contradiction visibility.

## Constraints

- No deletion of user files.
- No expensive compute, paid APIs, installs, uploads, or submissions without approval.
- No invented citations or results.
- Double-blind rules apply where submission artifacts are intended for review.
- Local/community context is not optional for Nigeria/Southeast Nigeria work.

## Failure modes

- Treating analogy as evidence.
- Letting drafts outrun source registries.
- Confusing implementation success with research novelty.
- Circular experiments.
- Stale venue/deadline assumptions.
- Secret leakage from environment files.

## Measurement strategy

- Count claims by evidence status.
- Count citation audit risk levels.
- Track paper gate blockers.
- Compare experiments against baselines with fixed commands and seeds.
- Record KEEP/REVISE/RETEST/PARK/REJECT after each loop.

## Falsification criteria

- PAGC numeric claims fail if primary source counts or robust experiments contradict them.
- OGI pilot claims fail if product event data cannot compute indicators.
- Paper readiness claims fail if any core claim lacks evidence or citations cannot be verified.
- Hyperloop value fails if it creates vague goals without minimal tests.

## Open unknowns

- ICEGOV deadline and ACM format source of truth.
- Final PAGC base count.
- Whether BPE refutation replicates on larger corpora.
- Whether active paper citation metadata is complete.
- Whether secret-risk paths contain real secrets.
