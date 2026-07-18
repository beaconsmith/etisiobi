# Real Submission Candidate

## Selected Candidate

```text
Foundation-Count Drift in Nwagu Aneke:
A Source-Critical Audit of 26 by 8, Derived f/v Split, and Layer-Promotion Error
```

## Why This Candidate

This is the strongest route because it starts from a real correction:

- source-observed layer: 26 rows x 8 vowel/modifier columns = 208 records;
- derived layer: 27 / 216 only by f/v split;
- failure mode: agents, drafts, and speculative theory can promote derived
  layers into source claims;
- research value: a reproducible source-critical audit plus a benchmark for
  layer-promotion error.

This candidate can become a serious paper only if it stops talking about the lab
and starts presenting the artifact, the audit method, the evidence, the
benchmark, the results, and the implications.

## Target Paper Type

Primary fit:

```text
Digital humanities / writing systems / research infrastructure paper
```

Secondary fit:

```text
Claim-verification / grounded-generation benchmark paper
```

## Research Question

How can a source-critical research pipeline prevent derived interpretations of
an underdocumented script from being promoted into source-observed manuscript
claims?

## Hypothesis

A layer-typed audit and benchmark will reduce layer-promotion errors compared
with ungated drafting and generic retrieval-assisted drafting.

## Required Experiments

### EXP-ARXIV-001 Source Count Audit

Goal: verify the source-observed 26 x 8 = 208 record claim.

Required artifacts:

- row inventory table;
- column/vowel/modifier inventory table;
- source locator for each row and column;
- uncertainty notes;
- reviewer signoff.

Kill criterion:

- if the source layer cannot be independently verified, no submission paper.

### EXP-ARXIV-002 Derived f/v Split Audit

Goal: show that 27/216 is a derived interpretation, not a source-observed layer.

Required artifacts:

- transformation rule;
- examples before and after split;
- claims that depend on the derived layer;
- non-claims that must be blocked.

Kill criterion:

- if the split cannot be specified without ambiguity, 27/216 must be removed
  from the paper except as a historical error.

### EXP-ARXIV-003 Layer-Promotion Error Benchmark

Goal: measure whether research agents/drafting methods incorrectly promote
derived layers to source-observed status.

Conditions:

1. ungated drafting baseline;
2. STORM-style perspective drafting;
3. Etisiobi layer-gated drafting.

Metrics:

- layer-promotion error rate;
- unsupported source-count claims;
- citation-faithfulness errors;
- public-release overclaims;
- reviewer correction burden.

Kill criterion:

- if the benchmark cannot distinguish methods or only tests trivial wording,
  it is not publishable.

### EXP-ARXIV-004 Prior-Art and Venue Audit

Goal: place the paper against serious prior work.

Required areas:

- Azuonye and Nwagu Aneke source scholarship;
- African writing systems and standardization;
- TEI/IIIF/Web Annotation for cultural heritage;
- source-critical digital editions;
- scientific claim verification;
- grounded long-form generation and STORM;
- research-object provenance.

Kill criterion:

- if the central method is already known and the Nwagu Aneke case adds no new
  result, convert to internal report.

### EXP-ARXIV-005 Rights and Source Review

Goal: decide what can be publicly shown and claimed.

Required artifacts:

- public-text clearance;
- figure/source-image clearance decision;
- cultural authority notes;
- author approval;
- data availability statement.

Kill criterion:

- if rights/source review blocks necessary evidence, publish no external paper.

## Manuscript Rule

The submission candidate may not contain:

- "internal approval";
- "review-team trace";
- "this article is part of";
- "first ten papers";
- "AI-to-AI";
- "not external submission";
- generated process justification as a result.

It must read as a normal research article:

1. Abstract.
2. Introduction.
3. Related Work.
4. Materials.
5. Method.
6. Experiments.
7. Results.
8. Discussion.
9. Limitations and Ethics.
10. Reproducibility.
11. Conclusion.

## Immediate Next Step

Create and run `EXP-ARXIV-001` and `EXP-ARXIV-002`. No new paper should be
generated before those two experiments produce evidence tables.

