import os, sys, pypdf, io, time
from curl_cffi import requests

sys.stdout.reconfigure(encoding='utf-8')

out_path = r"referensi/[Jung2002] - Walter G Jung (2002) - Op Amp Applications (Analog Devices).pdf"
writer = pypdf.PdfWriter()

print("=== FETCHING AND ASSEMBLING WALTER JUNG OP AMP APPLICATIONS ===")
# Sections: Section1, Section2, Section3, Section4, Section6, Section7
# (Section 5 was reorganized by ADI into individual app notes)
sections = [1, 2, 3, 4, 6, 7]
total_pages = 0

for s in sections:
    url = f"https://www.analog.com/media/en/training-seminars/design-handbooks/Op-Amp-Applications/Section{s}.pdf"
    print(f"Fetching Section {s}...")
    for attempt in range(3):
        try:
            r = requests.get(url, impersonate='chrome120', timeout=45, verify=False)
            if r.content.startswith(b'%PDF'):
                reader = pypdf.PdfReader(io.BytesIO(r.content))
                num_p = len(reader.pages)
                print(f"  Section {s} fetched: {len(r.content)} bytes, {num_p} pages")
                for page in reader.pages:
                    writer.add_page(page)
                total_pages += num_p
                break
            else:
                print(f"  Section {s} attempt {attempt+1} did not return PDF")
        except Exception as e:
            print(f"  Section {s} attempt {attempt+1} error: {e}")
        time.sleep(1)

if total_pages > 0:
    with open(out_path, 'wb') as f:
        writer.write(f)
    print(f"\nSUCCESS! Assembled Walter Jung Handbook: {total_pages} pages ({os.path.getsize(out_path)} bytes)")
else:
    print("Failed to assemble Jung book.")
