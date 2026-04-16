---
title: "Theoretical Analysis of Byte-Pair Encoding"
authors: [László Kozma, Johannes Voderholzer]
published: 2024-11-13
source_url: http://arxiv.org/abs/2411.08671v1
tags: [raw_source, arxiv]
processing_status: unread
---

# Theoretical Analysis of Byte-Pair Encoding

**Authors:** László Kozma, Johannes Voderholzer
**Published:** 2024-11-13
**Source:** [ArXiv Link](http://arxiv.org/abs/2411.08671v1)

## Abstract

Byte-Pair Encoding (BPE) is a widely used method for subword tokenization, with origins in grammar-based text compression. It is employed in a variety of language processing tasks such as machine translation or large language model (LLM) pretraining, to create a token dictionary of a prescribed size. Most evaluations of BPE to date are empirical, and the reasons for its good practical performance are not well understood. In this paper we focus on the optimization problem underlying BPE: finding a pair encoding that achieves optimal compression utility. We show that this problem is APX-complete, indicating that it is unlikely to admit a polynomial-time approximation scheme. This answers, in a stronger form, a question recently raised by Zouhar et al. On the positive side, we show that BPE approximates the compression utility of the optimal pair encoding to a worst-case factor between $0.333$ and $0.625$. Our results aim to explain the ongoing success of BPE and are, to our knowledge, the first rigorous guarantees on its compression utility that hold for all inputs.

## Extracted Concepts (Auto-Generated)
> [!info] 
> This is a raw source file. An autonomous agent should read this abstract and extract specific `[[concepts]]`, methodologies, and falsification tests related to the Principle of Ancestral Generative Compression (PAGC).

