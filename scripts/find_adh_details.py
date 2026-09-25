import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

html_file = 'File/Sensor Formaldehida pada Bakso Nanofiber + Fe₃O₄ + 6ef17e587f8f4e95a8ad1f3e2a0cd38e.html'
with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Search for "adh" or "adipic"
matches = [m.start() for m in re.finditer(r'adipic|bis-hidrazida|asam sitrat|curing', text, re.IGNORECASE)]
print(f"Total keyword occurrences: {len(matches)}")

for idx, pos in enumerate(matches[:8]):
    start = max(0, pos - 150)
    end = min(len(text), pos + 350)
    snippet = text[start:end]
    clean = re.sub(r'<[^>]+>', ' ', snippet)
    clean = re.sub(r'\s+', ' ', clean).strip()
    print(f"\n--- Occurrence {idx+1} ---")
    print(clean)
