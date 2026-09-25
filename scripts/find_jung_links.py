import os, sys, re, pypdf, io
from curl_cffi import requests

sys.stdout.reconfigure(encoding='utf-8')

url = 'https://www.analog.com/en/resources/technical-articles/op-amp-applications-handbook.html'
r = requests.get(url, impersonate='chrome120')

print(f"Status: {r.status_code}, Length: {len(r.text)}")
links = re.findall(r'href=[\'"]([^\'"]+?\.(?:pdf|zip))[\'"]', r.text, re.IGNORECASE)
print(f"Found {len(links)} links:")
for l in sorted(set(links)):
    print(" -", l)
