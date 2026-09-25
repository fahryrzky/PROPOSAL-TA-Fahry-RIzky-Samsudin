# Review Komprehensif Proposal Tugas Akhir Pasca-Revisi Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Menjalankan audit dan evaluasi kritis multi-disiplin terhadap seluruh naskah proposal skripsi yang telah direvisi (Bab I, Bab II, Bab III, Gambar Mekatronika, dan Bibliografi) menggunakan kombinasi 12 *agent skills* terpasang, menghasilkan laporan tinjauan akademik mendalam (*peer-review report*) serta simulasi pertahanan sidang proposal.

**Architecture:** Pendekatan tinjauan berlapis (*defense-in-depth review*):
1. **Lapis 1 - Integritas Redaksi & Narasi**: Pemeriksaan logika penalaran, konsistensi istilah 4 model (SVM, RF, QSVC, VQC), dan eliminasi jargon *AI slop*.
2. **Lapis 2 - Rigor Ilmiah & Fisika Eksperimental**: Verifikasi rantai sinyal sensor TMR, in-amp AD623 ($V_{\text{REF}} = 2.50\text{ V}$), ADC ADS1115, kemagnetan Helmholtz, reaksi enzimatis ADH, dan formulasi matematis model klasik vs kuantum.
3. **Lapis 3 - Visual & Mekatronika**: Audit keselarasan gambar mekatronika baru (`babIII-desainTMR.png`), diagram alir penelitian U-turn Draw.io, dan skematik sirkuit.
4. **Lapis 4 - Validitas Sitasi & Pustaka**: Pemeriksaan silang sitasi LaTeX terhadap `references.bib` dan arsip 100+ PDF `referensi/`.
5. **Lapis 5 - Radar Pertahanan Sidang**: Simulasi pertanyaan jebakan penguji seminar proposal dan formulasi jawaban berbasis bukti.

**Tech Stack:** LaTeX (`pdflatex`, `bibtex`), Python 3.13 (`pytest`, `ezdxf`, `shapely`, `build123d`), BibTeX parser, Markdown Reporter.

**Spec:** [AGENTS.md](file:///c:/Users/Fahry%20Rizky%20S/Documents/Tugas%20Akhir%20Fahry/Proposal/AGENTS.md), [skripsi.tex](file:///c:/Users/Fahry%20Rizky%20S/Documents/Tugas%20Akhir%20Fahry/Proposal/skripsi.tex), [Isi/Pendahuluan.tex](file:///c:/Users/Fahry%20Rizky%20S/Documents/Tugas%20Akhir%20Fahry/Proposal/Isi/Pendahuluan.tex), [Isi/Tinjauan Pustaka.tex](file:///c:/Users/Fahry%20Rizky%20S/Documents/Tugas%20Akhir%20Fahry/Proposal/Isi/Tinjauan%20Pustaka.tex), [Isi/Metode Penelitian.tex](file:///c:/Users/Fahry%20Rizky%20S/Documents/Tugas%20Akhir%20Fahry/Proposal/Isi/Metode%20Penelitian.tex).

## Global Constraints

- Rantai sinyal perangkat keras wajib mematuhi *Ground Truth*: $V_{\text{REF}} = 2.50\text{ V}$ (bukan 1.65 V), rentang linier TMR $\pm 1.0\text{ mT}$, catu daya Helmholtz $0.0 - 16.0\text{ V}$, knob fisik diatur secara eksternal.
- Model pembelajaran mesin wajib mencakup tepat 4 model: Klasik (SVM, Random Forest) dan Kuantum (QSVC, VQC).
- Struktur diagram alir Gambar 3.8 wajib mempertahankan topologi *U-turn flow* profesional Draw.io tanpa percabangan *AI slop*.
- Gambar prototipe mekatronika pada Gambar 3.1 wajib menggunakan `babIII-desainTMR.png` dengan deskripsi panel (a) tampak dalam (koil & TMR) dan (b) tampak luar (layar & porta).
- Semua sitasi wajib berkorespondensi 1-ke-1 dengan entri di `references.bib`.

## Review Focus

1. **Konsistensi Penamaan 4 Model**: Memastikan tidak ada naskah yang tertinggal menyebut "hanya SVM dan QSVC" tanpa menyertakan RF dan VQC.
2. **Kesesuaian Panel Gambar 3.1**: Memastikan keterangan caption (a) dan (b) pada `babIII-desainTMR.png` tidak terbalik antara interior koil dan eksterior layar LCD.
3. **Justifikasi Fisika Quantum Machine Learning**: Memastikan naskah Bab II & Bab III secara eksplisit menjelaskan *quantum feature map* ($ZZFeatureMap$) dan alasan matematis komparasi kuantum untuk data respon sensor TMR.
4. **Verifikasi Sitasi BibTeX**: Mendeteksi jika ada sitasi LaTeX `\cite{...}` yang *undefined* atau memicu `BibTeX warning: undefined citation`.
5. **Kompilasi Sempurna**: Memastikan dokumen proposal selalu menghasilkan `0 LaTeX Error (Sempurna)`.

---

## Rangkaian Keterampilan (*Agent Skills*) yang Dikerahkan

| Kategori Tinjauan | Keterampilan (*Skills*) yang Digunakan | Peran dan Fokus Penilaian |
|---|---|---|
| **Editorial & Anti-Slop** | `antislop-copywriting`, `avoid-ai-writing`, `scientific-critical-thinking` | Memeriksa ketajaman kalimat, membuang basa-basi/klise AI, menjaga nada akademis lugas dan formal. |
| **Peer Review Standar Jurnal** | `peer-review`, `review-paper-2`, `academic-manuscript-review` | Menilai metodologi, desain eksperimen, keterulangan (*reproducibility*), dan kekuatan kontribusi ilmiah seperti reviewer jurnal Q1. |
| **Fisika, Kemagnetan & Quantum** | `physical-review-b`, `prx-quantum`, `observability-and-instrumentation` | Memeriksa ketepatan rumus TMR, sirkuit pengkondisi sinyal AD623, medan seragam Helmholtz, dan sirkuit kuantum berparameter. |
| **Mekatronika, CAD & Fabrikasi** | `cad-physics-validation`, `dfm`, `dfam-check` | Menguji kelayakan desain mekanik casing 3D, toleransi fabrikasi, ventilasi panas kumparan, dan kekokohan dudukan preparat. |
| **Pustaka & Bibliografi** | `citation-audit`, `reference-checker`, `latex-compile-clean` | Memeriksa kelengkapan metadata referensi, konsistensi DOI, serta validasi kompilasi bebas error/warning. |
| **Simulasi Sidang Proposal** | `research-defense-radar`, `doubt-driven-development` | Mengantisipasi pertanyaan tajam dosen penguji, mendeteksi celah argumen, dan menyiapkan rekomendasi tanggapan. |

---

## Rincian Rencana Eksekusi Tugas

### Task 1: Audit Naskah Bab I (Pendahuluan) — Latar Belakang & Perumusan Masalah
**Files:**
- Audit: `Isi/Pendahuluan.tex`
- Output Report: `LAPORAN_EVALUASI_PROPOSAL_PASCA_REVISI.md` (Bagian I)

**Interfaces:**
- Input: Naskah Bab I proposal
- Skills: `antislop-copywriting`, `scientific-critical-thinking`, `research-defense-radar`
- Output: Skor kelayakan, daftar perbaikan narasi alur penalaran, verifikasi komparasi 4 model.

- [x] **Step 1: Ekstraksi dan audit argumen latar belakang**
  - Periksa 6 simpul penalaran: (1) Urgensi deteksi formalin pangan $\rightarrow$ (2) Keterbatasan sensor optik/kimia komersial $\rightarrow$ (3) Keunggulan reseptor nanofiber $\text{Fe}_3\text{O}_4$/PVA-Sitrat-ADH $\rightarrow$ (4) Transduser TMR ALT023-10E $\rightarrow$ (5) Integrasi pengkondisi sinyal AD623 & ADS1115 $\rightarrow$ (6) Komparasi komprehensif 4 model (SVM, RF, QSVC, VQC).
- [x] **Step 2: Pengecekan konsistensi Rumusan Masalah, Tujuan, dan Batasan Masalah**
  - Pastikan setiap butir Rumusan Masalah memiliki pasangan 1-ke-1 di Tujuan Penelitian.
  - Pastikan Batasan Masalah menegaskan konsentrasi formalin uji ($0.0 - 5.0\text{ ppm}$), sampel bakso lokal, dan simulator kuantum (Qiskit Statevector/Aer).
- [x] **Step 3: Dokumentasikan temuan audit Bab I ke laporan evaluasi**

---

### Task 2: Audit Naskah Bab II (Tinjauan Pustaka) — Rigor Teoretis & Formulasi Matematis
**Files:**
- Audit: `Isi/Tinjauan Pustaka.tex`
- Output Report: `LAPORAN_EVALUASI_PROPOSAL_PASCA_REVISI.md` (Bagian II)

**Interfaces:**
- Input: Naskah Bab II proposal
- Skills: `physical-review-b`, `prx-quantum`, `observability-and-instrumentation`
- Output: Evaluasi ketepatan persamaan fisika, rantai sinyal, biokimia enzim, dan sirkuit kuantum.

- [x] **Step 1: Audit teori kemagnetan & transduser TMR**
  - Evaluasi rumus TMR ratio: $\text{TMR} = \frac{R_{\text{AP}} - R_{\text{P}}}{R_{\text{P}}} = \frac{2P_1 P_2}{1 - P_1 P_2}$.
  - Evaluasi karakteristik jembatan Wheatstone TMR ALT023-10E bipolar dan linieritas rentang $\pm 1.0\text{ mT}$.
- [x] **Step 2: Audit teori instrumentasi elektronik & pengkondisi sinyal**
  - Verifikasi formula penguatan AD623: $G = 1 + \frac{100\ \text{k}\Omega}{R_G}$.
  - Verifikasi tegangan referensi: $V_{\text{REF}} = \frac{R_4}{R_3 + R_4} V_{CC} = 2.50\text{ V}$.
  - Verifikasi kuantisasi ADS1115 16-bit: resolusi $0.1875\text{ mV/LSB}$ pada gain 2/3.
- [x] **Step 3: Audit sintesis nanomaterial & fungsionalisasi enzim ADH**
  - Evaluasi mekanisme ikatan kovalen ADH via glutaraldehida terhadap gugus amina/hidroksil nanofiber PVA.
  - Evaluasi reaksi redoks formalin: $\text{HCHO} + \text{H}_2\text{O} + \text{NAD}^+ \xrightarrow{\text{ADH}} \text{HCOOH} + \text{NADH} + \text{H}^+$.
- [x] **Step 4: Audit landasan matematis 4 model Machine Learning**
  - Klasik: Optimasi Lagrangian SVM (dual problem dengan kernel RBF/linear), Ensembel bagging Random Forest (entropi/Gini).
  - Kuantum: *Quantum state preparation* $|\Phi(\mathbf{x})\rangle = U_{\Phi}(\mathbf{x}) |0\rangle^{\otimes n}$, estimasi kernel kuantum $K(\mathbf{x}_i, \mathbf{x}_j) = |\langle\Phi(\mathbf{x}_i)|\Phi(\mathbf{x}_j)\rangle|^2$ pada QSVC, dan optimasi gradien parameter sirkuit $U(\theta)$ pada VQC.
- [x] **Step 5: Dokumentasikan temuan audit Bab II ke laporan evaluasi**

---

### Task 3: Audit Naskah Bab III (Metode Penelitian) — Desain Eksperimen & Validasi Mekatronika
**Files:**
- Audit: `Isi/Metode Penelitian.tex`
- Verifikasi Gambar: `Gambar/Bab3/babIII-desainTMR.png`, `Gambar/Bab3/BABIII_DiagramAlirPenelitian.drawio.png`, `Gambar/Bab3/babIII_skematik_TMR_grounding_fix.png`
- Output Report: `LAPORAN_EVALUASI_PROPOSAL_PASCA_REVISI.md` (Bagian III)

**Interfaces:**
- Input: Naskah Bab III proposal & aset gambar
- Skills: `peer-review`, `cad-physics-validation`, `dfm`, `neurips-experiments`
- Output: Evaluasi metodologi fabrikasi, akuisisi, skema validasi silang, dan metrik uji.

- [x] **Step 1: Audit Gambar 3.1 & desain mekatronika casing baru**
  - Periksa integrasi `babIII-desainTMR.png` di baris 141–146.
  - Pastikan keterangan panel (a) tampak dalam dan (b) tampak luar sudah sinkron dengan gambar fisik.
  - Evaluasi DFM: ventilasi termal kumparan Helmholtz dan kepresisian dudukan kaca preparat di antara kumparan.
- [x] **Step 2: Audit Gambar 3.8 & diagram alir penelitian U-turn Draw.io**
  - Verifikasi bahwa diagram alir mempertahankan topologi profesional *U-turn flow* tanpa kekacauan visual.
  - Periksa konsistensi tahapan: Studi Literatur $\rightarrow$ Analisis Kebutuhan $\rightarrow$ Perancangan Hardware & Software $\rightarrow$ Sintesis Nanofiber $\rightarrow$ Karakterisasi Sensor $\rightarrow$ Pengujian Larutan Formalin $\rightarrow$ Ekstraksi Fitur $\rightarrow$ Komparasi 4 Model $\rightarrow$ Evaluasi Metrik & Analisis.
- [x] **Step 3: Audit protokol akuisisi data & parameter operasional**
  - Verifikasi durasi pengukuran: Lama Detik = 5.0 detik, settling time = 1.0 detik.
  - Verifikasi sapuan medan kumparan Helmholtz: tegangan $0.0 - 16.0\text{ V}$, arus maks $1.6\text{ A}$, resistansi koil $R \approx 10\ \Omega$.
  - Tegaskan bahwa pengaturan arus/tegangan bersifat manual via knob eksternal di meja uji.
- [x] **Step 4: Audit metodologi pemodelan & metrik evaluasi komparatif**
  - Periksa skema pemisahan data (*stratified split* 80:20) dan validasi silang (*5-fold cross-validation*).
  - Evaluasi metrik performa: Akurasi, Presisi, Recall, F1-Score, MCC (*Matthews Correlation Coefficient*), dan ROC-AUC.
- [x] **Step 5: Dokumentasikan temuan audit Bab III ke laporan evaluasi**

---

### Task 4: Audit Bibliografi & Integritas Sitasi (BibTeX & Folder Referensi)
**Files:**
- Audit: `references.bib`, `referensi/catalog.json`, seluruh berkas `.tex` di `Isi/`
- Output Report: `LAPORAN_EVALUASI_PROPOSAL_PASCA_REVISI.md` (Bagian IV)

**Interfaces:**
- Input: `references.bib`, `referensi/`
- Skills: `citation-audit`, `reference-checker`
- Output: Laporan integritas sitasi, daftar referensi terpakai vs tidak terpakai (*orphan keys*), verifikasi keberadaan PDF lokal.

- [x] **Step 1: Ekstraksi seluruh kunci sitasi dari naskah LaTeX**
  - Jalankan skrip analisis untuk mengumpulkan seluruh `\cite{key}` di `Isi/Pendahuluan.tex`, `Isi/Tinjauan Pustaka.tex`, `Isi/Metode Penelitian.tex`.
- [x] **Step 2: Verifikasi silang terhadap references.bib**
  - Pastikan setiap kunci yang disitasi memiliki entri lengkap di `references.bib` (Author, Title, Journal, Year, Volume, Pages, DOI).
  - Deteksi apakah ada sitasi yang hilang (*missing bib entry*).
- [x] **Step 3: Verifikasi ketersediaan berkas PDF di folder `referensi/`**
  - Periksa ketersediaan berkas PDF rujukan utama di folder `referensi/`.
- [x] **Step 4: Dokumentasikan temuan audit bibliografi ke laporan evaluasi**

---

### Task 5: Simulasi Pertahanan Sidang Proposal (*Proposal Defense Radar*)
**Files:**
- Output Report: `LAPORAN_EVALUASI_PROPOSAL_PASCA_REVISI.md` (Bagian V)

**Interfaces:**
- Input: Seluruh naskah proposal & latar belakang riset
- Skills: `research-defense-radar`, `doubt-driven-development`
- Output: 10 pertanyaan paling tajam dosen penguji, analisis jebakan argumen, dan rekomendasi jawaban berbasis bukti eksperimen.

- [x] **Step 1: Identifikasi 10 area rawan pertanyaan penguji**
  - Area 1: Mengapa memilih sensor TMR ALT023-10E dibandingkan Hall effect (A1302) atau GMR?
  - Area 2: Mengapa menggunakan enzim ADH dan bukan formaldehida dehidrogenase (FDH)?
  - Area 3: Mengapa $V_{\text{REF}}$ disetel ke 2.50 V, bukan 1.65 V atau ground?
  - Area 4: Bagaimana mengatasi efek pemanasan Joule pada kumparan Helmholtz ($I \approx 1.6\text{ A}$)?
  - Area 5: Apa urgensi menggunakan model kuantum (QSVC dan VQC) jika dataset sensor hanya berupa data 1D respon tegangan?
  - Area 6: Bagaimana membuktikan bahwa perubahan resistansi TMR murni berasal dari formaldehida dan bukan kelembapan atau asam lain dalam bakso?
  - Area 7: Mengapa menggunakan mikrokontroler Arduino Uno + Raspberry Pi alih-alih hanya mikrokontroler mandiri (ESP32)?
  - Area 8: Bagaimana mengatasi ketidakseimbangan kelas (*class imbalance*) antara sampel bakso kontrol dan bakso berformalin?
  - Area 9: Apa batas deteksi (LOD) teoretis dan regulasi batas maksimum formalin pada pangan menurut BPOM/Permenkes?
  - Area 10: Bagaimana arsitektur *quantum feature map* memetakan fitur ke ruang Hilbert tanpa mengalami *exponential barren plateau*?
- [x] **Step 2: Susun panduan jawaban komprehensif, berbasis data dan teori naskah**

---

### Task 6: Finalisasi Dokumen & Verifikasi Kompilasi LaTeX
**Files:**
- Eksekusi: `scripts/build_proposal.py`
- Laporan Utama: `LAPORAN_EVALUASI_PROPOSAL_PASCA_REVISI.md`

**Interfaces:**
- Input: Perbaikan (jika ada minor tweak) & naskah LaTeX
- Skills: `latex-compile-clean`
- Output: Naskah proposal `skripsi.pdf` terkompilasi sempurna (0 error) dan dokumen laporan review utuh.

- [x] **Step 1: Jalankan kompilasi proposal 4-tahap**
  - Pastikan output `0 LaTeX Error (Sempurna)` dan ukuran file valid.
- [x] **Step 2: Tinjau kelengkapan laporan akhir `LAPORAN_EVALUASI_PROPOSAL_PASCA_REVISI.md`**
- [x] **Step 3: Commit dan push pembaruan ke Git**
