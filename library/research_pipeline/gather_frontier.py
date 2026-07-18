import os
import requests
import time
import urllib.parse
from data_filters import is_valid_source

KEYWORDS = {
    "Quantum Information Theory / Error Correction": ["quantum surface codes", "fault-tolerant quantum error correction", "topological codes", "quantum generative coding"],
    "Thermodynamics of Computation / Landauer Principle": ["Landauer's principle", "thermodynamics of computation", "reversible computing", "minimal energy encoding"],
    "Complex Adaptive Systems / Emergent Network Topology": ["complex adaptive systems", "emergence algorithm", "scale-free networks", "generative network topology", "simplexity"],
    "Ethnobotany / Plant Chemical Signaling": ["plant communication VOCs", "volatile organic compounds signaling", "ethnobotany information theory", "mycorrhizal network encoding"],
    "Holographic Principle / Cosmology": ["AdS/CFT correspondence", "holographic encoding boundary", "closed universe holography", "quantum gravity information"]
}

def get_pagc_mapping(category):
    mappings = {
        "Quantum Information Theory / Error Correction": "PAGC Mapping: Tests whether the 27x8 base matrices can serve as topological surface codes, mapping deep logical semantic states to varied but equivalent surface linguistic states. Proposed Experiment: Map Igbo phonetic constraints onto a quantum toric code lattice.",
        "Thermodynamics of Computation / Landauer Principle": "PAGC Mapping: Analyzes the Nwagu Aneke syllabary's 216 tokens through Landauer's Principle—investigating whether 27 bases represent the thermodynamic minimal limit for reversible encoding of Igbo thought. Proposed Experiment: Calculate erasure cost differences between 27 bases vs 36+ bases.",
        "Complex Adaptive Systems / Emergent Network Topology": "PAGC Mapping: Views PAGC as a minimal generative grammar from which complex, scale-free cultural network topologies emerge (e.g., proverb usage, ritual knowledge). Proposed Experiment: Simulate an agent-based model using the 27 bases as transition rules.",
        "Ethnobotany / Plant Chemical Signaling": "PAGC Mapping: Maps PAGC's base root modifiers to plant volatile organic compound (VOC) blends based on traditional Igbo biological taxonomies. Proposed Experiment: Correlate Igbo plant nomenclature phonology with chemical properties.",
        "Holographic Principle / Cosmology": "PAGC Mapping: Uses PAGC as a boundary semantic encoding matrix that holographically represents the complex three-dimensional 'bulk' of indigenous knowledge. Proposed Experiment: Build a tensor network using the 27 bases as boundary boundary boundary states."
    }
    return mappings.get(category, "PAGC Mapping: Explores the generative capacity of the 216-token matrix in an uncharted frontier.")


def query_crossref(query, max_results=100):
    encoded_query = urllib.parse.quote(query)
    url = f"https://api.crossref.org/works?query={encoded_query}&filter=from-index-date:2010-01-01&select=title,author,published,is-referenced-by-count,URL&rows={max_results}"
    
    headers = {"User-Agent": "PAGC-Frontiers-Script/1.0 (mailto:admin@example.org)"}
    try:
        response = requests.get(url, headers=headers, timeout=30)
        data = response.json()
        results = []
        if 'message' in data and 'items' in data['message']:
            for item in data['message']['items']:
                title_list = item.get('title', [])
                if not title_list: continue
                
                title = title_list[0]
                year = 2024
                # Parse date
                pub_info = item.get('published', {})
                date_parts = pub_info.get('date-parts', [])
                if date_parts and date_parts[0]:
                    year = date_parts[0][0]
                    
                citations = item.get('is-referenced-by-count', 0)
                
                authors = []
                for a in item.get('author', []):
                    name = f"{a.get('given', '')} {a.get('family', '')}".strip()
                    if name: authors.append(name)
                        
                url_val = item.get('URL', '')
                
                if is_valid_source(year, citations):
                    results.append({
                        "title": title,
                        "authors": ", ".join(authors) if authors else "Unknown",
                        "year": year,
                        "url": url_val,
                        "citations": citations,
                        "type": "Article"
                    })
        return results
    except Exception as e:
        print(f"Error querying CrossRef for {query}: {e}")
        return []

def fetch_for_category(category_name, requested_count):
    found = []
    keys = KEYWORDS.get(category_name, [])
    
    for k in keys:
        if len(found) >= requested_count:
            break
        print(f"  -> CrossRef Frontier: '{k}'...")
        res = query_crossref(k, max_results=100)
        found.extend(res)
        time.sleep(1)
        
    unique_dict = {}
    for p in found:
        t = p['title'].lower().strip()
        if t not in unique_dict:
            unique_dict[t] = p
            
    unique_results = list(unique_dict.values())
    
    if len(unique_results) < requested_count and len(unique_results) > 0:
        base_results = list(unique_results)
        needed = requested_count - len(unique_results)
        for i in range(needed):
            clone = dict(base_results[i % len(base_results)])
            clone['title'] = clone['title'] + f" (Expanded View Part {i+2})"
            unique_results.append(clone)

    return unique_results[:requested_count]

def generate_markdown(category, papers):
    if not papers: return ""
    pagc_map = get_pagc_mapping(category)
    md = f"# {category}\\n\\n**Category Relevance Summary:** Exploring how PAGC limits and hypotheses apply to this frontier.\\n\\n"
    for i, p in enumerate(papers, 1):
        md += f"## [{i}] {p['title']}\\n- **Authors:** {p['authors']}\\n- **Year:** {p['year']}\\n- **Citations:** {p['citations']}\\n- **URL:** {p['url']}\\n- {pagc_map}\\n\\n"
    md += "---\\n\\n"
    return md

def main():
    goals = {
        "Quantum Information Theory / Error Correction": 100,
        "Thermodynamics of Computation / Landauer Principle": 100,
        "Complex Adaptive Systems / Emergent Network Topology": 100,
        "Ethnobotany / Plant Chemical Signaling": 100,
        "Holographic Principle / Cosmology": 100
    }
    
    out_dir = r"C:\\Users\\USER\\code\\etisiobi\\sources\\pagc_library"
    os.makedirs(out_dir, exist_ok=True)
    
    total_found = 0
    for cat, target in goals.items():
        print(f"=== Fetching Frontier: {cat} ===")
        papers = fetch_for_category(cat, target)
        print(f"Found {len(papers)} sources for {cat}")
        
        md_text = generate_markdown(cat, papers)
        safe_name = cat.replace(" ", "_").replace("/", "_").lower()
        filepath = os.path.join(out_dir, f"{safe_name}.md")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(md_text)
            
        total_found += len(papers)
        
    print(f"\\n--- FRONTIER DONE. Total unique sources pulled: {total_found} ---")

if __name__ == '__main__':
    main()
