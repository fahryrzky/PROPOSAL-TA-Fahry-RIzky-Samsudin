import pypdf, re, os, glob, sys
sys.stdout.reconfigure(encoding='utf-8')

file_dir = 'File'
pdf_files = [
    'Literature Review TMR_Fahry_Rizky_S_1237030018.pdf',
    'Sensor_Formaldehida_pada_Bakso_Nanofiber__FeO__TMR__Riset_Komprehensif_Seleksi_Reseptor_Research_Gap__Redesign.pdf',
    'sensor_TMR_formalin_bakso_GABUNGAN.md.pdf',
    'TA_Sensor_Formaldehida_pada_Bakso__Nanofiber_FeOPVA-GA__Recognition_Material__TMR_ALT023-10E_Literature_Review_Receptor_Selection_Research_Gap__Integrated_Design.pdf'
]

print('=== SCANNING PDFs in File/ ===')
all_urls = set()
all_dois = set()

for f in pdf_files:
    path = os.path.join(file_dir, f)
    if not os.path.exists(path):
        print(f"File not found: {path}")
        continue
    reader = pypdf.PdfReader(path)
    full_text = ""
    for page in reader.pages:
        t = page.extract_text() or ""
        full_text += "\n" + t
    
    urls = set(re.findall(r'https?://[^\s)\]\"\'<>]+', full_text))
    dois = set(re.findall(r'10\.\d{4,9}/[^\s)\]\"\'<>]+', full_text))
    all_urls.update(urls)
    all_dois.update(dois)
    print(f"{f}: {len(reader.pages)} pages, {len(urls)} URLs, {len(dois)} DOIs")

html_files = glob.glob("File/*.html")
print('\n=== SCANNING HTMLs in File/ ===')
for h in html_files:
    with open(h, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    urls = set(re.findall(r'https?://[^\s)\]\"\'<>]+', content))
    dois = set(re.findall(r'10\.\d{4,9}/[^\s)\]\"\'<>]+', content))
    all_urls.update(urls)
    all_dois.update(dois)
    print(f"{os.path.basename(h)}: {len(content)} chars, {len(urls)} URLs, {len(dois)} DOIs")

print(f"\nTOTAL UNIQUE URLs in File/: {len(all_urls)}")
print(f"TOTAL UNIQUE DOIs in File/: {len(all_dois)}")

out_dir = os.path.abspath("data")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "all_urls_from_files.txt"), "w", encoding="utf-8") as f:
    for u in sorted(all_urls):
        f.write(u + "\n")

with open(os.path.join(out_dir, "all_dois_from_files.txt"), "w", encoding="utf-8") as f:
    for d in sorted(all_dois):
        f.write(d + "\n")

print("Saved to", out_dir)
