import os
import sys
import zipfile
import re

sys.stdout.reconfigure(encoding='utf-8')

print("=== 1. CHECKING ZIP FILES IN 'File' ===")
for zf_name in ['drive-download-20260924T030457Z-1-001.zip', 'GMR-UIN-R1B-20260924T060535Z-1-001.zip']:
    zpath = os.path.join('File', zf_name)
    if os.path.exists(zpath):
        print(f"\nContents of {zf_name}:")
        with zipfile.ZipFile(zpath, 'r') as z:
            for info in z.infolist():
                print(f"  {info.filename} ({info.file_size/1024:.1f} KB)")

print("\n=== 2. CHECKING GMR-UIN-R1B FOLDER ===")
gmr_dir = os.path.join('File', 'GMR-UIN-R1B')
if os.path.exists(gmr_dir):
    for root, dirs, files in os.walk(gmr_dir):
        for f in files:
            print(f"  {os.path.join(root, f)}")

print("\n=== 3. SEARCHING HTML FILES FOR ADH, ASAM SITRAT, CROSSLINKER, RESEPTOR ===")
html_files = [
    'Sensor Formaldehida pada Bakso Nanofiber + Fe₃O₄ + 6ef17e587f8f4e95a8ad1f3e2a0cd38e.html',
    'Sensor Formaldehida pada Bakso — Nanofiber Fe₃O₄ P 98dbac2c6d684334a854990d9520fe72.html'
]

for hf in html_files:
    hpath = os.path.join('File', hf)
    if os.path.exists(hpath):
        print(f"\n--- Reading {hf[:40]}... ---")
        with open(hpath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Search snippets with ADH, citric, crosslink, receptor
        lines = re.split(r'[\r\n]+|<p>|<div>|<li>', content)
        matches = []
        for line in lines:
            line_clean = re.sub(r'<[^>]+>', ' ', line).strip()
            if any(k in line_clean.lower() for k in ['adh', 'crosslink', 'reseptor', 'asam sitrat', 'citric']):
                if len(line_clean) > 20 and len(line_clean) < 300:
                    matches.append(line_clean)
        
        print(f"Found {len(matches)} matching snippets. Showing first 10:")
        for m in matches[:10]:
            print(f" > {m}")
