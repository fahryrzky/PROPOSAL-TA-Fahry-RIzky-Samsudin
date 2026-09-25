import os
import re

size = os.path.getsize("rg_page.html")
print(f"rg_page.html size: {size} bytes")

with open("rg_page.html", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

titles = re.findall(r"<title>(.*?)</title>", text)
print("Title:", titles)

if "Request full-text" in text:
    print("Found text: 'Request full-text'")
if "Download full-text" in text:
    print("Found text: 'Download full-text'")

for m in re.finditer(r'href="([^"]+download[^"]*)"', text):
    print("Download URL:", m.group(1))

for m in re.finditer(r'href="([^"]+\.pdf[^"]*)"', text):
    print("PDF URL:", m.group(1))
