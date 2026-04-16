# AI/ML — Compression, Tokenization & Generative Models

## [1] Language Modeling Is Compression
- **Authors:** Grégoire Delétang, Anian Ruoss, Paul-Ambroise Duquenne, Elliot Catt, Tim Genewein, Christopher Mattern, Jordi Grau-Moya, Li Kevin Wenliang, Matthew Aitchison, Laurent Orseau, Marcus Hutter, Joel Veness
- **Venue:** arXiv / ICLR 2024
- **Year:** 2023 (submitted), 2024 (revised)
- **DOI/URL:** https://arxiv.org/abs/2309.10668
- **Abstract:** Establishes that predictive models are lossless compressors. Chinchilla 70B compresses ImageNet patches to 43.4% and LibriSpeech audio to 16.4% of original size — outperforming domain-specific tools (PNG, FLAC) — despite being trained only on text. Bridges information theory and modern ML.
- **PAGC Relevance:** Directly mirrors PAGC's claim: a compact generative matrix (27×8=216 tokens) can serve as a universal predictor/compressor across domains. If LMs compress via prediction, PAGC's lexical cache is an optimized prior over high-frequency tokens.

## [2] Tokenization Is More Than Compression
- **Authors:** Kyle Buettner, Anastasios Kyrillidis
- **Venue:** arXiv
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2402.18376
- **Abstract:** Challenges the assumption that BPE's effectiveness stems from compression alone. Introduces PathPiece tokenizer segmenting text into minimum token count. Finds compression is insufficient to explain model performance, suggesting structural/semantic factors dominate.
- **PAGC Relevance:** PAGC's lexical cache is not merely compressive — it encodes moral/equity salience. This paper supports the idea that semantic weighting of tokens matters beyond raw compression ratio.

## [3] Scaffold-BPE: Enhancing Byte Pair Encoding for Large Language Models
- **Authors:** Haoran Xu et al.
- **Venue:** arXiv
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2404.17808
- **Abstract:** Proposes scaffold token removal to address frequency imbalance in BPE vocabularies. Shows that token structure affects downstream task performance non-trivially.
- **PAGC Relevance:** PAGC's 27-base structure is analogous to a scaffold vocabulary — a fixed generative base from which surface forms are derived. Scaffold-BPE's findings validate the design philosophy of anchor-based token sets.

## [4] Parity-Aware Byte-Pair Encoding: Improving Cross-lingual Fairness in Tokenization
- **Authors:** Multiple
- **Venue:** arXiv
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2508.04796
- **Abstract:** At every BPE merge step, maximizes compression gain of the worst-compressed language, trading global compression for cross-lingual parity. Shows fairness and compression are in tension.
- **PAGC Relevance:** PAGC is explicitly designed for equity — the lexical cache prioritizes moral/equity terms. Parity-Aware BPE is the closest operational analog in mainstream NLP to PAGC's equity-weighted token design.

## [5] When Worse is Better: Navigating the Compression-Generation Tradeoff in Visual Tokenization
- **Authors:** Multiple
- **Venue:** arXiv
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2412.16326
- **Abstract:** Shows that smaller stage-2 generative models benefit from more compressed stage-1 latents even when reconstruction degrades. Fundamental tradeoff between compression fidelity and generative modeling capacity.
- **PAGC Relevance:** PAGC's deliberate redundancy is a design choice on this tradeoff curve — redundancy aids generation even at the cost of compression efficiency. This paper provides the theoretical framing.

## [6] Unpacking Tokenization: Evaluating Text Compression and Its Correlation with Model Performance
- **Authors:** Multiple
- **Venue:** arXiv
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2403.06265
- **Abstract:** Comprehensive study showing compression consistently correlates with generation performance across model sizes, with particularly pronounced impact for smaller models.
- **PAGC Relevance:** For low-resource languages (like Igbo), where model size is constrained, PAGC's compressed 216-token matrix may yield disproportionate gains consistent with this paper's finding.

## [7] On the Compatibility of Generative AI and Generative Linguistics
- **Authors:** Eva Portelance
- **Venue:** arXiv
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2411.10533
- **Abstract:** Examines theoretical compatibility between statistical generative AI and Chomskyan generative linguistics, arguing that surface-level generation in LLMs implicitly encodes structural linguistic priors.
- **PAGC Relevance:** PAGC bridges generative linguistics (syllabary structure) and generative AI. This paper provides the theoretical scaffold for claiming structural linguistic priors (like the 27×8 matrix) are implicitly learned or exploitable by LLMs.

## [8] Token Reduction Should Go Beyond Efficiency in Generative Models
- **Authors:** Multiple
- **Venue:** arXiv
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2505.18227
- **Abstract:** Reviews token reduction from vision, language, and multimodal perspectives, arguing efficiency is a narrow goal. Tokens should also encode semantic salience and representational quality.
- **PAGC Relevance:** PAGC's lexical cache is a form of principled token salience — high-frequency moral/equity terms are retained not for compression efficiency but for semantic load-bearing capacity.

## [9] Extreme Compression of Large Language Models via Additive Quantization
- **Authors:** Multiple
- **Venue:** arXiv
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2401.06118
- **Abstract:** AQLM: targets 2-3 bits per parameter using multi-codebook quantization. Joint optimization of codebook parameters across transformer blocks via learned additive quantization.
- **PAGC Relevance:** PAGC's 216-token matrix is a micro-codebook for language. AQLM's multi-codebook quantization parallels PAGC's base × modifier architecture — a combinatorial codebook where tokens are decoded from base+modifier combinations.

## [10] zip2zip: Inference-Time Adaptive Tokenization via Online Compression
- **Authors:** Multiple
- **Venue:** arXiv
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2506.01084
- **Abstract:** Dynamic vocabulary continuously expanded via LZW compression. Codebook maps hypertoken IDs to base tokens, enabling adaptive tokenization at inference time.
- **PAGC Relevance:** PAGC's base × modifier combinatorial structure is a static but principled version of adaptive tokenization — the 8 modifiers act as compression transforms on the 27 bases.
