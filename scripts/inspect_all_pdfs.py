import os
import pypdf

ref_dir = 'referensi'
files = [f for f in os.listdir(ref_dir) if f.endswith('.pdf')]

print(f"Total PDFs to inspect: {len(files)}\n")

for fn in sorted(files):
    fpath = os.path.join(ref_dir, fn)
    size_kb = os.path.getsize(fpath) // 1024
    try:
        reader = pypdf.PdfReader(fpath)
        num_pages = len(reader.pages)
        first_page_text = reader.pages[0].extract_text() if num_pages > 0 else ''
        lines = [l.strip() for l in first_page_text.split('\n') if l.strip()]
        snippet = " | ".join(lines[:4])
        
        is_blocked = any(w in first_page_text.lower() for w in [
            'access denied', 'cloudflare', 'just a moment', 'robot or human', 
            'captcha', '403 forbidden', '404 not found', 'security check'
        ])
        
        print(f"File: {fn}")
        print(f"  Pages: {num_pages} | Size: {size_kb} KB | Blocked: {is_blocked}")
        print(f"  Snippet: {snippet[:200]}")
        print("-" * 60)
    except Exception as e:
        print(f"File: {fn} -> ERROR: {e}\n" + "-" * 60)
