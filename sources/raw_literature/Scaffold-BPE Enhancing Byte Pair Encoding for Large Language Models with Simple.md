---
title: "Scaffold-BPE: Enhancing Byte Pair Encoding for Large Language Models with Simple and Effective Scaffold Token Removal"
authors: [Haoran Lian, Yizhe Xiong, Jianwei Niu, Shasha Mo, Zhenpeng Su, Zijia Lin, Hui Chen, Peng Liu, Jungong Han, Guiguang Ding]
published: 2024-04-27
source_url: http://arxiv.org/abs/2404.17808v3
tags: [raw_source, arxiv]
processing_status: unread
---

# Scaffold-BPE: Enhancing Byte Pair Encoding for Large Language Models with Simple and Effective Scaffold Token Removal

**Authors:** Haoran Lian, Yizhe Xiong, Jianwei Niu, Shasha Mo, Zhenpeng Su, Zijia Lin, Hui Chen, Peng Liu, Jungong Han, Guiguang Ding
**Published:** 2024-04-27
**Source:** [ArXiv Link](http://arxiv.org/abs/2404.17808v3)

## Abstract

Byte Pair Encoding (BPE) serves as a foundation method for text tokenization in the Natural Language Processing (NLP) field. Despite its wide adoption, the original BPE algorithm harbors an inherent flaw: it inadvertently introduces a frequency imbalance for tokens in the text corpus. Since BPE iteratively merges the most frequent token pair in the text corpus to generate a new token and keeps all generated tokens in the vocabulary, it unavoidably holds tokens that primarily act as components of a longer token and appear infrequently on their own. We term such tokens as Scaffold Tokens. Due to their infrequent occurrences in the text corpus, Scaffold Tokens pose a learning imbalance issue. To address that issue, we propose Scaffold-BPE, which incorporates a dynamic scaffold token removal mechanism by parameter-free, computation-light, and easy-to-implement modifications to the original BPE method. This novel approach ensures the exclusion of low-frequency Scaffold Tokens from the token representations for given texts, thereby mitigating the issue of frequency imbalance and facilitating model training. On extensive experiments across language modeling and even machine translation, Scaffold-BPE consistently outperforms the original BPE, well demonstrating its effectiveness.

## Extracted Concepts (Auto-Generated)
> [!info] 
> This is a raw source file. An autonomous agent should read this abstract and extract specific `[[concepts]]`, methodologies, and falsification tests related to the Principle of Ancestral Generative Compression (PAGC).

