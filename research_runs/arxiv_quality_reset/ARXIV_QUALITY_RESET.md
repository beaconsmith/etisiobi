# arXiv Quality Reset

## Decision

The generated Nwagu Aneke article packages are **not arXiv-level submission
quality**.

They may remain in the repository as internal scaffolding and branch notes, but
they must not be described as arXiv-ready, impact-journal-ready, or public
submission candidates.

## What Went Wrong

The lab optimized for file completeness instead of research contribution. The
previous internal gates rewarded:

- manuscript length,
- citation count,
- PDF compilation,
- review-trace shape,
- approval metadata,
- repeated source/derived-layer safety language.

Those checks are useful hygiene, but they do not prove a research paper exists.
They allowed AI-to-AI process documents to look like papers.

## Why the Current Papers Fail

The new arXiv-quality gate checks the actual failure modes:

- internal-process framing remains in the manuscripts;
- the papers explain the lab machinery more than they present discoveries;
- experiments are mostly approval/prewriting artifacts, not substantive results;
- the papers lack article-specific prior-art depth;
- the papers lack real figures/tables tied to data or formal analysis;
- the papers do not contain strong research-question/hypothesis/result arcs;
- their own readiness decisions say they are not arXiv-ready or journal-ready.

Fresh validator result:

```text
ARXIV_QUALITY_GATE_FAIL
passed=0/20
```

Report:

```text
research_runs/arxiv_quality_reset/arxiv_quality_gate_report.md
```

## Corrective Standard

From now on, a Nwagu Aneke paper cannot enter an arXiv-quality lane unless it
has:

1. one external-facing research question;
2. one original contribution that matters outside Etisiobi;
3. article-specific prior art, not only standards citations;
4. a substantive source-critical, empirical, formal, or negative result;
5. figures/tables generated from evidence;
6. verified citations supporting each major claim;
7. human source/rights review for public claims;
8. a manuscript that does not talk to itself about its own approval process;
9. a reviewer-2 attack and revision response;
10. an explicit not-ready decision if any gate fails.

## Best Real Paper Candidate

The strongest candidate is not one of the cycle-two STORM papers. The strongest
candidate remains:

```text
Foundation-Count Drift in Nwagu Aneke:
A Source-Critical Audit of 26 by 8, Derived f/v Split, and Layer-Promotion Error
```

Why:

- it has a concrete claim: source-observed 26 by 8 equals 208 records;
- it has a concrete derived-layer constraint: 27/216 only by f/v split;
- it corrects a real failure mode in the research archive;
- it can be converted into a source-critical/digital-humanities paper or a
  research-infrastructure paper;
- it has a falsifiable benchmark direction: layer-promotion error.

## Minimum Experiments Needed

The next real paper needs these experiments before drafting:

1. **Source Count Audit**
   - independently verify the 26 by 8 source layer;
   - record chart/image/source locator for every row and column claim;
   - mark uncertainty for each cell.

2. **Derived f/v Split Audit**
   - define the transformation from 26 rows to derived 27 row layer;
   - show exactly what changes and what does not;
   - prove the transformation is interpretation, not source observation.

3. **Layer-Promotion Error Benchmark**
   - create prompts or tasks that ask agents/reviewers to write about the
     artifact;
   - score whether they wrongly promote 27/216 to source-observed;
   - compare baseline drafting, STORM-style drafting, and gated drafting.

4. **Prior-Art Review**
   - review writing-system scholarship, African script standardization,
     source-critical digital editions, claim verification, and grounded
     generation;
   - identify whether layer-promotion error is already named elsewhere.

5. **Human Source/Rights Review**
   - decide what source material can be publicly described;
   - decide whether figures may reproduce any chart excerpts;
   - decide who must approve before submission.

## Immediate Next Command

Run:

```powershell
python scripts\validate_arxiv_quality_gate.py
```

Expected result until the real experiments exist:

```text
ARXIV_QUALITY_GATE_FAIL
passed=0/20
```

