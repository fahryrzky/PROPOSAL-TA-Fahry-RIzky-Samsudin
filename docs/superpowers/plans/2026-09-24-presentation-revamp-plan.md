# Presentation Overhaul & Anti-Slop Implementation Plan

**Goal:** Reconstruct the thesis proposal presentation slide deck to match the exact academic format of reference `1227030017_skripsi.pdf` (Gilang Pratama), eliminate all AI-slop patterns (no repetitive "Landasan Teori" headers, no company profile fluff, no em dashes, no generic card repetition), merge Rumusan + Batasan into 1 slide, merge Tujuan + Manfaat into 1 slide, present Latar Belakang as a clean visual flowchart, render all math equations with LaTeX 300 DPI, and thoroughly cover all Bab II topics including Electrospinning.

---

## 1. Problem Diagnosis & Critique Intake (Superpowers Diagnosis)

Berdasarkan evaluasi kritis pengguna dan perbandingan dengan `1227030017_skripsi.pdf` (Gilang Pratama, Sidang Fisika UIN SGD Bandung):

| Poin Temuan | Diagnosis Masalah (AI Slop / Redundansi) | Solusi & Tindakan Rombak Total |
|---|---|---|
| **Profil Mitra Bolabot** | Fluff tidak perlu untuk sidang proposal akademik skripsi. | **Dihapus total** dari dek slide presentasi. |
| **Sistematika Paparan Sidang** | Agenda 5 butir generik membuang waktu presentasi. | **Dihapus total**. Slide langsung masuk ke Latar Belakang. |
| **Latar Belakang Bertele-tele** | 4 slide penuh paragraf teks yang melelahkan. | **Diganti 1 Slide Desain Grafis (Flowchart Konseptual)**: Masalah $\to$ Gap $\to$ Reseptor $\to$ TMR $\to$ Instrumentasi $\to$ ML $\to$ Solusi. |
| **Rumusan & Batasan Masalah** | Terpisah di 2 slide berbeda. | **Digabung ke dalam 1 Slide**: Kolom Kiri 5 Rumusan Masalah; Kolom Kanan 6 Batasan Masalah. |
| **Tujuan & Manfaat Penelitian** | Terpisah di 2 slide berbeda. | **Digabung ke dalam 1 Slide**: Kolom Kiri 5 Tujuan Penelitian; Kolom Kanan 4 Manfaat Penelitian. |
| **Cover Identitas Slide 1** | Format card AI generik tidak sesuai tradisi UIN SGD. | **Disesuaikan 1-to-1 dengan Gilang Pratama**: Judul atas, Nama & NIM di TENGAH, Pembimbing I di KIRI, Pembimbing II di KANAN. |
| **Persamaan Matematis ASCII** | Teks matematika ditulis manual (`R-NH-NH2 --> ...`, `(4/5)^(3/2)`). | **Dirender ke LaTeX Computer Modern 300 DPI** transparan via Matplotlib (`output/equations/*.png`). |
| **Repetisi Header "Landasan Teori"** | Label "BAB II: TINJAUAN PUSTAKA / LANDASAN TEORI X" diulang di setiap slide (AI Slop keras). | **Dihapus total**. Judul slide langsung spesifik pada topik fisis: "Karakteristik Formaldehida & Reaksi Hidrazon", "Fisika TMR & Model Julliere", dst. |
| **Materi Elektrospinning Terlewat** | Penjelasan elektrospinning Bab II terabaikan. | **Dibuatkan 1 Slide Khusus Teori Elektrospinning**: Fisika elektrohidrodinamika, Taylor cone, whipping instability, voltase 15 kV, laju alir 0.5 mL/h. |
| **Tipografi & Kontras Teks** | Ukuran font terlalu kecil dan pudar. | Diperbesar ke 11–14 pt, bold kontras tinggi (`#0F172A`), hirarki tegas. |

---

## 2. Struktur Baru Dek Presentasi (26 Slide Terfokus & Bebas Slop)

1. **Slide 1: Cover Judul & Identitas** (Format Gilang: Judul Atas, Nama & NIM di Tengah, Pembimbing I di Kiri, Pembimbing II di Kanan).
2. **Slide 2: Latar Belakang Penelitian (Diagram Alir Konseptual Minim Teks)** (Infografis 6 Tahap Masalah-ke-Solusi).
3. **Slide 3: Rumusan Masalah & Batasan Masalah** (Kiri: 5 Rumusan Masalah; Kanan: 6 Batasan Masalah).
4. **Slide 4: Tujuan Penelitian & Manfaat Penelitian** (Kiri: 5 Tujuan Penelitian; Kanan: 4 Manfaat Penelitian).
5. **Slide 5: Metode Pengumpulan Data Penelitian** (4 Pilar: Studi Literatur, Observasi, Eksperimen Laboratorium, Analisis Pemodelan).
6. **Slide 6: Karakteristik Formaldehida & Mekanisme Reaksi Hidrazon ADH** (Formula LaTeX Ter-render `eq_01_hidrazon.png` & Gambar Struktur).
7. **Slide 7: Fisika Tunneling Magnetoresistance (TMR) & Model Julliere** (Formula LaTeX Ter-render `eq_02_julliere.png`, `eq_09_vout_tmr.png` & Diagram MTJ/ALT023).
8. **Slide 8: Kumparan Helmholtz sebagai Pembangkit Medan Acuan Presisi** (Formula LaTeX Ter-render `eq_03_helmholtz.png` & Spek Meja Lab Bolabot).
9. **Slide 9: Pengkondisi Sinyal AD623 & Desain Tegangan Referensi VREF = 2.50 V** (Formula LaTeX Ter-render `eq_04_ad623.png` & Pinout AD623).
10. **Slide 10: Filter Pasif Anti-Aliasing (RC LPF) & ADC ADS1115 16-Bit** (Formula LaTeX Ter-render `eq_05_lpf_adc.png` & Gambar LPF/ADS1115).
11. **Slide 11: Teknologi Elektrospinning untuk Fabrikasi Nanofiber PVA** (Tahapan Taylor Cone, Whipping Instability, Parameter 15 kV & Gambar `babII_elspinPVA.PNG`).
12. **Slide 12: Matriks Polimer PVA & Nanopartikel Fe3O4 Sintesis Hijau Kelor** (Fitokimia *Moringa oleifera*, sifat superparamagnetik, matriks hidrofilik PVA 10%).
13. **Slide 13: Asam Sitrat sebagai Capping Agent & Green Crosslinker (Curing 130°C)** (Stabilisasi dispersi & esterifikasi termal 130°C 1.5 jam anti-air).
14. **Slide 14: Adipic Acid Dihydrazide (ADH) & Reseptor Nanokomposit Fe3O4/PVA-Sitrat-ADH** (Mekanisme perturbasi medan magnetik stray lokal pada TMR).
15. **Slide 15: Pemodelan Support Vector Machine (SVM) Klasik** (Formula LaTeX Ter-render `eq_06_svm.png`, RBF Gaussian Kernel, parameter C & gamma).
16. **Slide 16: Pemodelan Quantum Support Vector Classifier (QSVC)** (Formula LaTeX Ter-render `eq_07_qsvc.png`, Ruang Hilbert $2^n$ qubit, Quantum Kernel Fidelity).
17. **Slide 17: Komparasi Model Klasik vs Kuantum & Lingkungan Perangkat Lunak** (Tabel Komparasi SVM vs QSVC, Arduino Uno, Raspberry Pi 5 & Python).
18. **Slide 18: Metodologi: Waktu, Lokasi Riset, dan Spesifikasi Alat & Bahan** (September–Desember 2026 di Bolabot & Tabel Hardware/Bahan).
19. **Slide 19: Metodologi: Diagram Alir Penelitian Komprehensif** (6 Tahapan Alur Kerja Riset & Gambar `BABIII_DiagramAlirPenelitian.drawio.png`).
20. **Slide 20: Metodologi: Desain Hardware Terpadu, Skematik Sirkuit & Housing Statif 3D** (Gambar Skematik Grounding & CAD 3D).
21. **Slide 21: Metodologi: Arsitektur Perangkat Lunak (Arduino & Python GUI)** (Diagram Alir Firmware Arduino & GUI Durasi 5s CustomTkinter).
22. **Slide 22: Metodologi: Prosedur Sintesis Hijau Fe3O4 & Fabrikasi Nanofiber Elektrospinning** (Diagram Alir Sintesis, 15 kV, 0.5 mL/jam, curing 130°C).
23. **Slide 23: Metodologi: Prosedur Kalibrasi Kumparan Helmholtz & Karakterisasi Sensor TMR** (Sapuan $0-1.6\ \text{A}$, teslameter acuan, kurva sensitivitas $dV/dB$).
24. **Slide 24: Metodologi: Preparasi Sampel Bakso & Ekstraksi 5 Fitur Sinyal Dinamis** (Maserasi & Sentrifugasi 4000 rpm, Formula LaTeX Ter-render `eq_08_fitur.png` & Tabel 5 Fitur).
25. **Slide 25: Metodologi: Pipeline Pelatihan SVM vs QSVC & Deployment ke Raspberry Pi 5** (5-Fold CV, Diagram Model Building & Model Deploy).
26. **Slide 26: Rencana Jadwal Riset 4 Bulan (Sep–Des 2026), Target Luaran & Penutup** (Gantt Chart 4 Bulan, Target Publikasi, dan Sesi Tanya Jawab).

---

## 3. Langkah Eksekusi (Action Tasks)

- [x] **Task 1: Render Seluruh Persamaan Matematika ke PNG 300 DPI**
  - Jalankan `scripts/render_math_equations.py` untuk menghasilkan 9 berkas formula di `output/equations/`.
- [x] **Task 2: Buat Diagram Alir Grafis Latar Belakang (Minim Teks)**
  - Jalankan `scripts/generate_latar_belakang_flowchart.py` untuk menghasilkan `output/diagrams/latar_belakang_flowchart.png`.
- [ ] **Task 3: Tulis Ulang Skrip Generator PPTX (`scripts/generate_proposal_presentation.py`)**
  - Terapkan 26 slide baru tanpa header AI-slop repetitif, layout cover Gilang Pratama, penyisipan gambar formula LaTeX 300 DPI, dan tabel komparasi.
  - Jalankan generator untuk menghasilkan `Proposal_TA_Fahry_Rizky_Samsudin.pptx`.
- [ ] **Task 4: Tulis Ulang Preview Interaktif HTML (`presentation_preview.html`)**
  - Terapkan 26 slide baru yang sinkron 1-ke-1 dengan PPTX, menyematkan gambar persamaan matematis dan diagram latar belakang, serta navigasi keyboard.
- [ ] **Task 5: Verifikasi Anti-Slop & Commit Git**
  - Audit seluruh teks: bebas em dash (`—`), kontras warna WCAG AAA, font Segoe UI / Cambria Math berbobot tegas.
  - Git add, commit, dan push ke GitHub `origin/main`.
