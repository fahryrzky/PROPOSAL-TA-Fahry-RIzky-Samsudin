import re
import os

with open('build_logs/skripsi.bbl', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

entries = text.split(r'\bibitem')
all_refs = []
for e in entries[1:]:
    lines = [l.strip() for l in e.strip().split('\n') if l.strip()]
    if not lines: continue
    raw = ' '.join(lines[1:])
    clean = re.sub(r'\\newblock', '', raw)
    clean = re.sub(r'\\emph\{([^}]+)\}', r'\1', clean)
    clean = re.sub(r'\\textit\{([^}]+)\}', r'\1', clean)
    clean = re.sub(r'\\textbf\{([^}]+)\}', r'\1', clean)
    clean = re.sub(r'\\url\{([^}]+)\}', r'\1', clean)
    clean = re.sub(r'\{\\em\s*([^}]+)\}', r'\1', clean)
    clean = re.sub(r'\\em\s+', '', clean)
    clean = clean.replace(r'~', ' ')
    clean = clean.replace(r'---', ' - ').replace(r'--', '-')
    clean = clean.replace(r"\'\i", 'i').replace(r"\'", '')
    clean = clean.replace(r'\v{c}', 'c').replace(r'\u{g}', 'g').replace(r'\"u', 'u')
    clean = clean.replace(r'\"o', 'o').replace(r'\"a', 'a')
    clean = re.sub(r'[{}]', '', clean)
    clean = re.sub(r'\s+', ' ', clean).strip()
    clean = clean.replace('``', '"').replace("''", '"')
    all_refs.append(clean)

all_refs.sort(key=lambda s: s.lower())
print(f"Total sorted refs: {len(all_refs)}")
os.makedirs('data', exist_ok=True)
with open('data/all_52_references.txt', 'w', encoding='utf-8') as out:
    for idx, r in enumerate(all_refs, 1):
        out.write(f"{idx:02d}. {r}\n")
        print(f"{idx:02d}. {r[:80]}...")
