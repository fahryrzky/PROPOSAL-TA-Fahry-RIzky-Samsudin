import json
import os

with open('scripts/active_references.json', 'r', encoding='utf-8') as f:
    refs = json.load(f)

downloaded_files = os.listdir('referensi')
pdf_map = {}
for f in downloaded_files:
    if f.endswith('.pdf') and f.startswith('['):
        key = f.split(']')[0].replace('[', '')
        pdf_map[key] = f

catalog = []
for k, v in refs.items():
    entry = dict(v)
    if k in pdf_map:
        entry['status'] = 'Downloaded'
        entry['filename'] = pdf_map[k]
        entry['filepath'] = os.path.join('referensi', pdf_map[k])
        entry['size_kb'] = os.path.getsize(os.path.join('referensi', pdf_map[k])) // 1024
    else:
        entry['status'] = 'External / Paywall / Physical'
        entry['filename'] = None
        entry['filepath'] = None
        entry['size_kb'] = None
    catalog.append(entry)

with open('referensi/catalog.json', 'w', encoding='utf-8') as f:
    json.dump(catalog, f, indent=2, ensure_ascii=False)

# Now generate Markdown README
md = []
md.append("# Katalog Referensi Proposal Tugas Akhir")
md.append("\n**Peneliti**: Fahry Rizky Samsudin (NIM: 1237030018)")
md.append("**Judul**: *Rancang Bangun Instrumentasi Sensor Tunneling Magnetoresistance Berbasis Nanofiber $\\text{Fe}_3\\text{O}_4$/PVA-Sitrat-ADH untuk Deteksi Formalin pada Bakso Menggunakan Komparasi Model SVM dan QSVC*")
md.append(f"\nFolder ini memuat seluruh berkas naskah PDF referensi dan indeks digital untuk 53 pustaka yang disitir dalam naskah proposal skripsi.\n")

md.append("## Ringkasan Koleksi")
downloaded_count = len(pdf_map)
total_count = len(refs)
md.append(f"- **Total Pustaka Disitir**: {total_count}")
md.append(f"- **Berkas PDF Tersedia Lokal**: {downloaded_count} berkas")
md.append(f"- **Pustaka Berbayar / Buku Fisik / Repositori Kampus**: {total_count - downloaded_count} pustaka\n")

md.append("---")
md.append("## 1. Berkas PDF Tersedia di Folder `referensi/`\n")
md.append("| No | Kunci BibTeX | Judul Referensi | Tipe / Sumber | Ukuran | Nama Berkas |")
md.append("|---|---|---|---|---|---|")

idx = 1
for entry in catalog:
    if entry['status'] == 'Downloaded':
        title = entry.get('title', '').replace('\n', ' ')
        author = entry.get('author', '').split(' and ')[0]
        year = entry.get('year', '')
        size = f"{entry['size_kb']} KB"
        fn = entry['filename']
        key = entry['key']
        md.append(f"| {idx} | `{key}` | **{title}**<br>_{author} ({year})_ | {entry.get('type', '')} | {size} | [{fn}](file:///c:/Users/Fahry%20Rizky%20S/Documents/Tugas%20Akhir%20Fahry/Proposal/referensi/{fn.replace(' ', '%20')}) |")
        idx += 1

md.append("\n---")
md.append("## 2. Referensi Penerbit Berbayar, Repositori Kampus & Buku Fisik\n")
md.append("Referensi berikut merupakan artikel berbayar (Elsevier, Wiley, ACS), buku teks cetak ber-ISBN, atau tugas akhir fisik yang dapat diakses melalui jaringan perpustakaan kampus / langganan jurnal UIN SGD Bandung:\n")
md.append("| No | Kunci BibTeX | Judul Referensi | Penulis & Tahun | Penerbit / Jurnal | Tautan / Akses |")
md.append("|---|---|---|---|---|---|")

idx_ext = 1
for entry in catalog:
    if entry['status'] != 'Downloaded':
        title = entry.get('title', '').replace('\n', ' ')
        author = entry.get('author', '').split(' and ')[0]
        year = entry.get('year', '')
        journal = entry.get('journal') or entry.get('publisher') or '-'
        doi = entry.get('doi', '')
        url = entry.get('url', '')
        key = entry.get('key', '')
        
        link = '-'
        if doi:
            link = f"[DOI: {doi}](https://doi.org/{doi})"
        elif url:
            link = f"[URL]({url})"
            
        md.append(f"| {idx_ext} | `{key}` | **{title}** | {author} ({year}) | {journal} | {link} |")
        idx_ext += 1

md.append("\n---\n*Katalog disusun dan disinkronkan secara otomatis berdasarkan berkas `daftar_pustaka.bib` proposal skripsi.*")

with open('referensi/README.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(md))

print(f"Catalog generated successfully! {downloaded_count}/{total_count} downloaded.")
