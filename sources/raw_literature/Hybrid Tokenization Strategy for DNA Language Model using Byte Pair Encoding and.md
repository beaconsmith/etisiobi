---
title: "Hybrid Tokenization Strategy for DNA Language Model using Byte Pair Encoding and K-MER Methods"
authors: [Ganesh Sapkota, Md Hasibur Rahman]
published: 2025-07-24
source_url: http://arxiv.org/abs/2507.18570v1
tags: [raw_source, arxiv]
processing_status: unread
---

# Hybrid Tokenization Strategy for DNA Language Model using Byte Pair Encoding and K-MER Methods

**Authors:** Ganesh Sapkota, Md Hasibur Rahman
**Published:** 2025-07-24
**Source:** [ArXiv Link](http://arxiv.org/abs/2507.18570v1)

## Abstract

This paper presents a novel hybrid tokenization strategy that enhances the performance of DNA Language Models (DLMs) by combining 6-mer tokenization with Byte Pair Encoding (BPE-600). Traditional k-mer tokenization is effective at capturing local DNA sequence structures but often faces challenges, including uneven token distribution and a limited understanding of global sequence context. To address these limitations, we propose merging unique 6mer tokens with optimally selected BPE tokens generated through 600 BPE cycles. This hybrid approach ensures a balanced and context-aware vocabulary, enabling the model to capture both short and long patterns within DNA sequences simultaneously. A foundational DLM trained on this hybrid vocabulary was evaluated using next-k-mer prediction as a fine-tuning task, demonstrating significantly improved performance. The model achieved prediction accuracies of 10.78% for 3-mers, 10.1% for 4-mers, and 4.12% for 5-mers, outperforming state-of-the-art models such as NT, DNABERT2, and GROVER. These results highlight the ability of the hybrid tokenization strategy to preserve both the local sequence structure and global contextual information in DNA modeling. This work underscores the importance of advanced tokenization methods in genomic language modeling and lays a robust foundation for future applications in downstream DNA sequence analysis and biological research.

## Extracted Concepts (Auto-Generated)
> [!info] 
> This is a raw source file. An autonomous agent should read this abstract and extract specific `[[concepts]]`, methodologies, and falsification tests related to the Principle of Ancestral Generative Compression (PAGC).

