# PAGC Falsification Tracker

> Active falsification control surface for Principle of Ancestral Generative Compression.
> Created: 2026-04-24.

## Rule

PAGC claims are false until proven. Claims advance only when they cite an archived source, an extraction method, and a test that can fail them. Cross-disciplinary analogies are treated as hypotheses until they pass discipline-specific tests.

## Source Integrity Gate

| Gate | Required before claim advancement |
|---|---|
| Source archive | Claim cites a local source artifact under `primary_sources/nwagu_aneke/` or another vetted source folder |
| Extraction method | Claim explains how evidence was transcribed, counted, measured, or computed |
| Falsification test | Claim states what result would defeat it |
| Status label | Claim is labeled `source-observed`, `extracted`, `tested`, or `speculative` |

## Claim Status (Updated 2026-04-27 — Chart Transcription Pass)

| Claim | Current status | Falsification test | Result / Blocking evidence |
|---|---|---|---|
| 27 bases exist as a source-derived inventory | **UNCERTAIN — 26–28 rows observed** | Transcribe archived chart and Azuonye appendix; count reusable base rows without assuming PAGC | Chart transcription shows 26–28 consonant rows (exact count ambiguous for ~3 rows). BMCG spec internally says "26", not "27". Web sources say "~200 symbols" not 216. **Azuonye PDF reading required to resolve.** |
| 8 modifiers exist as a source-derived inventory | **VISUALLY CONFIRMED from chart** | Transcribe archived chart and Azuonye appendix; count systematic columns/modifiers without assuming PAGC | Chart shows exactly 8 vowel columns matching Standard Igbo 8-vowel system (a, i, o, u, e, ị, ọ, ụ). ✅ Confirmed from source chart. |
| 27 bases are optimal for Igbo compression | **REFUTED on small corpus** | BPE/MDL sweep over diverse Igbo corpus; check whether optimum converges near 27 | BPE sweep (7,368 words) shows inflection at k=16, not k=27. Needs replication on CC-100 (~15MB) corpus. See `experiments/01_bpe_igbo_k27/results/report.md`. |
| 8 modifiers are structurally optimal | False until tested | Modifier ablation; check for perplexity or reconstruction discontinuity at k=8 | Explicit modifier inventory and corpus annotation needed. |
| 216-token matrix improves constrained memory | **INVALIDATED — circular experiment** | Compare bounded 216-token memory against baselines in non-stationary RL | Experiment 05 hardcodes `state % 27 == 0` as the invariant while PAGC agent uses `raw_state % 27` as encoder. Result is circular. Needs redesign with null-model baselines and non-aligned invariant structure. |
| E6 symmetry / 27-line correspondence | High-risk hypothesis | Embed bases; compute Gram/eigen structure; compare to E6 representation expectations | Blocked by unconfirmed base count. If count is 26 not 27, the E₆ connection (which requires exactly 27) is falsified at the foundational level. |
| Universal compression across domains | Extraordinary claim | MDL comparison across text, music, visual, and graph data | Cross-domain datasets and baseline compressors needed. |
| Genetic-code isomorphism | Speculative analogy | Information-theoretic distance from codon table vs. random/control code tables | Formal encoding relation and null model needed. |
| Decolonial epistemology contribution | **Strong independent contribution — survives all tests** | Historical/source audit and careful epistemic framing | Source audit in progress. Chart transcription + logograph semantic analysis supports concentration in moral/social domains. Independent of whether exact numbers are 26 or 27. |

## Kill / Downgrade Rules

- If BPE/MDL does not favor 27 on high-quality Igbo corpora, downgrade "27 optimality" to historical/design property.
- If E6 comparisons fail under a clear null model, remove exceptional-Lie claims from the main thesis.
- If cross-domain compression does not beat standard baselines, kill "universal compression" and retain only domain-specific claims.
- If provenance sources are weak, keep the math/linguistics claims separate from ancestral revelation framing.

## Next Tests (Updated 2026-04-27)

1. **🔴 CRITICAL: Download and read Azuonye 1992 PDF** — Resolve the 26 vs 27 vs 28 consonant row count. The PDF is freely available at `https://scholarworks.umb.edu/cgi/viewcontent.cgi?article=1012&context=africana_faculty_pubs`. This single action either confirms or refutes PAGC's foundational number.
2. **🔴 CRITICAL: Resolve internal inconsistency** — BMCG spec says "Consonant (26)", all other PAGC files say "27 bases." One of these is wrong. Fix after Azuonye PDF confirms the source count.
3. **🟡 Scale BPE experiment** — Re-run on CC-100 Igbo corpus (~15MB). k=27 was refuted on 7,368 words; check if larger corpus changes result.
4. **🟡 Redesign RL experiment** — Current experiment is circular (baked-in modular arithmetic). Needs: (a) non-aligned invariant, (b) random-hash null models of same size, (c) size ablation.
5. **🟢 Compile WIKI.md** — Synthesize discipline files, KB articles, and paper summaries into single KB with per-claim status linked to this tracker.
6. **🟢 Locate Ahamefula & Mbah 2011 full text** — Independent structural count from linguistic analysis.

