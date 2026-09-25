#!/usr/bin/env python3
"""
Extract all references from literature review PDFs and HTML files in the File folder.
"""
import os, sys, re, json

try:
    import fitz  # PyMuPDF
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'PyMuPDF', '-q'])
    import fitz

FILE_DIR = r"c:\Users\Fahry Rizky S\Documents\Tugas Akhir Fahry\Proposal\File"

def extract_pdf_text(path, max_pages=None):
    doc = fitz.open(path)
    texts = []
    for i, page in enumerate(doc):
        if max_pages and i >= max_pages:
            break
        texts.append(page.get_text())
    return "\n".join(texts)

def extract_html_text(path):
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        html = f.read()
    # Strip tags
    text = re.sub(r'<[^>]+>', ' ', html)
    text = re.sub(r'\s+', ' ', text)
    return text

# Extract from all files
all_text = ""
for fname in os.listdir(FILE_DIR):
    fpath = os.path.join(FILE_DIR, fname)
    if fname.endswith('.pdf'):
        print(f"Extracting: {fname}")
        try:
            text = extract_pdf_text(fpath)
            all_text += f"\n\n=== {fname} ===\n{text}"
        except Exception as e:
            print(f"  Error: {e}")
    elif fname.endswith('.html'):
        print(f"Extracting: {fname}")
        try:
            text = extract_html_text(fpath)
            all_text += f"\n\n=== {fname} ===\n{text}"
        except Exception as e:
            print(f"  Error: {e}")
    elif fname.endswith('.txt'):
        print(f"Extracting: {fname}")
        try:
            with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
                text = f.read()
            all_text += f"\n\n=== {fname} ===\n{text}"
        except Exception as e:
            print(f"  Error: {e}")

# Extract DOIs
dois = set(re.findall(r'10\.\d{4,}/[^\s,;"\'\]\)>}]+', all_text))
print(f"\n\nFound {len(dois)} unique DOIs:")
for d in sorted(dois):
    # Clean trailing periods or parentheses
    d = d.rstrip('.')
    print(f"  {d}")

# Extract reference patterns (Author, Year)
# Look for patterns like "Author et al. (2020)" or "(Author, 2020)"
author_year = set(re.findall(r'([A-Z][a-z]+(?:\s+(?:et\s+al\.?|and\s+[A-Z][a-z]+))?)\s*[\(,]\s*((?:19|20)\d{2})\s*\)', all_text))
print(f"\nFound {len(author_year)} Author-Year references:")
for author, year in sorted(author_year, key=lambda x: (x[1], x[0])):
    print(f"  {author} ({year})")

# Extract full reference lines (look for numbered refs [1], [2], etc.)
numbered_refs = re.findall(r'\[(\d+)\]\s*([^\[]{30,300})', all_text)
print(f"\nFound {len(numbered_refs)} numbered references:")
for num, ref in numbered_refs[:100]:
    print(f"  [{num}] {ref.strip()[:150]}")

# Save full extracted text for analysis
output_path = os.path.join(FILE_DIR, "all_extracted_references.txt")
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(all_text)
print(f"\nFull extracted text saved to: {output_path}")
print(f"Total text length: {len(all_text)} chars")
