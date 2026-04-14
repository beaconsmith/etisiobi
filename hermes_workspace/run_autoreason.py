import os
import time
from openai import OpenAI
import glob

# Set up parameters
API_KEY = "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"
BASE_URL = "https://integrate.api.nvidia.com/v1"

# Using a standard robust NVIDIA NIM model. Hermes 3 / Llama 3.1 70B
MODEL_NAME = "meta/llama-3.1-405b-instruct" 

client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)

def chat_complete(system_prompt, user_content):
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content}
            ],
            temperature=0.3,
            max_tokens=4000
        )
        return response.choices[0].message.content
    except Exception as e:
        # Fallback to an older 70b version if 405b is overloaded or requires special provisioning
        try:
            print(f"Error with 405b logic: {e}. Falling back to 70b.")
            response = client.chat.completions.create(
                model="meta/llama-3.1-70b-instruct",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_content}
                ],
                temperature=0.3,
                max_tokens=4000
            )
            return response.choices[0].message.content
        except Exception as e2:
            print(f"Fallback failed: {e2}")
            return "ERROR_IN_API_GENERATION"

def process_corpus():
    library_path = r"C:\\Users\\USER\\code\\etisiobi\\sources\\pagc_library\\*.md"
    files = glob.glob(library_path)
    
    print(f"Found {len(files)} source files. Building concept graph...")
    
    concept_graph_nodes = []
    
    for filepath in files:
        filename = os.path.basename(filepath)
        print(f"Processing discipline: {filename}...")
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Increased chunk limit to 50,000 characters to ensure all dense mapping, 
        # sources, and falsification conditions are digested.
        chunk = content[:50000]
        
        sys_prompt = "You are Hermes Autoreason, a research skill bot. Your job is to extract highly technical concept relationships linking the Principle of Ancestral Generative Compression (PAGC) to this discipline."
        user_prompt = f"Based on the following research bibliography and proposed mappings, extract 3 deeply novel concept pairs (nodes + edges) connecting PAGC 27x8 base matrices to this field's open problems. Format strictly as concisely as possible.\n\nCorpus:\n{chunk}"
        
        extracted_concepts = chat_complete(sys_prompt, user_prompt)
        concept_graph_nodes.append(f"\n### Discipline: {filename}\n{extracted_concepts}")
        time.sleep(1) # respectful API pacing
        
    print("Concept graphs built. Synthesizing final research paper draft...")
    
    # Compile the concept graph
    master_graph = "\n".join(concept_graph_nodes)
    
    synthesis_sys_prompt = (
        "You are Hermes, a frontier research scientist and co-author of a landmark interdisciplinary paper "
        "for Anthropic and the global scientific community. You write at the level of a Nature/Science feature "
        "combined with a rigorous technical arXiv preprint. Your audience spans theoretical physicists, "
        "computational linguists, cognitive scientists, AI alignment researchers, and synthetic biologists."
    )
    synthesis_user_prompt = f"""You have been given a multi-discipline concept graph (16 fields) derived from the 
Principle of Ancestral Generative Compression (PAGC) — a universal generative mechanism inspired by the 
Nwagu Aneke Igbo syllabary (27 base symbols × 8 modifiers = 216-token generative matrix), augmented with 
a moral/equity lexical cache and structural redundancy.

Write a full-length, publication-quality scientific paper entitled:
"The Principle of Ancestral Generative Compression (PAGC): A Universal 27-Base Framework for 
Topological Language, Error-Correcting Cognitive Networks, and Cross-Domain Generative Intelligence"

STRICT REQUIREMENTS — you MUST include ALL of the following:

1. ABSTRACT (250 words): Summarise PAGC, the 27×8 matrix, its moral lexical cache, redundancy mechanism, 
   and its cross-domain reach. State the strongest claim and key falsification condition.

2. INTRODUCTION: Motivate PAGC from first principles. Reference the Nwagu Aneke script's historical and 
   cultural significance. Connect to universal grammar, Kolmogorov complexity, holographic information 
   encoding, and the Landauer principle. State the paper's structure.

3. THEORETICAL FRAMEWORK — PAGC ARCHITECTURE:
   - Define base symbols (27), modifiers (8), and the resulting 216-token generative matrix mathematically.
   - Define the lexical cache of high-frequency moral/equity terms and its role as a structural prior.
   - Define the redundancy mechanism and its analogy to error-correcting codes.
   - Pose the core hypothesis: PAGC is a universal compression engine underlying language, cognition, 
     information, and physical law.

4. GRAPH-THEORETIC FOUNDATIONS:
   - Present the 3 concept-pair nodes extracted per discipline as formal graph edges (node A → edge → node B).
   - Cluster disciplines into thematic super-nodes: [Computation & AI], [Physics & Information], 
     [Biology & Chemistry], [Cognitive & Cultural Systems].
   - Describe the emergent topology of the full 16-discipline concept graph.

5. CROSS-DOMAIN APPLICATIONS (one subsection per discipline — do not skip any):
   For EACH of the 16 disciplines, write a structured subsection that includes:
   a) The core PAGC mapping (what do the 27 bases, 8 modifiers, and moral cache represent in this field?)
   b) At least 2 specific named experiments or computational tests
   c) The specific falsification condition (what result would disprove PAGC in this domain?)
   d) Impact tier: High / Medium / Low with justification
   e) Principia-level claim (if applicable): what would PAGC's success mean for the discipline's foundations?

6. FALSIFICATION & EMPIRICAL GAPS:
   - Compile the strongest cross-domain falsification tests into a unified table or list.
   - Identify the top 3 empirical gaps that need experimental resolution first.
   - Discuss the risk of anthropocentric bias (i.e. PAGC may be a culturally-specific artefact, not universal).

7. ETHICAL DIMENSIONS:
   - Address the risk of appropriating Igbo/indigenous knowledge systems without consent.
   - Propose a framework for ethical PAGC development with community co-authorship.

8. CONCLUSION:
   - State the strongest supported claim after cross-domain synthesis.
   - Name the single most promising experimental test to run next.
   - Identify what a 'Principia-level' breakthrough would look like if PAGC is valid.

Output in clean Markdown with section headers, sub-headers, and inline citations where possible.
Do NOT summarise or truncate. Write the full paper. Length: aim for 3,000–5,000 words minimum.

====== CONCEPT GRAPH BINDINGS (from 16-discipline Autoreason scan) ======
{master_graph}
====== END CONCEPT GRAPH ======
"""
    
    final_paper = chat_complete(synthesis_sys_prompt, synthesis_user_prompt)
    
    out_dir = r"C:\\Users\\USER\\code\\etisiobi\\paper"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "autoreason_draft_v3.md")
    
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write("# PAGC Autoreason Draft v3\n\n")
        f.write(final_paper)
        
    print(f"Done! Paper generated and saved to {out_path}.")

if __name__ == '__main__':
    process_corpus()
