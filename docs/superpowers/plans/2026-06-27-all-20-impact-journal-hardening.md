# All 20 Nwagu Aneke Articles Impact-Journal Hardening Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert the 20 internal Nwagu Aneke research articles into externally reviewable impact-journal candidates without overstating readiness, source authority, or publication approval.

**Architecture:** This is a gated hardening program, not a manuscript polishing pass. Each article must move through article-specific evidence, source authority, rights clearance, prior-art review, substantive result, manuscript rewrite, adversarial review, and validator gates before any impact-journal language is allowed.

**Tech Stack:** Markdown control files, JSON readiness matrix, existing Python validators, existing LaTeX article directories, and repo-local evidence artifacts only.

---

## File Structure

- Create: `research_goals/nwagu_aneke_impact_journal_20/README.md`
  - Human-readable control room for the all-20 hardening program.
- Create: `research_goals/nwagu_aneke_impact_journal_20/readiness_matrix.json`
  - Machine-readable article status and blocker ledger.
- Create per article only when evidence exists:
  - `arxiv_quality_candidate.json`
  - `external_prior_art_audit.md`
  - `article_specific_experiment.md`
  - `figures_tables_manifest.json`
  - `human_source_review.md`
  - `rights_submission_clearance.md`
  - `reviewer2_response_plan.md`
- Modify only after gates pass:
  - `papers/nwagu_aneke_articles/*/main.tex`
  - `papers/nwagu_aneke_articles_cycle2/*/main.tex`
  - final readiness decision files

## Current Truth

- External accepted papers: 0.
- Internal research papers: 20.
- Current arXiv quality gate: 0 / 20 pass.
- First-cycle articles 001-010 are working drafts.
- Cycle-2 articles 011-020 are quarantined AI-to-AI/process traces, useful as seeds but not paper candidates.
- No article may be called impact-journal ready until `scripts/validate_arxiv_quality_gate.py`, `scripts/validate_lab_standard.py`, and `scripts/validate_review_team_gate.py` pass and the article has paper-specific human authority and rights evidence.

## Task 1: Lock Portfolio Decision Without Inflating Readiness

**Files:**
- Create: `research_goals/nwagu_aneke_impact_journal_20/README.md`
- Create: `research_goals/nwagu_aneke_impact_journal_20/readiness_matrix.json`

- [ ] **Step 1: Record the human portfolio decision**

Add a README stating that the user has expanded active hardening intent from the default two articles to all 20, while retaining gate discipline.

- [ ] **Step 2: Record three lanes**

Use these lanes:

| Lane | Articles | Meaning |
|---|---|---|
| A | 002, 010 | Strongest near-term candidates; harden first. |
| B | 001, 003, 004, 005, 006, 007, 008, 009 | Working drafts needing article-specific results and evidence packs. |
| C | 011-020 | Quarantined process traces; rebuild as methods or lab-infrastructure papers only after substantive experiments exist. |

- [ ] **Step 3: Record non-negotiable blockers**

Each article starts blocked on:

- Human source review.
- Rights and authority clearance.
- External prior-art audit.
- Article-specific experiment or source-critical result.
- Figures/tables manifest.
- Reviewer 2 response plan.
- Removal of internal lab-process language.
- Manuscript depth and citation expansion.

- [ ] **Step 4: Run validators**

Run:

```powershell
python scripts\validate_lab_standard.py
python scripts\validate_review_team_gate.py
python scripts\validate_arxiv_quality_gate.py
```

Expected at this stage:

- Lab standard passes.
- Review team gate passes because no article is falsely marked submission-ready.
- arXiv quality gate fails until evidence packs and manuscripts are actually upgraded.

## Task 2: Build Shared Authority And Source Review Packet

**Files:**
- Read: `authority/approval_register.jsonl`
- Read: `papers/SELECTED_PAPER/final_submission_readiness_decision.md`
- Create only with human-provided evidence: `research_goals/nwagu_aneke_impact_journal_20/shared_authority_packet.md`

- [ ] **Step 1: Identify authority claims shared by all articles**

Record these shared items:

- Source-observed foundation: 26 rows by 8 vowel/modifier columns equals 208 records.
- Derived layer: 27 rows and 216 records only if f/v is split.
- Public source-image, glyph-record, and culturally sensitive claim release is not approved by repo evidence yet.

- [ ] **Step 2: List exact documents needed from humans**

Collect or reference:

- Permission to discuss source manuscripts publicly.
- Permission to reproduce or describe source images.
- Authority holder review of the count-layer foundation.
- Cultural/source authority review for claims that leave the repo.
- Final author approval for target venue submission.

- [ ] **Step 3: Do not convert user attestation into legal clearance**

The repo currently records internal approval. External release needs attached paper-specific clearance.

## Task 3: Harden Article 002 First

**Files:**
- Modify after evidence exists: `papers/nwagu_aneke_articles/002-count-layer-drift/main.tex`
- Create: `papers/nwagu_aneke_articles/002-count-layer-drift/external_prior_art_audit.md`
- Create: `papers/nwagu_aneke_articles/002-count-layer-drift/article_specific_experiment.md`
- Create: `papers/nwagu_aneke_articles/002-count-layer-drift/figures_tables_manifest.json`
- Create with human input: `papers/nwagu_aneke_articles/002-count-layer-drift/human_source_review.md`
- Create with human input: `papers/nwagu_aneke_articles/002-count-layer-drift/rights_submission_clearance.md`
- Create: `papers/nwagu_aneke_articles/002-count-layer-drift/reviewer2_response_plan.md`
- Create only after all above pass: `papers/nwagu_aneke_articles/002-count-layer-drift/arxiv_quality_candidate.json`

- [ ] **Step 1: Make the result specific**

State the article result as:

> A reproducible count-layer audit separates source-observed 26 x 8 evidence from derived f/v expansion and prevents numerical drift in downstream claims.

- [ ] **Step 2: Build prior-art audit**

Compare against script standardization, Unicode proposal evidence norms, African writing-system documentation, digital epigraphy/source-critical ledgers, and data provenance papers.

- [ ] **Step 3: Build experiment report**

Attach or regenerate a count reconciliation table that includes input sources, row/column logic, derived f/v split conditions, and falsification conditions.

- [ ] **Step 4: Rewrite manuscript**

Remove internal approval language. Add explicit research question, hypothesis, method, result, limitations, and reviewer-facing contribution.

- [ ] **Step 5: Gate**

Run the three validators and keep status below impact candidate until all pass.

## Task 4: Harden Article 010 Second

**Files:**
- Modify after evidence exists: `papers/nwagu_aneke_articles/010-layer-safe-generative-design/main.tex`
- Create the same seven evidence files listed in Task 3 under `010-layer-safe-generative-design/`.

- [ ] **Step 1: Make the result specific**

State the article result as:

> A non-promotion invariant for generative design prevents source-layer facts from being upgraded into derived or speculative claims.

- [ ] **Step 2: Build experiment report**

Run or document a layer-safety test suite showing prompts, expected failures, observed failures, scoring, and residual risks.

- [ ] **Step 3: Build prior-art audit**

Compare against data provenance, cultural heritage AI, prompt/evaluation guardrails, source-critical editing, and trustworthy AI evaluation.

- [ ] **Step 4: Rewrite manuscript**

Make it a methods/result paper, not a lab-process essay.

- [ ] **Step 5: Gate**

Run all validators and keep status below impact candidate until authority and result evidence pass.

## Task 5: Convert Lane B Working Drafts Into Real Article Candidates

**Files:**
- Article directories 001, 003, 004, 005, 006, 007, 008, and 009.

- [ ] **Step 1: Article 001 source-critical reconstruction**

Required result: source ledger completeness, uncertainty taxonomy, and falsification table.

- [ ] **Step 2: Article 003 f/v hinge**

Required result: formal derived-layer audit showing when f/v split is permitted and when it is forbidden.

- [ ] **Step 3: Article 004 logographs**

Required result: lead-set audit of whole-word signs with source references and uncertainty classes.

- [ ] **Step 4: Article 005 TEI/IIIF bridge**

Required result: working mapping table from source records to TEI, IIIF, Web Annotation, and provenance fields.

- [ ] **Step 5: Article 006 Unicode readiness**

Required result: Unicode-style evidence gap matrix with community review and character evidence categories.

- [ ] **Step 6: Article 007 provenance ledger**

Required result: CARE-first provenance ledger and public-release boundary analysis.

- [ ] **Step 7: Article 008 comparative standardization**

Required result: comparative matrix against African script standardization cases and evidence thresholds.

- [ ] **Step 8: Article 009 Igbo tokenization**

Required result: downstream NLP task or negative-result baseline; tokenization alone is insufficient.

## Task 6: Rebuild Lane C From Quarantine

**Files:**
- Article directories 011 through 020.

- [ ] **Step 1: Treat current manuscripts as seeds only**

Do not revise them directly into impact papers until each has a substantive article-specific experiment.

- [ ] **Step 2: Assign each a real result type**

Use:

- 011: question-compiler evaluation with independent human scoring.
- 012: layer-promotion benchmark with held-out examples and baseline comparison.
- 013: red-herring audit with false-positive reduction measurement.
- 014: perspective graph with retrieval or review improvement metric.
- 015: source-to-system transfer protocol with case-study validation.
- 016: evidence-weighted design grammar with scored rule application.
- 017: authority-aware turn-taking protocol with human review outcomes.
- 018: Oroma bridge with product-transfer risk ledger and rejected-claim audit.
- 019: portfolio pruning method with before/after quality and kill-decision metrics.
- 020: accelerator synthesis only after 011-019 produce validated results.

- [ ] **Step 3: Replace lab-process language**

The manuscripts must stop saying they are internal approvals, review-team traces, or second-cycle artifacts in the main contribution framing.

## Task 7: Final Per-Article Promotion Gate

**Files:**
- Per-article final readiness decisions.
- Per-article review traces.
- `research_goals/nwagu_aneke_impact_journal_20/readiness_matrix.json`

- [ ] **Step 1: Confirm evidence pack complete**

For each article, confirm all seven required quality files exist and contain article-specific evidence.

- [ ] **Step 2: Confirm human gates**

Confirm human source review and rights clearance are attached, not merely user-attested in chat.

- [ ] **Step 3: Confirm manuscript quality**

Minimum checks:

- At least 5,000 validator words.
- At least 25 unique citations.
- Explicit research question and hypothesis.
- Limitations section.
- No internal approval/process language as contribution framing.
- Central result stated in abstract.

- [ ] **Step 4: Run validators**

Run:

```powershell
python scripts\validate_arxiv_quality_gate.py
python scripts\validate_lab_standard.py
python scripts\validate_review_team_gate.py
```

- [ ] **Step 5: Update status honestly**

Allowed statuses:

- `WORKING_DRAFT_NEEDS_EVIDENCE`
- `JOURNAL_TRACK_DRAFT_HUMAN_GATES_OPEN`
- `IMPACT_CANDIDATE_GATES_PASSED`
- `READY_FOR_HUMAN_SUBMISSION_REVIEW`

Do not use `READY_FOR_HUMAN_SUBMISSION_REVIEW` until all validators and human gates pass.

## Self-Review

Spec coverage: The plan covers all 20 articles, impact-journal criteria, validator gates, authority/rights blockers, and the distinction between internal approval and external readiness.

Placeholder scan: No task relies on unspecified "TBD" evidence; missing evidence is named as a blocker and cannot be papered over.

Type consistency: Status names and required evidence file names match the current arXiv quality validator expectations.
