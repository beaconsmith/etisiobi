---
schema: etisiobi.agent-contract/v1
scope: /
owner: The Beaconsmith Collective
last_verified: 2026-06-20
canonical: true
---

# etisiobi — Research Studio Harness

> *signals from the tree*
>
> The Beaconsmith Collective Research Archive

This is the canonical operating contract for every human or agent working in this repository. It governs the entire tree unless a nearer `AGENTS.md` adds more specific rules for its subtree.

## 1. Mission

`etisiobi` is the research infrastructure of The Beaconsmith Collective, a creative-technology studio in Enugu, Southeast Nigeria. It holds research programs, primary-source archives, literature wikis, evidence ledgers, experiments, paper drafts, and the research-to-product bridge for Oroma.

The repository exists to produce research that is:

- traceable to evidence;
- explicit about uncertainty;
- reproducible where possible;
- useful to the communities it concerns;
- safe to review, challenge, and falsify;
- publishable only through a human-controlled gate.

The working method combines metric-driven autoresearch, reusable research skills, artifact-first inquiry, search-before-building, and user sovereignty.

## 2. Normative language and precedence

`MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY` are normative.

### 2.1 Instruction precedence

Apply rules in this order:

1. platform and runtime safety requirements;
2. the user's explicit instruction for the current task;
3. the nearest `AGENTS.md` in the working directory ancestry;
4. this root `AGENTS.md`;
5. research policy files;
6. program wikis, skills, READMEs, and prose notes.

A nested `AGENTS.md` may specialize this file but may not weaken evidence, consent, rights, privacy, publication, or review gates.

### 2.2 Source-of-truth precedence

Do not resolve every conflict the same way. Use the correct authority chain:

- **Evidence truth:** immutable source or source event → extraction record → structured fact → claim ledger → maintained wiki → draft prose.
- **Program status:** dated submission receipt or decision record → `current_state` / portfolio record → append-only log → README or static overview.
- **Method and governance:** nearest `AGENTS.md` → evidence/citation/submission policy → registered skill → local convention.
- **Venue requirements:** current official venue rules override copied summaries. Record the source and retrieval date when updating repo rules.

When two authoritative records conflict, do not silently choose one. Preserve both, open or update a contradiction record, and mark the affected claim or status `needs-review`.

## 3. Non-negotiable invariants

1. **Raw evidence is immutable.** Never edit a raw source, source image, event export, or original transcript in place. Corrections are new files with provenance and a supersession link.
2. **No evidence, no claim.** A confident sentence is not evidence. Every material empirical claim must resolve to a source record or an explicitly labelled illustrative artifact.
3. **Observation is not interpretation.** Store what was observed separately from what it may mean.
4. **No fabrication.** Never invent citations, quotations, page numbers, identifiers, participants, data, results, review outcomes, submission receipts, or tool output.
5. **Contradictions are first-class evidence.** Add contradictions; do not erase or overwrite inconvenient evidence.
6. **Negative results survive.** Failed experiments, null findings, and killed hypotheses remain discoverable and are logged.
7. **Claim maturity is explicit.** Use only: `draft`, `supported`, `weak`, `contradicted`, `rejected`, or `needs-review`.
8. **Illustrative is not empirical.** Simulated, hypothetical, synthetic, or design-demonstration values must be labelled `ILLUSTRATIVE` at every reuse point.
9. **Community sovereignty is a hard gate.** CARE-aligned authority, consent, privacy, benefit, and rights checks apply before community data is analyzed or shared.
10. **Publication is human-triggered.** Agents may prepare, test, critique, and recommend. They may not submit, publish, disclose blinded identities, or represent approval without explicit human authorization.
11. **Research does not become product doctrine automatically.** Product recommendations require evidence, review, and the designated bridge.
12. **Reproducibility beats rhetoric.** Preserve inputs, parameters, code version, environment assumptions, outputs, and evaluation criteria.
13. **Secrets and personal data do not enter the repo.** Never commit credentials, private keys, access tokens, raw direct identifiers, or unapproved sensitive attributes.
14. **Irreversible actions require explicit authorization.** Do not delete evidence, rewrite history, force-push, merge, publish, or send externally merely because they appear useful.

## 4. Session startup protocol

Run this protocol automatically at the start of substantive work. Do not require the user to recite a magic phrase.

### 4.1 Establish operating context

1. Identify the repository root, current branch, working-tree state, and current date.
2. Locate all applicable `AGENTS.md` files from root to the target path.
3. Identify the task class: source ingest, literature review, evidence extraction, experiment, synthesis, paper editing, review, submission, or research-product bridge.
4. Determine whether the task touches human subjects, community data, sensitive attributes, blinded material, external publication, or irreversible state.

### 4.2 Load memory in this order

Read the first existing file in each row; read more than one when the task spans scopes.

| Purpose | Preferred path | Fallback / compatibility path |
|---|---|---|
| Cross-program navigation | `wiki/index.md` | `repo_map.md`, `README.md` |
| Research governance | `research/AGENTS.md` | `research/REGISTRY.md`, `RESEARCH_SPINE.md` |
| Portfolio state | `research/PORTFOLIO.md` | program `INDEX.md`, recent `log.md` entries |
| Current program knowledge | `research/<program>/WIKI.md` | `research/<program>/INDEX.md` |
| Current machine state | `spine/events/current_state.md` | latest file under `research/<program>/facts/` |
| Evidence and citation rules | `research/EVIDENCE_POLICY.md`, `research/CITATION_POLICY.md` | `research/REGISTRY.md` |
| Venue rules | `research/SUBMISSION_RULES.md` | dated official source recorded in the task log |
| Recent episode history | tail of `log.md` and relevant run log | `reflection_log.md`, `research_loop_changelog.md` |

A missing preferred path is not permission to invent its contents. Use the fallback, report the control gap, and create a canonical file only when the task authorizes it.

### 4.3 State the work contract

Before changing files, establish:

- objective and target artifact;
- canonical input files;
- evidence boundary;
- success metric or acceptance criteria;
- applicable safety, rights, review, and publication gates;
- expected files to change;
- stop condition.

Ask a question only when an unresolved ambiguity would materially alter the evidence, rights, publication status, or irreversible outcome. Otherwise make the smallest reversible assumption and record it.

## 5. Repository path contract

The live tree is authoritative. Search it before creating new paths. The following are canonical destinations or migration targets; legacy paths may coexist temporarily.

| Area | Canonical role |
|---|---|
| `AGENTS.md` | Root operating contract |
| `CLAUDE.md` | Compatibility adapter only; it must not maintain divergent policy |
| `README.md` | Public-facing overview, never the sole status authority |
| `log.md` | Append-only record of meaningful ingests, merges, decisions, and research state changes |
| `wiki/index.md` | Thin cross-program atlas and default session entry point |
| `wiki/topics/`, `wiki/entities/` | Canonical topic and entity memory; update instead of duplicating |
| `research/` | Programs, policies, portfolio, papers, facts, claims, and contradictions |
| `research/<program>/WIKI.md` | Maintained semantic memory for a program |
| `research/<program>/INDEX.md` | Source and artifact catalog |
| `research/<program>/facts/` | Structured observations and extracted evidence |
| `research/<program>/contradictions/` | Unresolved and resolved conflicts, never silently deleted |
| `research/<program>/paper/` | Paper source, evaluations, review trace, build artifacts, and submission records |
| `experiments/` | Reproducible empirical work and run outputs |
| `library/` | Global research library; preferred successor to legacy `sources/` |
| `spine/` | Evidence extraction, normalization, state, and research infrastructure |
| `skills/` | Reusable, executable research procedures |
| `bridges/` | Controlled product-to-research signal ingest |
| `ETISIOBI_OROMA_FEED.md` | Reviewed research-to-product output |
| `decisions/` | Durable product or research decisions with rationale |
| `uncertainty/` | Unresolved uncertainty and calibration records |

Do not create a parallel raw-source hierarchy, a second wiki for the same scope, or a new entity/topic page when a canonical one exists. Do not bulk-migrate `sources/`, the Obsidian vault, or any archive without a migration plan, redirect map, and validation.

## 6. Active research programs

### 6.1 ICEGOV / OGI

The Oroma Governance Indicator Framework studies community-led digital governance in Southeast Nigeria for ICEGOV 2026 Track 6, “New Metrics and Approaches for Measuring Digital Governance Success.”

Canonical paper source, when present:

`research/icegov/paper/OGI_PAPER_SUBMISSION_CANONICAL.md`

Hard rules:

- Do not infer submission from the existence, filename, freeze date, or quality of a draft.
- `SUBMITTED` requires a dated EDAS receipt or equivalent submission record.
- `ACCEPTED`, `REJECTED`, or `REVISION_REQUESTED` requires a venue decision record.
- Workspace A / prototype material remains an illustrative design-science demonstration unless a reviewed evidence package promotes it.
- Keep blinded and identified variants separate. Never reintroduce direct identifiers into a blinded artifact.
- The official 2026 extended paper deadline was 8 May 2026. The official decision-notification date is 14 July 2026.
- For an **ongoing research** paper in the thematic tracks, the official range is 8–10 pages. A seven-page build fails the format gate; do not describe it as page-compliant.
- An official abstract limit of up to 300 words applies to research and ongoing-research papers; the repo may impose a stricter local target.

Product evidence dependencies currently include:

- dispute state-machine closure evidence for DRL-01;
- Ichi credential issuance contract enforcement with at least three qualifying events for CPS-01;
- contract-level TTI-01 metadata enforcement, including purpose length and proposal reference;
- onboarding survey instrumentation at wallet creation for FID-01.

Treat this list as a pointer to the relevant contradiction and product-bridge records, not as proof that the product gap remains open. Verify current product state before repeating it.

### 6.2 PAGC

The Principle of Ancestral Generative Compression is an artifact-first program grounded in the Nwagu Aneke source layer.

Current epistemic boundary:

- **Source-observed layer:** 26 rows × 8 vowel/modifier columns = 208 records in the current evidence package.
- **Derived layer:** 27 / 216 arises from an explicit `f/v` split transformation; it is not source-observed in the current package.

Agents MUST preserve that distinction in datasets, diagrams, prose, filenames, formulas, and citations. Exceptional-math, universal-compression, exact-27, or cross-disciplinary analogy branches remain `weak`, `rejected`, or `needs-review` until a dated evidence-promotion event changes their status.

Start PAGC work from, when present:

- `research/pagc/PAGC_RESET.md`;
- `research/pagc/primary_sources/nwagu_aneke/README.md`;
- `spine/events/current_state.md`.

Historical material may inform question generation but may not silently override the reset or source/derived boundary.

## 7. Evidence model and claim promotion

### 7.1 Evidence classes

Use these classes consistently:

| Class | Meaning | Public-claim eligibility |
|---|---|---|
| `RAW_SOURCE` | Immutable original artifact or event export | No |
| `RAW_FACT` | Direct observation or query result without interpretation | No |
| `STRUCTURED_FACT` | Normalized fact with schema and provenance pinned | No |
| `DRAFT_INSIGHT` | Agent or human interpretation awaiting review | No |
| `ILLUSTRATIVE` | Explicitly hypothetical, synthetic, or demonstrative material | Only when labelled |
| `HUMAN_JUDGMENT` | Attributed qualitative judgment with authority context | With review and consent |
| `PUBLISHABLE_CLAIM` | Reviewed claim linked to evidence and a named approver | Yes |

### 7.2 Minimum provenance record

Every extracted fact, experiment result, or promoted claim SHOULD include:

- stable ID;
- program and artifact type;
- source path or source ID;
- source version, checksum, or event identifier;
- locator such as page, section, timestamp, row, or query;
- extraction method and tool version;
- schema version;
- authoring agent or human;
- created and reviewed timestamps in ISO 8601;
- evidence class;
- claim maturity;
- known limitations and contradictions;
- rights, consent, and disclosure status when relevant.

### 7.3 Promotion gates

Promotion is monotonic only when evidence improves. A claim may always be demoted when evidence weakens.

`RAW_SOURCE → RAW_FACT → STRUCTURED_FACT → DRAFT_INSIGHT → PUBLISHABLE_CLAIM`

A `PUBLISHABLE_CLAIM` requires:

1. a claim-ledger entry;
2. a precise evidence link;
3. citation verification where external literature is involved;
4. methods review for empirical or computational claims;
5. rights/authority review for community or cultural material;
6. contradiction check;
7. named human approval.

A derived transformation must never be relabelled as source-observed merely because it is reproducible.

## 8. Source ingestion protocol

When adding a source:

1. Search for an existing copy, canonical record, DOI, title variant, and entity/topic page.
2. Preserve the original bytes or original text unchanged in the established source location.
3. Record acquisition date, origin, author/creator, rights status, checksum, and stable source ID.
4. Prefer embedded text extraction over OCR. Use OCR only when necessary and record its error risk.
5. Create or update a source note that separates summary, direct observations, interpretation, quotations, and open questions.
6. Add precise locators for every extracted claim.
7. Update the program `INDEX.md` and relevant `WIKI.md` without duplicating canonical pages.
8. Add contradictions rather than reconciling them by deletion.
9. Update `wiki/index.md` only when navigation or cross-program meaning changes.
10. Append a meaningful ingest record to `log.md`.

Never citation-launder a claim through a secondary source when the primary source is available. Never cite a search snippet as the evidence itself.

## 9. Literature and citation protocol

- Search the repository before the web and search primary literature before commentary.
- Match every citation to the exact proposition it supports.
- Verify author, title, venue, year, DOI or stable identifier, and page/section locator.
- Distinguish a source's finding from the current author's inference.
- Represent disagreement and null findings fairly.
- Do not use citation count, prestige, or repeated secondary citation as proof of correctness.
- Do not insert a citation that has not been opened and checked.
- Do not preserve a citation merely because removing it would weaken a paragraph.
- Record retractions, corrections, inaccessible sources, and unresolved bibliographic ambiguity.
- For fast-changing facts, record the retrieval date and prefer the current official source.

A paper's reference list and in-text citations must reconcile before any readiness claim.

## 10. Autoresearch and experiment loop

Use the loop:

`question → preregistered metric → baseline → hypothesis → smallest useful change → run → evaluate → falsify → decide → log`

Before a run, freeze:

- research question;
- hypothesis and plausible alternative explanations;
- input dataset and inclusion/exclusion rules;
- primary metric and direction of improvement;
- guardrail metrics;
- baseline;
- compute/time budget;
- stop and kill criteria.

Each run must produce or update a durable record containing:

```yaml
run_id:
started_at:
program:
question:
hypothesis:
inputs:
code_version:
metric_definition:
baseline:
target:
change:
result:
delta:
guardrails:
uncertainty:
contradictions:
decision: keep | revise | revert | kill | needs-review
next_step:
```

Rules:

- Never redefine the primary metric after seeing the result without starting a new run.
- Never hide a failed run or cherry-pick seeds, subsets, or stopping points.
- Use held-out data or independent checks where the claim requires generalization.
- Separate exploratory work from confirmatory work.
- Record environment and randomness controls.
- Prefer the smallest change that can test the hypothesis.
- Stop when kill criteria are met. Do not keep polishing a dead branch to rescue sunk cost.
- Update the relevant wiki only after the run record exists.

## 11. Paper workflow and readiness gate

### 11.1 Paper state machine

Use explicit states:

`DRAFT → EVIDENCE_REVIEW → METHODS_REVIEW → ADVERSARIAL_REVIEW → HUMAN_SUBMISSION_REVIEW → SUBMITTED → DECISION_RECEIVED`

A file freeze is not submission. A high self-score is not review. A compiled PDF is not format compliance. Absence of a blocking issue in prose is not a passing gate.

### 11.2 Mandatory review-team trace

No agent may declare a paper `complete`, `submission-ready`, `READY_FOR_HUMAN_ARXIV_REVIEW`, or equivalent unless the paper directory contains `review_team_trace.jsonl` with passing reviews from all of these roles:

- `research_lead`;
- `domain_postdoc`;
- `methods_reviewer`;
- `adversarial_impact_reviewer`;
- `citation_evidence_reviewer`;
- `rights_authority_reviewer`.

Every row must contain:

```json
{
  "role": "methods_reviewer",
  "agent_id": "stable-reviewer-id",
  "status": "PASS",
  "summary": "...",
  "files_reviewed": ["..."],
  "blocking_issues": [],
  "reviewed_at": "2026-06-20T00:00:00Z"
}
```

Readiness requires:

- one current `PASS` for every required role;
- no unresolved `blocking_issues`;
- reviews covering the current canonical paper revision;
- no reviewer claiming to have inspected files or evidence they did not inspect.

Run:

```bash
python scripts/validate_review_team_gate.py
```

A missing validator, missing trace, stale review, malformed row, non-`PASS` status, or unresolved blocker means the strongest allowed status is:

`NOT_READY_REVIEW_TEAM_BLOCKED`

The authoring agent must not manufacture independent review by changing role labels. Record reviewer identity and revision coverage honestly.

### 11.3 Additional readiness gates

Before human submission review, verify:

- claim-to-evidence coverage;
- citation existence and entailment;
- methods and statistical validity;
- reproducibility of computational results;
- rights, consent, authority, and disclosure;
- contradiction disposition;
- anonymization and double-blind requirements where applicable;
- venue category, page count, abstract limit, formatting, and required metadata;
- figure/table legibility and provenance;
- title, abstract, body, supplement, and submission form consistency;
- a clean build from the documented source.

Never fix a page-count failure by shrinking text, hiding content, or manipulating layout beyond venue rules. Improve substance and category fit first.

## 12. Memory maintenance

The memory flow is:

`immutable sources → maintained wiki → explicit schema and policy`

Memory homes:

| Type | Canonical home |
|---|---|
| Navigation | `wiki/index.md`, `obsidian_vault/00_Home.md`, `repo_map.md` |
| Semantic | `research/*/WIKI.md`, `wiki/topics/` |
| Entity | `wiki/entities/` |
| Episodic | `log.md`, `reflection_log.md`, `research_loop_changelog.md`, run records |
| Summary | `external_sources/source_notes/`, `library/`, program sources |
| Procedural | `AGENTS.md`, `research/AGENTS.md`, `skills/`, policy files |
| Claim | `obsidian_vault/Claims/`, claim ledgers, `uncertainty/` |
| Product decision | `ETISIOBI_OROMA_FEED.md`, `research/icegov/PRODUCT_BRIDGE.md`, `decisions/` |
| Learning | `self_improvement_proposals/`, `research_loop_changelog.md` |

Maintenance rules:

- Update the canonical page instead of creating near-duplicates.
- Every wiki claim should point to source records where possible.
- Separate observation, interpretation, hypothesis, and decision.
- Preserve superseded material through links or history; do not quietly rewrite the past.
- Keep `wiki/index.md` navigational, not a replacement for program wikis.
- Log meaningful ingests, merges, promotions, demotions, and decisions.
- Use absolute dates, not “today,” “recently,” or “currently,” in durable records.

## 13. Research ↔ Oroma boundary

Research-to-product output flows through `ETISIOBI_OROMA_FEED.md` or the current reviewed equivalent. Product-to-research input flows through `bridges/oroma-signal-ingest.md` and must contain anonymized, consent-compatible signals only.

Agents MUST NOT:

- turn a research hypothesis into Oroma doctrine without evidence and review;
- convert a missing research instrument into a product requirement without checking user value, safety, and governance;
- import direct identifiers or private workspace content into research memory;
- claim that a shipped product feature validates a research claim without a recorded measurement;
- optimize the product merely to improve a paper metric.

Every material research output should state what it teaches Oroma, what it does **not** establish, and what evidence would change the recommendation.

## 14. Change discipline

### 14.1 Before editing

- Search for the canonical file and prior attempts.
- Inspect nearby conventions, tests, schemas, and nested instructions.
- Check the working tree for unrelated changes.
- Prefer an atomic, reviewable change over a broad rewrite.

### 14.2 While editing

- Do not mix raw-source changes, derived-data changes, policy changes, and paper prose without clear separation.
- Preserve stable IDs and links.
- Update schemas and migrations before dependent artifacts.
- Do not hand-edit generated files unless the generator explicitly permits it.
- Avoid opportunistic renames and formatting churn.
- For parallel work, assign one owner per canonical file and merge through a designated integrator.

### 14.3 Validation

Discover project commands from the repository rather than inventing them. At minimum, run the checks relevant to changed files, plus:

```bash
git diff --check
```

Conditional expectations:

- Python: targeted tests, static checks if configured, and import/compile validation.
- Data: schema, row-count, null, duplicate, range, and provenance checks.
- Experiments: deterministic smoke run plus metric reproduction.
- Papers: clean build, page count, reference reconciliation, figure/table check, and review-team validator.
- Markdown/wiki: internal-link check and duplicate canonical-page search.

If a required check cannot run, report the exact command, reason, and risk. Never replace a failed check with “looks good.”

## 15. Definition of done

A task is done only when:

1. the requested artifact changed in the correct canonical location;
2. evidence and provenance are attached at the required level;
3. applicable tests and validators pass, or failures are explicitly blocking;
4. contradictions and uncertainty are recorded;
5. indexes, wikis, schemas, and logs are updated when their contract requires it;
6. no raw evidence, privacy boundary, blinded identity, or rights constraint was violated;
7. the result is reviewed at the level implied by the status being claimed;
8. the handoff says what changed, what was checked, what remains uncertain, and the next decision owner.

Use this handoff shape:

```markdown
## Handoff
- Objective:
- Canonical artifact:
- Evidence used:
- Files changed:
- Validation:
- Claim/status changes:
- Contradictions or uncertainty:
- Blocking issues:
- Next owner/action:
```

## 16. Prohibited shortcuts

Never:

- modify raw evidence to make a theory fit;
- present 27 / 216 as source-observed under the current PAGC evidence package;
- present illustrative OGI values as pilot findings;
- infer submission, acceptance, consent, review, or approval from filenames or silence;
- cite a source you did not inspect;
- delete a contradiction because it weakens a paper;
- mark your own output as independently reviewed;
- duplicate canonical wiki pages to avoid reconciling conflicts;
- copy private Oroma data into public research artifacts;
- suppress negative results or change metrics after the fact;
- publish, submit, merge, force-push, or disclose identities without the required human gate.

## 17. Operating principles

- **Boil the lake:** make the artifact complete enough to withstand review, not bloated with speculation.
- **Search before building:** inspect the tree, prior art, evidence, and failure history first.
- **Artifact-first:** prefer inspectable objects over persuasive assertions.
- **Falsification-first:** actively seek the observation that would prove the claim wrong.
- **User sovereignty:** recommend clearly; the human decides what is adopted or published.
- **Community sovereignty:** research must preserve authority, context, benefit, and rights for the communities from which it grows.
