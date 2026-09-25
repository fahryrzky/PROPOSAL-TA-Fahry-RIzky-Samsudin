import sys, re, json, hashlib, base64
from curl_cffi import requests

sys.stdout.reconfigure(encoding='utf-8')

url = 'https://sci-hub.ru/10.1016/j.jmmm.2022.169903'
r = requests.get(url, impersonate='chrome120', doh_url='https://dns.google/dns-query')

print("Status:", r.status_code)
# Search for altcha tag or challenge
altcha_match = re.search(r'challenge=[\'"]([^\'"]+)[\'"]', r.text)
if not altcha_match:
    altcha_match = re.search(r'name=[\'"]altcha[\'"][^>]*value=[\'"]([^\'"]+)[\'"]', r.text)
if not altcha_match:
    # search all custom elements or data-challenge
    altcha_match = re.search(r'data-challenge=[\'"]([^\'"]+)[\'"]', r.text)

print("Altcha match:", altcha_match.group(1) if altcha_match else "Not found in regex")

# Let's print snippet around altcha
for line in r.text.splitlines():
    if 'altcha' in line.lower():
        print("LINE:", line[:120])
