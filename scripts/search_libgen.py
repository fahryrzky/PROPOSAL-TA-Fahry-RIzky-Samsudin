import urllib.request
import urllib.parse
import re
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
doi = "10.1088/1361-6560/ade92c"

# Try Libgen.li
url = f"https://libgen.li/index.php?req={urllib.parse.quote(doi)}"
print("Checking Libgen.li:", url)
try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
        get_links = re.findall(r'href="([^"]*get\.php[^"]*)"', html)
        print("Libgen.li get links:", get_links)
        for gl in get_links:
            if not gl.startswith("http"):
                gl = "https://libgen.li/" + gl
            print("Trying download:", gl)
            with urllib.request.urlopen(urllib.request.Request(gl, headers=headers), context=ctx, timeout=20) as gresp:
                gdata = gresp.read()
                if gdata[:4] == b"%PDF":
                    out_path = "Referensi/Schafer_2023_Monte_Carlo_modeling_Elekta_TOPASMC.pdf"
                    with open(out_path, "wb") as f:
                        f.write(gdata)
                    print("SUCCESS! Saved to", out_path)
                    exit(0)
except Exception as e:
    print("Libgen.li error:", e)

# Try Sci-Hub via IPFS/CID or Telegram Nexus
url_nexus = f"https://nexus.openstc.org/api/doi/{doi}"
print("Checking STC/Nexus API:", url_nexus)
try:
    with urllib.request.urlopen(urllib.request.Request(url_nexus, headers=headers), context=ctx, timeout=10) as resp:
        print("Nexus response:", resp.read().decode("utf-8"))
except Exception as e:
    print("Nexus error:", e)

print("Finished search.")
