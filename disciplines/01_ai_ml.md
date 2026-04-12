# Discipline 01: Artificial Intelligence / Machine Learning

**Impact Rating:** HIGH
**Principia-Level Flag:** YES

---

## Relevance Summary

AI/ML is the discipline most immediately actionable for PAGC. The 27×8 generative matrix is structurally identical to the codebook architectures underlying tokenization (BPE, SentencePiece) and quantization (multi-codebook AQLM). The lexical cache mirrors high-frequency token priors in language models. PAGC proposes a principled, culturally-grounded alternative to entropy-only tokenizer design for low-resource African languages.

---

## Sources

See `paper/papers/ai_ml_compression_tokenization.md` for full citations. Key sources:

1. Delétang et al. (2023/2024) — "Language Modeling Is Compression" — arXiv 2309.10668
2. Buettner & Kyrillidis (2024) — "Tokenization Is More Than Compression" — arXiv 2402.18376
3. Xu et al. (2024) — "Scaffold-BPE" — arXiv 2404.17808
4. Multiple (2025) — "Parity-Aware BPE" — arXiv 2508.04796
5. Multiple (2024) — "When Worse is Better" — arXiv 2412.16326
6. Multiple (2024) — "Unpacking Tokenization" — arXiv 2403.06265
7. Portelance (2024) — "Generative AI and Generative Linguistics" — arXiv 2411.10533
8. Multiple (2025) — "Token Reduction Beyond Efficiency" — arXiv 2505.18227
9. Multiple (2024) — "Extreme Compression via Additive Quantization" — arXiv 2401.06118
10. Multiple (2025) — "zip2zip Adaptive Tokenization" — arXiv 2506.01084

---

## PAGC Mapping

| PAGC Component | AI/ML Analog | Implication |
|---|---|---|
| 27 bases | BPE vocabulary scaffold | 27 roots = minimum generative vocabulary for Igbo |
| 8 modifiers | Codebook quantization dimensions | 8 compression transforms on base tokens |
| 216 tokens | Multi-codebook codebook size | Optimal vocabulary size for low-resource Igbo LM |
| Lexical cache | High-frequency token prior | Equity/moral terms get zero-entropy prior |
| Surface variation tolerance | Token normalization | Multiple surface forms → single canonical embedding |
| Deliberate redundancy | Compression-generation tradeoff | Redundancy improves generalization (Redundancy as Structural Principle, 2024) |

**Open Problem PAGC Could Solve:** The equity gap in tokenization — Igbo is ~3× over-tokenized relative to English in GPT-4's tokenizer (same semantic content requires 3× more tokens). PAGC's 216-token matrix trained as a BPE vocabulary for Igbo would directly close this gap.

---

## Proposed Experiments

1. **PAGC Tokenizer Benchmark:** Train a BPE tokenizer seeded with PAGC's 216-token vocabulary on Igbo text corpus. Compare compression ratio, downstream task performance, and equity metrics against standard BPE on the same corpus.

2. **Lexical Cache Validation:** Test whether PAGC's high-frequency moral/equity terms have systematically lower surprisal (lower N400 analog in LM) than non-cache tokens — confirms that the cache captures true frequency structure.

3. **Cross-domain Compression:** Following Delétang et al., test whether a PAGC-trained LM compresses non-text Igbo data (drumming patterns, textile patterns, oral narrative structures) better than generic LMs — tests PAGC's universality claim empirically.

4. **Modifier Ablation:** Train LMs with progressively fewer modifiers (8→4→2→1). Measure perplexity on held-out Igbo text. If perplexity increases super-linearly below 8, this confirms the 8-modifier dimension is not arbitrary.

---

## Critiques & Counter-Arguments

- **The vocabulary size is not special:** Any vocabulary of ~200 tokens trained on Igbo text would achieve similar compression. PAGC's 27×8 structure needs to show it outperforms a random 216-token vocabulary.
- **The lexical cache is circular:** If the cache is defined as high-frequency moral terms, it will trivially score low surprisal on a corpus of moral texts. It needs validation on diverse, naturalistic Igbo corpora.
- **Surface variation tolerance is standard normalization:** Unicode normalization and stemming already handle this in NLP. PAGC needs to show its approach handles cases that standard normalization misses.
- **"Ancestral" provenance does not confer mathematical validity:** The claim that the structure was revealed by ancestors is epistemologically separate from whether the 27×8 structure is optimal. These must be evaluated independently.
