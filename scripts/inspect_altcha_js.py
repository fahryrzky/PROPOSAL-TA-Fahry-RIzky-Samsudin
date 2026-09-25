import sys, re
from curl_cffi import requests

sys.stdout.reconfigure(encoding='utf-8')

url = 'https://sci-hub.ru/10.1016/j.jmmm.2022.169903'
r = requests.get(url, impersonate='chrome120', doh_url='https://dns.google/dns-query')

# Find all script blocks
scripts = re.findall(r'<script\b[^>]*>(.*?)</script>', r.text, re.DOTALL)
for i, s in enumerate(scripts):
    if 'altcha' in s:
        print(f"=== SCRIPT {i} ===")
        print(s)
