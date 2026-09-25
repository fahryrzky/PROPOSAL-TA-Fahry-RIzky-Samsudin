import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

html2 = 'File/Sensor Formaldehida pada Bakso Nanofiber + Fe₃O₄ + 6ef17e587f8f4e95a8ad1f3e2a0cd38e.html'
with open(html2, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

headings = re.findall(r'<(h[1-3])[^>]*>(.*?)</\1>', content, re.IGNORECASE | re.DOTALL)
print("--- ALL HEADINGS IN HTML 2 ---")
for idx, (tag, h_text) in enumerate(headings):
    clean_h = re.sub(r'<[^>]+>', ' ', h_text).strip()
    clean_h = re.sub(r'\s+', ' ', clean_h)
    print(f"[{idx+1}] {tag.upper()}: {clean_h}")
