# Thermodynamics of Computation — Reports & Reviews

## [1] Landauer's Principle: Past, Present and Future
- **Authors:** Multiple
- **Venue:** Entropy (MDPI)
- **Year:** 2025
- **URL:** https://www.mdpi.com/1099-4300/27/4/437 | PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC12026021/
- **Abstract:** Comprehensive review of Landauer's principle across 60 years. Covers experimental verifications, quantum extensions, and generalizations to many-valued logic. Bridges information erasure, entropy, and energy cost of computation.
- **PAGC Relevance:** PAGC's deliberate redundancy has a thermodynamic cost — encoding the same semantic content in multiple surface variants requires more bits and more energy to erase. This review frames the thermodynamic tradeoff of PAGC's design choices.

## [2] Experimentally Probing Landauer's Principle in the Quantum Many-Body Regime
- **Authors:** Multiple
- **Venue:** Nature Physics
- **Year:** 2025
- **URL:** https://www.nature.com/articles/s41567-025-02930-9
- **Abstract:** First experimental test of Landauer's principle in a quantum many-body system using ultracold Bose gas quantum field simulator. Confirms that irreversibility in quantum many-body processes has a lower-bounded thermodynamic cost.
- **PAGC Relevance:** PAGC's lexical cache represents logically irreversible compression — cached high-frequency terms are fixed (cannot be erased without semantic cost). This paper grounds the irreversibility of PAGC's cache in thermodynamic first principles.

## [3] Landauer Bound in the Context of Minimal Physical Principles: Meaning, Experimental Verification, Controversies and Perspectives
- **Authors:** Multiple
- **Venue:** PMC
- **Year:** 2024
- **URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC11119825/
- **Abstract:** Reviews the Landauer bound from first principles, addressing controversies about whether it is a thermodynamic law or a consequence of statistical mechanics. Covers experimental verifications and outstanding theoretical questions.
- **PAGC Relevance:** PAGC's minimum token set (216) defines a Landauer-like lower bound for Igbo semantic representation — below this threshold, semantic information is irreversibly lost. The bound is both informational and thermodynamic.

## [4] Generalization of the Landauer Principle for Computing Devices Based on Many-Valued Logic
- **Authors:** Bormashenko
- **Venue:** PMC
- **Year:** 2020
- **URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC7514495/
- **Abstract:** Extends Landauer's principle from binary to many-valued logic. Shows that the minimum energy cost of erasing one trit (base-3 unit) is kT·ln(3). Generalizes to arbitrary base-n logic.
- **PAGC Relevance:** PAGC uses base-27 logic (27 bases) with 8-valued modifiers. The generalized Landauer bound for PAGC's 216-valued logic is kT·ln(216) — a specific, calculable thermodynamic cost that defines PAGC's physical lower bound.

## [5] Landauer Principle and Thermodynamics of Computation
- **Authors:** Multiple
- **Venue:** arXiv / ResearchGate
- **Year:** 2025
- **URL:** https://arxiv.org/pdf/2506.10876 | https://www.researchgate.net/publication/391610287_Landauer_principle_and_thermodynamics_of_computation
- **Abstract:** Current state-of-the-art review on thermodynamics of computation, covering Szilard engines, Maxwell's Demon, reversible computation, and quantum thermodynamic circuits.
- **PAGC Relevance:** Maxwell's Demon selects from a finite set of states — the Demon's memory is PAGC's lexical cache. The entropy cost of the Demon's cache reset = the thermodynamic cost of updating PAGC's high-frequency token list.

## [6] Notes on Landauer's Principle, Reversible Computation, and Maxwell's Demon (Bennett)
- **Authors:** Charles Bennett
- **Venue:** Studies in History and Philosophy of Modern Physics
- **Year:** 2003 (foundational)
- **URL:** https://www.cs.princeton.edu/courses/archive/fall06/cos576/papers/bennett03.pdf
- **Abstract:** Classic paper establishing that logically reversible computation has no fundamental thermodynamic cost; only logical irreversibility (erasure) requires energy. Founds thermodynamics of computation as a field.
- **PAGC Relevance:** PAGC's redundancy enables reversible semantic computation — the original message can be recovered from any redundant encoding. Bennett's framework predicts this reversibility is thermodynamically free; only cache updates cost energy.
