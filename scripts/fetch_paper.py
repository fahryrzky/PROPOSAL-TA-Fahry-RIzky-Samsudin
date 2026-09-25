import urllib.request
import re
import os
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

doi = "10.1088/1361-6560/ade92c"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}

out_file = os.path.join("Referensi", "Schafer_2023_Monte_Carlo_modeling_Elekta_TOPASMC.pdf")

def try_download(url, referer=None):
    req_headers = dict(headers)
    if referer:
        req_headers["Referer"] = referer
    req = urllib.request.Request(url, headers=req_headers)
    with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
        data = resp.read()
        if data[:4] == b"%PDF":
            with open(out_file, "wb") as f:
                f.write(data)
            print(f"SUCCESS! Downloaded {len(data)} bytes to {out_file}")
            return True
        else:
            print(f"Not a PDF from {url}: {data[:50]}")
    return False

# 1. Try Anna's Archive API / Fast download
print("Checking Anna's Archive...")
try:
    anna_url = f"https://annas-archive.org/search?q={doi}"
    req = urllib.request.Request(anna_url, headers=headers)
    with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
        md5s = re.findall(r"/md5/([a-f0-9]{32})", html)
        print("Found MD5s on Anna's Archive:", md5s)
        if md5s:
            for md5 in md5s[:2]:
                detail_url = f"https://annas-archive.org/md5/{md5}"
                d_req = urllib.request.Request(detail_url, headers=headers)
                with urllib.request.urlopen(d_req, context=ctx, timeout=15) as d_resp:
                    d_html = d_resp.read().decode("utf-8", errors="ignore")
                    dl_links = re.findall(r'href="(https?://[^"]+)"[^>]*>Fast Partner Server', d_html)
                    if not dl_links:
                        dl_links = re.findall(r'href="(https?://[^"]+download[^"]*)"', d_html)
                    print(f"Anna download links for {md5}:", dl_links)
                    for dl in dl_links:
                        try:
                            if try_download(dl, referer=detail_url):
                                exit(0)
                        except Exception as e:
                            print(f"Failed {dl}: {e}")
except Exception as e:
    print("Anna error:", e)

# 2. Try ResearchGate publication
print("Checking ResearchGate...")
try:
    rg_url = "https://www.researchgate.net/publication/392947116_Monte_Carlo_modeling_of_the_Elekta_Synergy_linear_accelerator_platform_with_Agility_MLC_using_TOPASMC_for_secondary_dose_calculation"
    req = urllib.request.Request(rg_url, headers=headers)
    with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
        # Look for fulltext download link
        matches = re.findall(r'href="([^"]+downloadFulltext[^"]*)"', html)
        if not matches:
            matches = re.findall(r'href="([^"]+fulltext[^"]*\.pdf)"', html)
        print("RG matches:", matches)
        for m in matches:
            if not m.startswith("http"):
                m = "https://www.researchgate.net" + m
            try:
                if try_download(m, referer=rg_url):
                    exit(0)
            except Exception as e:
                print(f"Failed RG {m}: {e}")
except Exception as e:
    print("RG error:", e)

# 3. Try Nexus / IPFS
print("Checking Nexus / STC...")
try:
    nexus_url = f"https://nexus.openstc.org/api/doi/{doi}"
    req = urllib.request.Request(nexus_url, headers=headers)
    with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        print("Nexus data:", data)
except Exception as e:
    print("Nexus error:", e)
