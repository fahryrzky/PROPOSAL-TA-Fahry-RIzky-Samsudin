import urllib.request, ssl, pypdf, io, os, sys, time
sys.stdout.reconfigure(encoding='utf-8')

ctx = ssl._create_unverified_context()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

temp_dir = 'temp_jung'
os.makedirs(temp_dir, exist_ok=True)
section_files = []

print("=== DOWNLOADING WALTER JUNG OP AMP APPLICATIONS (8 SECTIONS) ===")
for s in range(1, 9):
    url = f"https://www.analog.com/media/en/training-seminars/design-handbooks/Op-Amp-Applications/Section{s}.pdf"
    sec_file = os.path.join(temp_dir, f"Section{s}.pdf")
    
    if os.path.exists(sec_file) and os.path.getsize(sec_file) > 100000:
        print(f"Section {s} already cached ({os.path.getsize(sec_file)} bytes)")
        section_files.append(sec_file)
        continue
        
    print(f"Downloading Section {s} in 64KB chunks...")
    req = urllib.request.Request(url, headers=headers)
    
    success = False
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, context=ctx, timeout=60) as r:
                with open(sec_file, 'wb') as f:
                    while True:
                        chunk = r.read(65536)
                        if not chunk: break
                        f.write(chunk)
            size = os.path.getsize(sec_file)
            print(f"Section {s} downloaded successfully ({size} bytes)")
            section_files.append(sec_file)
            success = True
            break
        except Exception as e:
            print(f"  Section {s} attempt {attempt+1} failed: {e}")
            time.sleep(2)
            
    if not success:
        print(f"Failed to download Section {s}")

print("\n=== MERGING ALL SECTIONS INTO MASTER PDF ===")
writer = pypdf.PdfWriter()
for sf in section_files:
    print(f"Appending {sf}...")
    reader = pypdf.PdfReader(sf)
    for page in reader.pages:
        writer.add_page(page)

out_path = r"referensi/[Jung2002] - Walter G Jung (2002) - Op Amp Applications (Analog Devices).pdf"
with open(out_path, 'wb') as f:
    writer.write(f)

print(f"\nSUCCESSFULLY ASSEMBLED COMPLETE JUNG BOOK!")
print(f"Path: {out_path} ({os.path.getsize(out_path)} bytes, {len(writer.pages)} pages)")

# Cleanup temp files
for sf in section_files:
    try: os.remove(sf)
    except: pass
try: os.rmdir(temp_dir)
except: pass
