# Rencana Implementasi: Restrukturisasi Flowchart TikZ, Parameter Elektrospinning, dan Sistematika Material Bab II & III

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Menyusun ulang Bab II (Tinjauan Pustaka) agar memuat PVA, Asam Sitrat, ADH, dan nanofiber komposit secara bertahap; memperbarui parameter elektrospinning di Bab III (Metodologi) dengan nilai optimal hasil riset literatur untuk mengatasi masalah partikel Fe3O4 mendekati nol pada SEM; serta mengganti seluruh Gambar 3.6--3.9 berbasis drawio PNG dengan diagram alir native TikZ yang akurat sesuai kode TMR terbaru.

**Architecture:** Modifikasi file LaTeX modular (`Isi/Tinjauan Pustaka.tex`, `Isi/Metode Penelitian.tex`, `references.bib`). Gambar 3.6--3.9 digambar ulang sepenuhnya menggunakan kode vektor TikZ di dalam lingkungan `figure[H]` dengan style konsisten (`process`, `decision`, `arrow`, `startstop`), menghapus ketergantungan pada file `.drawio.png` lama.

**Tech Stack:** LaTeX (pdflatex, BibTeX, TikZ package, chemformula, siunitx), Python 3.12 (pyserial, numpy, matplotlib, scipy), Arduino C/C++ (Adafruit ADS1X15, Wire).

**Spec:** `docs/decisions/ADR-001-revamp-flowcharts-materials-electrospinning.md`

## Global Constraints
- Seluruh rumus kimia wajib menggunakan paket `\ch{}` (contoh: `\ch{Fe3O4}`).
- Seluruh gambar diagram alir harus menggunakan lingkungan `\begin{figure}[H]` tepat di bawah subbab yang relevan dan menggunakan TikZ native.
- Tidak boleh ada residu istilah GMR, glukosa, saliva, LM358, atau drawio PNG untuk Gambar 3.6--3.9.
- Kompilasi LaTeX 4 tahap (`pdflatex` $\rightarrow$ `bibtex` $\rightarrow$ `pdflatex` $\rightarrow$ `pdflatex`) harus menghasilkan 0 error dan 0 undefined citation.

## Review Focus
1. Diagram TikZ harus muat rapi di halaman A4 dengan margin report tanpa terpotong atau keluar batas (*overfull \hbox*).
2. Alur logika pada TikZ Arduino harus mencerminkan fungsi riil di `sensor_tmr_formalin.ino` (I2C ADS1115, non-averaging streaming, dual voltage computation).
3. Alur logika pada TikZ Python harus mencerminkan fungsi riil di `kalibrasi_tmr_formalin.py` dan `karakterisasi_sensor_B.py` (stabilize skip, readings per point, linear regression, plot generation).
4. Penjelasan parameter elektrospinning harus secara eksplisit menerangkan alasan ilmiah mengapa partikel Fe3O4 pada SEM Gilang mendekati nol dan bagaimana capping asam sitrat + optimasi kV/flowrate mengatasinya.
5. Pembahasan material di Bab II dan Bab III harus runtut: PVA $\rightarrow$ Asam Sitrat $\rightarrow$ ADH $\rightarrow$ Nanofiber \ch{Fe3O4}/PVA-Sitrat-ADH.


---

### Task 0: Pembaruan Judul Proposal pada Seluruh Berkas

**Files:**
- Modify: `skripsi.tex:52`
- Modify: `Header/sampul.tex:6`
- Modify: `Header/persetujuan.tex:10`
- Modify: `Header/Keaslian.tex:17`
- Modify: `Header/prakata.tex:7`
- Modify: `Isi/Pendahuluan.tex:16, 74`
- Modify: `Isi/Metode Penelitian.tex:4, 129`

**Interfaces:**
- Menyelaraskan seluruh judul menjadi:
  `Rancang Bangun Instrumentasi Sensor \textit{Tunneling Magnetoresistance} Berbasis Nanofiber \ch{Fe3O4}/PVA-Sitrat-ADH untuk Deteksi Formalin pada Bakso Menggunakan Komparasi Model SVM dan QSVC`

- [x] **Step 1: Perbarui judul pada `skripsi.tex` dan seluruh berkas di direktori `Header/`**
- [x] **Step 2: Perbarui judul pada `Isi/Pendahuluan.tex` dan `Isi/Metode Penelitian.tex`**
- [x] **Step 3: Uji kompilasi untuk memverifikasi kesesuaian judul di sampul dan daftar gambar**

---

### Task 1: Restrukturisasi Subbab Material pada Bab II (Tinjauan Pustaka)

**Files:**
- Modify: `Isi/Tinjauan Pustaka.tex:109-120`
- Modify: `references.bib`

**Interfaces:**
- Menghasilkan 4 subbab mandiri:
  - `\subsection{\textit{Polyvinyl Alcohol} (PVA)}`
  - `\subsection{Asam Sitrat (\textit{Citric Acid})}`
  - `\subsection{\textit{Adipic Acid Dihydrazide} (ADH)}`
  - `\subsection{Nanofiber \ch{Fe3O4}/PVA-Sitrat-ADH sebagai Elemen Reseptor}`

- [x] **Step 1: Tambahkan referensi BibTeX untuk PVA dan karakterisasinya jika belum lengkap**
- [x] **Step 2: Pecah Subbab 2.1.8 menjadi 4 subbab terpisah dengan uraian kimiawi dan fungsi yang komprehensif**
- [x] **Step 3: Uji kompilasi cepat Bab II untuk memastikan tidak ada konflik label atau sitasi**

---

### Task 2: Pembaruan Subbab 3.4 (Metodologi Sintesis & Optimasi Parameter Elektrospinning)

**Files:**
- Modify: `Isi/Metode Penelitian.tex:252-270`

**Interfaces:**
- Menyajikan tahapan sintesis terstruktur:
  - 3.4.1 Sintesis Nanopartikel Magnetik \ch{Fe3O4}
  - 3.4.2 Preparasi Matriks PVA dan Dispersi Terstabilisasi Asam Sitrat
  - 3.4.3 Sintesis Nanofiber Komposit via Elektrospinning (dengan parameter optimal: 16--18 kV, 0,4--0,8 mL/jam, TCD 13--15 cm, dan justifikasi hasil SEM)
  - 3.4.4 Penautan Silang (*Thermal Curing*) dan Fungsionalisasi ADH

- [x] **Step 1: Tuliskan justifikasi kegagalan dispersi Fe3O4 pada SEM awal dan solusi stabilisasi sitrat**
- [x] **Step 2: Perbarui tabel dan teks parameter elektrospinning dengan nilai optimal (kV, laju alir, TCD)**
- [x] **Step 3: Sesuaikan penomoran dan urutan bahan di Tabel 3.3 dan narasi pendukungnya**

---

### Task 3: Pembaruan Format dan Diagram Alir Gambar 3.6 (Arduino) dan Gambar 3.7 (Python) Berbasis Draw.io

**Files:**
- Modify: `Isi/Metode Penelitian.tex:185-217`
- Artifacts: `babIII_AlurSoftwareArduino.drawio`, `babIII_AlurSoftwareArduino.drawio.png`, `babIII_DiagramAlirPython.drawio`, `babIII_DiagramAlirPython.drawio.png`

**Interfaces:**
- Menggunakan `\includegraphics` format Draw.io asli seperti milik Gilang (warna soft peach dan soft sky blue, bentuk standar ISO/SNI).
- Menyediakan berkas `.drawio` yang dapat diedit langsung di diagrams.net.

- [x] **Step 1: Validasi diagram alir Arduino (inisialisasi ADS1115, pembacaan serial label, konversi ADC, kalkulasi LSB, streaming CSV)**
- [x] **Step 2: Validasi diagram alir Python (komunikasi serial, input konsentrasi, pembacaan tegangan, plotting realtime, simpan PNG dan XLSX/CSV)**
- [x] **Step 3: Pastikan pemanggilan gambar menggunakan \includegraphics dengan lebar proporsional (0.33\textwidth & 0.85\textwidth)**

---

### Task 4: Pembaruan Format dan Diagram Alir Gambar 3.8 (Model Building) dan Gambar 3.9 (Model Deploy) Berbasis Draw.io

**Files:**
- Modify: `Isi/Metode Penelitian.tex:218-235`
- Artifacts: `babIIIModelBuilding.drawio`, `babIIIModelBuilding.drawio.png`, `babIIIModelDeploy.drawio`, `babIIIModelDeploy.drawio.png`

**Interfaces:**
- Memperbarui diagram Model Building dari glukosa/regresi R2 ke konsentrasi formalin, ekstraksi fitur, validasi silang K-Fold, dan metrik evaluasi.
- Memperbarui diagram Model Deploy dari deteksi glukosa ke prediksi konsentrasi formalin bakso realtime.
- Menyediakan berkas `.drawio` dan `.drawio.png` dengan metadata embedded mxfile.

- [x] **Step 1: Perbarui teks dan struktur model building dari glukosa ke formalin dan klasifikasi**
- [x] **Step 2: Perbarui teks dan struktur model deployment untuk deteksi formalin pada sampel bakso**
- [x] **Step 3: Hubungkan dengan \includegraphics pada narasi Metode Penelitian dan pastikan tata letak rapi**

---

### Task 5: Validasi Kompilasi Lengkap LaTeX dan Inspeksi Visual

**Files:**
- Command: `pdflatex -interaction=nonstopmode skripsi.tex`
- Command: `bibtex skripsi`
- Command: `pdflatex -interaction=nonstopmode skripsi.tex`
- Command: `pdflatex -interaction=nonstopmode skripsi.tex`

**Interfaces:**
- Memastikan `skripsi.pdf` ter-generate sempurna dengan 0 error, 0 bad boxes parah, dan tata letak gambar proporsional.

- [x] **Step 1: Jalankan kompilasi LaTeX 4 tahap**
- [x] **Step 2: Periksa log untuk memastikan 0 error dan 0 undefined references**
- [x] **Step 3: Verifikasi keberadaan dan keterbacaan 4 diagram alir Draw.io pada halaman PDF**
