import urllib.request
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

doi = "10.1088/1361-6560/ade92c"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

# Let's test Nexus search endpoint
nexus_hosts = ["https://libgen.li", "https://libgen.is", "https://libgen.rs"]
for h in nexus_hosts:
    try:
        url = f"{h}/scimag/index.php?s={doi}"
        print(f"Testing {url}...")
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
            if "ade92c" in html or "TOPASMC" in html:
                print(f"FOUND ON {h}!")
            else:
                print(f"Not found on {h} (length {len(html)})")
    except Exception as e:
        print(f"Error on {h}: {e}")
