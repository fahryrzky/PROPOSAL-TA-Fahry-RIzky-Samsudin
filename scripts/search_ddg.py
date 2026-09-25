import urllib.request
import urllib.parse
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

query = '"Monte Carlo modeling of the Elekta Synergy" "TOPASMC"'
url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(query)}"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
        # Extract uddg links
        urls = re.findall(r'uddg=([^&"\']+)', html)
        for u in urls:
            dec = urllib.parse.unquote(u)
            print("Found URL:", dec)
except Exception as e:
    print("DDG search error:", e)
