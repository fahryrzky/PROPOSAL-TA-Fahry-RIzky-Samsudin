import json
import os

with open('scripts/active_references.json', 'r', encoding='utf-8') as f:
    refs = json.load(f)

downloaded = [f for f in os.listdir('referensi') if f.endswith('.pdf')]

print(f"Total active references: {len(refs)}")
print(f"Currently downloaded PDFs: {len(downloaded)}")

missing = []
for k, v in refs.items():
    found = any(f"[{k}]" in f for f in downloaded)
    if not found:
        missing.append((k, v))

print(f"\nMissing references: {len(missing)}")
for k, v in missing:
    doi = v.get("doi", "")
    url = v.get("url", "")
    print(f"- [{k}] ({v.get('year')}): {v.get('title')[:60]} | DOI: {doi} | URL: {url[:40]}")
