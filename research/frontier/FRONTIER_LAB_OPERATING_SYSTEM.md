# Frontier Lab Operating System

## Objective

Etisiobi becomes A-grade only when it repeatedly produces externally legible
research results. The lab standard is therefore:

```text
research branch -> benchmarked question -> result -> adversarial review -> paper candidate
```

The lab must not optimize for document count.

## Lab Roles

Every promoted research branch gets a standing team:

| Role | Responsibility |
|---|---|
| Research lead | Owns thesis, result, scope, and decision trace. |
| Domain postdoc | Checks source-critical, linguistic, historical, or cultural claims. |
| Methods reviewer | Checks experimental design, benchmark validity, and reproducibility. |
| SOTA scout | Runs external search and maintains prior-art collision risk. |
| Adversarial impact reviewer | Writes the rejection case before the paper is expanded. |
| Citation/evidence reviewer | Verifies claims, locators, citation metadata, and quote discipline. |
| Rights/authority reviewer | Blocks public release until source, community, and rights questions are handled. |
| Product translator | States what the result teaches Oroma or Beaconsmith systems. |

## Frontier Research Lanes

| Lane | Frontier question | First benchmark/result |
|---|---|---|
| Artifact reconstruction | How can unencoded African scripts be reconstructed without collapsing source and interpretation? | Nwagu source/derived count ledger. |
| Layer-safe generative systems | How can artifact-derived design systems prevent speculative claims from becoming source facts? | Layer Promotion Error benchmark. |
| Low-resource NLP | Can artifact-derived constraints improve Igbo tokenization or evaluation beyond generic BPE? | Source-layer vs derived-layer tokenizer baselines with downstream task gate. |
| Cultural heritage interoperability | Can TEI/IIIF/Web Annotation/CIDOC CRM represent Nwagu evidence without overclaiming glyph certainty? | Standards mapping with explicit blocked fields. |
| Community-governance evidence | Can Oroma events produce evidence strong enough for governance measurement claims? | OGI event-to-claim benchmark. |

## Promotion Tournament

Every month, research branches are ranked by:

```text
frontier_score =
  0.20 * external_problem_importance
+ 0.20 * result_strength
+ 0.15 * benchmark_quality
+ 0.15 * prior_art_gap
+ 0.10 * reproducibility
+ 0.10 * reviewer_survivability
+ 0.05 * rights_authority_clarity
+ 0.05 * product_or_field_reuse
- 0.20 * overclaim_risk
- 0.10 * weak_branch_sprawl
```

Only the top two branches may enter paper hardening.

## Current Frontier Bet

The first frontier bet is:

```text
Layer Promotion Error detection for artifact-derived research and design systems.
```

Reason:

- It is rooted in the accepted Nwagu Aneke foundation: source layer is 26 x 8 = 208; 27/216 is derived.
- It generalizes beyond this repo to AI-assisted humanities, cultural heritage, standards work, and design systems.
- It produces a benchmarkable failure mode, not just prose.
- It directly fixes the lab's recurring error: letting generated outputs upgrade weak claims.

## Stop Condition

The lab must kill or park this frontier bet if the next sprint cannot show that
Layer Promotion Error is distinct from ordinary claim verification, provenance
validation, or type checking. A new name is not a contribution.

The contribution must be one of:

- a benchmark that existing claim-verification/provenance tools do not already
  cover;
- an empirical result showing common AI research-writing systems commit layer
  promotion errors;
- a formal type/evidence system that prevents such promotion across artifact,
  design, and publication layers;
- a negative result proving the problem is better handled by existing methods.
