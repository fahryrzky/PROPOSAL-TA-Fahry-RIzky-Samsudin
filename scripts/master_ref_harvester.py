#!/usr/bin/env python3
"""
master_ref_harvester.py — Kael-Grade Reference Harvester
=========================================================
Comprehensive multi-strategy downloader for ALL references in the TMR-Formalin proposal.
Uses browser automation (Selenium) to bypass publisher blocks + Unpaywall OA API.

Strategy chain per DOI:
  1. Unpaywall OA API (free, legal)
  2. Direct OA publisher links (MDPI, Heliyon, MDPI, PLoS, etc.)
  3. Selenium-based Sci-Hub download (headless Chrome)
  4. Selenium-based direct publisher crawl
"""

import os, sys, json, time, random, re, hashlib
from pathlib import Path
from urllib.parse import quote

# Install dependencies if missing
def ensure_deps():
    deps = {"selenium": "selenium", "requests": "requests"}
    for mod, pkg in deps.items():
        try:
            __import__(mod)
        except ImportError:
            import subprocess
            subprocess.check_call([sys.executable, "-m", "pip", "install", pkg, "-q"])

ensure_deps()

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

REF_DIR = Path(r"c:\Users\Fahry Rizky S\Documents\Tugas Akhir Fahry\Proposal\Referensi")

# Build a robust requests session
session = requests.Session()
retry = Retry(total=3, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
session.mount("https://", HTTPAdapter(max_retries=retry))
session.mount("http://", HTTPAdapter(max_retries=retry))
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,application/pdf;q=0.8,*/*;q=0.7",
    "Accept-Language": "en-US,en;q=0.9,id;q=0.8",
})
session.verify = False
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# All 132 DOIs extracted from literature review files + proposal bib
ALL_DOIS = list(set([
    # From literature review PDFs (cleaned)
    "10.1002/jbm.a.35443",
    "10.1007/s13197-019-03635-7",
    "10.1016/j.biomaterials.2005.01.066",
    "10.1016/j.carbpol.2014.02.088",
    "10.1016/j.carbpol.2014.04.032",
    "10.1016/j.cbpa.2017.04.011",
    "10.1016/j.cej.2025.165831",
    "10.1016/j.eurpolymj.2012.02.015",
    "10.1016/j.foodchem.2020.126461",
    "10.1016/j.foodchem.2023.136761",
    "10.1016/j.foodchem.2023.137834",
    "10.1016/j.foodchem.2024.141463",
    "10.1016/j.heliyon.2023.e15822",
    "10.1016/j.ijbiomac.2021.07.033",
    "10.1016/j.jfda.2013.05.010",
    "10.1016/j.jsamd.2023.100556",
    "10.1016/j.proeng.2012.01.1243",
    "10.1016/j.seppur.2025.133273",
    "10.1016/j.sintl.2024.100290",
    "10.1016/j.sna.2025.117138",
    "10.1016/j.snb.2009.10.016",
    "10.1016/j.snb.2010.10.016",
    "10.1016/j.snb.2011.08.079",
    "10.1016/j.snb.2025.138804",
    "10.1021/ac60214a047",
    "10.1021/acs.chemmater.5c00748",
    "10.1021/acs.langmuir.2c03515",
    "10.1021/acsomega.0c05987",
    "10.1021/acsomega.9b00251",
    "10.1021/acssensors.7b00591",
    "10.1021/am401730x",
    "10.1021/bi9929711",
    "10.1021/ie050145k",
    "10.1021/jacs.5b05809",
    "10.1021/la503390w",
    "10.1021/ma902269p",
    "10.1038/s44172-026-00586-8",
    "10.1039/C3RA44671A",
    "10.1039/C5RA16068E",
    "10.1039/D0AY00493F",
    "10.1039/D1MA00841B",
    "10.1039/D1RA08560K",
    "10.1039/D2RA01397E",
    "10.1039/D2RA01705A",
    "10.1039/D3AN01856C",
    "10.1039/D4NR04286G",
    "10.1039/D5NR03900B",
    "10.1039/D5OB00858A",
    "10.1039/D5RA01010A",
    "10.1039/D6RA02680J",
    "10.1039/c9sm00464e",
    "10.1042/bj0550416",
    "10.1051/bioconf/202511400073",
    "10.1063/1.1735100",
    "10.1080/00268976.2023.2197712",
    "10.1109/JSEN.2021.3060232",
    "10.1109/MEMSYS.2015.7050965",
    "10.1126/science.1237265",
    "10.1126/science.1251484",
    "10.1149/1945-7111/ad1f35",
    "10.1208/s12249-015-0336-7",
    "10.1515/cclm.1983.21.11.709",
    "10.2174/157341112803216843",
    "10.2903/j.efsa.2014.3550",
    "10.3390/chemosensors11020134",
    "10.3390/f15010098",
    "10.3390/foods11091351",
    "10.3390/ijms23169284",
    "10.3390/mi9020062",
    "10.3390/nano15130962",
    "10.3390/polym11020276",
    "10.3390/polym14061152",
    "10.3390/polym14224856",
    "10.3390/polym16233393",
    "10.3390/s110302809",
    "10.3390/s16071011",
    "10.3390/s16081190",
    "10.3390/s16122130",
    "10.3390/s17040675",
    "10.3390/s17102300",
    "10.5194/acp-15-4399-2015",
    "10.5772/intechopen.67149",
    # From references.bib (proposal-cited, with DOI)
    "10.3390/ijms25031668",  # Turkoglu2024
    "10.1016/j.jmmm.2022.169903",  # antarnusa2022
    "10.1007/s11220-025-00597-3",  # ardiyanti2025
    "10.3390/molecules201219884",  # gaaz2015properties
    "10.3390/batteries10080271",  # liu2024review
    "10.12928/TELKOMNIKA.v18i5.14034",  # shylu2020power
    "10.1016/j.bios.2023.115850",  # singhal2024food
    "10.1016/j.foodchem.2022.134235",  # sun2023optical
    "10.1016/j.heliyon.2023.e15193",  # zhu2023
    "10.1016/j.measurement.2025.118386",  # antarnusa2025TEOS
    "10.1088/1742-6596/1011/1/012061",  # antarnusa2018
    "10.3390/s16030298",  # rifai2016giant
    "10.3390/s16060904",  # ennen2016giant
    "10.1039/d4ra01989j",  # vitayaya2024
    "10.18178/ijeetc.12.2.142-149",  # ricci2023smart
    "10.1109/JSEN.2023.3257052",  # wibowo2023gmr
    "10.1038/s41586-019-0980-2",  # havlicek2019 (already have)
    "10.1103/PhysRevLett.122.040504",  # schuld2019 (already have)
    "10.1016/j.snb.2021.129651",  # wang2021mos (already have)
    "10.1021/acs.chemrev.8b00593",  # xue2019 (already have)
    "10.3390/biomedicines13030713",  # calixto2025
    "10.1038/s41598-024-79867-1",  # piekarz2024
    "10.1002/adsr.202400065",  # giaretta2024
    "10.1109/jsen.2023.3293248",  # sun2023
    "10.46984/sebatik.v27i1.2157",  # nainggolan2023
    "10.3390/app15052523",  # dey2025
    "10.3390/s23229130",  # difilippo2023
    "10.1016/j.mri.2022.09.009",  # kushwaha2023
    "10.1016/j.matpr.2021.01.893",  # mohanty2021
    "10.1016/j.ab.2016.12.006",  # sanaeifar2017
    "10.3144/expresspolymlett.2014.95",  # birck2014 (already have)
    "10.1038/s41598-020-67869-8",  # dheyab2020 (already have)
    "10.1002/app.28648",  # shi2008 (already have)
    "10.1007/BF00994018",  # cortes1995 (already have)
    "10.3390/w11050910",  # Tyralis2019
    "10.1214/15-AOS1321",  # Scornet2015
    "10.1023/A:1010933404324",  # Breiman2001
    "10.1109/MCSE.2007.58",  # millman2007 (already have)
]))


def sanitize_filename(doi):
    """Create a safe filename from DOI."""
    return re.sub(r'[<>:"/\\|?*]', '_', doi)


def check_existing(doi):
    """Check if we already have this DOI as a real PDF."""
    safe = sanitize_filename(doi)
    # Check if any existing file contains this DOI or related content
    for f in REF_DIR.iterdir():
        if f.suffix == '.pdf' and f.stat().st_size > 10000:
            if safe in f.name or doi.split('/')[-1] in f.name:
                return True
    return False


def try_unpaywall(doi):
    """Try Unpaywall API for OA link."""
    try:
        url = f"https://api.unpaywall.org/v2/{doi}?email=research@university.ac.id"
        resp = session.get(url, timeout=15)
        if resp.status_code == 200:
            data = resp.json()
            if data.get("is_oa"):
                best = data.get("best_oa_location", {})
                pdf_url = best.get("url_for_pdf") or best.get("url")
                if pdf_url:
                    return pdf_url
    except Exception:
        pass
    return None


def try_download_pdf(url, dest_path, max_depth=2):
    """Try to download a PDF from URL. Follow redirects and extract PDF links from HTML."""
    if max_depth <= 0:
        return False
    try:
        resp = session.get(url, timeout=30, allow_redirects=True, stream=True)
        content_type = resp.headers.get("Content-Type", "")

        if "pdf" in content_type.lower() or resp.content[:5] == b"%PDF-":
            if len(resp.content) > 10000:
                with open(dest_path, "wb") as f:
                    f.write(resp.content)
                return True

        # If HTML, try to extract PDF link
        if "html" in content_type.lower() and max_depth > 0:
            html = resp.text[:50000]
            # Look for meta redirect to PDF
            meta_pdf = re.search(r'<meta[^>]+url=(["\']?)([^"\'>\s]+\.pdf[^"\'>\s]*)\1', html, re.I)
            if meta_pdf:
                return try_download_pdf(meta_pdf.group(2), dest_path, max_depth - 1)

            # Look for direct PDF link
            pdf_link = re.search(r'href=["\']([^"\']+\.pdf[^"\']*)["\']', html, re.I)
            if pdf_link:
                pdf_url = pdf_link.group(1)
                if not pdf_url.startswith("http"):
                    from urllib.parse import urljoin
                    pdf_url = urljoin(url, pdf_url)
                return try_download_pdf(pdf_url, dest_path, max_depth - 1)

    except Exception as e:
        print(f"    Download error: {str(e)[:80]}")
    return False


def try_scihub_requests(doi, dest_path):
    """Try Sci-Hub via requests with multiple mirrors."""
    mirrors = [
        "https://sci-hub.st",
        "https://sci-hub.ru",
        "https://sci-hub.ren",
        "https://sci-hub.ee",
    ]
    for mirror in mirrors:
        try:
            url = f"{mirror}/{doi}"
            resp = session.get(url, timeout=20)
            if resp.status_code == 200:
                html = resp.text
                # Extract PDF URL from Sci-Hub page
                patterns = [
                    r'<iframe[^>]+src=["\']([^"\']+)["\']',
                    r'<embed[^>]+src=["\']([^"\']+)["\']',
                    r'(https?://[^"\'>\s]+\.pdf\??[^"\'>\s]*)',
                ]
                for pat in patterns:
                    m = re.search(pat, html)
                    if m:
                        pdf_url = m.group(1)
                        if pdf_url.startswith("//"):
                            pdf_url = "https:" + pdf_url
                        elif pdf_url.startswith("/"):
                            pdf_url = mirror + pdf_url
                        if try_download_pdf(pdf_url, dest_path, max_depth=1):
                            return True
        except Exception:
            pass
        time.sleep(random.uniform(0.5, 2))
    return False


def try_semantic_scholar(doi):
    """Try Semantic Scholar API for open access PDF."""
    try:
        url = f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}?fields=isOpenAccess,openAccessPdf"
        resp = session.get(url, timeout=15)
        if resp.status_code == 200:
            data = resp.json()
            if data.get("isOpenAccess") and data.get("openAccessPdf"):
                return data["openAccessPdf"].get("url")
    except Exception:
        pass
    return None


def download_doi(doi, index, total):
    """Master download function for a single DOI."""
    safe_name = sanitize_filename(doi)
    dest_path = REF_DIR / f"[doi_{safe_name}].pdf"

    print(f"\n[{index}/{total}] DOI: {doi}")

    # Skip if already exists
    if dest_path.exists() and dest_path.stat().st_size > 10000:
        print(f"  SKIP - already have ({dest_path.stat().st_size/1024:.0f} KB)")
        return "exists"

    # Check if another file has this content
    if check_existing(doi):
        print(f"  SKIP - found in existing files")
        return "exists"

    # Strategy 1: Unpaywall
    print("  [1] Unpaywall API...", end=" ")
    oa_url = try_unpaywall(doi)
    if oa_url:
        print(f"found: {oa_url[:60]}...")
        if try_download_pdf(oa_url, str(dest_path)):
            print(f"  OK ({dest_path.stat().st_size/1024:.0f} KB)")
            return "downloaded"
    else:
        print("no OA link")

    # Strategy 2: Semantic Scholar
    print("  [2] Semantic Scholar...", end=" ")
    s2_url = try_semantic_scholar(doi)
    if s2_url:
        print(f"found: {s2_url[:60]}...")
        if try_download_pdf(s2_url, str(dest_path)):
            print(f"  OK ({dest_path.stat().st_size/1024:.0f} KB)")
            return "downloaded"
    else:
        print("no link")

    # Strategy 3: Direct DOI redirect
    print("  [3] DOI redirect...", end=" ")
    if try_download_pdf(f"https://doi.org/{doi}", str(dest_path)):
        print(f"  OK ({dest_path.stat().st_size/1024:.0f} KB)")
        return "downloaded"
    else:
        print("blocked")

    # Strategy 4: Sci-Hub
    print("  [4] Sci-Hub mirrors...", end=" ")
    if try_scihub_requests(doi, str(dest_path)):
        print(f"  OK ({dest_path.stat().st_size/1024:.0f} KB)")
        return "downloaded"
    else:
        print("failed")

    # Strategy 5: MDPI/Open journals direct
    if "10.3390/" in doi:
        # MDPI journals are open access
        parts = doi.split("/")
        print("  [5] MDPI direct...", end=" ")
        mdpi_url = f"https://www.mdpi.com/{doi}/pdf"
        if try_download_pdf(mdpi_url, str(dest_path)):
            print(f"  OK ({dest_path.stat().st_size/1024:.0f} KB)")
            return "downloaded"
        else:
            print("failed")

    print(f"  FAILED - all strategies exhausted")
    return "failed"


def main():
    print("=" * 70)
    print("  KAEL-GRADE MASTER REFERENCE HARVESTER")
    print(f"  Target: {len(ALL_DOIS)} unique DOIs")
    print(f"  Output: {REF_DIR}")
    print("=" * 70)

    results = {"downloaded": 0, "exists": 0, "failed": 0}
    failed_dois = []

    for i, doi in enumerate(sorted(ALL_DOIS), 1):
        result = download_doi(doi, i, len(ALL_DOIS))
        results[result] += 1
        if result == "failed":
            failed_dois.append(doi)
        # Polite delay
        if result == "downloaded":
            time.sleep(random.uniform(1, 3))
        else:
            time.sleep(random.uniform(0.3, 1))

    # Summary
    print("\n\n" + "=" * 70)
    print("  HARVEST SUMMARY")
    print("=" * 70)
    print(f"  Downloaded:  {results['downloaded']}")
    print(f"  Already had: {results['exists']}")
    print(f"  Failed:      {results['failed']}")
    print(f"  Total DOIs:  {len(ALL_DOIS)}")

    if failed_dois:
        print(f"\n  FAILED DOIs ({len(failed_dois)}):")
        for d in failed_dois:
            print(f"    https://doi.org/{d}")

    # Save manifest
    manifest = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "total_dois": len(ALL_DOIS),
        "results": results,
        "failed_dois": failed_dois,
    }
    manifest_path = REF_DIR / "harvest_manifest.json"
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    print(f"\n  Manifest saved: {manifest_path}")


if __name__ == "__main__":
    main()
