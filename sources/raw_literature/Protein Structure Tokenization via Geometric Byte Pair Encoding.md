---
title: "Protein Structure Tokenization via Geometric Byte Pair Encoding"
authors: [Michael Sun, Weize Yuan, Gang Liu, Wojciech Matusik, Marinka Zitnik]
published: 2025-11-13
source_url: http://arxiv.org/abs/2511.11758v2
tags: [raw_source, arxiv]
processing_status: unread
---

# Protein Structure Tokenization via Geometric Byte Pair Encoding

**Authors:** Michael Sun, Weize Yuan, Gang Liu, Wojciech Matusik, Marinka Zitnik
**Published:** 2025-11-13
**Source:** [ArXiv Link](http://arxiv.org/abs/2511.11758v2)

## Abstract

Protein structure is central to biological function, and enabling multimodal protein models requires joint reasoning over sequence, structure, and function. A key barrier is the lack of principled protein structure tokenizers (PSTs): existing approaches fix token size or rely on continuous vector codebooks, limiting interpretability, multi-scale control, and transfer across architectures. We introduce GeoBPE, a geometry-grounded PST that transforms continuous, noisy, multi-scale backbone conformations into discrete ``sentences'' of geometry while enforcing global constraints. Analogous to byte-pair encoding, GeoBPE generates a hierarchical vocabulary of geometric primitives by iteratively (i) clustering Geo-Pair occurrences with k-medoids to yield a resolution-controllable vocabulary; (ii) quantizing each Geo-Pair to its closest medoid prototype; and (iii) reducing drift through differentiable inverse kinematics that optimizes boundary glue angles under an $\mathrm{SE}(3)$ end-frame loss. GeoBPE offers compression ($>$10x reduction in bits-per-residue at similar distortion rate), data efficiency ($>$10x less training data), and generalization (maintains test/train distortion ratio of $1.0-1.1$). It is architecture-agnostic: (a) its hierarchical vocabulary provides a strong inductive bias for coarsening residue-level embeddings from large PLMs into motif- and protein-level representations, consistently outperforming leading PSTs across $12$ tasks and $24$ test splits; (b) paired with a transformer, GeoBPE supports unconditional backbone generation via language modeling; and (c) tokens align with CATH functional families and support expert-interpretable case studies, offering functional meaning absent in prior PSTs. Code is available at https://github.com/shiningsunnyday/PT-BPE/.

## Extracted Concepts (Auto-Generated)
> [!info] 
> This is a raw source file. An autonomous agent should read this abstract and extract specific `[[concepts]]`, methodologies, and falsification tests related to the Principle of Ancestral Generative Compression (PAGC).

