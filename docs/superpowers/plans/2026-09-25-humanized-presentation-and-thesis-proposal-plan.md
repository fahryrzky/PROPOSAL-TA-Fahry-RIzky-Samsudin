# Rencana Induk Implementasi: Humanisasi Naskah Proposal Skripsi, Standardisasi EYD V, Diagram Alir Bab III, Subbab Penelitian Terdahulu, dan Rekonstruksi Slide Presentasi Anti-Slop (22 Slide)

> **Dokumen Rencana Terpadu (Homogen & Komprehensif)**
> Menggabungkan dan menyelaraskan seluruh rencana kerja naskah proposal skripsi (LaTeX) dan presentasi sidang proposal (PPTX), mencakup integrasi 4 Rumusan Masalah, Subbab 2.3 Penelitian Terdahulu, diagram alir sintesis & QML, audit humanisasi paragraf anti-AI slop, perbaikan ejaan EYD V, eliminasi konjungsi "Untuk" di awal paragraf, pengelolaan folder referensi, dan kalibrasi tipografi skala besar proyektor.

---

## 1. Ringkasan Tujuan Proyek

1. **Penyelarasan Struktur Masalah & Tujuan (4 Butir)**:
   - Menggabungkan RM 1 dan RM 2 pada naskah LaTeX ([Isi/Pendahuluan.tex](file:///c:/Users/Fahry%20Rizky%20S/Documents/Tugas%20Akhir%20Fahry/Proposal/Isi/Pendahuluan.tex)) dan slide presentasi ([Proposal_TA_Fahry_Rizky_Samsudin.pptx](file:///c:/Users/Fahry%20Rizky%20S/Documents/Tugas%20Akhir%20Fahry/Proposal/Proposal_TA_Fahry_Rizky_Samsudin.pptx)) menjadi tepat 4 Rumusan Masalah dan 4 Tujuan Penelitian yang proporsional.
2. **Humanisasi Paragraf, Pembasmian AI Slop & Larangan Kata "Untuk" di Awal Paragraf**:
   - Menghilangkan frasa pembuka klise AI, klaim hiperbolis/bombastis ("lompatan teknologi", "sensitivitas superior"), dan tanda pisah em-dash (`---`).
   - Memecah kalimat majemuk bertingkat yang menumpuk (>50 kata) menjadi 2–3 kalimat ilmiah efektif.
   - **Koreksi Larangan Kata "Untuk"**: Memperbaiki kalimat pembuka paragraf atau kalimat pengantar yang diawali kata "Untuk" (karena berkedudukan sebagai preposisi/konjungsi subordinatif tujuan, bukan subjek) menjadi struktur kalimat baku dengan subjek aktif/pasif yang jelas.
3. **Subbab 2.3 "Penelitian Terdahulu" di Bab II**:
   - Menambahkan Subbab 2.3 di akhir [Isi/Tinjauan Pustaka.tex](file:///c:/Users/Fahry%20Rizky%20S/Documents/Tugas%20Akhir%20Fahry/Proposal/Isi/Tinjauan%20Pustaka.tex), memuat tabel matriks komparasi 5 penelitian (Wang et al. 2021, Singhal et al. 2024, Sun et al. 2023, Gilang Pratama 2026, dan penelitian ini) serta analisis kebaruan riset (*research gap*).
4. **Desain Diagram Alir Metodologi Bab III**:
   - Merancang diagram alir terstruktur untuk Sintesis Sampel Uji (`babIII_DiagramAlirSintesis.drawio.png`) dan mengintegrasikannya ke Subbab 3.4.
   - Memodifikasi diagram alir pemodelan cerdas (`babIIIModelBuilding.drawio.png`) agar merefleksikan komparasi paralel SVM klasik versus QSVC kuantum, lalu mengintegrasikannya ke Subbab 3.3.
5. **Standardisasi Ejaan EYD V / KBBI VI & Penulisan Formula Kimia**:
   - Menertibkan kata non-baku (`kelembaban` $\rightarrow$ `kelembapan`, `linier` $\rightarrow$ `linear`, `respon` $\rightarrow$ `respons`, `standarisasi` $\rightarrow$ `standardisasi`, `insulator` $\rightarrow$ `isolator`, dll.).
   - Memperbaiki penggunaan kata penghubung intrakalimat ("namun") dan penghubung relasional ("di mana").
   - Mengubah notasi matematika kimia seperti `$Fe_3O_4$` menjadi sintaks mhchem resmi `\ch{Fe3O4}`.
6. **Sinkronisasi Metodologis Hardware & Machine Learning**:
   - Menyelaraskan teks narasi dengan arsitektur riil: akuisisi berbasis durasi waktu (5.0 detik) dengan pembuangan waktu stabilisasi (*settling time* 1.0 detik), serta penegasan fokus utama SVM vs QSVC dengan Random Forest sebagai komparator dasar.
7. **Pengelolaan Pustaka & Repositori Referensi (`referensi/`)**:
   - Memelihara 24 berkas naskah PDF referensi tervalidasi dan katalog digital lengkap ([referensi/catalog.json](file:///c:/Users/Fahry%20Rizky%20S/Documents/Tugas%20Akhir%20Fahry/Proposal/referensi/catalog.json) & [referensi/README.md](file:///c:/Users/Fahry%20Rizky%20S/Documents/Tugas%20Akhir%20Fahry/Proposal/referensi/README.md)) untuk 53 pustaka.
8. **Rekonstruksi Deck Presentasi Sidang Proposal (22 Slide Anti-Slop)**:
   - Rekonstruksi Cover Slide 1 persis format autentik Gilang Pratama (`slide_ref_1.png`): foto lab gelap, logo pill UIN+Fisika, bingkai oranye tebal (`#f97316`), tipografi gagah (19.5 pt), tanpa bento box putih AI.
   - Penambahan Slide 11 Baru "Perbandingan dengan Penelitian Terdahulu & Kebaruan Riset".
   - Kalibrasi skala font besar (Header 24 pt, Judul Kartu 17 pt, Bullet 13.5–14 pt, spasi 1.25) agar terbaca jelas dari jarak jauh oleh dosen penguji di layar proyektor sidang.
   - Pembasmian total seluruh label meta kurung (`(4 Aspek)`), prefix artifisial (`T-1:`, `RM-1:`), dan penutup formal santun.

---

## 2. Arsitektur Komponen & Keterkaitan Berkas

```
Proposal/
├── Isi/
│   ├── Pendahuluan.tex         <-- Task 1 (4 RM & 4 Tujuan) & Task 2 (Humanisasi, anti-slop, larangan "Untuk" diawal)
│   ├── Tinjauan Pustaka.tex    <-- Task 3 (Subbab 2.3 Penelitian Terdahulu + Matriks Komparasi) & Task 6 (EYD V)
│   └── Metode Penelitian.tex   <-- Task 4 & 5 (Integrasi Diagram Alir Sintesis 3.5 & QML 3.8, durasi 5s, \ch{Fe3O4})
├── Gambar/
│   ├── Bab3/
│   │   ├── babIII_DiagramAlirSintesis.drawio.png <-- Diagram alir sintesis sampel (Subbab 3.4)
│   │   └── babIIIModelBuilding.drawio.png        <-- Diagram alir komparasi SVM vs QSVC (Subbab 3.3)
│   ├── Logo/logo_uin_fisika_pill.png             <-- Aset kapsul logo UIN & Fisika untuk Slide 1
│   └── cover_bg_gilang.png                       <-- Latar belakang foto lab gelap beraksen navy
├── referensi/                                    <-- Task 7 (24 PDF referensi terverifikasi, README.md, catalog.json)
├── scripts/
│   ├── generate_cover_assets.py                  <-- Generator komposit latar lab & kapsul logo
│   ├── generate_proposal_presentation.py         <-- Generator deck presentasi 22 slide tipografi besar
│   ├── verify_deck.py                            <-- Skrip verifikasi otomatis struktur presentasi
│   └── build_proposal.py                         <-- Pipeline kompilasi LaTeX 4-tahap bebas sampah
└── skripsi.pdf                                   <-- Proposal Fahry Rizky Samsudin.pdf
```

---

## 3. Matriks Standar Tipografi Presentasi Proyektor

| Elemen Slide | Ukuran Lama (Kecil/Slop) | Ukuran Baru (Besar & Terbaca Jelas) | Keterangan Tata Letak |
|---|---|---|---|
| **Judul Slide Utama (Header)** | 20 pt | **23 – 24 pt** (Bold, Navy) | Tegas di bagian atas |
| **Subjudul Slide (Header Sub)** | 11 pt | **12.5 – 13 pt** (Slate-600) | Menjelaskan konteks slide |
| **Judul Kartu Konten** | 11.5 – 12 pt | **16.5 – 17.5 pt** (Bold, Navy) | Pembeda sub-topik yang kuat |
| **Teks Isi / Bullet (Slide 2 Kolom)** | 9.5 – 10 pt | **13.5 – 14.5 pt** (Regular/Bold) | Mengisi 85–90% tinggi kartu (spasi 1.25) |
| **Teks Isi / Bullet (Slide 3 Kolom)** | 8.5 – 9.0 pt | **11.5 – 12.5 pt** (Regular/Bold) | Pas pada kartu berlebar 3.7 inci |
| **Teks Tabel Komparasi Studi (Slide Baru)** | - | Header: **11.5 pt** (Bold), Isi: **10.5 pt** | Jelas, kontras, matriks 5 baris |
| **Teks Tabel Alat & Bahan (Slide 12)** | 9.5 pt / 9.0 pt | Header: **12 pt** (Bold), Isi: **11 pt** | Baris tabel jelas dan lapang |
| **Daftar Pustaka (Slide 20 & 21)** | 7.5 pt | **8.5 – 9.0 pt** (Kompak & Terbaca) | Memanfaatkan batas kolom penuh |
| **Cover: Judul Skripsi** | 18 pt | **19.5 – 20.5 pt** (All-Caps Bold) | Memenuhi kotak oranye dengan gagah |
| **Cover: Identitas Mahasiswa** | 15 pt / 12 pt | **17 pt** (Nama) / **13.5 pt** (NIM) | Putih bersih di atas latar lab |
| **Cover: Pembimbing & Institusi** | 10 pt | **13 – 14 pt** (Bold, Putih) | Jelas dan berwibawa |

---

## 4. Tahapan Rencana Aksi Terpadu (*Action Plan*)

### FASE A: Naskah Akademik Proposal Skripsi (LaTeX)

#### Task 1: Restrukturisasi Rumusan Masalah & Tujuan Penelitian (4 Butir)
**Berkas:** [Isi/Pendahuluan.tex](file:///c:/Users/Fahry%20Rizky%20S/Documents/Tugas%20Akhir%20Fahry/Proposal/Isi/Pendahuluan.tex)
- [ ] Gabungkan RM poin 1 & 2 menjadi 1 poin terpadu mengenai sensitivitas, LOD, dan karakteristik respons magnetoresistif.
- [ ] Susun 4 butir Rumusan Masalah yang presisi:
  1. Sensitivitas, batas deteksi (LOD), dan pengaruh gugus fungsional hidrazida ADH terhadap respons magnetoresistif sensor TMR.
  2. Karakteristik medan magnetik acuan kumparan Helmholtz dan respons linieritas transduser TMR ALT023-10E.
  3. Desain dan validasi rantai instrumentasi (AD623-ADS1115-Arduino-Raspberry Pi) dalam menghasilkan kurva kalibrasi konsentrasi formalin pada bakso.
  4. Komparasi performa klasifikasi antara model klasik SVM dan model kuantum QSVC pada sampel bakso berformalin.
- [ ] Selaraskan 4 butir Tujuan Penelitian agar berkorespondensi 1-ke-1 secara logis dengan Rumusan Masalah.

#### Task 2: Humanisasi Paragraf Bab I, Eliminasi AI-Tells, dan Larangan Preposisi/Konjungsi "Untuk" di Awal Kalimat Pembuka
**Berkas:** [Isi/Pendahuluan.tex](file:///c:/Users/Fahry%20Rizky%20S/Documents/Tugas%20Akhir%20Fahry/Proposal/Isi/Pendahuluan.tex)
- [ ] **Koreksi Larangan Kata "Untuk" di Awal Paragraf/Kalimat Pengantar**:
  - Perbaiki kalimat pada baris 65 (`\section{Metode Pengumpulan Data}`):
    - *Sebelum:* "Untuk mencapai tujuan dari penelitian, dilaksanakan serangkaian metode pengumpulan data sebagai berikut:"
    - *Sesudah:* "Pencapaian tujuan penelitian ditempuh melalui serangkaian metode pengumpulan data sebagai berikut:"
  - Perbaiki kalimat di dalam paragraf Latar Belakang yang diawali "Untuk":
    - Baris 12: Ganti "Untuk menciptakan selektivitas kimiawi..." menjadi "Penciptaan selektivitas kimiawi terhadap formalin diwujudkan melalui fungsionalisasi..." atau "Guna menciptakan selektivitas kimiawi..."
    - Baris 14: Ganti "Untuk mendeteksi perubahan sinyal medan magnet berskala sangat kecil tersebut, diperlukan..." menjadi "Deteksi pergeseran medan magnetik mikro tersebut menuntut transduser magnetik dengan resolusi tinggi."
    - Baris 16: Ganti "Untuk memastikan validitas dan keterulangan..." menjadi "Kepastian validitas dan keterulangan (\textit{repeatability}) metrologis dijamin melalui kalibrasi awal sistem..."
- [ ] Hilangkan tanda pisah em-dash (`---`) pada baris 12 ("...akurat --- terutama..."), ganti dengan anak kalimat alami berkaidah EYD V.
- [ ] Tulis ulang kalimat bernada bombastis AI pada Paragraf 4 dan 5 ("Sebagai lompatan teknologi...", "Sensitivitas superior ini menjamin...").
- [ ] Pecah kalimat Paragraf 8 yang menumpuk 62 kata menjadi 2–3 kalimat ilmiah efektif dan terstruktur.

#### Task 3: Penambahan Subbab 2.3 "Penelitian Terdahulu" & Matriks Komparasi Riset
**Berkas:** [Isi/Tinjauan Pustaka.tex](file:///c:/Users/Fahry%20Rizky%20S/Documents/Tugas%20Akhir%20Fahry/Proposal/Isi/Tinjauan%20Pustaka.tex)
- [ ] Sisipkan `\section{Penelitian Terdahulu}` di akhir Bab II sebelum transisi ke Bab III.
- [ ] Susun tabel matriks perbandingan komparatif (`Table 2.1`) yang membandingkan:
  1. Wang et al. (2021) — Sensor gas MOS $\mathrm{SnO_2}$
  2. Singhal et al. (2024) — Biosensor elektrokimia enzim FDH
  3. Sun et al. (2023) — Sensor optik kolorimetri digital
  4. Gilang Pratama (2026) — Sensor GMR Nanofiber $\mathrm{Fe_3O_4}$/PVA-GOx + Random Forest
  5. Penelitian Ini (Fahry, 2026) — Sensor TMR ALT023-10E + Nanofiber $\mathrm{Fe_3O_4}$/PVA-Sitrat-ADH + Komparasi SVM vs QSVC
- [ ] Tambahkan ulasan narasi ilmiah mengenai 3 pilar kebaruan riset (*research gap*): reseptor ADH kovalen ramah lingkungan, transduser kuantum TMR >200%, dan paradigma komparasi algoritma klasik SVM vs kuantum QSVC.

#### Task 4: Desain Diagram Alir Metodologi Bab III (Sintesis & QML)
**Berkas:** `Gambar/Bab3/babIII_DiagramAlirSintesis.drawio.png`, `Gambar/Bab3/babIIIModelBuilding.drawio.png`
- [ ] Buat diagram alir sintesis sampel uji `babIII_DiagramAlirSintesis.drawio` mencakup:
  1. Preparasi Sol-Gel Nanokomposit ($\text{Fe}_3\text{O}_4$ + PVA + Asam Sitrat + ADH)
  2. Fabrikasi Nanofiber via Elektrospinning (Tegangan 15 kV, Jarak 15 cm, Laju Alir 0.8 mL/h)
  3. Stabilisasi Termal / *Curing* (Suhu 130 $^\circ\text{C}$, 2 Jam)
  4. Deposisi Lapisan Reseptor pada Permukaan Sensor TMR
  5. Pengujian Daya Lekat & Karakterisasi Awal
- [ ] Ekspor ke PNG transparan resolusi tinggi (300 DPI) di `Gambar/Bab3/babIII_DiagramAlirSintesis.drawio.png`.
- [ ] Perbarui diagram alir `babIIIModelBuilding.drawio.png` dengan skema 2-kolom paralel simetris:
  - Jalur Kiri: Ekstraksi 5 Fitur $\rightarrow$ Normalisasi $\rightarrow$ Model Klasik SVM (Kernel RBF) $\rightarrow$ Metrik Evaluasi
  - Jalur Kanan: Ekstraksi 5 Fitur $\rightarrow$ Penskalaan $\rightarrow$ Quantum Feature Map ($ZZ\text{FeatureMap}$) $\rightarrow$ Quantum Kernel Estimator $\rightarrow$ Model QSVC $\rightarrow$ Metrik Evaluasi

#### Task 5: Integrasi Diagram Alir dan Sinkronisasi Metodologis di `Isi/Metode Penelitian.tex`
**Berkas:** [Isi/Metode Penelitian.tex](file:///c:/Users/Fahry%20Rizky%20S/Documents/Tugas%20Akhir%20Fahry/Proposal/Isi/Metode%20Penelitian.tex)
- [ ] Tambahkan pemanggilan Gambar 3.5 pada Subbab 3.4 (*Tahapan Sintesis Sampel Uji*) lengkap dengan narasi pengantar.
- [ ] Perbarui label dan narasi Gambar 3.8 (*Diagram Alir Pemodelan Cerdas*) agar menerangkan komparasi paralel SVM vs QSVC.
- [ ] Sinkronkan spesifikasi sistem akuisisi data: jelaskan akuisisi berbasis durasi waktu (5.0 detik) dengan pembuangan *settling time* (1.0 detik), selaras dengan backend `DurationAcquisitionEngine` dan `AGENTS.md`.
- [ ] Hilangkan kalimat pembuka "Untuk..." pada baris 274 dan baris 287 menjadi kalimat aktif/pasif bernalar baku.

#### Task 6: Standardisasi Ejaan EYD V / KBBI VI & Penulisan Formula Kimia Lintas Bab
**Berkas:** `Isi/Pendahuluan.tex`, `Isi/Tinjauan Pustaka.tex`, `Isi/Metode Penelitian.tex`
- [ ] Koreksi kata serapan non-baku:
  - `kelembaban` $\rightarrow$ `kelembapan`
  - `linier` $\rightarrow$ `linear`
  - `non-linier` $\rightarrow$ `nonlinear`
  - `respon` $\rightarrow$ `respons`
  - `standarisasi` $\rightarrow$ `standardisasi`
  - `insulator` $\rightarrow$ `isolator`
  - `terfilter` $\rightarrow$ `tersaring`
  - `kecoklatan` $\rightarrow$ `kecokelatan`
  - `melarut` $\rightarrow$ `larut`
- [ ] Perbaiki penggunaan kata hubung "namun" di tengah kalimat intrakalimat (ganti dengan "tetapi" atau pisahkan menjadi kalimat baru).
- [ ] Ganti seluruh notasi matematika kimia `$Fe_3O_4$` atau $\mathrm{Fe_3O_4}$ menjadi sintaks mhchem resmi `\ch{Fe3O4}`.

---

### FASE B: Pengelolaan Pustaka dan Repositori Referensi

#### Task 7: Pengelolaan Berkas Referensi dan Katalog Digital `referensi/`
**Berkas:** [referensi/](file:///c:/Users/Fahry%20Rizky%20S/Documents/Tugas%20Akhir%20Fahry/Proposal/referensi), [referensi/README.md](file:///c:/Users/Fahry%20Rizky%20S/Documents/Tugas%20Akhir%20Fahry/Proposal/referensi/README.md), [referensi/catalog.json](file:///c:/Users/Fahry%20Rizky%20S/Documents/Tugas%20Akhir%20Fahry/Proposal/referensi/catalog.json)
- [x] Folder `referensi/` telah menampung 24 berkas PDF tervalidasi yang diberi prefix `[kunci_bibtex]`.
- [x] Seluruh 53 pustaka tercatat dalam `referensi/catalog.json` dan terdokumentasi dalam tabel Markdown `referensi/README.md`.
- [ ] Verifikasi bahwa seluruh kunci sitasi di `Isi/*.tex` cocok 100% dengan katalog referensi.

---

### FASE C: Rekonstruksi Slide Presentasi Sidang Proposal (PPTX)

#### Task 8: Pembuatan Aset Visual Cover Autentik Gilang Pratama
**Berkas:** `Gambar/cover_bg_gilang.png`, `Gambar/Logo/logo_uin_fisika_pill.png`, `scripts/generate_cover_assets.py`
- [ ] Buat skrip `scripts/generate_cover_assets.py` untuk mengolah gambar lab fisik (`Statif.jpg`, `Casing.jpg`, `Tampak Depan.jpg`) menjadi latar gelap bergradien navy (`#08101E`, 82% opacity) berukuran 2880x1620 px.
- [ ] Susun kapsul logo putih (`logo_uin_fisika_pill.png`) beresolusi tinggi yang memadukan `Logo UIN.png` dan `Logo Fisika UIN.png`.

#### Task 9: Rekonstruksi Cover Slide 1 di `scripts/generate_proposal_presentation.py`
**Berkas:** [scripts/generate_proposal_presentation.py](file:///c:/Users/Fahry%20Rizky%20S/Documents/Tugas%20Akhir%20Fahry/Proposal/scripts/generate_proposal_presentation.py)
- [ ] Pasang latar belakang penuh `cover_bg_gilang.png`.
- [ ] Bagian atas: teks `"2026"` (kiri), kapsul logo pill UIN+Fisika (tengah), teks `"Seminar Proposal"` (kanan).
- [ ] Kotak judul tengah: persegi panjang navy (`#112240`) dengan garis bingkai oranye tebal (`#f26522`, 4.5 pt). Font judul all-caps: **19.5 pt**, bold, putih.
- [ ] Bagian bawah: Nama Mahasiswa (**17 pt** bold putih), NIM (**13.5 pt**), dua pill dosen pembimbing (**13 pt**), dan institusi (**13.5 pt** bold). Bebas bento box putih AI.

#### Task 10: Sinkronisasi Slide 3 & 4 (4 RM, 4 Tujuan, Tipografi Besar 13.5–14 pt)
**Berkas:** [scripts/generate_proposal_presentation.py](file:///c:/Users/Fahry%20Rizky%20S/Documents/Tugas%20Akhir%20Fahry/Proposal/scripts/generate_proposal_presentation.py)
- [ ] Slide 3: Judul kartu kiri murni `"Rumusan Masalah"` (17 pt bold navy), 4 butir penomoran murni `1.`, `2.`, `3.`, `4.` dengan font **13.5–14.0 pt** (spasi 1.25). Judul kartu kanan murni `"Batasan Masalah"` (17 pt bold emerald, 6 butir font **12.0–12.5 pt**).
- [ ] Slide 4: Judul kartu kiri murni `"Tujuan Penelitian"` (17 pt bold navy, 4 butir font **13.5–14.0 pt**). Judul kartu kanan murni `"Manfaat Penelitian"` (17 pt bold emerald, 4 butir font **13.5–14.0 pt**).

#### Task 11: Penambahan Slide 11 Baru "Perbandingan dengan Penelitian Terdahulu"
**Berkas:** [scripts/generate_proposal_presentation.py](file:///c:/Users/Fahry%20Rizky%20S/Documents/Tugas%20Akhir%20Fahry/Proposal/scripts/generate_proposal_presentation.py)
- [ ] Buat slide baru sebelum bab metodologi (Slide 11):
  - Header: `"Perbandingan dengan Penelitian Terdahulu & Kebaruan Riset"`
  - Tabel matriks 5 baris x 6 kolom memuat perbandingan Wang (2021), Singhal (2024), Sun (2023), Gilang (2026), dan Penelitian Ini (2026, baris highlight navy).
  - Kotak bawah penegasan 3 kebaruan riset (*research gap*).

#### Task 12: Kalibrasi Tipografi Skala Besar di Seluruh Slide & Pembasmian AI Slop
**Berkas:** [scripts/generate_proposal_presentation.py](file:///c:/Users/Fahry%20Rizky%20S/Documents/Tugas%20Akhir%20Fahry/Proposal/scripts/generate_proposal_presentation.py)
- [ ] Hapus seluruh badge kategori kaku di atas judul kartu pada fungsi `add_card_header`.
- [ ] Besarkan ukuran font di seluruh slide:
  - Slide 5 (Metode Pengumpulan Data): judul kartu 15 pt bold, isi 11.5–12 pt.
  - Slide 6–10 (Teori TMR, AD623, Nanofiber, SVM/QSVC): bullet teks ditingkatkan ke **13.0–13.5 pt**.
  - Slide 12 (Alat & Bahan): tabel teks header 12 pt, isi sel 11 pt.
  - Slide 13–18 (Tahapan Riset, Hardware, Sintesis, Kalibrasi, Matriks Pangan): bullet teks ditingkatkan ke **13.0 pt**.
  - Slide 22 (Penutup): format formal akademik ("TERIMA KASIH" 42 pt bold putih, permohonan arahan penguji 13 pt navy).
- [ ] Total susunan presentasi menjadi tepat **22 slide** presisi.

---

### FASE D: Otomasi Kompilasi, Verifikasi Komprehensif, dan *Artifact Delivery*

#### Task 13: Regenerasi Presentasi PPTX & Verifikasi Otomatis
**Berkas:** `scripts/verify_deck.py`, `Proposal_TA_Fahry_Rizky_Samsudin.pptx`
- [ ] Jalankan skrip generator presentasi:
  ```bash
  python scripts/generate_proposal_presentation.py
  ```
- [ ] Jalankan verifikasi otomatis `python scripts/verify_deck.py`:
  - Memastikan tepat 22 slide.
  - Memastikan 0 kemunculan em-dash (`—`).
  - Memastikan 4 RM pada Slide 3 dan 4 Tujuan pada Slide 4.
  - Memastikan Slide 15 dan Slide 19 murni memuat 2 diagram alir tanpa gangguan teks.
  - Memastikan Slide 20 dan 21 memuat seluruh 52 daftar pustaka alfabetis APA.

#### Task 14: Kompilasi 4-Tahap LaTeX Bersih & Verifikasi PDF Akhir
**Berkas:** [scripts/build_proposal.py](file:///c:/Users/Fahry%20Rizky%20S/Documents/Tugas%20Akhir%20Fahry/Proposal/scripts/build_proposal.py), `skripsi.pdf`, `Proposal Fahry Rizky Samsudin.pdf`
- [ ] Jalankan kompilasi naskah proposal skripsi:
  ```bash
  python scripts/build_proposal.py
  ```
  atau
  ```cmd
  build.bat
  ```
- [ ] Pastikan 4-pass kompilasi (`pdflatex` $\rightarrow$ `bibtex` $\rightarrow$ `pdflatex` $\rightarrow$ `pdflatex`) selesai dengan exit code 0.
- [ ] Verifikasi keberadaan Subbab 2.3 dengan Tabel 2.1, Gambar 3.5, Gambar 3.8, dan nol kata non-baku pada `skripsi.pdf` / `Proposal Fahry Rizky Samsudin.pdf`.

---

## 5. Checkpoint Kesiapan Eksekusi
- [x] Seluruh kebutuhan digabungkan secara homogen ke dalam satu dokumen rencana induk.
- [x] Larangan kata "Untuk" di awal paragraf dan kalimat pengantar telah dipetakan secara detail.
- [x] Folder referensi 53 pustaka telah siap dan terindeks.
- [ ] Menunggu konfirmasi pengguna untuk mengeksekusi penyuntingan naskah LaTeX dan regenerasi slide presentasi PPTX.
