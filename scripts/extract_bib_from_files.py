import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('File/docx_extracted_text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
print(f"Total lines in docx_extracted_text.txt: {len(lines)}")

# Find DAFTAR PUSTAKA
dp_idx = -1
for i, l in enumerate(lines):
    if 'DAFTAR PUSTAKA' in l.upper():
        dp_idx = i
        print(f"Found 'DAFTAR PUSTAKA' at line {i}: {l}")

if dp_idx != -1:
    print("\n=== DAFTAR PUSTAKA FROM DOCX ===")
    for l in lines[dp_idx:]:
        if l.strip():
            print(f"  {l}")

# Also search for references in HTML 2 (where it mentions Bagian 46 Daftar Pustaka)
html2_path = 'File/Sensor Formaldehida pada Bakso — Nanofiber Fe₃O₄ P 98dbac2c6d684334a854990d9520fe72.html'
if os.path.exists(html2_path):
    with open(html2_path, 'r', encoding='utf-8', errors='ignore') as f:
        h2 = f.read()
    
    pos = h2.find('Daftar Pustaka')
    if pos != -1:
        print("\n=== DAFTAR PUSTAKA FROM HTML 2 ===")
        snippet = h2[pos:pos+5000]
        # remove tags
        import re
        clean = re.sub(r'<[^>]+>', '\n', snippet)
        clean = '\n'.join([l.strip() for l in clean.split('\n') if l.strip()])
        print(clean[:2000])
