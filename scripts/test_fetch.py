import urllib.request, ssl

ctx = ssl._create_unverified_context()
urls = [
    ('nve_alt023', 'https://www.nve.com/Downloads/alt023.pdf'),
    ('nve_evb01', 'https://www.nve.com/Downloads/EVB01.pdf'),
    ('ti_cookbook', 'https://www.ti.com/lit/an/sboa269a/sboa269a.pdf'),
    ('ti_ads1115', 'https://www.ti.com/lit/ds/symlink/ads1115.pdf'),
    ('adi_ad623', 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD623.pdf')
]
for k, u in urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
        with urllib.request.urlopen(req, context=ctx, timeout=15) as r:
            d = r.read()
            print(f"{k}: {len(d)} bytes, is_pdf: {d.startswith(b'%PDF')}")
    except Exception as e:
        print(f"{k}: err {e}")
