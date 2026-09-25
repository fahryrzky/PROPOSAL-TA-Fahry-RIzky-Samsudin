import os

print("=== SEARCHING DIRECTORY FOR NOTES, LITERATURE, REFERENCES ===")
for root, dirs, files in os.walk('.'):
    # Skip .git, .gemini, etc.
    rel_root = os.path.relpath(root, '.')
    if rel_root.startswith('.'):
        continue
    for f in files:
        full_path = os.path.join(root, f)
        ext = os.path.splitext(f)[1].lower()
        if ext in ['.txt', '.md', '.tex', '.bib', '.json', '.pdf', '.docx', '.csv', '.xlsx', '.py']:
            low = f.lower()
            if any(k in low for k in ['lit', 'note', 'jurnal', 'pustaka', 'referensi', 'daftar', 'ref', 'paper', 'bbl', 'review', 'adh', 'sitrat', 'formalin', 'asam']):
                print(f"MATCH: {full_path}")

print("=== CHECKING PARENT DIRECTORY AS WELL ===")
parent = os.path.abspath('..')
print(f"Parent dir: {parent}")
for item in os.listdir(parent):
    p_path = os.path.join(parent, item)
    if os.path.isdir(p_path):
        print(f"Parent folder: {item}")
    else:
        print(f"Parent file: {item}")
