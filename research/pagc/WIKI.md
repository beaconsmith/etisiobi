# PAGC Research Wiki
> LLM-maintained knowledge base. Status: stub — compile from disciplines/ and paper/kb/ on next session.
> Say: "Compile PAGC wiki from existing sources" to build this out.

---

## What This Wiki Covers

The Principle of Ancestral Generative Compression (PAGC): a 27-base × 8-modifier generative matrix (216 tokens) originating from the Nwagu Aneke Igbo syllabary, mapped across 17 frontier disciplines. Active research focus: mathematical falsification tests for the E₆ symmetry claim and universal compression claim.

---

## Quick Reference

| Resource | Location |
|----------|----------|
| Full discipline rankings (17 disciplines) | `INDEX.md` |
| Nwagu Aneke syllabary primary source | `paper/kb/nwagu_aneke_syllabary.md` |
| Mathematics: E₆, 27 lines, Albert algebra | `paper/kb/mathematics_27_e6_jordan.md` |
| BPE sweep experiment (k=27) | `../../experiments/01_bpe_igbo_k27/` |
| Sovereign Memory RL simulation | `../../experiments/05_sovereign_memory_rl/` |
| Frontier applications (all disciplines) | `sources/pagc_library/frontier_applications.md` |

---

## Core Claim

PAGC is a proposed universal generative mechanism, inspired by the Nwagu Aneke Igbo script's combinatorial design (27 base symbols × 8 modifiers = 216 tokens). The claim is that this structure recurs in or can be mapped onto information theory, mathematics (E₆ Lie group), quantum computing, synthetic biology, and cognitive science.

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
