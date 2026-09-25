import pypdf, glob, os

files = glob.glob('File/*.pdf')
for f in files:
    print('='*60)
    print(f, f"({os.path.getsize(f)} bytes)")
    try:
        reader = pypdf.PdfReader(f)
        print(f"Num pages: {len(reader.pages)}")
        # Print first page summary
        first_page = reader.pages[0].extract_text()
        print("Page 1 preview:")
        print(first_page[:300])
    except Exception as e:
        print(f"Error: {e}")
