---
title: "Boundless Byte Pair Encoding: Breaking the Pre-tokenization Barrier"
authors: [Craig W. Schmidt, Varshini Reddy, Chris Tanner, Yuval Pinter]
published: 2025-03-31
source_url: http://arxiv.org/abs/2504.00178v2
tags: [raw_source, arxiv]
processing_status: unread
---

# Boundless Byte Pair Encoding: Breaking the Pre-tokenization Barrier

**Authors:** Craig W. Schmidt, Varshini Reddy, Chris Tanner, Yuval Pinter
**Published:** 2025-03-31
**Source:** [ArXiv Link](http://arxiv.org/abs/2504.00178v2)

## Abstract

Pre-tokenization, the initial step in many modern tokenization pipelines, segments text into smaller units called pretokens, typically splitting on whitespace and punctuation. While this process encourages having full, individual words as tokens, it introduces a fundamental limitation in most tokenization algorithms such as Byte Pair Encoding (BPE). Specifically, pre-tokenization causes the distribution of tokens in a corpus to heavily skew towards common, full-length words. This skewed distribution limits the benefits of expanding to larger vocabularies, since the additional tokens appear with progressively lower counts. To overcome this barrier, we propose BoundlessBPE, a modified BPE algorithm that relaxes the pretoken boundary constraint. Our approach selectively merges two complete pretokens into a larger unit we term a superword. Superwords are not necessarily semantically cohesive. For example, the pretokens " of" and " the" might be combined to form the superword " of the". This merging strategy results in a substantially more uniform distribution of tokens across a corpus than standard BPE, and compresses text more effectively, with up to a 15% increase in bytes per token.

## Extracted Concepts (Auto-Generated)
> [!info] 
> This is a raw source file. An autonomous agent should read this abstract and extract specific `[[concepts]]`, methodologies, and falsification tests related to the Principle of Ancestral Generative Compression (PAGC).

