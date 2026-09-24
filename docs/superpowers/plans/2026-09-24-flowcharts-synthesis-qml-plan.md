# Implementation Plan: Pembuatan Diagram Alir Sintesis Nanofiber dan Penyempurnaan Evaluasi Model Kuantum QSVC

## Overview
Rencana kerja ini bertujuan menyempurnakan bagan alir metodologi penelitian pada proposal skripsi Fahry Rizky Samsudin:
1. **Membuat Diagram Alir Baru (Gambar 3.5)**: Diagram Alir Sintesis dan Fabrikasi Nanofiber Komposit \ch{Fe3O4}/PVA-Sitrat-ADH berbasis Draw.io asli (`babIII_DiagramAlirSintesis.drawio.png` dan `.drawio`) untuk memvisualisasikan seluruh tahapan kimia, dispersi sitrat, elektrospinning, dan penautan silang ADH.
2. **Menyempurnakan Gambar 3.8 (Model Building)**: Merombak diagram alir pelatihan model pada Draw.io (`babIIIModelBuilding.drawio.png` dan `.drawio`) agar secara eksplisit memuat percabangan komparasi paralel antara **SVM Klasik** dan **QSVC Kuantum** (*ZZFeatureMap*, *Quantum Kernel Matrix*, dan uji *noise robustness*).
3. **Sinkronisasi Penomoran dan Narasi LaTeX**: Memperbarui berkas `Isi/Metode Penelitian.tex` agar memuat gambar sintesis baru, menyelaraskan label gambar, dan melakukan kompilasi penuh 4-tahap dengan hasil 0 error.

---

## Architecture & Design Decisions
- **Gaya Visual Diagram**: Tetap 100% menggunakan format Draw.io asli (`.drawio.png` dengan metadata embedded `mxfile` dan berkas sumber `.drawio`), warna pastel seragam (*soft green/sage* untuk sintesis material, *soft sky blue* untuk perangkat lunak dan ML), bentuk standar flowchart (oval, persegi panjang, jajar genjang, belah ketupat), dan tipografi bersih (Arial/Helvetica).
- **Struktur Komparasi QML**: Diagram pelatihan model tidak boleh lagi linier satu arah, melainkan membagi data ke dua cabang simetris: SVM Klasik vs QSVC Kuantum, lalu menyatu kembali di metrik evaluasi (*Confusion Matrix, ROC-AUC, Noise Robustness*).
- **Penempatan Gambar Sintesis**: Disisipkan pada awal Subbab 3.4 (*Tahapan Sintesis Sampel Uji*) sebelum Subsubbab 3.4.1 agar menjadi peta panduan visual bagi pembaca dan dosen penguji.

---

## Task List

### Task 1: Desain dan Pembuatan Diagram Alir Sintesis Nanofiber (Gambar 3.5)
**Description:** Merancang berkas Draw.io XML dan mengekspor citra PNG berkualitas tinggi untuk seluruh rantai sintesis material: Prekursor besi $\rightarrow$ Kopresipitasi $\ch{Fe3O4}$ $\rightarrow$ Stabilisasi Penudung Asam Sitrat (*Citrate Capping*) $\rightarrow$ Matriks PVA 11% $\rightarrow$ Pemintalan Elektrospinning (17 kV, 0.6 mL/jam, TCD 14 cm) $\rightarrow$ *Thermal Curing* 130°C + Penautan Silang ADH 2% $\rightarrow$ Membran Nanofiber Siap Pakai.

**Acceptance criteria:**
- [ ] Berkas `babIII_DiagramAlirSintesis.drawio` dibuat dengan format Draw.io XML yang valid dan dapat diedit di diagrams.net.
- [ ] Berkas `babIII_DiagramAlirSintesis.drawio.png` dihasilkan dengan tampilan jernih, proporsional, font Arial, dan warna pastel elegan (soft sage/green).
- [ ] Seluruh tahapan kunci sintesis (termasuk solusi penudung sitrat pencegah sedimentasi dan parameter elektrospinning 17 kV, 0.6 mL/h) tertulis secara sistematis.

**Verification:**
- [ ] Tinjau citra PNG menggunakan `view_file` untuk memastikan tidak ada teks tumpang tindih.
- [ ] Uji ekstraksi metadata `mxfile` dari berkas PNG.

**Dependencies:** None.  
**Files touched:**
- `babIII_DiagramAlirSintesis.drawio`
- `babIII_DiagramAlirSintesis.drawio.png`
**Estimated scope:** Small (2 files).

---

### Task 2: Redesain Gambar 3.8 untuk Komparasi Paralel SVM vs QSVC (Model Building)
**Description:** Memperbarui diagram Draw.io `babIIIModelBuilding.drawio` dan `babIIIModelBuilding.drawio.png` dari struktur linier sederhana menjadi struktur percabangan komparatif dua jalur (Dual-track Branching) yang merefleksikan evaluasi model kuantum secara persis.

**Acceptance criteria:**
- [ ] Dataset fitur sinyal TMR ($V_{\text{mean}}, \Delta V, \sigma_V$) dibagi menjadi Data Latih dan Data Uji.
- [ ] Jalur Model Klasik: SVM dengan Kernel RBF/Linear dan GridSearch parameter ($C, \gamma$).
- [ ] Jalur Model Kuantum: QSVC dengan *ZZFeatureMap* (encoding ruang Hilbert) dan penghitungan *Quantum Kernel Matrix* ($K_Q$).
- [ ] Jalur Evaluasi Bersama: Evaluasi Komparatif (Akurasi, Presisi, Recall, F1-Score, Confusion Matrix, ROC-AUC) serta Uji Ketahanan Derau (*Noise Robustness Test*).
- [ ] Berkas `babIIIModelBuilding.drawio` dan `babIIIModelBuilding.drawio.png` tersimpan dengan metadata embedded.

**Verification:**
- [ ] Tinjau citra `babIIIModelBuilding.drawio.png` menggunakan `view_file`.
- [ ] Pastikan tata letak 2 kolom tetap seimbang, rapi, dan konsisten dengan format Draw.io Gilang.

**Dependencies:** None.  
**Files touched:**
- `babIIIModelBuilding.drawio`
- `babIIIModelBuilding.drawio.png`
**Estimated scope:** Small (2 files).

---

### Task 3: Integrasi Gambar dan Penyelarasan Narasi pada `Isi/Metode Penelitian.tex`
**Description:** Memasukkan Gambar 3.5 ke dalam Subbab 3.4 (*Tahapan Sintesis Sampel Uji*), memperbarui pemanggilan Gambar 3.8, dan menyelaraskan seluruh penomoran label gambar (`\label{fig:...}`) serta kalimat pengantar di sekitarnya.

**Acceptance criteria:**
- [ ] Gambar 3.5 terpasang menggunakan `\includegraphics[width=...]{babIII_DiagramAlirSintesis.drawio.png}` di bawah judul Subbab 3.4 dengan caption "Diagram Alir Sintesis dan Fabrikasi Nanofiber Komposit \ch{Fe3O4}/PVA-Sitrat-ADH".
- [ ] Narasi pengantar Subbab 3.4 merujuk ke Gambar 3.5.
- [ ] Gambar 3.8 (Model Building) diperbarui caption dan narasinya agar menerangkan komparasi paralel SVM vs QSVC.
- [ ] Tidak ada label ganda atau referensi gambar yang rusak.

**Verification:**
- [ ] Periksa sintaks LaTeX pada file `Isi/Metode Penelitian.tex`.

**Dependencies:** Task 1, Task 2.  
**Files touched:**
- `Isi/Metode Penelitian.tex`
**Estimated scope:** Small (1 file).

---

### Task 4: Kompilasi Penuh 4-Tahap LaTeX dan Verifikasi Visual Akhir
**Description:** Menjalankan pipeline kompilasi penuh (`pdflatex` $\rightarrow$ `bibtex` $\rightarrow$ `pdflatex` $\rightarrow$ `pdflatex`) dan memverifikasi kualitas dokumen akhir `skripsi.pdf`.

**Acceptance criteria:**
- [ ] Kompilasi menghasilkan exit code 0.
- [ ] Log kompilasi bebas dari `Error`, `Fatal Error`, dan `Undefined references`.
- [ ] Seluruh diagram alir (Gambar 3.1, 3.5, 3.6, 3.7, 3.8, 3.9) tampil presisi pada halaman masing-masing tanpa terpotong (*no overfull vbox*).

**Verification:**
- [ ] Jalankan perintah kompilasi di PowerShell.
- [ ] Periksa ukuran dan timestamp file `skripsi.pdf`.

**Dependencies:** Task 3.  
**Files touched:**
- `skripsi.pdf`
- `skripsi.log`
**Estimated scope:** Small (verification).

---

## Checkpoint: Rencana Siap Dijalankan
- [ ] Rencana diverifikasi dan disetujui pengguna untuk dieksekusi.
