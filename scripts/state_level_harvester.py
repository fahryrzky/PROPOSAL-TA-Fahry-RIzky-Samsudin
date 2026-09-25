import os, sys, time, pypdf, io
from curl_cffi import requests
sys.stdout.reconfigure(encoding='utf-8')

out_dir = 'referensi'

# 1. Download MDPI Papers
mdpi_targets = {
    'Turkoglu2024': {
        'url': 'https://www.mdpi.com/1422-0067/25/3/1668/pdf',
        'file': '[Turkoglu2024] - Turkoglu et al (2024) - PVA-Based Electrospun Materials A Review (IJMS).pdf'
    },
    'gaaz2015properties': {
        'url': 'https://www.mdpi.com/1420-3049/20/12/19884/pdf',
        'file': '[gaaz2015properties] - Gaaz et al (2015) - Properties and applications of polyvinyl alcohol nanocomposites (Molecules).pdf'
    },
    'liu2024review': {
        'url': 'https://www.mdpi.com/2313-0105/10/8/271/pdf',
        'file': '[liu2024review] - Liu et al (2024) - Review of Energy Storage Capacitor Technology (Batteries).pdf'
    },
    'ginisa2015': {
        'url': 'https://media.neliti.com/media/publications/188280-ID-desain-pembuatan-dan-uji-coba-kumparan-h.pdf',
        'file': '[ginisa2015] - Ginisa et al (2015) - Desain Pembuatan dan Uji Coba Kumparan Helmholtz.pdf'
    }
}

print("=== DOWNLOADING OPEN ACCESS PAPERS VIA CHROME IMPERSONATION ===")
for key, item in mdpi_targets.items():
    dest = os.path.join(out_dir, item['file'])
    if os.path.exists(dest) and os.path.getsize(dest) > 10000:
        print(f"[{key}] Already exists ({os.path.getsize(dest)} bytes)")
        continue
    print(f"[{key}] Fetching {item['url']} ...")
    try:
        r = requests.get(item['url'], impersonate='chrome120', timeout=30, verify=False)
        print(f"  Status: {r.status_code}, Size: {len(r.content)}")
        if r.content.startswith(b'%PDF'):
            with open(dest, 'wb') as f:
                f.write(r.content)
            print(f"  SUCCESS! Saved to {item['file']}")
        else:
            print(f"  FAILED: Not a PDF (header: {r.content[:20]})")
    except Exception as e:
        print(f"  Error: {e}")
    time.sleep(1)


# 2. Download and assemble complete Walter Jung book (8 sections)
jung_file = os.path.join(out_dir, "[Jung2002] - Walter G Jung (2002) - Op Amp Applications (Analog Devices).pdf")
if not os.path.exists(jung_file) or os.path.getsize(jung_file) < 500000:
    print("\n=== DOWNLOADING WALTER JUNG OP AMP APPLICATIONS (8 SECTIONS) ===")
    writer = pypdf.PdfWriter()
    jung_success = True
    for s in range(1, 9):
        sec_url = f"https://www.analog.com/media/en/training-seminars/design-handbooks/Op-Amp-Applications/Section{s}.pdf"
        print(f"Fetching Jung Section {s} ...")
        try:
            r = requests.get(sec_url, impersonate='chrome120', timeout=40, verify=False)
            if r.content.startswith(b'%PDF'):
                print(f"  Section {s} fetched: {len(r.content)} bytes")
                reader = pypdf.PdfReader(io.BytesIO(r.content))
                for page in reader.pages:
                    writer.add_page(page)
            else:
                print(f"  Section {s} failed (not PDF)")
                jung_success = False
        except Exception as e:
            print(f"  Section {s} error: {e}")
            jung_success = False
        time.sleep(1)
        
    if jung_success and len(writer.pages) > 0:
        with open(jung_file, 'wb') as f:
            writer.write(f)
        print(f"SUCCESS! Saved complete Jung book ({os.path.getsize(jung_file)} bytes, {len(writer.pages)} pages)")
else:
    print(f"[Jung2002] Already exists ({os.path.getsize(jung_file)} bytes)")

print("\n=== BATCH HARVEST FINISHED ===")
