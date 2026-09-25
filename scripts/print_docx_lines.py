import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('File/docx_extracted_text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
for idx in range(80, 180):
    if idx < len(lines):
        print(f"[{idx}] {lines[idx]}")
