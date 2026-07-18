# Quality Bar

> What "submission-ready" means for this lab.

---

## Minimum Literature Depth

A paper should not be promoted to drafting unless it has:

- **8–12 foundational/theory sources** — established works that anchor the argument
- **10–20 recent sources** (2020+) — showing awareness of current debates
- **5–10 region-specific sources** — Nigeria, Southeast Nigeria, or directly comparable context
- **3–5 methods/measurement sources** — anchoring the paper's methodology or evaluation approach
- **3–5 counterargument/critique sources** — demonstrating intellectual honesty
- **2–4 policy/standards/legal sources** — where the paper touches governance frameworks

Not all papers need every category equally, but every paper needs counterarguments and regional grounding.

---

## Acceptable Claim Types

| Type | Acceptable? | Requirements |
|------|-------------|--------------|
| Empirical claim from data | ✅ | Must cite data source, method, limitations |
| Theoretical claim from established framework | ✅ | Must cite framework and show application logic |
| Design claim from design science | ✅ | Must follow DSR conventions (Hevner, Peffers) |
| Analogical claim ("X is like Y") | ⚠️ Cautious | Must explicitly state it is analogy, not evidence |
| Speculative claim | ❌ Unless marked | Must be labelled as conjecture or future work |
| Claim from a single grey-literature source | ❌ | Must be corroborated or explicitly flagged as preliminary |

---

## Unacceptable AI-Slop Patterns

These patterns disqualify a draft from promotion:

- **Generic framing**: "In today's rapidly evolving digital landscape…"
- **Empty sophistication**: "This paper explores the multifaceted interplay…"
- **False certainty**: "This framework will transform governance…"
- **Buzzword stacking**: "leveraging blockchain for transparent, inclusive, sustainable, equitable…"
- **Uncited claims**: Any substantive claim without a source reference
- **Romanticized local institutions**: "community institutions have always governed wisely…"
- **Reviewer-bait without substance**: citing Ostrom or Tyler without showing how their framework applies
- **Aspirational methods**: describing evaluation plans that won't be executed before submission

---

## Threshold for Promoting to Draft

A paper may be promoted when:

- [ ] `claim_map.md` has at least 5 core claims with support levels of "moderate" or better
- [ ] `contradiction_map.md` is non-empty (at least 2 documented disagreements)
- [ ] `source_gaps.md` has no "critical" gaps remaining
- [ ] `reviewer_attack_surface.md` has at least 3 anticipated objections with defense strategies
- [ ] `thesis.md` has a stable thesis (not changing every session)
- [ ] `scope.md` is clear enough to write a coherent outline from
- [ ] `track_fit.md` is credible (track language maps to paper's actual contribution)
- [ ] Regional grounding exists (for papers about Nigeria/SE Nigeria)

---

## Impact-Journal Thresholds

The lab must not use "impact-journal", "submission-ready", or "global standard"
language for a paper package unless all of these are true:

- Article-specific prior-art review passes for that exact paper, not only for
  the lab infrastructure.
- Rights, source authority, and public-release scope are clear.
- A domain expert or domain postdoc has reviewed the argument.
- An adversarial impact-journal reviewer has signed the review trace.
- The manuscript is a full paper, not a 1,400-word skeleton with a table.
- The paper has a central result that matters outside the repo.
- The result is either empirical, formal, source-critical, or negative-result
  evidence strong enough to survive review in the target field.
- The abstract states the result, not the lab machinery.

Readiness categories:

| Category | Meaning | Allowed language |
|---|---|---|
| Working paper set | Evidence exists, but novelty, rights, depth, or domain review is insufficient. | "working draft", "internal review draft" |
| Journal-track draft | Clear result and venue path, but one or more human gates remain. | "journal-track draft", "not submission-ready" |
| Impact candidate | Prior art, rights, domain review, adversarial review, and manuscript depth pass. | "impact-journal candidate" |
| Submission-ready | All impact-candidate gates plus final format/package/review-team trace pass. | "ready for human submission review" |

For the Nwagu Aneke ten-article package, the current correct status is
`WORKING_PAPER_SET_NOT_IMPACT_READY` until article-specific prior art, rights,
source authority, domain review, and manuscript depth are fixed.

## A+ Lab Stage Gate

The stronger rule is: no output may look more mature than its evidence stage.

The canonical stages are:

1. `RESEARCH_PROGRAM`
2. `SOURCE_DOSSIER`
3. `CLAIM_MODEL`
4. `EXPERIMENTAL_RESULT`
5. `PAPER_CANDIDATE`
6. `SUBMISSION_CANDIDATE`
7. `PUBLIC_RELEASE_READY`

For Nwagu Aneke, the ten article directories are research branches with internal
review PDFs. They are not ten impact papers. Only two branches should be under
active article hardening at a time unless a human explicitly changes the
portfolio decision:

- `ARTICLE-NA-002` count-layer drift
- `ARTICLE-NA-010` layer-safe generative design

Run:

```bash
python scripts/validate_lab_standard.py
```

before article regeneration, package hardening, or readiness claims.

---

## Writing Standards

All prose must:

- Use precise contribution language (not "explores" — says what it actually does)
- Define key terms before using them
- Distinguish between what is known, what is argued, and what is speculated
- Handle disagreement explicitly, not by omission
- Acknowledge limitations honestly, not as a formulaic paragraph at the end
- Avoid rhetorical inflation: "groundbreaking," "novel," "first-ever" require actual evidence of novelty
- Maintain internal coherence: abstract matches body, claims match evidence, methods match evaluation

---

## Definition of "Good Enough for ICEGOV"

ICEGOV is a serious e-governance venue with interdisciplinary reviewers. A paper is good enough when:

1. A skeptical governance researcher would learn something from it
2. The claims are defensible under peer review
3. The local grounding is genuine, not cosmetic
4. The methodology is appropriate for the paper type (research / ongoing research / short)
5. The paper compiles, reads cleanly, and meets formatting requirements
6. The abstract honestly represents the paper's actual content

---

## Research-Team Completion Gate

A formatted PDF, passing compile, or high internal benchmark score is never
enough to call a paper complete. Before any readiness status can be set to
`READY_FOR_HUMAN_ARXIV_REVIEW`, `READY_FOR_SUBMISSION`, or equivalent, the paper
must have a passing `review_team_trace.jsonl` with these roles:

- `research_lead`
- `domain_postdoc`
- `methods_reviewer`
- `adversarial_impact_reviewer`
- `citation_evidence_reviewer`
- `rights_authority_reviewer`

The adversarial impact reviewer must attack venue fit, novelty, evidence
strength, public readability, and whether the paper would be rejected as a
formatted lab note rather than a real article. Any missing role, conditional
pass, or blocking issue downgrades the paper to
`NOT_READY_REVIEW_TEAM_BLOCKED`.

Validation command:

```bash
python scripts/validate_review_team_gate.py
```
