#!/usr/bin/env python3
"""
download_missing_refs.py
========================
Downloads the 20 missing cited references for the TMR-Formalin proposal.
Strategy:
  - DOI-based papers: tries Sci-Hub mirrors + Unpaywall + direct publisher OA
  - Non-DOI refs: tries Google Scholar, direct URL, or marks for manual fetch
"""

import os
import sys
import json
import time
import random
import urllib.request
import urllib.error
import ssl
import re
from pathlib import Path

# Disable SSL verification for Sci-Hub mirrors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

REF_DIR = Path(r"c:\Users\Fahry Rizky S\Documents\Tugas Akhir Fahry\Proposal\Referensi")
CATALOG_PATH = REF_DIR / "catalog.json"

# Sci-Hub mirrors (try multiple)
SCIHUB_MIRRORS = [
    "https://sci-hub.se",
    "https://sci-hub.st",
    "https://sci-hub.ru",
    "https://sci-hub.ren",
    "https://sci-hub.ee",
]

# References that need download
REFS_WITH_DOI = [
    {
        "key": "Turkoglu2024",
        "doi": "10.3390/ijms25031668",
        "filename": "[Turkoglu2024] - Turkoglu (2024) - PVA-Based Electrospun Materials A Promising Route to Design Biocompatible Scaffolds.pdf",
        "oa_url": "https://www.mdpi.com/1422-0067/25/3/1668/pdf",  # MDPI is OA
    },
    {
        "key": "antarnusa2022",
        "doi": "10.1016/j.jmmm.2022.169903",
        "filename": "[antarnusa2022] - Antarnusa (2022) - Synthesis of Fe3O4 at Different Reaction Temperatures.pdf",
    },
    {
        "key": "ardiyanti2025",
        "doi": "10.1007/s11220-025-00597-3",
        "filename": "[ardiyanti2025] - Ardiyanti (2025) - Facile and Fast Assay of Biomolecule Using ICs-Based GMR.pdf",
    },
    {
        "key": "gaaz2015properties",
        "doi": "10.3390/molecules201219884",
        "filename": "[gaaz2015properties] - Gaaz et al (2015) - Properties and Applications of Polyvinyl Alcohol (Molecules).pdf",
        "oa_url": "https://www.mdpi.com/1420-3049/20/12/19884/pdf",  # MDPI is OA
    },
    {
        "key": "liu2024review",
        "doi": "10.3390/batteries10080271",
        "filename": "[liu2024review] - Liu (2024) - Review of Energy Storage Capacitor Technology and Dielectric Physics.pdf",
        "oa_url": "https://www.mdpi.com/2313-0105/10/8/271/pdf",  # MDPI is OA
    },
    {
        "key": "shylu2020power",
        "doi": "10.12928/TELKOMNIKA.v18i5.14034",
        "filename": "[shylu2020power] - Shylu (2020) - A Power Efficient Delta-Sigma ADC with Series-Bilinear Switched Capacitor.pdf",
    },
    {
        "key": "singhal2024food",
        "doi": "10.1016/j.bios.2023.115850",
        "filename": "[singhal2024food] - Singhal (2024) - Advances in Electrochemical Biosensors for Formaldehyde Detection.pdf",
    },
    {
        "key": "sun2023optical",
        "doi": "10.1016/j.foodchem.2022.134235",
        "filename": "[sun2023optical] - Sun (2023) - Smartphone-Integrated Colorimetric Sensor Array for Rapid Detection of Formaldehyde.pdf",
    },
    {
        "key": "zhu2023",
        "doi": "10.1016/j.heliyon.2023.e15193",
        "filename": "[zhu2023] - Zhu (2023) - Design of improved four-coil structure with high uniformity based on GA.pdf",
        "oa_url": "https://www.cell.com/heliyon/pdf/S2405-8440(23)02400-5.pdf",  # Heliyon is OA
    },
    {
        "key": "arduino2022",
        "doi": "",
        "filename": "[arduino2022] - Arduino (2022) - Arduino Open Source Report 2022.pdf",
        "direct_url": "https://www.arduino.cc/resources/open-source-report/Arduino_Open_Source_Report_2022.pdf",
    },
    {
        "key": "pythonorg",
        "doi": "",
        "filename": "[pythonorg] - Python Software Foundation (2025) - Welcome to Python.org Technical Documentation.pdf",
    },
]

REFS_NO_DOI = [
    {
        "key": "Firmansyah2017",
        "title": "Perancangan Sistem Electromyography (EMG) Sebagai Penggerak Jari Robot",
        "filename": "[Firmansyah2017] - Firmansyah (2017) - Perancangan Sistem Electromyography EMG Sebagai Penggerak.pdf",
        "search_query": "Firmansyah 2017 Perancangan Sistem Electromyography EMG Penggerak Jari Robot filetype:pdf",
    },
    {
        "key": "Supriyanto2023",
        "title": "Rancang Bangun Modul Low Pass Filter (LPF) Orde 1 dan Orde 2",
        "filename": "[Supriyanto2023] - Supriyanto (2023) - Rancang Bangun Modul Low Pass Filter LPF Orde 1 dan Orde 2.pdf",
        "search_query": "Supriyanto 2023 Rancang Bangun Modul Low Pass Filter LPF Orde 1 Orde 2 filetype:pdf",
    },
    {
        "key": "dinata2016",
        "title": "Arduino Itu Pintar",
        "filename": "[dinata2016] - Yuwono Marta Dinata (2016) - Arduino Itu Pintar.pdf",
        "note": "Indonesian book - ISBN 978-602-02-8394-5",
    },
    {
        "key": "gantrade_adh",
        "title": "Adipic Acid Dihydrazide - A Unique Crosslinking Agent and Curative",
        "filename": "[gantrade_adh] - Gantrade (2024) - Adipic Acid Dihydrazide A Unique Crosslinking Agent and Curative.pdf",
        "direct_url": "https://www.gantrade.com/blog/adipic-acid-dihydrazide-a-unique-crosslinking-agent-and-curative",
    },
    {
        "key": "magneticsmag_alt023",
        "title": "NVE Introduces Ultraminiature Analog TMR Sensors",
        "filename": "[magneticsmag_alt023] - Magnetics Magazine (2023) - NVE Introduces Ultraminiature Analog TMR Sensors.pdf",
    },
    {
        "key": "pekanbaru_bakso",
        "title": "Identifikasi Kandungan Formalin pada Bakso dan Mie Kuning yang Beredar di Jalan Soebrantas Kota Pekanbaru",
        "filename": "[pekanbaru_bakso] - Agustin (2023) - Identifikasi Kandungan Formalin pada Bakso dan Mie Kuning di Pekanbaru.pdf",
        "search_query": "Agustin 2023 Identifikasi Formalin Bakso Mie Kuning Pekanbaru Soebrantas filetype:pdf",
    },
    {
        "key": "sanjaya2025",
        "title": "Basic Mobile Robot Arduino Berbasis Pemrograman IDE Arduino + Interface Python",
        "filename": "[sanjaya2025] - Mada Sanjaya (2025) - Basic Mobile Robot Arduino Berbasis Pemrograman IDE Arduino.pdf",
        "note": "Indonesian book - publisher BOLABOT",
    },
    {
        "key": "sanjayab2025",
        "title": "Membuat Robot Berbasis Raspberry Pi Pico W + Pemrograman Python",
        "filename": "[sanjayab2025] - Mada Sanjaya (2025) - Membuat Robot Berbasis Raspberry Pi Pico W + Pemrograman Python.pdf",
        "note": "Indonesian book - publisher BOLABOT",
    },
    {
        "key": "sunar2021",
        "title": "Pemrograman Arduino untuk Pemula",
        "filename": "[sunar2021] - Sunardi (2021) - Pemrograman Arduino untuk Pemula.pdf",
        "note": "Indonesian book - publisher Cipta Prima Nusantara",
    },
    {
        "key": "yogyakarta_bakso",
        "title": "Identifikasi Kandungan Formalin pada Bakso di Yogyakarta",
        "filename": "[yogyakarta_bakso] - Pratama (2025) - Identifikasi Kandungan Formalin pada Bakso di Yogyakarta.pdf",
        "search_query": "Pratama 2025 Identifikasi Formalin Bakso Yogyakarta Rapid Test Kit filetype:pdf",
    },
    {
        "key": "yudhistira2019",
        "title": "Pengukuran Medan Magnetik Helmholtz Coil Melalui Konversi Tegangan Efek Hall",
        "filename": "[yudhistira2019] - Yudhistira (2019) - Pengukuran Medan Magnetik Helmholtz Coil Melalui Konversi Tegangan.pdf",
        "search_query": "Yudhistira 2019 Pengukuran Medan Magnetik Helmholtz Coil Konversi Tegangan Efek Hall filetype:pdf",
    },
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/pdf,*/*",
}


def download_file(url, dest_path, timeout=30):
    """Download a file from URL to dest_path. Returns True on success."""
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            data = resp.read()
            if len(data) < 5000:
                print(f"    ⚠ Downloaded only {len(data)} bytes — likely not a real PDF")
                return False
            # Check PDF magic bytes
            if not data[:5].startswith(b"%PDF"):
                # Try to find PDF URL in HTML
                html = data.decode("utf-8", errors="ignore")
                pdf_match = re.search(r'(https?://[^"\'>\s]+\.pdf)', html, re.IGNORECASE)
                if pdf_match:
                    print(f"    → Found embedded PDF link: {pdf_match.group(1)[:80]}...")
                    return download_file(pdf_match.group(1), dest_path, timeout)
                # Check for iframe/embed src
                iframe_match = re.search(r'<iframe[^>]+src=["\']([^"\']+)["\']', html)
                if iframe_match:
                    src = iframe_match.group(1)
                    if not src.startswith("http"):
                        parsed = urllib.parse.urlparse(url)
                        src = f"{parsed.scheme}://{parsed.netloc}{src}"
                    print(f"    → Found iframe src: {src[:80]}...")
                    return download_file(src, dest_path, timeout)
                print(f"    ⚠ Response is not a PDF ({len(data)} bytes)")
                return False
            with open(dest_path, "wb") as f:
                f.write(data)
            print(f"    ✓ Saved {len(data)/1024:.0f} KB")
            return True
    except Exception as e:
        print(f"    ✗ Error: {e}")
        return False


def try_unpaywall(doi):
    """Try Unpaywall API (free, no key needed for polite pool)."""
    url = f"https://api.unpaywall.org/v2/{doi}?email=student@university.ac.id"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": HEADERS["User-Agent"]})
        with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
            data = json.loads(resp.read())
            if data.get("is_oa"):
                best = data.get("best_oa_location", {})
                pdf_url = best.get("url_for_pdf") or best.get("url")
                if pdf_url:
                    return pdf_url
    except Exception:
        pass
    return None


def try_scihub(doi, dest_path):
    """Try downloading from Sci-Hub mirrors."""
    for mirror in SCIHUB_MIRRORS:
        print(f"  Trying {mirror}...")
        url = f"{mirror}/{doi}"
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=20, context=ctx) as resp:
                html = resp.read().decode("utf-8", errors="ignore")
                # Find the PDF embed/iframe URL
                patterns = [
                    r'<iframe[^>]+src=["\']([^"\']+)["\']',
                    r'<embed[^>]+src=["\']([^"\']+)["\']',
                    r'location\.href\s*=\s*["\']([^"\']+\.pdf[^"\']*)["\']',
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
                        print(f"    Found PDF URL: {pdf_url[:80]}...")
                        if download_file(pdf_url, dest_path, timeout=45):
                            return True
        except Exception as e:
            print(f"    Mirror failed: {e}")
        time.sleep(random.uniform(1, 3))
    return False


def download_doi_ref(ref):
    """Download a DOI-based reference."""
    key = ref["key"]
    doi = ref.get("doi", "")
    dest = REF_DIR / ref["filename"]
    print(f"\n{'='*60}")
    print(f"[{key}] DOI: {doi}")

    # Skip if already have a real PDF
    if dest.exists() and dest.stat().st_size > 10000:
        print(f"  ✓ Already have real PDF ({dest.stat().st_size/1024:.0f} KB)")
        return True

    # Strategy 1: Direct OA URL (MDPI, Heliyon, etc.)
    oa_url = ref.get("oa_url")
    if oa_url:
        print(f"  Strategy 1: Direct OA URL")
        if download_file(oa_url, str(dest)):
            return True

    # Strategy 1b: Direct URL
    direct_url = ref.get("direct_url")
    if direct_url:
        print(f"  Strategy 1b: Direct URL")
        if download_file(direct_url, str(dest)):
            return True

    if not doi:
        print(f"  ⚠ No DOI available, skipping DOI-based strategies")
        return False

    # Strategy 2: Unpaywall
    print(f"  Strategy 2: Unpaywall API")
    oa_link = try_unpaywall(doi)
    if oa_link:
        print(f"    Found OA link: {oa_link[:80]}...")
        if download_file(oa_link, str(dest)):
            return True

    # Strategy 3: DOI redirect (some publishers serve PDF directly)
    print(f"  Strategy 3: DOI redirect")
    doi_url = f"https://doi.org/{doi}"
    if download_file(doi_url, str(dest)):
        return True

    # Strategy 4: Sci-Hub
    print(f"  Strategy 4: Sci-Hub mirrors")
    if try_scihub(doi, str(dest)):
        return True

    print(f"  ✗ ALL STRATEGIES FAILED for [{key}]")
    return False


def download_nodoi_ref(ref):
    """Download a non-DOI reference (Indonesian journals, books, web articles)."""
    key = ref["key"]
    dest = REF_DIR / ref["filename"]
    print(f"\n{'='*60}")
    print(f"[{key}] {ref['title'][:60]}...")

    if dest.exists() and dest.stat().st_size > 10000:
        print(f"  ✓ Already have real PDF ({dest.stat().st_size/1024:.0f} KB)")
        return True

    # Strategy 1: Direct URL if available
    direct_url = ref.get("direct_url")
    if direct_url:
        print(f"  Strategy 1: Direct URL")
        if download_file(direct_url, str(dest)):
            return True

    # For books and other non-downloadable items, just note them
    note = ref.get("note")
    if note:
        print(f"  ℹ Note: {note}")
        print(f"  ⚠ This is a physical book — cannot be auto-downloaded")
        return False

    # Strategy 2: Search via Google Scholar (just print search URL)
    search_query = ref.get("search_query")
    if search_query:
        print(f"  ℹ Manual search suggested:")
        print(f"    https://scholar.google.com/scholar?q={urllib.parse.quote(search_query)}")

    print(f"  ✗ Cannot auto-download [{key}] — manual intervention needed")
    return False


def main():
    print("=" * 70)
    print("  TMR-Formalin Proposal — Missing Reference Downloader")
    print(f"  Target directory: {REF_DIR}")
    print("=" * 70)

    success = 0
    failed = 0
    manual = 0

    # Phase 1: DOI-based downloads
    print("\n\n▶ PHASE 1: DOI-based references")
    print("-" * 40)
    for ref in REFS_WITH_DOI:
        if download_doi_ref(ref):
            success += 1
        else:
            failed += 1
        time.sleep(random.uniform(0.5, 2))

    # Phase 2: Non-DOI downloads
    print("\n\n▶ PHASE 2: Non-DOI references")
    print("-" * 40)
    for ref in REFS_NO_DOI:
        result = download_nodoi_ref(ref)
        if result:
            success += 1
        elif ref.get("note"):
            manual += 1
        else:
            failed += 1
        time.sleep(random.uniform(0.5, 1))

    # Summary
    print("\n\n" + "=" * 70)
    print("  DOWNLOAD SUMMARY")
    print("=" * 70)
    print(f"  ✓ Successfully downloaded: {success}")
    print(f"  ✗ Failed (need manual):    {failed}")
    print(f"  📚 Physical books (skip):   {manual}")
    print(f"  Total:                      {success + failed + manual}")

    # Update catalog
    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    updated = 0
    for entry in catalog:
        fname = entry.get("local_filename")
        if fname:
            fpath = REF_DIR / fname
            if fpath.exists() and fpath.stat().st_size > 10000:
                if not entry.get("has_local_pdf"):
                    entry["has_local_pdf"] = True
                    updated += 1

    with open(CATALOG_PATH, "w", encoding="utf-8") as f:
        json.dump(catalog, f, indent=2, ensure_ascii=False)

    if updated:
        print(f"\n  📝 Updated {updated} catalog entries")


if __name__ == "__main__":
    main()
