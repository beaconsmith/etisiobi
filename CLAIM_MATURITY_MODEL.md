# Claim Maturity Model

Generated: 2026-05-28

Every Etisiobi claim must carry a maturity label.

| Label | Name | Meaning |
|---|---|---|
| C0 | raw observation | A file, event, source, note, image, or artifact exists but has not been extracted into a claim. |
| C1 | extracted claim | A claim has been extracted from a source, but the source locator or support relation is incomplete. |
| C2 | source-located claim | The claim has a source path or external locator and can be revisited by another researcher. |
| C3 | internally consistent claim | The claim does not contradict stronger repo-local evidence in the current corpus. |
| C4 | externally contextualized claim | The claim has been checked against relevant external prior art or standards. |
| C5 | experimentally/formally supported claim | The claim has reproducible empirical, formal, or source-critical support. |
| C6 | publication-ready claim | The claim has evidence, citations, limitations, contradiction review, and reproducibility notes. |
| C7 | emitted claim | The claim has been released in a paper, dataset, software artifact, policy brief, standard, or atlas. |
| CX | rejected claim | The claim is false, contradicted, overclaimed, or too weak for use except as a negative result. |

## Promotion Rules

- C0 -> C1: extract a claim from an artifact, source, event, result, or note.
- C1 -> C2: add path, line, page, event id, DOI, URL, or other locator.
- C2 -> C3: check against repo-local contradictions.
- C3 -> C4: contextualize with external prior art or standards.
- C4 -> C5: run a reproducible experiment, source-critical audit, or formal derivation.
- C5 -> C6: add limitations, reviewer objections, citation audit, rights review, and reproduction commands.
- C6 -> C7: emit through a governed output channel.
- Any level -> CX: contradiction, failed experiment, unsupported overclaim, or rights/ethics failure.

## Current Lab Contradictions

| ID | Contradiction | Status | Action |
|---|---|---|---|
| CONTRA-001 | 26 printed rows vs derived 27 bases vs 216 matrix | resolved into layers, not closed as exact 27 | Keep 27 and 216 out of positive source claims. |
| CONTRA-002 | 164 actual symbols vs 224 ideal syllabary space | open | Archive/extract Ahamefula and reconcile with Azuonye Appendix I/II. |
| CONTRA-003 | E6 and exceptional math depend on an unstable 27-object | blocked | Move E6 to rejected/speculative lattice until formal object is defined. |
| CONTRA-004 | OGI deadline and ACM format drift | open publication risk | Human venue/date decision before any submission package. |
| CONTRA-005 | Conceptual simulations risk being promoted as empirical results | guarded | Emit as concept/demo only unless benchmarks and null models exist. |
