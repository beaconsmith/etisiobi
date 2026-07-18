# PAGC Research Wiki
> LLM-maintained knowledge base. Status: stub — compile from disciplines/ and paper/kb/ on next session.
> Say: "Compile PAGC wiki from existing sources" to build this out.

---

## Reset Rule

All PAGC claims are false until proven. This wiki must distinguish source-observed facts from extracted inventories, tested claims, and speculative analogies.

Primary source gate: [`primary_sources/nwagu_aneke/README.md`](primary_sources/nwagu_aneke/README.md). Reset note: [`PAGC_RESET.md`](PAGC_RESET.md). Derived formal hypotheses use the [`DERIVED_HYPOTHESIS_CHARTER.md`](DERIVED_HYPOTHESIS_CHARTER.md) lane.

---

## What This Wiki Covers

The Principle of Ancestral Generative Compression (PAGC): a hypothesis program around whether the Nwagụ Aneke Igbo syllabary supports any reproducible base/modifier structure or useful compression/tokenization experiments. The previous `27-base × 8-modifier` framing is now treated as an unproven claim, not a theory.

---

## Quick Reference

| Resource | Location |
|----------|----------|
| Full discipline rankings (17 disciplines) | `INDEX.md` |
| Nwagụ Aneke source archive | `primary_sources/nwagu_aneke/` |
| Nwagu Aneke syllabary source note | `paper/kb/nwagu_aneke_syllabary.md` |
| Mathematics: E₆, 27 lines, Albert algebra | `paper/kb/mathematics_27_e6_jordan.md` |
| BPE sweep experiment (k=27) | `../../experiments/01_bpe_igbo_k27/` |
| Sovereign Memory RL simulation | `../../experiments/05_sovereign_memory_rl/` |
| Falsification tracker | `FALSIFICATION_TRACKER.md` |
| Frontier applications (all disciplines) | `sources/pagc_library/frontier_applications.md` |

---

## Core Hypothesis

PAGC asks whether a source-derived inventory of the Nwagụ Aneke script reveals a reusable base/modifier structure, and whether that structure helps with measurable Igbo tokenization, compression, memory, or representation tasks.

The current repository does not yet prove `27×8`, E₆ symmetry, universal compression, or genetic-code isomorphism.

Formal hypotheses may still be developed as modern derived constructions when
they keep source claims strict, define the invented step, state baselines, and
name kill conditions.

Current derived-hypothesis record:
[`DH-001: Derived 27 x 8 Completion`](hypotheses/DH-001-derived-27x8-completion.md)
has a bounded internal toy baseline plus a small source-promotion
counterexample screen and source-record screen. It keeps `27 x 8 = 216` in the
derived formal lane and does not change the source-observed `26 x 8 = 208`
foundation. The global benchmark gate parks it because its current positive
signal is label-dependent.

Current strongest next derived-hypothesis branch:
[`DH-003: Layer-Promotion Error Benchmark`](hypotheses/DH-003-layer-promotion-error-benchmark.md)
has produced a significant internal knowledge breakthrough: ten bounded,
traceable benchmark-design knowledge units from repo-local LPE cases, label
quality-gate evidence, and the layer-safety proof. This is internal research
knowledge only, not a public benchmark, paper-candidate, or global novelty
claim.

---

## Principia-Level Pathways (from INDEX.md)

1. **E₆ Symmetry Claim** — PAGC's 27 bases transform under Weyl group W(E₆). Test: embed bases in semantic vector space; compare Gram matrix eigenvalues to W(E₆) character table.

2. **Universal Compression Claim** — PAGC achieves MDL encoding of Igbo semantic space. Test: MDL comparison against UTF-8, BPE-Igbo, IPA on diverse Igbo corpus.

3. **BPE k=27 Hypothesis** — Optimal BPE vocabulary for Igbo is k=27 matching PAGC's base count. Test: active in `experiments/01_bpe_igbo_k27/`.

4. **Sovereign Memory Claim** — 216-token constrained memory buffer outperforms unbounded episodic memory in non-stationary RL environments. Test: complete in `experiments/05_sovereign_memory_rl/`.

---

## Status: Wiki Needs Compiling

The existing knowledge base is distributed across:
- `disciplines/` — 8 discipline analysis files
- `paper/kb/` — 3 knowledge base articles
- `paper/papers/` — 6 compiled paper summaries
- `sources/pagc_library/` — 17 source cluster files

To compile this wiki fully, run:
> "Compile PAGC wiki — synthesize disciplines/, paper/kb/, and paper/papers/ into WIKI.md with cross-references and a health check"

## Harness Status

The falsification layer now lives in `FALSIFICATION_TRACKER.md`. Any future PAGC paper draft should cite that tracker before making claims about E6 symmetry, universal compression, genetic-code isomorphism, or 216-token memory advantages.
