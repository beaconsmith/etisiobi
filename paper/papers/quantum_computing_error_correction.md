# Quantum Computing — Error Correction & Combinatorial Codes

## [1] Tutorial on Quantum Error Correction for 2024 QuIK Workshop
- **Authors:** Multiple contributors
- **Venue:** arXiv
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2407.12737
- **Abstract:** Comprehensive tutorial covering stabilizer codes, CSS codes, surface codes, and quantum LDPC codes. Covers combinatorial matrix representations of error syndromes.
- **PAGC Relevance:** Quantum error correction codes are defined by parity-check matrices — exactly the combinatorial matrix structure PAGC employs. The 27×8 PAGC matrix can be analyzed as a classical analog of a quantum stabilizer code matrix.

## [2] Architectures for Heterogeneous Quantum Error Correction Codes
- **Authors:** Multiple
- **Venue:** arXiv
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2411.03202
- **Abstract:** Explores architectures combining multiple QECC types. Shows that heterogeneous code composition improves logical qubit fidelity over homogeneous approaches.
- **PAGC Relevance:** PAGC's deliberate redundancy is analogous to heterogeneous code composition — different redundancy mechanisms stack to improve robustness. PAGC's surface variation tolerance = logical equivalence classes across physical encodings.

## [3] Entanglement-Assisted Quantum Error-Correcting Codes Using Matrix-Product Codes
- **Authors:** Multiple
- **Venue:** Designs, Codes and Cryptography (Springer)
- **Year:** 2025
- **URL:** https://link.springer.com/article/10.1007/s10623-025-01685-x
- **Abstract:** Non-singular quasi-orthogonal matrices as defining matrices for entanglement-assisted QECC. Shows that matrix structure directly determines code distance and error correction capability.
- **PAGC Relevance:** PAGC's 27×8 matrix structure can be evaluated through the lens of matrix-product code theory. The quasi-orthogonality of the modifier dimension relative to bases has direct implications for robustness.

## [4] Advances in Quantum Error Correction with Efficient LDPC Code Sampling
- **Authors:** Multiple
- **Venue:** Quantum Zeitgeist / Technical
- **Year:** 2024
- **URL:** https://quantumzeitgeist.com/quantum-error-correction-advances-efficient-low-density-parity/
- **Abstract:** Combinatorial approach to quantum LDPC codes overcomes algebraic construction limits. Row sparsity guided by information set decoding. Key breakthrough in scalable fault-tolerant quantum computing.
- **PAGC Relevance:** PAGC's sparse combinatorial design (27 bases, 8 modifiers vs. full combinatorial space of thousands) mirrors LDPC sparsity principles — most information is encoded by the structure of non-zeros, not the density.

## [5] Construction of Single Quantum Deletion Codes via Combinatorial Conditions and Adjacency Matrices
- **Authors:** Multiple
- **Venue:** Quantum Information Processing
- **Year:** 2021
- **URL:** https://dl.acm.org/doi/abs/10.1007/s11128-021-03242-6
- **Abstract:** Derives combinatorial conditions for quantum deletion-correcting codes using adjacency matrix representations. Establishes graph-theoretic characterization of code properties.
- **PAGC Relevance:** PAGC encodes surface variation tolerance — sequences of tokens that differ in surface form but share the same deep base×modifier encoding. This is precisely a deletion/substitution correction code at the semantic level.

## [6] A Combinatorial Approach to Quantum Error Correcting Codes
- **Authors:** Multiple
- **Venue:** arXiv
- **Year:** 2013 (foundational)
- **URL:** https://arxiv.org/abs/1304.6743
- **Abstract:** Pure combinatorial approach to QECCs focusing on matrix row sparsity. Foundational paper establishing the link between combinatorial design and quantum error correction capability.
- **PAGC Relevance:** Foundational for understanding how combinatorial matrices encode robustness. PAGC's claim that deliberate redundancy provides robustness can be formalized using the framework developed here.
