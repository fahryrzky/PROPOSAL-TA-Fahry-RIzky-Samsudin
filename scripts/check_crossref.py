import urllib.request
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

doi = "10.1088/1361-6560/ade92c"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

# Let's check crossref for alternative links
req = urllib.request.Request(f"https://api.crossref.org/works/{doi}", headers=headers)
with urllib.request.urlopen(req, context=ctx) as resp:
    data = json.loads(resp.read().decode("utf-8"))
    msg = data["message"]
    print("Crossref links:")
    for link in msg.get("link", []):
        print(link)
    print("Alternative IDs:", msg.get("alternative-id"))
    print("Indexed:", msg.get("indexed"))
