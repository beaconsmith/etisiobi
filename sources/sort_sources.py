"""
sort_sources.py
Sorts randomly downloaded PDFs from general/ into structured discipline folders
based on the download_manifest.jsonl
"""

import os
import json
import glob
import shutil
import re
from pathlib import Path

def sanitize_filename(text: str) -> str:
    """Same sanitization used during download."""
    safe = text.replace(" ", "_").replace("/", "_").replace(":", "")
    safe = "".join(c for c in safe if c.isalnum() or c in "_-")
    return safe

def main():
    base_dir = Path(__file__).parent
    manifest_path = base_dir / "download_manifest.jsonl"
    papers_dir = base_dir / "papers"
    
    if not manifest_path.exists():
        print(f"Manifest not found at {manifest_path}")
        return

    # 1. Load Manifest
    expected = {}
    total_manifest_count = 0
    with open(manifest_path, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip(): continue
            try:
                data = json.loads(line)
                title = data.get("title")
                if title:
                    safe_title = sanitize_filename(title)
                    expected[safe_title] = data
                    total_manifest_count += 1
            except Exception as e:
                pass
    
    print(f"Loaded {total_manifest_count} entries from manifest.")

    # 2. Find all PDFs in papers_dir
    all_pdfs = list(papers_dir.rglob("*.pdf"))
    print(f"Found {len(all_pdfs)} total PDFs on disk.")

    # 3. Match and Move
    moved_count = 0
    matched_manifest_safe_titles = set()
    unmatched_pdfs = []

    for pdf_path in all_pdfs:
        filename = pdf_path.name
        # Remove .pdf extension for matching
        stem = pdf_path.stem
        
        # Exact match check
        if stem in expected:
            matched_manifest_safe_titles.add(stem)
            target_discipline = expected[stem].get('discipline', 'general')
            
            # Create target folder if it doesn't exist
            target_folder = papers_dir / target_discipline
            target_folder.mkdir(parents=True, exist_ok=True)
            
            target_file = target_folder / filename
            
            # If it's already in the right place, skip
            if pdf_path != target_file:
                shutil.move(str(pdf_path), str(target_file))
                moved_count += 1
        else:
            # Fuzzy match or unknown
            # For this script we will just leave unmatched ones alone for now
            unmatched_pdfs.append(pdf_path)
            
    print(f"Moved {moved_count} files into their correct discipline folders.")
    
    if unmatched_pdfs:
        print(f"Found {len(unmatched_pdfs)} PDFs that could not be matched to the manifest.")
        print("Example unmatched:")
        for p in unmatched_pdfs[:5]:
            print(f"  {p.name}")

    # 4. Generate Missing Report Data
    missing_items = []
    for safe_title, data in expected.items():
        if safe_title not in matched_manifest_safe_titles:
            missing_items.append(data)

    print(f"Missing items from manifest: {len(missing_items)}")
    
    report_path = base_dir / "missing_report_metadata.json"
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(missing_items, f, indent=2)
        
    print(f"Missing items data saved to {report_path}")

    # Optional structure cleanup
    general_dir = papers_dir / "general"
    if general_dir.exists() and not list(general_dir.iterdir()):
        general_dir.rmdir()
        print("Removed empty 'general' directory.")

if __name__ == "__main__":
    main()
