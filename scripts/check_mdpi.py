import sys
from curl_cffi import requests

sys.stdout.reconfigure(encoding='utf-8')

url = 'https://www.mdpi.com/1422-0067/25/3/1668/pdf'
r = requests.get(url, impersonate='chrome120')
print("Status:", r.status_code)
print("Length:", len(r.text))
print("Content snippet:\n", r.text[:500])
