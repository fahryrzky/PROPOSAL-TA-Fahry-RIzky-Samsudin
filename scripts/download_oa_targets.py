import os
from curl_cffi import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'Accept': 'application/pdf,*/*;q=0.9',
}

oa_targets = [
    {
        "key": "Turkoglu2024",
        "url": "https://www.mdpi.com/1422-0067/25/3/1668/pdf",
        "filename": "[Turkoglu2024] - Turkoglu et al (2024) - PVA-Based Electrospun Materials A Promising Route to Design of Advanced Biocompatible Scaffolds.pdf"
    },
    {
        "key": "liu2024review",
        "url": "https://www.mdpi.com/2313-0105/10/8/271/pdf",
        "filename": "[liu2024review] - Liu et al (2024) - Review of Energy Storage Capacitor Technology.pdf"
    },
    {
        "key": "gaaz2015properties",
        "url": "https://www.mdpi.com/1420-3049/20/12/19884/pdf",
        "filename": "[gaaz2015properties] - Gaaz et al (2015) - Properties and Applications of Polyvinyl Alcohol Halloysite Nanotubes Nanocomposites.pdf"
    },
    {
        "key": "zhu2023",
        "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10126588/pdf/main.pdf",
        "filename": "[zhu2023] - Zhu et al (2023) - Design of improved four-coil structure with high uniformity of magnetic field based on genetic algorithm.pdf"
    }
]

out_dir = "referensi"
for t in oa_targets:
    dest = os.path.join(out_dir, t["filename"])
    if os.path.exists(dest):
        print(f"[EXISTS] {t['key']}")
        continue
    print(f"[FETCHING] {t['key']} from {t['url']}...")
    try:
        r = requests.get(t['url'], headers=headers, impersonate="chrome120", doh_url="https://dns.google/dns-query", timeout=30)
        if r.status_code == 200 and r.content.startswith(b'%PDF'):
            with open(dest, 'wb') as f:
                f.write(r.content)
            print(f" [SUCCESS] Saved {dest} ({len(r.content)/1024:.1f} KB)")
        else:
            print(f" [FAIL] Status: {r.status_code}, length: {len(r.content)}, magic: {r.content[:10]}")
    except Exception as e:
        print(f" [ERROR] {e}")
