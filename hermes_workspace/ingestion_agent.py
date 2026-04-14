import os
import re
import xml.etree.ElementTree as ET
import urllib.request
import urllib.parse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

# ── Configuration ──────────────────────────────────────────────
VAULT_ROOT = Path(r"C:\Users\USER\code\etisiobi")
RAW_SOURCES_DIR = VAULT_ROOT / "sources" / "raw_literature"
RAW_SOURCES_DIR.mkdir(parents=True, exist_ok=True)

ARXIV_QUERIES = [
    # AI & Compute (Tokenization, Compression)
    "tokenization embedding byte pair encoding",
    "kolmogorov complexity neural networks",
    "algorithmic information theory compressibility",
    "minimum description length neural networks",
    "lossless compression generative models",
    "subword tokenization language models",
    
    # Physics & Thermodynamics
    "landauer principle thermodynamics of computation",
    "holographic principle information encoding",
    "Maxwell's demon reversible computing",
    "entropy creation algorithmic complexity",
    "cellular automata universal computation",
    
    # Quantum Information
    "quantum autoencoder generator",
    "quantum error correction topological space",
    "tensor networks quantum many body",
    "sycamore processor error mitigation",
    
    # Networks & Topology
    "scale-free networks generative models",
    "topological data analysis complex systems",
    "stochastic block models generative",
    "small-world networks resilience",
    "network topology emergent behavior",
    "graph neural networks message passing",
    
    # Linguistics & Cognitive Science
    "universal grammar computational linguistics",
    "working memory chunking cognitive architecture",
    "linguistic relativity cognitive processing",
    "structural linguistics embedding spaces",
    "fodor language of thought",
    
    # Synthetic Biology & Systems
    "synthetic biology logic gates gene regulatory networks",
    "bioinformatics genetic sequence compression",
    "reaction networks autocatalytic sets",
    "morphogenesis turing patterns",
    
    # Mathematical Frameworks
    "category theory deep learning",
    "homotopy type theory computation",
    "combinatorial generation algorithms",
    "lie algebras invariant theory neural",
    
    # Decolonial Epistemology & Indigenous Tech
    "indigenous knowledge systems computation",
    "ethnomathematics fractals",
    "oral traditions information transmission",
    "traditional ecological knowledge adaptive cycles"
]

SPECIFIC_THEORIES = [
    "Nwagu Aneke syllabary",
    "Chomsky Syntactic Structures",
    "Rota mathematical clearing compression",
    "Shannon information entropy",
    "Wolfram A New Kind of Science",
    "Hopfield networks associative memory",
    "Friston free energy principle"
]

def clean_text(text: str) -> str:
    """Removes weird newlines from arXiv XML text."""
    if not text: return ""
    return " ".join(text.split())

def fetch_arxiv(query: str, max_results: int = 35):
    """Hits the ArXiv API and returns a list of dictionaries with paper metadata."""
    print(f"[*] Searching arXiv for: {query}")
    safe_query = urllib.parse.quote(query)
    url = f"http://export.arxiv.org/api/query?search_query=all:{safe_query}&max_results={max_results}&sortBy=relevance"
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            xml_data = response.read()
            
        root = ET.fromstring(xml_data)
        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        
        papers = []
        for entry in root.findall('atom:entry', ns):
            title = entry.find('atom:title', ns).text
            summary = entry.find('atom:summary', ns).text
            published = entry.find('atom:published', ns).text
            link = entry.find('atom:id', ns).text
            
            authors = [a.find('atom:name', ns).text for a in entry.findall('atom:author', ns)]
            
            papers.append({
                "title": clean_text(title),
                "summary": clean_text(summary),
                "published": published[:10], # YYYY-MM-DD
                "link": link,
                "authors": authors
            })
        return papers
    except Exception as e:
        print(f"[!] Error fetching {query}: {e}")
        return []

def save_to_markdown(paper: dict):
    """Formats the paper metadata as a clean Obsidian-style Markdown file and saves it."""
    # Create a clean filename from the title
    safe_title = re.sub(r'[^\w\s-]', '', paper['title'])[:80].strip()
    filename = RAW_SOURCES_DIR / f"{safe_title}.md"
    
    # Avoid overwriting
    if filename.exists():
        return False
        
    authors_str = ", ".join(paper['authors'])
    
    # Markdown with YAML frontmatter (Karpathy LLM Wiki style)
    md_content = f"""---
title: "{paper['title']}"
authors: [{authors_str}]
published: {paper['published']}
source_url: {paper['link']}
tags: [raw_source, arxiv]
processing_status: unread
---

# {paper['title']}

**Authors:** {authors_str}
**Published:** {paper['published']}
**Source:** [ArXiv Link]({paper['link']})

## Abstract

{paper['summary']}

## Extracted Concepts (Auto-Generated)
> [!info] 
> This is a raw source file. An autonomous agent should read this abstract and extract specific `[[concepts]]`, methodologies, and falsification tests related to the Principle of Ancestral Generative Compression (PAGC).

"""
    filename.write_text(md_content, encoding="utf-8")
    return True

def run_ingestion():
    all_papers = []
    
    # 1. Fetch papers based on thematic queries
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = executor.map(fetch_arxiv, ARXIV_QUERIES)
        for res in results:
            all_papers.extend(res)
            
    # 2. Add specific theoretical queries
    for theory in SPECIFIC_THEORIES:
        all_papers.extend(fetch_arxiv(theory, max_results=5))
        
    print(f"\n[*] Target total papers to process: {len(all_papers)}")
    
    # 3. Save to disk
    saved_count = 0
    for paper in all_papers:
        if save_to_markdown(paper):
            saved_count += 1
            
    print(f"\n[*] Ingestion Complete! Added {saved_count} new raw academic sources to:")
    print(f"      {RAW_SOURCES_DIR}")

if __name__ == "__main__":
    print("==================================================")
    print("   WikiOS — Scientific Source Ingestion Agent     ")
    print("==================================================")
    run_ingestion()
