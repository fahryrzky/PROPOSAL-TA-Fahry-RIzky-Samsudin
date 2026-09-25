import urllib.request
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
out_file = os.path.join("Referensi", "Schafer_2023_Monte_Carlo_modeling_Elekta_TOPASMC.pdf")

mirrors = [
    "https://sci-hub.ren",
    "https://sci-hub.wf",
    "https://sci-hub.ee",
    "https://libgen.li/scimag",
]

for m in ["https://sci-hub.ren", "https://sci-hub.wf", "https://sci-hub.ee"]:
    url = f"{m}/{doi}"
    print(f"Trying {url}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
            # Look for pdf links
            pdf_urls = re.findall(r'src=["\']([^"\']+\.pdf[^"\']*)["\']', html)
            if not pdf_urls:
                pdf_urls = re.findall(r'href=["\']([^"\']+\.pdf[^"\']*)["\']', html)
            if not pdf_urls:
                pdf_urls = re.findall(r'location\.href\s*=\s*["\']([^"\']+)["\']', html)
            print(f"Result for {m}: pdf_urls={pdf_urls}")
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
                    data = dl_resp.read()
                    if data[:4] == b"%PDF":
                        with open(out_file, "wb") as f:
                            f.write(data)
                        print(f"SUCCESS! Downloaded {len(data)} bytes to {out_file}")
                        exit(0)
    except Exception as e:
        print(f"Failed {m}: {e}")

print("Sci-hub did not have it or blocked. Trying Libgen / other queries...")
