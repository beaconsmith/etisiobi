---
title: "MorphTok: Morphologically Grounded Tokenization for Indian Languages"
authors: [Maharaj Brahma, N J Karthika, Atul Singh, Devaraj Adiga, Smruti Bhate, Ganesh Ramakrishnan, Rohit Saluja, Maunendra Sankar Desarkar]
published: 2025-04-14
source_url: http://arxiv.org/abs/2504.10335v2
tags: [raw_source, arxiv]
processing_status: unread
---

# MorphTok: Morphologically Grounded Tokenization for Indian Languages

**Authors:** Maharaj Brahma, N J Karthika, Atul Singh, Devaraj Adiga, Smruti Bhate, Ganesh Ramakrishnan, Rohit Saluja, Maunendra Sankar Desarkar
**Published:** 2025-04-14
**Source:** [ArXiv Link](http://arxiv.org/abs/2504.10335v2)

## Abstract

Tokenization is a crucial step in NLP, especially with the rise of large language models (LLMs), impacting downstream performance, computational cost, and efficiency. Existing LLMs rely on the classical Byte-pair Encoding (BPE) algorithm for subword tokenization that greedily merges frequent character bigrams, often leading to segmentation that does not align with linguistically meaningful units. To address this, we propose morphology-aware segmentation as a pre-tokenization step before applying BPE. To facilitate morphology-aware segmentation, we create a novel dataset for Hindi and Marathi, incorporating sandhi splitting to enhance the subword tokenization. Experiments on downstream tasks show that morphologically grounded tokenization improves machine translation and language modeling performance. Additionally, to handle the dependent vowels common in syllable-based writing systems used by Indic languages, we propose Constrained BPE (CBPE), an extension to the standard BPE algorithm incorporating script-specific constraints. In particular, CBPE handles dependent vowels to form a cohesive unit with other characters instead of occurring as a single unit. Our results show that CBPE achieves a 1.68\% reduction in fertility scores while maintaining comparable or improved downstream performance in machine translation and language modeling, offering a computationally efficient alternative to standard BPE. Moreover, to evaluate segmentation across different tokenization algorithms, we introduce a new human evaluation metric, \textit{EvalTok}, enabling more human-grounded assessment.

## Extracted Concepts (Auto-Generated)
> [!info] 
> This is a raw source file. An autonomous agent should read this abstract and extract specific `[[concepts]]`, methodologies, and falsification tests related to the Principle of Ancestral Generative Compression (PAGC).

