import urllib.request
import urllib.parse
import json
import re
import os
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

doi = "10.1088/1361-6560/ade92c"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}
out_path = os.path.join("Referensi", "Schafer_2023_Monte_Carlo_modeling_Elekta_TOPASMC.pdf")

def save_if_pdf(data, source_name):
    if len(data) > 1000 and data[:4] == b"%PDF":
        with open(out_path, "wb") as f:
            f.write(data)
        print(f"SUCCESS from {source_name}! Saved {len(data)} bytes to {out_path}")
        return True
    return False

# 1. Check OpenAlex for all OA locations and landing pages
print("[1] Checking OpenAlex...")
try:
    url = f"https://api.openalex.org/works/https://doi.org/{doi}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        print("OpenAlex title:", data.get("title"))
        print("OpenAlex is_oa:", data.get("is_oa"))
        print("Primary location:", data.get("primary_location", {}).get("pdf_url"))
        for loc in data.get("locations", []):
            pdf_url = loc.get("pdf_url")
            landing_url = loc.get("landing_page_url")
            print(f"Location: pdf={pdf_url}, landing={landing_url}")
            if pdf_url:
                try:
                    p_req = urllib.request.Request(pdf_url, headers=headers)
                    with urllib.request.urlopen(p_req, context=ctx, timeout=20) as p_resp:
                        if save_if_pdf(p_resp.read(), f"OpenAlex ({pdf_url})"):
                            exit(0)
                except Exception as e:
                    print(f"Failed {pdf_url}: {e}")
except Exception as e:
    print("OpenAlex error:", e)

# 2. Check CORE API
print("\n[2] Checking CORE API...")
try:
    core_url = f"https://api.core.ac.uk/v3/discover?doi={doi}"
    req = urllib.request.Request(core_url, headers=headers)
    with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
        cdata = json.loads(resp.read().decode("utf-8"))
        print("CORE response:", cdata)
        dl = cdata.get("downloadUrl")
        if dl:
            try:
                with urllib.request.urlopen(urllib.request.Request(dl, headers=headers), context=ctx, timeout=20) as d_resp:
                    if save_if_pdf(d_resp.read(), "CORE"):
                        exit(0)
            except Exception as e:
                print(f"CORE download error: {e}")
except Exception as e:
    print("CORE error:", e)

# 3. Check Dissemin
print("\n[3] Checking Dissemin...")
try:
    dis_url = f"https://dissem.in/api/{doi}"
    req = urllib.request.Request(dis_url, headers=headers)
    with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
        ddata = json.loads(resp.read().decode("utf-8"))
        paper = ddata.get("paper", {})
        print("Dissemin pdf_url:", paper.get("pdf_url"))
        records = paper.get("records", [])
        for r in records:
            purl = r.get("pdf_url")
            print("Record purl:", purl)
            if purl:
                try:
                    with urllib.request.urlopen(urllib.request.Request(purl, headers=headers), context=ctx, timeout=20) as d_resp:
                        if save_if_pdf(d_resp.read(), "Dissemin"):
                            exit(0)
                except Exception as e:
                    print(f"Dissemin download error: {e}")
except Exception as e:
    print("Dissemin error:", e)

# 4. Check Google Scholar / Universitaetsbibliothek Halle repository
print("\n[4] Checking MLU Halle repository & German DNB...")
try:
    search_terms = urllib.parse.quote("Monte Carlo modeling of the Elekta Synergy TOPASMC")
    mlu_url = f"https://opendata.uni-halle.de/simple-search?query={search_terms}"
    req = urllib.request.Request(mlu_url, headers=headers)
    with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
        mhtml = resp.read().decode("utf-8", errors="ignore")
        links = re.findall(r'href="([^"]+\.pdf[^"]*)"', mhtml)
        print("MLU Halle PDF links:", links)
except Exception as e:
    print("MLU Halle error:", e)

print("\nFinished hunting script pass 1.")
