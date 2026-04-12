# Knowledge Base: Information Theory Fundamentals Relevant to PAGC

## [1] Language Modeling Is Compression (Delétang et al., 2023)
- **URL:** https://arxiv.org/abs/2309.10668
- **Key result:** Predictive models = lossless compressors. LMs trained on text compress cross-domain data better than domain-specific tools (PNG, FLAC). Compression ↔ prediction equivalence.
- **PAGC mapping:** A 216-token PAGC model is a compressor. Its compression ratio on Igbo text vs. standard UTF-8 is a direct empirical measure of PAGC's generative efficiency.

## [2] Redundancy as a Structural Information Principle for Learning and Generalization
- **Authors:** Multiple
- **Venue:** arXiv
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2510.10938
- **Abstract:** Shows that redundancy in representations improves generalization beyond efficiency gains from compression. Redundancy enables robust learning from limited examples.
- **PAGC Mapping:** Directly validates PAGC's deliberate redundancy design. Redundancy is not a bug — it is the mechanism by which the 216-token vocabulary generalizes to novel surface forms.

## [3] Structured Grammar-Based Codes for Universal Lossless Data Compression
- **Authors:** Multiple
- **Venue:** ResearchGate / IEEE
- **URL:** https://www.researchgate.net/publication/228880174_Structured_grammar-based_codes_for_universal_lossless_data_compression
- **Abstract:** Context-free grammar decomposition into structure + data, encoding data conditional on structure. Maximal redundancy O(1/log n). Demonstrates that grammatical structure achieves near-universal compression.
- **PAGC Mapping:** PAGC is a grammar-based code. Its 27×8 matrix is the structural component; lexical cache items are the data component. This framework allows PAGC to be formally analyzed as a universal code.

## [4] Information Theory as a Bridge Between Language Function and Language Form
- **Authors:** Multiple
- **Venue:** Frontiers in Communication
- **Year:** 2022
- **URL:** https://www.frontiersin.org/journals/communication/articles/10.3389/fcomm.2022.657725/full
- **Abstract:** Shows that information-theoretic principles (entropy, redundancy, surprisal) link functional communicative pressures to the observable forms of language.
- **PAGC Mapping:** PAGC's form (27×8 matrix) is shaped by functional pressure (moral/equity communication efficiency). This paper provides the theoretical link between PAGC's communicative function and its structural form.

## [5] Minimum Description Length: Tutorial Introduction (Grünwald)
- **Authors:** Peter Grünwald
- **Venue:** CWI / MIT Press
- **Year:** 2004
- **URL:** https://homepages.cwi.nl/~paulv/course-kc/mdlintro.pdf
- **Abstract:** Tutorial on MDL principle. Model selection = finding the model that most compresses the data. MDL = approximation to Kolmogorov complexity for practical inference.
- **PAGC Mapping:** PAGC's 27×8 design can be evaluated as an MDL model of Igbo phonological/semantic data. If it achieves lower description length than Unicode/UTF-8 for Igbo text, it is the preferred model by MDL.

## [6] English Redundancy (~50%)
- **Source:** Shannon (1948, 1951); multiple replications
- **Key result:** English has ~50% redundancy — half of letters in a typical sentence could be removed and meaning recovered. This redundancy enables error correction.
- **PAGC Mapping:** PAGC's deliberate redundancy (surface variation tolerance) mirrors Shannon's finding. The question is: what is the optimal redundancy for Igbo specifically? PAGC posits it is achieved by the 27×8 structure.
