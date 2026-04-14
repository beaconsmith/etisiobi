---
title: "Byte Pair Encoding for Symbolic Music"
authors: [Nathan Fradet, Nicolas Gutowski, Fabien Chhel, Jean-Pierre Briot]
published: 2023-01-27
source_url: http://arxiv.org/abs/2301.11975v3
tags: [raw_source, arxiv]
processing_status: unread
---

# Byte Pair Encoding for Symbolic Music

**Authors:** Nathan Fradet, Nicolas Gutowski, Fabien Chhel, Jean-Pierre Briot
**Published:** 2023-01-27
**Source:** [ArXiv Link](http://arxiv.org/abs/2301.11975v3)

## Abstract

When used with deep learning, the symbolic music modality is often coupled with language model architectures. To do so, the music needs to be tokenized, i.e. converted into a sequence of discrete tokens. This can be achieved by different approaches, as music can be composed of simultaneous tracks, of simultaneous notes with several attributes. Until now, the proposed tokenizations rely on small vocabularies of tokens describing the note attributes and time events, resulting in fairly long token sequences, and a sub-optimal use of the embedding space of language models. Recent research has put efforts on reducing the overall sequence length by merging embeddings or combining tokens. In this paper, we show that Byte Pair Encoding, a compression technique widely used for natural language, significantly decreases the sequence length while increasing the vocabulary size. By doing so, we leverage the embedding capabilities of such models with more expressive tokens, resulting in both better results and faster inference in generation and classification tasks. The source code is shared on Github, along with a companion website. Finally, BPE is directly implemented in MidiTok, allowing the reader to easily benefit from this method.

## Extracted Concepts (Auto-Generated)
> [!info] 
> This is a raw source file. An autonomous agent should read this abstract and extract specific `[[concepts]]`, methodologies, and falsification tests related to the Principle of Ancestral Generative Compression (PAGC).

