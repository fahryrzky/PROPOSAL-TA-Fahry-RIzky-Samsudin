import os
import sys
import re
import urllib.request
import urllib.parse
import json

sys.stdout.reconfigure(encoding='utf-8')

# Target high-value open access papers from the 97 references
targets = [
    {
        'key': 'rovina2022formaldehyde',
        'title': 'Formaldehyde in food: occurrence, legislation, toxicity, and analytical methods',
        'doi': '10.3390/foods11091351',
        'url': 'https://www.mdpi.com/2304-8158/11/9/1351/pdf',
        'filename': '[rovina2022formaldehyde] - Rovina et al (2022) - Formaldehyde in Food Review (Foods).pdf'
    },
    {
        'key': 'si2018polyethyleneimine',
        'title': 'Ultrathin Polyethyleneimine Nanofiber Networks for Formaldehyde Gas Sensors',
        'doi': '10.3390/mi9020062',
        'url': 'https://www.mdpi.com/2072-666X/9/2/62/pdf',
        'filename': '[si2018nanofiber] - Si et al (2018) - Nanofiber Networks for Formaldehyde Gas Sensors (Micromachines).pdf'
    },
    {
        'key': 'lagocachon2020tmr',
        'title': 'Contactless Measurement of Magnetic Nanoparticles on Lateral Flow Strips Using Tunneling Magnetoresistance Sensors',
        'doi': '10.3390/s20143894',
        'url': 'https://www.mdpi.com/1424-8220/20/14/3894/pdf',
        'filename': '[lagocachon2020tmr] - Lago-Cachon et al (2020) - Magnetic Nanoparticles Detection Using TMR Sensors (Sensors).pdf'
    },
    {
        'key': 'ishihara2025swcnt',
        'title': 'Purge-Free Actuator-Driven SWCNT Hydroxylamine Gas Sensor with 50 ppb Sensitivity',
        'doi': '10.3390/nano15130962',
        'url': 'https://www.mdpi.com/2079-4991/15/13/962/pdf',
        'filename': '[ishihara2025swcnt] - Ishihara et al (2025) - SWCNT Hydroxylamine Formaldehyde Gas Sensor (Nanomaterials).pdf'
    }
]

ref_dir = 'referensi'
os.makedirs(ref_dir, exist_ok=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

downloaded = 0
for t in targets:
    out_path = os.path.join(ref_dir, t['filename'])
    if os.path.exists(out_path):
        print(f"[EXISTS] {t['filename']}")
        continue
    
    print(f"\n[DOWNLOADING] {t['title']} ...")
    try:
        req = urllib.request.Request(t['url'], headers=headers)
        with urllib.request.urlopen(req, timeout=20) as resp:
            content = resp.read()
            # Verify it is a valid PDF
            if content.startswith(b'%PDF'):
                with open(out_path, 'wb') as f:
                    f.write(content)
                size_kb = len(content) / 1024
                print(f" -> SUCCESS! Saved {t['filename']} ({size_kb:.1f} KB)")
                downloaded += 1
            else:
                print(f" -> FAILED: Response is not a PDF (starts with {content[:30]})")
    except Exception as e:
        print(f" -> ERROR downloading {t['doi']}: {e}")

print(f"\nTotal new verified OA papers downloaded: {downloaded}")
