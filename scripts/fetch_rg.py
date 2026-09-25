import urllib.request
import ssl
import re

ctx = ssl._create_unverified_context()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5'
}

rg_urls = [
    ('yogyakarta_bakso', 'https://www.researchgate.net/publication/388487771_IDENTIFIKASI_KANDUNGAN_FORMALIN_PADA_BAKSO_MENGGUNAKAN_METODE_KUALITATIF_DI_WILAYAH_KOTAGEDE_YOGYAKARTA'),
    ('pekanbaru_bakso', 'https://www.researchgate.net/publication/371900350_IDENTIFIKASI_KANDUNGAN_FORMALIN_PADA_BAKSO_DAN_MIE_KUNING_YANG_BEREDAR_DI_KECAMATAN_TAMPAN_KOTA_PEKANBARU')
]

for key, url in rg_urls:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=10) as r:
            html = r.read().decode('utf-8', errors='ignore')
            pdf_links = re.findall(r'href=[\'"]([^\'"]+download[^\'"]*)[\'"]', html)
            print(f'{key}: found {len(pdf_links)} download links -> {pdf_links[:3]}')
    except Exception as e:
        print(f'{key}: error {e}')
