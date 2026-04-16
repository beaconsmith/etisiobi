# Claim Ledger — ICegov / OGI Framework
> Every non-trivial sentence intended for a paper, memo, or public artifact must have an entry here.
> Nothing moves to PUBLISHABLE without a ledger entry and a named reviewer.
> See: `research/REGISTRY.md` for promotion rules.

---

## Active Claims

| ID | Claim text (abbreviated) | Type | Source | Status | Reviewer | Notes |
|----|--------------------------|------|--------|--------|----------|-------|
| CL-001 | "Africa's average EGDI score is 0.4247" | `computed` | UN EGov Survey 2024 | `publishable` | — | Cite UN DESA 2024 directly |
| CL-002 | "17% of Nigerian adults save in informal savings groups" | `computed` | World Bank GHS Panel | `publishable` | — | Cite World Bank GHSP data |
| CL-003 | "Only 4.9% of Nigerian households received government COVID assistance (March-July 2020)" | `computed` | Nwangwu (2024) | `publishable` | — | Cite Nwangwu IJRISS 2024 |
| CL-004 | "e-ROSCA DRC experiment: ~90% contribution compliance" | `computed` | Francois & Squires 2021 | `publishable` | — | Cite Science Advances 2021 |
| CL-005 | Workspace A: RV-01 = 94%, DPR-01 = 71%, OGI-Core = 83% | `illustrative` | None (fabricated) | **BLOCKED — see CONT-006** | — | Must be labelled illustrative or removed in v3 |
| CL-006 | "town unions... directly accountable to communities through consensus-based selection" | `human_judgment` | Nwangwu 2024 | `publishable` | — | Cite Nwangwu IJRISS 2024 |
| CL-007 | "WJP Rule of Law Index explicitly recognizes 'Informal Justice' but excludes it from aggregated scores" | `computed` | WJP 2025 methodology | `publishable` | — | Verify against WJP 2025 methodology doc |
| CL-008 | "The missing piece isn't money movement — it's verifiable coordination at scale" | `human_judgment` | Oroma README | `draft` | Nzube | This is a product framing claim, not a research claim — remove from paper or source clearly |

---

## Claim Types
- `computed` — value from a citable source (paper, dataset, official report)
- `illustrative` — hypothetical value for demonstration purposes — MUST be labelled in paper
- `interpretive` — inference from evidence, with reasoning stated
- `human_judgment` — qualitative statement from named person with direct knowledge
- `draft` — under review, not yet classified

## Promotion Rules
- `draft` → `publishable`: requires named reviewer + evidence reference
- `illustrative` → publishable: **not possible** — must remain labelled as illustrative
- Any claim of type `computed` must have a citable DOI or stable URL

---

## How to Add a Claim

When drafting a paper section, add every non-trivial factual claim here before writing it into the draft:

```markdown
| CL-NNN | "exact or abbreviated claim text" | type | source citation | draft | — | notes |
```

Then promote only after review.
