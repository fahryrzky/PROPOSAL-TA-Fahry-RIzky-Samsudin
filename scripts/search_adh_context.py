import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('File/docx_extracted_text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's search for "ADH" or "bis-hidrazida" or "asam sitrat" or "glutaraldehida"
paragraphs = text.split('\n')
print(f"Total paragraphs: {len(paragraphs)}")

matched_indices = set()
for idx, p in enumerate(paragraphs):
    if any(k in p.lower() for k in ['bis-hidrazida', 'adh', 'adipic', 'asam sitrat', 'reseptor', 'gate 2', 'arsitektur']):
        for j in range(max(0, idx - 1), min(len(paragraphs), idx + 2)):
            matched_indices.add(j)

sorted_indices = sorted(list(matched_indices))
print(f"Matched paragraphs count: {len(sorted_indices)}")

# Group consecutive indices
blocks = []
curr_block = []
for i in sorted_indices:
    if not curr_block or i == curr_block[-1] + 1:
        curr_block.append(i)
    else:
        blocks.append(curr_block)
        curr_block = [i]
if curr_block:
    blocks.append(curr_block)

print(f"Total blocks: {len(blocks)}")
for b_idx, block in enumerate(blocks[:8]):
    print(f"\n--- BLOCK {b_idx+1} (lines {block[0]}-{block[-1]}) ---")
    for line_num in block:
        print(f"[{line_num}] {paragraphs[line_num]}")
