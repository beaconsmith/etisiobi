---
title: "Entropy-Driven Pre-Tokenization for Byte-Pair Encoding"
authors: [Yifan Hu, Frank Liang, Dachuan Zhao, Jonathan Geuter, Varshini Reddy, Craig W. Schmidt, Chris Tanner]
published: 2025-06-18
source_url: http://arxiv.org/abs/2506.15889v1
tags: [raw_source, arxiv]
processing_status: unread
---

# Entropy-Driven Pre-Tokenization for Byte-Pair Encoding

**Authors:** Yifan Hu, Frank Liang, Dachuan Zhao, Jonathan Geuter, Varshini Reddy, Craig W. Schmidt, Chris Tanner
**Published:** 2025-06-18
**Source:** [ArXiv Link](http://arxiv.org/abs/2506.15889v1)

## Abstract

Byte-Pair Encoding (BPE) has become a widely adopted subword tokenization method in modern language models due to its simplicity and strong empirical performance across downstream tasks. However, applying BPE to unsegmented languages such as Chinese presents significant challenges, as its frequency-driven merge operation is agnostic to linguistic boundaries. To address this, we propose two entropy-informed pre-tokenization strategies that guide BPE segmentation using unsupervised information-theoretic cues. The first approach uses pointwise mutual information and left/right entropy to identify coherent character spans, while the second leverages predictive entropy derived from a pretrained GPT-2 model to detect boundary uncertainty. We evaluate both methods on a subset of the PKU dataset and demonstrate substantial improvements in segmentation precision, recall, and F1 score compared to standard BPE. Our results suggest that entropy-guided pre-tokenization not only enhances alignment with gold-standard linguistic units but also offers a promising direction for improving tokenization quality in low-resource and multilingual settings.

## Extracted Concepts (Auto-Generated)
> [!info] 
> This is a raw source file. An autonomous agent should read this abstract and extract specific `[[concepts]]`, methodologies, and falsification tests related to the Principle of Ancestral Generative Compression (PAGC).

