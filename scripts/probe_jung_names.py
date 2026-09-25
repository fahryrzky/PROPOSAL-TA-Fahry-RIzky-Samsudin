import sys
from curl_cffi import requests

sys.stdout.reconfigure(encoding='utf-8')

base = "https://www.analog.com/media/en/training-seminars/design-handbooks/Op-Amp-Applications/"
probes = [
    "Section5.pdf", "Section-5.pdf", "Section5_1.pdf", "Section5-1.pdf", 
    "Section5-1to5-4.pdf", "Section5-5to5-8.pdf", "Section5_part1.pdf",
    "Section5A.pdf", "Section5B.pdf", "Section8.pdf", "SectionH.pdf", 
    "Index.pdf", "OpAmpApps.zip", "OpAmpApps_Full.pdf", "Full_Book.pdf",
    "Section5_part2.pdf", "Section5_1-4.pdf", "Section5_5-8.pdf",
    "Section-5-1-to-5-4.pdf", "Section-5-5-to-5-8.pdf"
]

for p in probes:
    url = base + p
    r = requests.head(url, impersonate='chrome120', allow_redirects=True)
    if r.status_code == 200:
        print(f"FOUND: {p} (status: {r.status_code}, length: {r.headers.get('content-length')})")
    else:
        # print first 5 failed to see pattern
        if p in ["SectionH.pdf", "Section5.pdf", "Index.pdf"]:
            print(f"FAIL: {p} ({r.status_code})")
