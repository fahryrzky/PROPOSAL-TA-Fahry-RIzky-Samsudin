import urllib.request, ssl, pypdf, io, os, sys

ctx = ssl._create_unverified_context()
writer = pypdf.PdfWriter()

out_path = os.path.abspath(r"referensi/[Jung2002] - Walter G Jung (2002) - Op Amp Applications (Analog Devices).pdf")
print("Target path:", out_path)
sys.stdout.flush()

for s in range(1, 9):
    url = f"https://www.analog.com/media/en/training-seminars/design-handbooks/Op-Amp-Applications/Section{s}.pdf"
    print(f"Downloading section {s}...")
    sys.stdout.flush()
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=60) as r:
            data = r.read()
            print(f"Section {s} fetched: {len(data)} bytes")
            sys.stdout.flush()
            reader = pypdf.PdfReader(io.BytesIO(data))
            writer.append(reader)
    except Exception as e:
        print(f"Section {s} error: {e}")
        sys.stdout.flush()

print("Writing merged PDF...")
sys.stdout.flush()
with open(out_path, "wb") as f:
    writer.write(f)

print(f"DONE! File size: {os.path.getsize(out_path)} bytes")
sys.stdout.flush()
