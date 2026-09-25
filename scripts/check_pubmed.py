import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://pubmed.ncbi.nlm.nih.gov/40578398/"
headers = {"User-Agent": "Mozilla/5.0"}
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, context=ctx) as resp:
    html = resp.read().decode("utf-8")
    for m in re.finditer(r'class="link-item[^"]*"[^>]*href="([^"]+)"', html):
        print("PubMed fulltext link:", m.group(1))
    # print abstract text
    m_abs = re.search(r'<div class="abstract-content selected"[^>]*>(.*?)</div>', html, re.DOTALL)
    if m_abs:
        print("Abstract found, length:", len(m_abs.group(1)))
