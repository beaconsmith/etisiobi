# Reviewer 2 Response Plan

Article: `ARTICLE-NA-010`

Status: `DRAFT_ATTACK_SURFACE`

## Core Reviewer Risk

The likely rejection risk is that reviewers read the non-promotion invariant as
too obvious, too synthetic, or insufficiently distinguished from provenance and
type-system work.

## Anticipated Objections and Planned Responses

| Objection | Risk | Response Needed |
|---|---|---|
| This is just provenance with another name. | High | Show that provenance records derivation, while the invariant constrains allowed output assertions. |
| Seven test cases are too small. | High | Expand with held-out claims from multiple Nwagu Aneke branches and add no-label/provenance-only baselines. |
| The layer order is arbitrary. | Medium | Justify the order as claim-strength governance, not ontological truth. |
| The paper is not really about Nwagu Aneke. | Medium | Frame Nwagu Aneke as the motivating artifact and evaluation surface, not as a universal proof source. |
| It may suppress useful derived design. | Medium | Emphasize that derived claims remain allowed when labeled as derived. |
| Public-release rights are unclear. | High | Keep source examples text-only until rights and authority clearance is attached. |
| The manuscript contains lab-process language. | Medium | Rewrite the article around research question, hypothesis, invariant, test cases, and limitations. |

## Required Manuscript Changes

1. State a concise research question and hypothesis.
2. Move development-status discussion out of the main contribution frame.
3. Compare the invariant to provenance, type systems, and claim verification.
4. Add the layer-safety case table.
5. Add a benchmark expansion plan with baselines.
6. Keep rights/source-authority blockers visible.

## Current Decision

This response plan is sufficient to guide the next rewrite. It is not evidence
that the article can survive peer review yet.
