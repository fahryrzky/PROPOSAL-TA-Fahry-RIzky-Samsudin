import os
import re
import json
import ssl
import shutil
import urllib.request
import urllib.parse
import time

REF_DIR = "referensi"
os.makedirs(REF_DIR, exist_ok=True)

# 1. Copy local thesis if exists
if os.path.exists("1227030017_skripsi.pdf"):
    dst = os.path.join(REF_DIR, "[gilang2026skripsi] - Gilang Pratama (2026) - Instrumentasi Sensor GMR Nanofiber Fe3O4 PVA-GOx.pdf")
    if not os.path.exists(dst):
        shutil.copy("1227030017_skripsi.pdf", dst)
        print("Copied local skripsi: gilang2026skripsi")

# Load active references
with open("scripts/active_references.json", "r", encoding="utf-8") as f:
    refs = json.load(f)

ctx = ssl._create_unverified_context()
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

def clean_filename(s):
    # Remove characters invalid in Windows filenames
    s = re.sub(r'[\\/*?:"<>|]', "", s)
    s = re.sub(r'\s+', " ", s).strip()
    return s[:120]

def is_valid_pdf(filepath):
    try:
        with open(filepath, "rb") as f:
            header = f.read(5)
            return header.startswith(b"%PDF")
    except Exception:
        return False

def download_file(url, out_path):
    if not url:
        return False
    try:
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, context=ctx, timeout=25) as resp:
            data = resp.read()
            if data.startswith(b"%PDF") or b"%PDF" in data[:1024]:
                with open(out_path, "wb") as f:
                    f.write(data)
                return True
            else:
                # Some servers return html redirect or paywall
                return False
    except Exception as e:
        return False

def find_pdf_via_openalex(doi):
    if not doi:
        return None
    url = f"https://api.openalex.org/works/https://doi.org/{urllib.parse.quote(doi)}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            data = json.loads(resp.read().decode())
            # check primary location
            pl = data.get("primary_location") or {}
            if pl.get("pdf_url"):
                return pl["pdf_url"]
            # check best oa location
            boa = data.get("best_oa_location") or {}
            if boa.get("pdf_url"):
                return boa["pdf_url"]
            # check all locations
            for loc in data.get("locations", []):
                if loc.get("pdf_url"):
                    return loc["pdf_url"]
            if boa.get("landing_page_url") and "arxiv.org/abs/" in boa["landing_page_url"]:
                return boa["landing_page_url"].replace("/abs/", "/pdf/") + ".pdf"
    except Exception:
        pass
    return None

def find_pdf_via_unpaywall(doi):
    if not doi:
        return None
    url = f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi)}?email=fahry.rizky@example.com"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            data = json.loads(resp.read().decode())
            boa = data.get("best_oa_location") or {}
            if boa.get("url_for_pdf"):
                return boa["url_for_pdf"]
            for loc in data.get("oa_locations", []):
                if loc.get("url_for_pdf"):
                    return loc["url_for_pdf"]
    except Exception:
        pass
    return None

def find_pdf_via_semanticscholar(doi):
    if not doi:
        return None
    url = f"https://api.semanticscholar.org/graph/v1/paper/{urllib.parse.quote(doi)}?fields=openAccessPdf"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            data = json.loads(resp.read().decode())
            oa = data.get("openAccessPdf") or {}
            if oa.get("url"):
                return oa["url"]
    except Exception:
        pass
    return None

def find_pdf_via_arxiv(title):
    # search arxiv by title
    clean_t = re.sub(r'[^a-zA-Z0-9 ]', '', title)
    words = clean_t.split()[:8]
    q = "+AND+".join(words)
    url = f"http://export.arxiv.org/api/query?search_query=ti:{urllib.parse.quote(q)}&max_results=1"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            xml_data = resp.read().decode()
            m = re.search(r'<id>(http://arxiv.org/abs/[^<]+)</id>', xml_data)
            if m:
                abs_url = m.group(1)
                pdf_url = abs_url.replace('/abs/', '/pdf/') + ".pdf"
                return pdf_url
    except Exception:
        pass
    return None

results = []

print(f"Starting processing {len(refs)} references...\n")

for i, (key, item) in enumerate(sorted(refs.items()), 1):
    author = item.get("author") or "Unknown"
    first_author = author.split(" and ")[0].split(",")[0].strip()
    year = item.get("year") or "ND"
    title = item.get("title") or "Untitled"
    clean_t = clean_filename(title)
    filename = f"[{key}] - {first_author} ({year}) - {clean_t}.pdf"
    filepath = os.path.join(REF_DIR, filename)
    
    status = "Pending"
    download_url = ""
    source_method = ""

    # Check if file already exists and valid
    if os.path.exists(filepath) and is_valid_pdf(filepath):
        status = "Already exists"
        results.append({
            "key": key,
            "filename": filename,
            "status": "Exists (PDF)",
            "title": title,
            "doi": item.get("doi"),
            "url": item.get("url"),
            "type": item.get("type")
        })
        print(f"[{i}/{len(refs)}] EXISTS: {key}")
        continue

    # Attempt 1: Direct URL from bibtex
    raw_url = item.get("url") or ""
    if raw_url.lower().endswith(".pdf") or "arxiv.org/pdf" in raw_url.lower() or "downloads" in raw_url.lower() or "technical-documentation" in raw_url.lower():
        if download_file(raw_url, filepath):
            status = "Success"
            download_url = raw_url
            source_method = "Direct Bib URL"

    # Attempt 2: OpenAlex via DOI
    if status != "Success" and item.get("doi"):
        pdf_url = find_pdf_via_openalex(item["doi"])
        if pdf_url and download_file(pdf_url, filepath):
            status = "Success"
            download_url = pdf_url
            source_method = "OpenAlex (OA)"

    # Attempt 3: Unpaywall via DOI
    if status != "Success" and item.get("doi"):
        pdf_url = find_pdf_via_unpaywall(item["doi"])
        if pdf_url and download_file(pdf_url, filepath):
            status = "Success"
            download_url = pdf_url
            source_method = "Unpaywall (OA)"

    # Attempt 4: Semantic Scholar via DOI
    if status != "Success" and item.get("doi"):
        pdf_url = find_pdf_via_semanticscholar(item["doi"])
        if pdf_url and download_file(pdf_url, filepath):
            status = "Success"
            download_url = pdf_url
            source_method = "Semantic Scholar"

    # Attempt 5: Arxiv search by title (especially for quantum/physics papers)
    if status != "Success":
        pdf_url = find_pdf_via_arxiv(title)
        if pdf_url and download_file(pdf_url, filepath):
            status = "Success"
            download_url = pdf_url
            source_method = "arXiv Search"

    # Attempt 6: Any generic URL in bib
    if status != "Success" and raw_url and "http" in raw_url:
        if download_file(raw_url, filepath):
            status = "Success"
            download_url = raw_url
            source_method = "Generic URL"

    if status == "Success" and is_valid_pdf(filepath):
        size_kb = os.path.getsize(filepath) // 1024
        print(f"[{i}/{len(refs)}] DOWNLOADED ({size_kb} KB): {key} via {source_method}")
        results.append({
            "key": key,
            "filename": filename,
            "status": f"Downloaded ({size_kb} KB)",
            "title": title,
            "doi": item.get("doi"),
            "url": download_url or item.get("url"),
            "type": item.get("type")
        })
    else:
        # Clean up partial/corrupted file if created
        if os.path.exists(filepath):
            try: os.remove(filepath)
            except: pass
        print(f"[{i}/{len(refs)}] NOT AVAILABLE DIRECTLY: {key} ({item.get('type')})")
        results.append({
            "key": key,
            "filename": filename,
            "status": "Requires Institutional/Manual Access",
            "title": title,
            "doi": item.get("doi"),
            "url": item.get("url"),
            "type": item.get("type")
        })

    time.sleep(0.5)

with open(os.path.join(REF_DIR, "catalog.json"), "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print(f"\nDone! Processed {len(refs)} references.")
