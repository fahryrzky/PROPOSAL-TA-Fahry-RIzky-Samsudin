import os
import sys
import zipfile
import xml.etree.ElementTree as ET
import re

sys.stdout.reconfigure(encoding='utf-8')

docx_path = os.path.join('File', 'Rancangan_Sensor_Formaldehida_Nanofiber_TMR.docx')
if os.path.exists(docx_path):
    print(f"Reading docx: {docx_path}")
    with zipfile.ZipFile(docx_path, 'r') as z:
        xml_content = z.read('word/document.xml').decode('utf-8')
    
    # Strip XML tags
    tree = ET.fromstring(xml_content)
    # Extract all text elements w:t
    namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    texts = []
    for node in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
        p_texts = [t.text for t in node.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if t.text]
        if p_texts:
            texts.append("".join(p_texts))
            
    full_docx_text = "\n".join(texts)
    print(f"Docx extracted lines: {len(texts)}, total characters: {len(full_docx_text)}")
    with open('File/docx_extracted_text.txt', 'w', encoding='utf-8') as f:
        f.write(full_docx_text)
        
    keywords = ['adh', 'adipic', 'asam sitrat', 'citric', 'crosslink', 'reseptor', 'receptor', 'daftar pustaka', 'pustaka']
    print("\nOccurrences in docx:")
    for kw in keywords:
        matches = [line for line in texts if kw in line.lower()]
        print(f" - '{kw}': {len(matches)} lines matched")
        for m in matches[:3]:
            print(f"    > {m[:140]}...")

# Also search html files completely
html_files = [f for f in os.listdir('File') if f.endswith('.html')]
for hf in html_files:
    hpath = os.path.join('File', hf)
    print(f"\n--- Checking HTML: {hf} ---")
    with open(hpath, 'r', encoding='utf-8', errors='ignore') as f:
        txt = f.read()
    
    # remove html tags
    clean_txt = re.sub(r'<[^>]+>', ' ', txt)
    clean_txt = re.sub(r'\s+', ' ', clean_txt)
    print(f"Length: {len(clean_txt)} chars")
    
    # Check for citations / daftar pustaka
    for kw in ['daftar pustaka', 'referensi', 'references', 'adh', 'adipic', 'asam sitrat', 'reseptor', 'crosslink']:
        pos = [m.start() for m in re.finditer(kw, clean_txt, re.IGNORECASE)]
        print(f" - '{kw}': {len(pos)} matches")
        if pos:
            first_pos = pos[0]
            snippet = clean_txt[max(0, first_pos - 100):min(len(clean_txt), first_pos + 300)]
            print(f"    Snippet: ...{snippet}...\n")
