---
title: "Language Model Tokenizers Introduce Unfairness Between Languages"
authors: [Aleksandar Petrov, Emanuele La Malfa, Philip H. S. Torr, Adel Bibi]
published: 2023-05-17
source_url: http://arxiv.org/abs/2305.15425v2
tags: [raw_source, arxiv]
processing_status: unread
---

# Language Model Tokenizers Introduce Unfairness Between Languages

**Authors:** Aleksandar Petrov, Emanuele La Malfa, Philip H. S. Torr, Adel Bibi
**Published:** 2023-05-17
**Source:** [ArXiv Link](http://arxiv.org/abs/2305.15425v2)

## Abstract

Recent language models have shown impressive multilingual performance, even when not explicitly trained for it. Despite this, there are concerns about the quality of their outputs across different languages. In this paper, we show how disparity in the treatment of different languages arises at the tokenization stage, well before a model is even invoked. The same text translated into different languages can have drastically different tokenization lengths, with differences up to 15 times in some cases. These disparities persist even for tokenizers that are intentionally trained for multilingual support. Character-level and byte-level models also exhibit over 4 times the difference in the encoding length for some language pairs. This induces unfair treatment for some language communities in regard to the cost of accessing commercial language services, the processing time and latency, as well as the amount of content that can be provided as context to the models. Therefore, we make the case that we should train future language models using multilingually fair subword tokenizers.

## Extracted Concepts (Auto-Generated)
> [!info] 
> This is a raw source file. An autonomous agent should read this abstract and extract specific `[[concepts]]`, methodologies, and falsification tests related to the Principle of Ancestral Generative Compression (PAGC).

