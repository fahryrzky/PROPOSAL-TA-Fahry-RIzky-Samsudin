import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

doi = "10.1088/1361-6560/ade92c"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

# Let's test annas-archive.li
for mirror in ["https://annas-archive.li", "https://annas-archive.pm"]:
    try:
        url = f"{mirror}/search?q={doi}"
        print("Checking", url)
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
            print("Response length:", len(html))
            md5s = re.findall(r"/md5/([a-f0-9]{32})", html)
            print("Found MD5s:", md5s)
    except Exception as e:
        print("Error on", mirror, e)
