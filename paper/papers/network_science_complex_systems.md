# Network Science & Complex Adaptive Systems

## ── SESSION 2 ADDITIONS ──

## [S2-1] Network Reconstruction via the Minimum Description Length Principle
- **Authors:** Tiago P. Peixoto
- **Venue:** Physical Review X, Vol. 15, 011065
- **Year:** 2025
- **URL:** https://link.aps.org/doi/10.1103/PhysRevX.15.011065
- **Abstract:** Information-theoretic approach to reconstructing hidden networks from observed data. Minimizes description length of data given the network model. Applications in biology, neuroscience, economics. Improves accuracy and efficiency over existing methods.
- **PAGC Relevance:** PAGC's 27×8 concept graph has a minimum description length — the Kolmogorov complexity of the Igbo semantic graph. This paper's MDL framework is the formal tool for proving PAGC achieves minimum-complexity encoding of Igbo knowledge. If the MDL of the full Igbo semantic graph equals the MDL of PAGC's 216-token matrix, PAGC is a Kolmogorov-optimal description.

## [S2-2] Comprehensive Survey on Link Prediction: From Heuristics to Graph Transformers
- **Authors:** Multiple
- **Venue:** The Journal of Supercomputing (Springer)
- **Year:** 2025
- **URL:** https://link.springer.com/article/10.1007/s11227-025-07882-8
- **Abstract:** Full survey from classical similarity indices to graph embedding methods, GNNs, and Graph Transformers for link prediction. Covers static and dynamic networks. State-of-the-art comparison.
- **PAGC Relevance:** Link prediction in PAGC's concept graph = predicting which base×modifier combinations will generate the next high-frequency token in Igbo cultural production. The Marwitz-style methodology (concept graph + link prediction) is directly applicable to PAGC, and this survey provides the full methodological toolkit.

## [S2-3] Survey of GNN Methods for Dynamic Link Prediction
- **Authors:** Multiple
- **Venue:** ScienceDirect (Procedia)
- **Year:** 2025
- **URL:** https://www.sciencedirect.com/science/article/pii/S1877050925007938
- **Abstract:** Reviews temporal GNN architectures for dynamic link prediction. Covers TGNN, TGN, CAWN, and related models for evolving graphs.
- **PAGC Relevance:** PAGC's lexical cache should evolve as language evolves — high-frequency moral/equity terms shift over generations. Dynamic link prediction methods applied to PAGC's concept graph would model this temporal drift.

## [S2-4] Defining Complex Adaptive Systems: An Algorithmic Approach
- **Authors:** Multiple
- **Venue:** Systems, MDPI, Vol. 12, Issue 2
- **Year:** 2024
- **URL:** https://www.mdpi.com/2079-8954/12/2/45
- **Abstract:** Formal algorithmic framework for evaluating whether a system meets CAS attributes: autonomy, memory, self-organisation, emergence. Separates complexity-related attributes from adaptivity-related ones.
- **PAGC Relevance:** PAGC's generative matrix is a CAS: it has memory (lexical cache), self-organizes (surface variation from fixed deep structure), and exhibits emergence (novel token combinations from base×modifier). This paper provides a formal checklist to verify PAGC's CAS classification.

## [S2-5] Unveiling Simplexity: A New Paradigm for Understanding Complex Adaptive Systems
- **Authors:** Multiple
- **Venue:** ScienceDirect
- **Year:** 2025
- **URL:** https://www.sciencedirect.com/science/article/pii/S2666675825001572
- **Abstract:** Introduces "simplexity" — intricate interactions giving rise to simple, intuitive outcomes without losing underlying complexity. Complexity as balance between emergence and self-organization.
- **PAGC Relevance:** PAGC is a simplexity system: a 27×8 matrix (simple surface) generates semantically rich Igbo expression (complex emergence). Simplexity theory provides the vocabulary for describing PAGC's compression/generation tradeoff non-reductively.

## [S2-6] BioPathNet: Path-Based GNN for Link Prediction in Biomedical Knowledge Graphs
- **Authors:** Multiple
- **Venue:** Nature Biomedical Engineering
- **Year:** 2025
- **URL:** https://www.nature.com/articles/s41551-025-01598-z
- **Abstract:** GNN framework based on neural Bellman-Ford networks for biomedical KG link prediction. Path-based reasoning across all relations along paths between node pairs. Addresses multi-relational link prediction limitations.
- **PAGC Relevance:** PAGC's 8 modifier types define 8 distinct relation types in the concept graph. BioPathNet's multi-relational path-based approach is the correct architecture for link prediction in a PAGC-structured graph — each modifier type is a distinct edge relation, and PAGC prediction traverses paths through modifier-typed edges.

---

## [1] Network Community Detection via Neural Embeddings
- **Authors:** Multiple
- **Venue:** Nature Communications
- **Year:** 2024
- **URL:** https://www.nature.com/articles/s41467-024-52355-w | PubMed: https://pubmed.ncbi.nlm.nih.gov/39487114/
- **Abstract:** Node2vec encodes communities into separable clusters better than random partitioning, reaching the information-theoretic detectability limit for stochastic block models. Neural embedding of graph structure recovers community organization.
- **PAGC Relevance:** PAGC's 27 bases can be embedded as nodes in a semantic graph where modifiers define edge types. Community detection on this graph would reveal which bases cluster into semantic families — a direct empirical test of PAGC's structural claims.

## [2] Community Detection in Hypergraphs via Mutual Information Maximization
- **Authors:** Multiple
- **Venue:** Scientific Reports (Nature)
- **Year:** 2024
- **URL:** https://www.nature.com/articles/s41598-024-55934-5 | PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC10960844/
- **Abstract:** Information-theoretic hypergraph community detection compresses observed data via community labels. Extends pairwise graph methods to higher-order interactions.
- **PAGC Relevance:** PAGC's modifier dimension creates hyperedges across bases — a single modifier connects multiple bases simultaneously. Hypergraph community detection is the correct tool for analyzing PAGC's combinatorial structure.

## [3] A Comprehensive Review of Community Detection in Graphs
- **Authors:** Multiple
- **Venue:** Neurocomputing / arXiv
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2309.11798
- **Abstract:** Reviews modularity-based, spectral, probabilistic, and deep learning methods for community detection. Identifies open problems in scalability and ground-truth validation.
- **PAGC Relevance:** Survey of state-of-the-art for analyzing the community structure that PAGC's 216-node token graph would exhibit. Methods here provide the experimental toolkit for empirically mapping PAGC.

## [4] Community Detection in Large-Scale Complex Networks via Structural Entropy Game
- **Authors:** Multiple
- **Venue:** WWW 2025
- **Year:** 2025
- **URL:** https://penghao-bdsc.github.io/papers/WWW25.pdf
- **Abstract:** Game-theoretic formulation of community detection using structural entropy. Players optimize local entropy reduction, producing globally coherent community structure.
- **PAGC Relevance:** PAGC's lexical cache represents a game-theoretic equilibrium — high-frequency moral/equity terms are fixed points of entropy minimization games played by language users over generations.

## [5] Defining Complex Adaptive Systems: An Algorithmic Approach
- **Authors:** Multiple
- **Venue:** Systems (MDPI)
- **Year:** 2024
- **URL:** https://www.mdpi.com/2079-8954/12/2/45
- **Abstract:** Proposes algorithmic framework for defining CAS. Two-stage evaluation of complexity attributes (autonomy, memory, self-organization, emergence) before adaptivity attributes.
- **PAGC Relevance:** PAGC as a linguistic system exhibits all CAS properties — it is autonomous (self-organizing from use patterns), has memory (lexical cache), self-organizes (redundancy emerges from use), and is emergent (surface variants from deep structure).

## [6] Self-Organizing Systems: What, How, and Why?
- **Authors:** Multiple
- **Venue:** npj Complexity (Nature)
- **Year:** 2025
- **URL:** https://www.nature.com/articles/s44260-025-00031-5
- **Abstract:** Characterizes self-organization as production of global patterns without centralized control. Reviews mechanisms: local interactions, feedback, symmetry breaking.
- **PAGC Relevance:** PAGC's 27×8 structure may have self-organized from Igbo phonological space over time — the matrix is a symmetry-broken attractor of the acoustic/semantic space of the language.

## [7] Large Language Models and Emergence: A Complex Systems Perspective
- **Authors:** Multiple
- **Venue:** arXiv
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2506.11135
- **Abstract:** Analyzes emergent capabilities in LLMs through the lens of complex systems theory. Shows that phase transitions in capability emerge at critical scale thresholds.
- **PAGC Relevance:** If PAGC is a generative engine, emergent capabilities should appear at critical vocabulary thresholds — not at 100 or 1000 tokens, but at specific combinatorial completeness points. The 216-token threshold may be such a critical point.
