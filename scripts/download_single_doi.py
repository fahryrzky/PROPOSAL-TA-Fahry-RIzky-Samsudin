import urllib.request
import re
import os
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

doi = "10.1088/1361-6560/ade92c"
mirrors = ["https://sci-hub.se", "https://sci-hub.st", "https://sci-hub.ru"]
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

out_dir = os.path.join(os.getcwd(), "Referensi")
os.makedirs(out_dir, exist_ok=True)
out_file = os.path.join(out_dir, "Schafer_2023_Monte_Carlo_Elekta_Synergy_TOPASMC.pdf")

success = False
for m in mirrors:
    try:
        url = f"{m}/{doi}"
        print(f"Checking mirror: {url}")
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
            # find pdf links
            pdf_urls = re.findall(r'src=["\']([^"\']+\.pdf[^"\']*)["\']', html)
            if not pdf_urls:
                pdf_urls = re.findall(r'href=["\']([^"\']+\.pdf[^"\']*)["\']', html)
            if not pdf_urls:
                pdf_urls = re.findall(r'location\.href\s*=\s*["\']([^"\']+)["\']', html)

            print(f"Found URLs: {pdf_urls}")
            for pu in pdf_urls:
                if pu.startswith("//"):
                    pu = "https:" + pu
                elif pu.startswith("/"):
                    pu = m + pu
                elif not pu.startswith("http"):
                    pu = f"{m}/{pu}"
                print(f"Downloading from {pu}...")
                dl_req = urllib.request.Request(pu, headers=headers)
                with urllib.request.urlopen(dl_req, context=ctx, timeout=30) as dl_resp:
                    content = dl_resp.read()
                    if content[:4] == b"%PDF":
                        with open(out_file, "wb") as f:
                            f.write(content)
                        print(f"SUCCESS! Saved to {out_file} ({len(content)} bytes)")
                        success = True
                        break
                    else:
                        print(f"Downloaded content was not PDF: header is {content[:20]}")
            if success:
                break
    except Exception as e:
        print(f"Mirror {m} failed: {e}")

if not success:
    print("Trying alternative direct search / repositories...")
