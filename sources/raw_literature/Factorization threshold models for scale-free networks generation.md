---
title: "Factorization threshold models for scale-free networks generation"
authors: [Akmal Artikov, Aleksandr Dorodnykh, Yana Kashinskaya, Egor Samosvat]
published: 2015-09-15
source_url: http://arxiv.org/abs/1509.04733v3
tags: [raw_source, arxiv]
processing_status: unread
---

# Factorization threshold models for scale-free networks generation

**Authors:** Akmal Artikov, Aleksandr Dorodnykh, Yana Kashinskaya, Egor Samosvat
**Published:** 2015-09-15
**Source:** [ArXiv Link](http://arxiv.org/abs/1509.04733v3)

## Abstract

Many real networks such as the World Wide Web, financial, biological, citation and social networks have a power-law degree distribution. Networks with this feature are also called scale-free. Several models for producing scale-free networks have been obtained by now and most of them are based on the preferential attachment approach. We will offer the model with another scale-free property explanation. The main idea is to approximate the network's adjacency matrix by multiplication of the matrices $V$ and $V^T$, where $V$ is the matrix of vertices' latent features. This approach is called matrix factorization and is successfully used in the link prediction problem. To create a generative model of scale-free networks we will sample latent features $V$ from some probabilistic distribution and try to generate a network's adjacency matrix. Entries in the generated matrix are dot products of latent features which are real numbers. In order to create an adjacency matrix, we approximate entries with the Boolean domain $\{0, 1\}$. We have incorporated the threshold parameter $θ$ into the model for discretization of a dot product. Actually, we have been influenced by the geographical threshold models which were recently proven to have good results in a scale-free networks generation. The overview of our results is the following. First, we will describe our model formally. Second, we will tune the threshold $θ$ in order to generate sparse growing networks. Finally, we will show that our model produces scale-free networks with the fixed power-law exponent which equals two. In order to generate oriented networks with tunable power-law exponents and to obtain other model properties, we will offer different modifications of our model. Some of our results will be demonstrated using computer simulation.

## Extracted Concepts (Auto-Generated)
> [!info] 
> This is a raw source file. An autonomous agent should read this abstract and extract specific `[[concepts]]`, methodologies, and falsification tests related to the Principle of Ancestral Generative Compression (PAGC).

