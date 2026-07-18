# ARTICLE-NA-002 Hardening Plan

Candidate:

```text
Foundation-Count Drift in Nwagu Aneke:
A Source-Critical Audit of 26 by 8, Derived f/v Split, and Layer-Promotion Error
```

## Current Decision

Status: `PAPER_CANDIDATE_BLOCKED_PENDING_REAL_EVIDENCE`

ARTICLE-NA-002 is the only Nwagu Aneke branch currently worth developing toward
a serious external paper. The existing draft should not be reused as the final
manuscript. It should be mined for claims, then rewritten from evidence.

## Why ARTICLE-NA-002

- It has a real source-critical correction.
- It matters outside the repo because layer confusion is a known failure mode in
  digitizing underdocumented scripts and generating grounded research prose.
- It can produce a negative/control result even if the grand PAGC theory stays
  speculative.
- It can support a benchmark: layer-promotion error.

## Required Evidence Before Drafting

### 1. Source Count Dossier

Files to create:

```text
research_runs/arxiv_quality_reset/article_002/source_count_dossier.csv
research_runs/arxiv_quality_reset/article_002/source_count_dossier.md
```

Required columns:

```text
item_id, source, locator, row_label, column_label, observed_value,
confidence, reviewer, uncertainty_note
```

Gate:

```text
No source-count table, no manuscript.
```

### 2. Derived f/v Split Dossier

Files to create:

```text
research_runs/arxiv_quality_reset/article_002/derived_f_v_split_audit.md
research_runs/arxiv_quality_reset/article_002/derived_f_v_split_examples.csv
```

Required content:

- what the split does;
- why it is derived;
- which claims depend on it;
- examples of blocked misstatements.

### 3. Layer-Promotion Benchmark

Files to create:

```text
research_runs/arxiv_quality_reset/article_002/lpe_benchmark_items.jsonl
research_runs/arxiv_quality_reset/article_002/lpe_gold_labels.jsonl
research_runs/arxiv_quality_reset/article_002/lpe_scoring_report.md
```

Task:

Given a claim or generated paragraph, classify each count-layer statement as:

```text
source_observed
derived
speculative
blocked
```

Metric:

```text
critical promotion errors must be zero for any submission candidate.
```

### 4. External Prior Art Audit

Files to create:

```text
research_runs/arxiv_quality_reset/article_002/external_prior_art_audit.md
research_runs/arxiv_quality_reset/article_002/external_prior_art_matrix.csv
```

Required clusters:

- Nwagu Aneke / Azuonye / indigenous African writing systems;
- script standardization and encoding readiness;
- digital critical editions;
- cultural heritage provenance;
- scientific claim verification;
- grounded long-form generation and STORM;
- source/interpretation layer drift.

### 5. Rights and Human Source Review

Files to create:

```text
research_runs/arxiv_quality_reset/article_002/human_source_review.md
research_runs/arxiv_quality_reset/article_002/rights_submission_clearance.md
```

Gate:

```text
If source excerpts, chart images, or cultural claims cannot be cleared, the
paper must use text-only discussion or remain internal.
```

## Manuscript Rewrite Rules

The eventual manuscript must not contain:

- internal approval language;
- review-team trace language;
- “this article is part of” framing;
- “first ten papers” framing;
- generated-validator commands as public research method;
- claims of public release or submission readiness.

The manuscript must contain:

1. one external-facing research question;
2. one result;
3. source table;
4. derived-layer table;
5. benchmark table;
6. prior-art table;
7. limitations and rights statement;
8. reproducibility package.

## Kill Criteria

Kill or park the candidate if:

- source count cannot be verified;
- f/v split cannot be defined cleanly;
- layer-promotion benchmark is trivial or unscorable;
- prior art already solves the same problem without a Nwagu Aneke contribution;
- rights/source review blocks necessary evidence;
- reviewers find the result too local to matter outside the repo.

