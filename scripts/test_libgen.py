import sys, re
from curl_cffi import requests

sys.stdout.reconfigure(encoding='utf-8')

doi = "10.1016/j.jmmm.2022.169903" # antarnusa2022

# Libgen scimag
libgen_mirrors = [
    f"https://libgen.li/scimag/ads.php?doi={doi}",
    f"https://libgen.is/scimag/?q={doi}",
    f"https://libgen.rs/scimag/?q={doi}"
]

for url in libgen_mirrors:
    print(f"Testing Libgen: {url} ...")
    try:
        r = requests.get(url, impersonate='chrome120', timeout=15)
        print(f"  Status: {r.status_code}, Length: {len(r.text)}")
        if "get.php" in r.text or "download" in r.text.lower():
            links = re.findall(r'href=[\'"]([^\'"]*(?:get\.php|download|\.pdf)[^\'"]*)[\'"]', r.text, re.I)
            print("  Links found:", links[:5])
    except Exception as e:
        print(f"  Error: {e}")
