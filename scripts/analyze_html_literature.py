import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

html1 = 'File/Sensor Formaldehida pada Bakso — Nanofiber Fe₃O₄ P 98dbac2c6d684334a854990d9520fe72.html'
html2 = 'File/Sensor Formaldehida pada Bakso Nanofiber + Fe₃O₄ + 6ef17e587f8f4e95a8ad1f3e2a0cd38e.html'

def analyze_html(path, name):
    print(f"\n=======================================================")
    print(f"ANALYZING: {name}")
    print(f"Path: {path}")
    print(f"=======================================================")
    if not os.path.exists(path):
        print("File not found.")
        return
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    title_m = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
    title = title_m.group(1).strip() if title_m else "No Title"
    print(f"TITLE: {title}\n")
    
    headings = re.findall(r'<(h[1-3])[^>]*>(.*?)</\1>', content, re.IGNORECASE | re.DOTALL)
    print(f"Total Headings: {len(headings)}")
    print("--- Headings List ---")
    for tag, h_text in headings[:45]:
        clean_h = re.sub(r'<[^>]+>', ' ', h_text).strip()
        clean_h = re.sub(r'\s+', ' ', clean_h)
        print(f"  {tag.upper()}: {clean_h}")
    if len(headings) > 45:
        print(f"  ... and {len(headings) - 45} more headings.")

analyze_html(html1, "HTML 1 (P 98dbac...)")
analyze_html(html2, "HTML 2 (6ef17e...)")
