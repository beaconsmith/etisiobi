# Entities — entity memory

An **entity page** is the single maintained page about one actor, system, or
standard that recurs across research programs: a product (Oroma), an
organisation (IC3, LEMA Lab, Flow-Research), a protocol/chain (Citrea, Miden), or
a standard (ERC-8004, EIP-7702).

Entity memory answers: *"What do we currently know and believe about X, and what
should we watch?"* — without re-deriving it in every session or program wiki.

## Rules

1. **One page per entity.** Do not create duplicates; update the canonical page.
2. **Separate observation from interpretation.** State facts, then our reading.
3. **Cite sources** where a claim depends on evidence — link `external_sources/`,
   `library/`, or a program wiki. Unsourced reasoning must be marked as such.
4. **Mark claim status** inline: `supported`, `weak`, `contradicted`, `rejected`,
   `needs-review`, or `draft`.
5. **If evidence contradicts a claim, add the contradiction** — do not silently
   overwrite. Link `uncertainty/contradictions.md` or the program contradictions file.
6. **Say what it teaches Oroma** where relevant. Research exists to serve the product.
7. **No product doctrine is set here.** Entity pages inform; they do not decide.
   Promotion to Oroma product work goes through `ETISIOBI_OROMA_FEED.md` review.

## Template

```markdown
# <Entity>
> status: draft | maintained   | updated: YYYY-MM-DD

## What it is
## Current state / stage
## What we believe (with claim status + sources)
## Open questions
## What Etisiobi must watch
## What this teaches Oroma
## Sources
```
