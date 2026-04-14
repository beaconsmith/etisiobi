def is_valid_source(year, citation_count, is_eric_weinstein=False):
    """
    Validates if a source meets the criteria:
    - Past 15 years (>= 2011)
    - If older than 15 years, MUST be before 1990 AND high impact (citation_count > 500)
    """
    if is_eric_weinstein:
        return True # Weinstein requests might be older
        
    if year is None:
        return False
        
    try:
        y = int(year)
    except:
        return False
        
    if y >= 2011:
        return True
    elif y <= 1990 and citation_count > 500:
        return True
    
    return False

def get_pagc_mapping(category):
    """
    Returns a generative mapping for the specific category.
    """
    mappings = {
        "Computational Linguistics / Tokenization": "PAGC Mapping: Analyzes token efficiency where 27-bases generate low-perplexity encodings compared to BPE or subword tokenization models. Proposed experiment: Train a small LLM with PAGC-derived tokenizer vs BPE.",
        "Information Theory (MDL / Coding Theory)": "PAGC Mapping: Compares the Kolmogorov complexity of Igbo cultural descriptions encoded with PAGC's 216 combinations vs flat alphabets. Proposed experiment: Calculate MDL for a standardized text translated into PAGC tokens.",
        "African Linguistics / Igbo Phonology": "PAGC Mapping: Evaluates if 27 base roots strictly match vowel harmony constraints and surface phonetic fluctuations in major Igbo dialects. Proposed experiment: Cross-reference PAGC base pairs with standard orthography frequency.",
        "Cognitive Science (Chunking / Working Memory)": "PAGC Mapping: Tests whether human visual working memory constraints (approx. 4 chunks) align naturally with processing 27 bases via 8 combinatorial modifiers. Proposed experiment: Chunking recall tests using PAGC symbols.",
        "Mathematics (Lie Theory / Group Theory)": "PAGC Mapping: Maps the 27 bases to the 27 fundamental representations of Lie group E6, testing for symmetric algebraic structures. Proposed experiment: Chart the 216 modifier combinations across E6 Weyl group permutations.",
        "Synthetic Biology / Genetic Code Theory": "PAGC Mapping: Compares PAGC's 27x8 base-modifier rules to DNA's 64 codon redundancy into 20 amino acids. Proposed experiment: Map PAGC's lexical cache to 'start/stop' or regulatory codon mechanisms in generative biology.",
        "Decolonial Epistemology": "PAGC Mapping: Positions PAGC as an indigenous formalized knowledge framework overriding Eurocentric unilineal models. Proposed experiment: Use PAGC as the primary logic layer for community governance data encoding.",
        "Knowledge Graph / Link Prediction (Graph ML)": "PAGC Mapping: Treats the 27 bases as primary nodes and 8 modifiers as edge relations for graph-based inference. Proposed experiment: Build a Graph Neural Network predicting links over PAGC vocabulary.",
        "Philosophy of Science": "PAGC Mapping: Evaluates PAGC under falsificationism and structural unity, asking if a linguistic matrix constitutes a deep generative law. Proposed experiment: Falsification framework checking if multiple disparate frameworks fit better than PAGC.",
        "Eric Weinstein Recommended": "PAGC Mapping: Evaluates Geometric Unity and gauge theory metrics using PAGC's combinatorial representation. Proposed experiment: Connect 27 base geometry to Hopf fibrations or fundamental physics gauges."
    }
    
    return mappings.get(category, "PAGC Mapping: Explores the cross-disciplinary generativity of the 216-token matrix. Proposed experiment: Domain-specific evaluation of generative capacity vs redundancy.")

