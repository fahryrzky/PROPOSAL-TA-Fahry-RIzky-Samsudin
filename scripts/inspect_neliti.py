import sys, re
from curl_cffi import requests

sys.stdout.reconfigure(encoding='utf-8')

url = 'https://media.neliti.com/media/publications/188280-ID-desain-pembuatan-dan-uji-coba-kumparan-h.pdf'
r = requests.get(url, impersonate='chrome120')
print("Status:", r.status_code)
print("Length:", len(r.text))
pdf_links = re.findall(r'href=[\'"]([^\'"]+?\.pdf[^\'"]*)[\'"]', r.text, re.IGNORECASE)
print("PDF links found:", pdf_links)
# Look for download links
down_links = re.findall(r'href=[\'"]([^\'"]*download[^\'"]*)[\'"]', r.text, re.IGNORECASE)
print("Download links found:", down_links)
