import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('File/docx_extracted_text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
dp_idx = -1
for i, l in enumerate(lines):
    if 'DAFTAR PUSTAKA' in l.upper():
        dp_idx = i
        break

if dp_idx != -1:
    ref_lines = lines[dp_idx:]
    print(f"Total lines from DAFTAR PUSTAKA: {len(ref_lines)}")
    
    parsed_refs = []
    curr_ref = ""
    curr_num = None
    for l in ref_lines:
        m = re.match(r'^\s*\[(\d+)\]\s*(.*)', l)
        if m:
            if curr_ref and curr_num is not None:
                parsed_refs.append((curr_num, curr_ref.strip()))
            curr_num = int(m.group(1))
            curr_ref = m.group(2)
        else:
            if curr_num is not None:
                curr_ref += " " + l.strip()
    if curr_ref and curr_num is not None:
        parsed_refs.append((curr_num, curr_ref.strip()))
        
    print(f"Parsed {len(parsed_refs)} references.")
    with open('data/extracted_literature_refs_97.txt', 'w', encoding='utf-8') as out:
        for num, r in parsed_refs:
            out.write(f"[{num:02d}] {r}\n")
            
    print("First 10 references:")
    for num, r in parsed_refs[:10]:
        print(f"[{num:02d}] {r[:100]}...")
        
    print("\nReferences mentioning ADH / hydrazide / citric / crosslink / TMR:")
    keywords = ['adh', 'hydrazide', 'hidrazida', 'citric', 'sitrat', 'tmr', 'alt023', 'formal', 'crosslink']
    for num, r in parsed_refs:
        if any(k in r.lower() for k in keywords):
            print(f"[{num:02d}] {r}")
