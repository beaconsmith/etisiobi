# Cycle-Two Quarantine

Status: `QUARANTINED_AI_TO_AI_PROCESS_TRACES_NOT_PAPER_CANDIDATES`

The files in this directory are **not arXiv-quality papers** and must not be
used as public submission candidates.

## Why Quarantined

The cycle-two package passed weak internal structure checks, but failed the
arXiv-quality gate:

```text
ARXIV_QUALITY_GATE_FAIL
passed=0/20
```

The failure is substantive:

- the manuscripts read like internal AI-to-AI process documents;
- the experiments are prewriting/approval traces, not empirical or formal
  research results;
- the section structure is heavily templated across ten alleged articles;
- external prior art is generic rather than article-specific;
- rights and source authority are not cleared for public submission;
- the papers themselves say they are not arXiv-ready or journal-ready.

## Allowed Use

- Negative examples for validator hardening.
- Process archaeology.
- Branch-selection input.
- Source for deciding what not to do.

## Not Allowed Use

- arXiv submission.
- Impact-journal submission.
- Public release as research papers.
- Evidence that Etisiobi has ten submission-quality papers.

## Replacement Path

Develop one real candidate:

```text
Foundation-Count Drift in Nwagu Aneke:
A Source-Critical Audit of 26 by 8, Derived f/v Split, and Layer-Promotion Error
```

See:

```text
research_runs/arxiv_quality_reset/REAL_SUBMISSION_CANDIDATE.md
```

