# Rencana Optimasi Dek Slide Presentasi Seminar Proposal Tugas Akhir (Bebas AI-Slop)

> **Untuk Pekerja Agen / Pengembang:** KETERAMPILAN WAJIB: Gunakan `academic-slides`, `antislop`, dan `ppt-master` dalam mengeksekusi rencana tugas demi tugas. Status langkah dilacak menggunakan kotak centang (`- [ ]`).

**Tujuan:** Merombak total dek slide presentasi seminar proposal Tugas Akhir Fahry Rizky Samsudin menjadi 20 slide yang sangat padat, minimalis, dan elegan; menyelaraskan struktur 1-ke-1 dengan presentasi akademik acuan `1227030017_skripsi.pdf` (Gilang Pratama); mengelompokkan Dasar Teori menjadi 2 hingga 4 konsep per slide dengan persamaan LaTeX 300 DPI dan teks kunci yang menonjol; menyajikan flowchart murni 2 diagram per slide tanpa teks pengganggu; menyusun Latar Belakang infografis panah melengkung dengan sitasi nama; serta menetapkan urutan akhir: Daftar Pustaka $\to$ Lampiran $\to$ Penutup.

**Arsitektur & Pendekatan:**
1. Generator PPTX berbasis `python-pptx` modular (`scripts/generate_proposal_presentation.py`) yang menghasilkan `Proposal_TA_Fahry_Rizky_Samsudin.pptx`.
2. Generator diagram alir infografis Latar Belakang resolusi tinggi (`scripts/generate_latar_belakang_flowchart.py`) yang mereproduksi alur panah melengkung bernuansa akademik dengan sitasi nama & tahun.
3. Generator preview interaktif berbasis HTML/CSS/JS (`scripts/generate_html_preview.py` $\to$ `presentation_preview.html`) untuk inspeksi visual instan di peramban sebelum finalisasi.
4. Laporan proposal LaTeX (`skripsi.tex`) telah disinkronisasi dan diverifikasi dengan gambar geometri Kumparan Helmholtz (`babII_Two-coils-of-WPT-system.png`), lulus kompilasi 4-tahap tanpa galat (0 error).

**Tech Stack:** Python 3.13, `python-pptx`, `Pillow`, `matplotlib`, `pypdfium2`, LaTeX (`pdflatex`, `bibtex`), HTML5/CSS3.

**Dokumen Spesifikasi & Rujukan:**
- Referensi Acuan Sidang: `1227030017_skripsi.pdf` (Gilang Pratama Putra Siswanto, UIN SGD Bandung)
- Naskah Bab I Proposal: `Isi/Pendahuluan.tex`
- Naskah Bab II Proposal: `Isi/Tinjauan Pustaka.tex`
- Naskah Bab III Proposal: `Isi/Metode Penelitian.tex`
- Panduan Desain Anti-Slop: `SKILL.md` (academic-slides & antislop)

---

## Batasan Global (Global Constraints)
1. **Bebas Em Dash (`—`)**: Karakter strip panjang dilarang keras pada seluruh naskah dan slide UI (Gunakan titik dua `:`, kurung `()`, atau tanda koma `,`).
2. **Sitasi Nama Pengarang**: Sitasi pada slide harus berformat nama dan tahun (misal: `Julliere, 1975`, `Zhu et al., 2023`, `Havlíček et al., 2019`), bukan format numerik kurung siku `[1]`, `[2]`.
3. **Persamaan Matematika LaTeX 300 DPI**: Seluruh formula matematika ditampilkan menggunakan citra ter-render transparan beresolusi 300 DPI dari `output/equations/*.png`.
4. **Flowchart 2 per Slide**: Slide perancangan perangkat lunak dan pemodelan machine learning hanya memuat 2 diagram alir berdampingan, tanpa paragraf teks tambahan.
5. **Urutan Bagian Akhir**: Slide Daftar Pustaka ditempatkan SEBELUM Lampiran Penelitian.
6. **Sumber Rumusan, Batasan, Tujuan, Manfaat**: Harus persis berakar dari berkas `Isi/Pendahuluan.tex` yang dipanggil di `skripsi.tex`.

---

## Struktur 20 Slide Hasil Optimasi

| No. Slide | Judul & Kategori | Format Layout & Elemen Kunci |
|---|---|---|
| **01** | **Cover Identitas Sidang** | Format Gilang: Judul atas, Logo UIN tengah, Nama & NIM tengah, Pembimbing I kiri bawah, Pembimbing II kanan bawah. |
| **02** | **Latar Belakang Penelitian** | Infografis alur panah melengkung: Masalah Formalin $\to$ Limitasi Uji $\to$ Reseptor Nanofiber $\to$ Sensor TMR $\to$ Rantai Sinyal $\to$ Gap Research SVM vs QSVC (sitasi nama). |
| **03** | **Rumusan & Batasan Masalah** | 2 Kolom berdampingan: Kiri 5 Rumusan Masalah, Kanan 6 Batasan Masalah (murni dari `Isi/Pendahuluan.tex`). |
| **04** | **Tujuan & Manfaat Penelitian** | 2 Kolom berdampingan: Kiri 5 Tujuan Penelitian, Kanan 4 Manfaat Penelitian (murni dari `Isi/Pendahuluan.tex`). |
| **05** | **Metode Pengumpulan Data** | 4 Pilar terstruktur: Studi Literatur, Observasi Prototipe, Eksperimen Laboratorium, Pemodelan Cerdas. |
| **06** | **Dasar Teori 1: Sensor TMR & Kumparan Helmholtz** | **2 Konsep (Fisika Magnetik)**: Kiri TMR & Model Julliere (rumus Julliere & Vout, diagram MTJ); Kanan Kumparan Helmholtz (rumus B(0), geometri 2 kumparan). |
| **07** | **Dasar Teori 2: Rantai Sinyal & Instrumentasi** | **4 Konsep (Elektronika & Fabrikasi)**: Kiri Atas AD623 (rumus gain & Vref 2.50V); Kiri Bawah RC LPF (rumus fc); Kanan Atas ADS1115 (LSB 0.1875 mV); Kanan Bawah Elektrospinning (diagram alat, 15 kV, 0.5 mL/h). |
| **08** | **Dasar Teori 3: Material Nanokomposit & Reseptor ADH** | **4 Konsep (Kimia & Nanomaterial)**: Kiri Atas Formalin & Reaksi Hidrazon ADH (persamaan reaksi C=N); Kiri Bawah Nanopartikel Fe3O4 Kelor; Kanan Atas PVA & Sitrat 130°C; Kanan Bawah Reseptor Nanofiber (perturbasi momen magnetik). |
| **09** | **Dasar Teori 4: Pemodelan Machine Learning SVM vs QSVC** | **2 Konsep (Komparasi Model)**: Kiri SVM Klasik (optimasi margin, kernel RBF Gauss); Kanan QSVC Kuantum (sirkuit ZZFeatureMap, ruang Hilbert 2^n, fidelitas kernel). |
| **10** | **Komparasi Model Klasik vs Kuantum & Software** | Tabel Komparasi 5 Parameter SVM vs QSVC + Peran Arduino IDE & Python 3.x. |
| **11** | **Metodologi: Waktu, Lokasi, Spesifikasi Alat & Bahan** | Banner Pelaksanaan 4 Bulan di Bolabot + Tabel Spesifikasi Perangkat Keras & Bahan Kimia. |
| **12** | **Metodologi: Diagram Alir Penelitian Komprehensif** | 6 Tahapan Metodologi Riset + Diagram Alir Menyeluruh (`BABIII_DiagramAlirPenelitian.drawio.png`). |
| **13** | **Metodologi: Desain Hardware Terpadu & Skematik Sirkuit** | Skematik Grounding Bintang (`babIII_skematik_TMR_grounding_fix.png`) + Render CAD 3D (`babIII_Desainnnn.png`). |
| **14** | **Metodologi: Diagram Alir Perangkat Lunak** | **MURNI 2 FLOWCHART (TANPA TEKS LAIN)**: Kiri Diagram Alir Arduino (`babIII_AlurSoftwareArduino.drawio.png`), Kanan Diagram Alir GUI Python (`babIII_DiagramAlirPython.drawio.png`). |
| **15** | **Metodologi: Sintesis Nanofiber & Parameter Elektrospinning** | Kiri Diagram Alir Sintesis (`babIII_DiagramAlirSintesis.drawio.png`), Kanan Parameter Optimal Lab (tegangan 15 kV, laju 0.5 mL/jam, curing 130°C). |
| **16** | **Metodologi: Kalibrasi Helmholtz & Karakterisasi Sensor TMR** | Prosedur Kalibrasi Medan Helmholtz (sapuan 0-16 V, teslameter) + Kurva Karakteristik Sensitivitas dV/dB Sensor TMR. |
| **17** | **Metodologi: Preparasi Sampel Bakso & 5 Fitur Sinyal** | Ekstraksi Supernatan (sentrifugasi 4000 rpm 10 menit) + Formula LaTeX 5 Fitur Dinamis + Tabel Fitur ($dV_{max}, t_{resp}, (dV/dt)_0, V_{steady}, \text{AUC}$). |
| **18** | **Metodologi: Diagram Alir Pemodelan Machine Learning** | **MURNI 2 FLOWCHART (TANPA TEKS LAIN)**: Kiri Pelatihan Model Building SVM vs QSVC (`babIII_ModelBuilding.drawio.png`), Kanan Deployment Sistem Tertanam (`babIII_ModelDeploy.drawio.png`). |
| **19** | **Jadwal Pelaksanaan Riset 4 Bulan & Target Luaran** | Tabel Gantt Chart 4 Bulan (Sep-Des 2026) + Target Publikasi Scopus/SINTA & Prototipe Alat. |
| **20** | **Daftar Pustaka (References)** | Format nama pengarang & tahun alfabetis (Antarnusa, Ardiyanti, Havlíček, Julliere, NVE, Türkoğlu, Xue, Zhu). Ditempatkan SEBELUM Lampiran. |
| **21** | **Lampiran Penelitian (Appendix)** | Foto fisik casing mekatronika (`lampiran_Casing.jpg`), interior sirkuit sensor & kumparan Helmholtz (`babIII_desaindalam.jpg`), dan layar penampil LCD. |
| **22** | **Slide Penutup & Sesi Diskusi** | Ucapan apresiasi kepada penguji/pembimbing dan pembukaan sesi tanya jawab. |

---

## Rincian Tugas Pelaksanaan (Actionable Tasks)

### Task 1: Regenerasi Diagram Alir Grafis Latar Belakang dengan Alur Melengkung & Sitasi Nama
- File: `scripts/generate_latar_belakang_flowchart.py`
- Output: `output/diagrams/latar_belakang_flowchart.png`
- Aksi:
  - Bangun diagram infografis 6 blok dengan panah melengkung (*curved arrows*) ala Slide 2 Gilang Pratama.
  - Setiap blok menyertakan nama pengarang dan tahun sitasi: (BPOM, 2023; IARC, 2018), (Cai et al., 2021), (Türkoğlu et al., 2024), (Julliere, 1975; NVE Corp, 2021), (Green et al., 2019), (Havlíček et al., 2019).
  - Teks ringkas, visual tajam, resolusi tinggi (300 DPI).

### Task 2: Modifikasi Generator PPTX (`scripts/generate_proposal_presentation.py`) Menjadi 22 Slide Padat
- File: `scripts/generate_proposal_presentation.py`
- Output: `Proposal_TA_Fahry_Rizky_Samsudin.pptx`
- Aksi:
  - Slide 1: Pertahankan cover identitas formal Gilang Pratama.
  - Slide 2: Sematkan diagram latar belakang baru dengan alur melengkung.
  - Slide 3: Rumusan Masalah (5) & Batasan Masalah (6) dari `Isi/Pendahuluan.tex`.
  - Slide 4: Tujuan Penelitian (5) & Manfaat Penelitian (4) dari `Isi/Pendahuluan.tex`.
  - Slide 5: Metode Pengumpulan Data (4 pilar).
  - Slide 6 (DT 1 - 2 Konsep): TMR & Helmholtz (Persamaan Julliere, Biot-Savart, MTJ diagram, Geometri kumparan Helmholtz).
  - Slide 7 (DT 2 - 4 Konsep): In-Amp AD623, RC LPF, ADS1115, Elektrospinning (Persamaan gain, fc, LSB, skema pemintalan).
  - Slide 8 (DT 3 - 4 Konsep): Formalin & ADH, Fe3O4 Kelor, PVA & Sitrat 130°C, Reseptor Nanofiber (Persamaan reaksi hidrazon, sitasi nama).
  - Slide 9 (DT 4 - 2 Konsep): SVM Klasik vs QSVC Kuantum (Persamaan optimasi margin, sirkuit kuantum ZZFeatureMap).
  - Slide 10: Tabel Komparasi SVM vs QSVC + Arduino IDE & Python.
  - Slide 11: Metodologi Waktu, Lokasi, Tabel Alat & Bahan.
  - Slide 12: Diagram Alir Penelitian Komprehensif.
  - Slide 13: Desain Hardware Terpadu & Skematik Sirkuit.
  - Slide 14: **MURNI 2 FLOWCHART (Perangkat Lunak)**: Diagram alir Arduino & Python GUI berdampingan tanpa teks penjelas lain.
  - Slide 15: Sintesis Nanofiber & Parameter Elektrospinning.
  - Slide 16: Kalibrasi Helmholtz & Karakterisasi Sensor TMR.
  - Slide 17: Preparasi Sampel Bakso & 5 Fitur Sinyal Dinamis.
  - Slide 18: **MURNI 2 FLOWCHART (Machine Learning)**: Model building & Model deploy berdampingan tanpa teks penjelas lain.
  - Slide 19: Rencana Jadwal Riset 4 Bulan & Target Luaran.
  - Slide 20: **Daftar Pustaka (References)**: Gaya sitasi APA berurutan nama alfabetis (ditaruh SEBELUM Lampiran).
  - Slide 21: **Lampiran Penelitian (Appendix)**: Foto fisik casing, interior alat, LCD penampil.
  - Slide 22: Slide Penutup & Sesi Diskusi.

### Task 3: Sinkronisasi Preview Interaktif HTML (`presentation_preview.html`)
- File: `scripts/generate_html_preview.py`
- Output: `presentation_preview.html`
- Aksi:
  - Sinkronkan seluruh 22 slide baru ke dalam format HTML 16:9 (1280x720).
  - Pastikan formula LaTeX rendered dan diagram alir termuat sempurna.
  - Sediakan kontrol navigasi keyboard (panah kiri/kanan, fullscreen).

### Task 4: Verifikasi Laporan LaTeX Proposal (`skripsi.tex`)
- File: `Isi/Tinjauan Pustaka.tex`, `Isi/Metode Penelitian.tex`, `skripsi.tex`
- Output: `skripsi.pdf` dan `Proposal Fahry Rizky Samsudin.pdf`
- Aksi:
  - Pastikan citra Kumparan Helmholtz (`babII_Two-coils-of-WPT-system.png`) tampil rapi pada Bab II dan terujuk pada Bab III.
  - Jalankan script `python scripts/build_proposal.py` untuk mengonfirmasi kompilasi 4-tahap tetap 0 error.

### Task 5: Audit Anti-Slop & Quality Gate
- Cek ketiadaan karakter em dash (`—`).
- Cek kontras warna teks terhadap latar (WCAG AA/AAA).
- Cek seluruh teks terbaca jelas dan tidak ada font ukuran kecil yang sulit dibaca.
- Pastikan tidak ada tombol mati, card repetitif generik, atau placeholder tanpa arti.
