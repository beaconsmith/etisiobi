# Kill Criteria

> When to stop working on a paper. Killing a paper is a quality decision, not a failure.

---

## Automatic Kill Triggers

A paper should be killed or frozen immediately if any of the following become true:

### 1. Contribution Overlap
The paper's core contribution is not sufficiently distinct from another paper in the portfolio. Two papers arguing the same thing from different angles is one paper, not two.

### 2. Thin Source Base After Full Loop
After one complete source acquisition loop (seed queries + citation chasing + author following), the paper still has fewer than 8 vetted sources with direct usability. This means the literature doesn't support a standalone paper.

### 3. No Regional Grounding
For papers about Nigeria, Southeast Nigeria, community institutions, or informal governance: after two search sweeps, the paper still has no direct Nigeria/SE Nigeria empirical sources. Generic "Global South" or "Africa" is not sufficient.

### 4. Unevidenceable Thesis
The thesis depends on claims that cannot be evidenced within the submission timeline. "We will demonstrate X" when X requires pilot data that doesn't exist yet = kill unless the paper can be reframed as conceptual/design-only.

### 5. No Credible Methods Story
The paper proposes methods it cannot execute (e.g., "we conducted interviews" when no interviews were conducted; "we deployed a pilot" when no pilot exists).

### 6. Rhetoric Without Spine
The paper is mostly framing, motivation, and conceptual ambition with no stable argument spine. If you can't write 5 defensible claims in `claim_map.md`, the paper doesn't have a paper.

### 7. Weak Track Fit
The paper's actual content doesn't match the track description. Opportunistic submission to a less-competitive track is not a strategy.

### 8. Deadline-Forced Sloppiness
Deadline pressure would require cutting corners that violate `QUALITY_BAR.md`. A bad submission is worse than no submission.

---

## Soft Kill Signals

These don't trigger immediate kill but should prompt serious reconsideration:

- The paper keeps changing thesis every session
- Core claims are all rated "weak" in the claim map
- No counterargument sources can be found (suspicious — usually means the paper isn't engaging a real debate)
- The reviewer attack surface has high-risk items with no viable defense
- The paper depends heavily on a single source or framework
- The human researcher isn't excited about the paper's contribution

---

## Kill Procedure

When a paper is killed:

1. Update `PORTFOLIO.md` — change disposition to "Killed" with date and reason
2. Update the paper's `autoresearch.md` — record kill decision in Section 17
3. Update `decision_log.md` — append kill entry with reasoning
4. **Redistribute assets**: move any high-value sources to surviving papers' `source_inbox.md`
5. Do not delete the paper folder — it may contain reusable evidence

---

## Current Kill Candidates

| Paper | Risk | Reason | Decision Due |
|-------|------|--------|-------------|
| `platform-governance` (T10) | **High** | 4 sources, thinnest base, no academic spine, high anecdotal risk | After next source loop |
| `digital-sovereignty` (T2) | **Medium-High** | 5 sources, zero SE Nigeria coverage, Indigenous sovereignty transfer is speculative | After next source loop |
