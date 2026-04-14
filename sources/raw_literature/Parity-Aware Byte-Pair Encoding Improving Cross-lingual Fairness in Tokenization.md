---
title: "Parity-Aware Byte-Pair Encoding: Improving Cross-lingual Fairness in Tokenization"
authors: [Negar Foroutan, Clara Meister, Debjit Paul, Joel Niklaus, Sina Ahmadi, Antoine Bosselut, Rico Sennrich]
published: 2025-08-06
source_url: http://arxiv.org/abs/2508.04796v2
tags: [raw_source, arxiv]
processing_status: unread
---

# Parity-Aware Byte-Pair Encoding: Improving Cross-lingual Fairness in Tokenization

**Authors:** Negar Foroutan, Clara Meister, Debjit Paul, Joel Niklaus, Sina Ahmadi, Antoine Bosselut, Rico Sennrich
**Published:** 2025-08-06
**Source:** [ArXiv Link](http://arxiv.org/abs/2508.04796v2)

## Abstract

Tokenization is the first -- and often least scrutinized -- step of most NLP pipelines. Standard algorithms for learning tokenizers rely on frequency-based objectives, which favor languages dominant in the training data and consequently leave lower-resource languages with tokenizations that are disproportionately longer, morphologically implausible, or even riddled with <UNK> placeholders. This phenomenon ultimately amplifies computational and financial inequalities between users from different language backgrounds. To remedy this, we introduce Parity-aware Byte Pair Encoding (BPE), a variant of the widely-used BPE algorithm. At every merge step, Parity-aware BPE maximizes the compression gain of the currently worst-compressed language, trading a small amount of global compression for cross-lingual parity. We find empirically that Parity-aware BPE leads to more equitable token counts across languages, with negligible impact on global compression rate and no substantial effect on language-model performance in downstream tasks.

## Extracted Concepts (Auto-Generated)
> [!info] 
> This is a raw source file. An autonomous agent should read this abstract and extract specific `[[concepts]]`, methodologies, and falsification tests related to the Principle of Ancestral Generative Compression (PAGC).

