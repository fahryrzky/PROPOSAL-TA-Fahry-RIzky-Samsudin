# LAPORAN DIAGNOSTIK REVIEW AKADEMIK PROPOSAL PENELITIAN TUGAS AKHIR
**Standar Evaluasi**: *Academy of Management Journal (AMJ)*, *Academy of Management Review (AMR)*, *Journal of the Academy of Marketing Science (JAMS)*, serta Jurnal Internasional Terindeks Scopus Q1/Q2 (*IEEE Sensors Journal*, *Sensors and Actuators B: Chemical*, *Biosensors and Bioelectronics*).

---

### Identitas Naskah yang Ditelaah
- **Judul Proposal**: *Rancang Bangun Instrumentasi Sensor Tunneling Magnetoresistance Berbasis Nanofiber $\text{Fe}_3\text{O}_4$/PVA-Sitrat-ADH untuk Deteksi Formalin pada Bakso Menggunakan Komparasi Model SVM dan QSVC*
- **Peneliti**: Fahry Rizky Samsudin (NIM: 1237030018)
- **Institusi**: Jurusan Fisika, Fakultas Sains dan Teknologi, UIN Sunan Gunung Djati Bandung
- **Tahun**: 2026
- **Dokumen Sumber**: `Isi/Pendahuluan.tex`, `Isi/Tinjauan Pustaka.tex`, `Isi/Metode Penelitian.tex`, `skripsi.tex`, `references.bib`, serta rangkaian skematik & kode instrumentasi.

---

## 1. Top-Line Editorial Verdict & Status Naskah

### 1.1 Penilaian Status Saat Ini (*Current State Judgment*)
**Status**: *Viable with Focused Revision* (Sangat Layak untuk Seminar Proposal dengan Perbaikan Terfokus pada Konsistensi Internal dan Justifikasi Metodologis).

Naskah proposal ini memiliki fondasi rekayasa fisik dan instrumentasi yang solid, eksekusi hardware yang berada di atas rata-rata tugas akhir sarjana fisika, serta artikulasi kimia material yang telah berhasil mengoreksi jebakan penggunaan glutaraldehida beracun dengan memisahkan peran asam sitrat (*green crosslinker* & *capping agent*) dan ADH (*chemo-receptor*). Namun demikian, terdapat inkonsistensi internal antarbab yang fatal jika diuji oleh reviewer kritis atau dewan penguji:
1. Inkonsistensi ruang lingkup pemodelan (Judul dan Bab I hanya menjanjikan SVM vs. QSVC, namun Bab III tiba-tiba memunculkan *Random Forest* dan *Variational Quantum Classifier*).
2. Kontradiksi ekstraksi fitur (Bab I menjanjikan 5 fitur domain waktu, sedangkan Bab III Subbab 3.4.5 hanya menjabarkan 3 fitur).
3. Hilangnya pustaka kuantum (`qiskit` / `pennylane`) pada Tabel 3.2 (*Software*).
4. Ketiadaan spesifikasi nilai nominal resistor gain $R_G$ pada rangkaian AD623.

### 1.2 Potensi Naskah ke Depan (*Upside Potential*)
**Prospek**: *Strong path to High-Grade Thesis & Scopus Q1/Q2 Publication* (*Sensors and Actuators B: Chemical* atau *IEEE Sensors Journal*).

Jika celah mekanisme transduksi magnetik (bagaimana reaksi hidrazon memodulasi medan magnet bocor partikel $\text{Fe}_3\text{O}_4$) diperjelas dengan model fisis, dan batas komputasi kuantum QSVC diartikulasikan secara jujur tanpa *overclaiming* keunggulan kuantum mutlak (*quantum supremacy/advantage*) pada data berdimensi rendah, penelitian ini memiliki nilai kebaruan multidisiplin yang sangat langka: integrasi nanomaterial pintar, transduser kuantum TMR, dan algoritma *quantum machine learning*.

### 1.3 Preamble Status Naskah (*Manuscript State Preamble*)
- **Bagian Siap**: Bab I, Bab II, dan Bab III telah terkompilasi bersih tanpa *error* di LaTeX dengan dokumen induk `skripsi.tex`.
- **Bagian Mengambang/Draft**: File `Isi/Profil Industri.tex` masih tertinggal di direktori (berisi sitasi angka `\cite{15}` dan `\cite{6}` peninggalan format PKL/magang), namun telah berhasil diisolasi dan tidak di-*input* ke dalam `skripsi.tex`.
- **Tabel & Gambar**: Seluruh gambar Bab I, II, dan III telah direferensikan dengan baik, namun terdapat catatan pada skematik hardware terkait pelabelan nilai $R_G$.

---

## 2. Kontribusi Aktual vs. Kontribusi yang Diklaim vs. Persepsi Reviewer Skeptis

| Dimensi | Kontribusi yang Diklaim (*Claimed Contribution*) | Kontribusi Aktual (*Actual Contribution*) | Persepsi Reviewer Skeptis (*Skeptical Reviewer*) |
|---|---|---|---|
| **Transduser & Instrumentasi** | Rancang bangun instrumentasi TMR beresolusi tinggi (rasio TMR $>200\%$, sensitivitas 15--25 mV/V/mT) menggantikan sensor GMR untuk deteksi formalin sub-ppm. | Implementasi rangkaian analog AD623 ($V_{REF}=2,50$ V) dan ADC ADS1115 16-bit untuk membaca jembatan TMR ALT023-10E dalam kumparan Helmholtz terkalibrasi. | Modul sensor komersial (NVE ALT023-10E) yang dirangkai dengan IC instrumentasi standar; bukan fabrikasi chip sensor baru melainkan integrasi sistem tingkat papan (PCB). |
| **Material Reseptor** | Sintesis nanofiber hijau $\text{Fe}_3\text{O}_4$/PVA-Sitrat-ADH dengan pemisahan peran asam sitrat (*thermal curing* $130^\circ\text{C}$) dan ADH (reseptor spesifik hidrazon). | Fabrikasi membran elektropuntal (*electrospun*) PVA-$\text{Fe}_3\text{O}_4$ yang distabilkan sitrat dan direndam ADH untuk menangkap formaldehida cair/uap. | Modifikasi protokol literatur yang menggabungkan dispersi sitrat dan perendaman ADH; pengujian selektivitas terhadap molekul volatil bumbu bakso lainnya belum dibuktikan secara eksperimental. |
| **Pemodelan Cerdas (QML)** | Komparasi perdana model klasik SVM kernel RBF vs model kuantum QSVC ruang Hilbert ($ZZ\text{FeatureMap}$) dengan ketahanan derau (*noise resilience*). | Tolok ukur (*benchmarking*) algoritma SVM klasik vs simulasi QSVC (*statevector*) berbasis Qiskit pada dataset tabular berukuran kecil (3--5 fitur sinyal). | *Toy-problem quantum ML*: menerapkan QSVC pada data berdimensi sangat rendah yang sebenarnya dapat diselesaikan secara tuntas oleh regresi kuadrat terkecil atau SVM linear sederhana. |

**Diagnosis Kesenjangan (*Gap Diagnosis*)**:
Klaim kebaruan naskah berada pada tingkat **rekabentuk terpadu (*integrated system novelty*)** dan **interdisipliner (material-elektronika-kuantum)**. Bahaya utama yang harus dihindari oleh penulis adalah *overclaiming* pada aspek QML: jangan mengeklaim QSVC "pasti mengungguli SVM karena memanfaatkan superposisi dan keterikatan kuantum", melainkan posisikan sebagai *studi eksploratif kelayakan representasi kernel kuantum pada data instrumentasi sensor kimia*.

---

## 3. Aset Terkuat Naskah (Hal yang Wajib Dipertahankan)

1. **Integritas Rantai Sinyal Analog-ke-Digital (*Signal Chain Rigor*)**:
   Arsitektur perangkat keras dirancang sangat disiplin. Pemilihan AD623 dengan catu daya tunggal $+5$ V yang digeser ke $V_{REF} = 2,50$ V (bukan membiarkannya mengambang atau 0 V) menunjukkan pemahaman mendalam tentang penanganan sinyal diferensial bipolar sensor jembatan Wheatstone. Integrasi filter RFI diferensial/common-mode, tapis lolos-rendah anti-aliasing, pemisahan ground analog (AGND) dan digital (DGND), serta ADC 16-bit ADS1115 pada skala $\pm 6,144$ V merupakan eksekusi metrologis tingkat tinggi.

2. **Rasionalisasi Kimia Material yang Elegan**:
   Pemisahan peran fungsional antara asam sitrat dan ADH pada Subbab 1.1 dan Subbab 2.1.8--2.1.10 merupakan lompatan konseptual yang sangat kuat. Menghilangkan glutaraldehida (GA) yang selama ini menjadi kontradiksi dalam deteksi formalin (karena GA sendiri adalah dialdehida yang toksik dan mengacaukan situs aldehida) dan menggantikannya dengan esterifikasi termal asam sitrat $130^\circ\text{C}$ adalah keunggulan ilmiah yang harus dipertahankan dan ditonjolkan.

3. **Rekayasa Firmware dan Software Akuisisi Waktu-Nyata**:
   Pemilihan akuisisi berbasis durasi waktu (*Duration-Based Acquisition*, 5.0 detik) dengan pembuangan waktu stabilisasi awal (*settling time*, 1.0 detik) pada modul `DurationAcquisitionEngine` adalah keputusan praktis laboratorium yang sangat tepat untuk mengeliminasi lonjakan transien mekanis dan hidrodinamis saat sampel diteteskan.

---

## 4. Audit Logika Penjelasan & Mekanisme Fisis-Kimiawi Transduksi

### 4.1 Celah Penjelasan Transduksi Magnetik (P5p3 vs P12p2)
- **Masalah**: Bagaimana persisnya pembentukan ikatan hidrazon ($\text{ADH} + \text{Formalin} \rightarrow \text{Hidrazon} + \text{Air}$) dapat mengubah medan magnetik yang dirasakan oleh sensor TMR di bawahnya?
- **Analisis Kritis**: Molekul formaldehida dan ADH bersifat diamagnetik dengan suseptibilitas magnetik negatif yang sangat kecil ($\chi \sim -10^{-6}$). Ikatan kimia antara gugus aldehida dan hidrazida tidak memiliki momen magnetik tak berpasangan (*unpaired electron spins*). Oleh karena itu, perubahan medan magnetik tidak berasal dari molekul formaldehida itu sendiri.
- **Rekomendasi Perbaikan**: Naskah harus menguraikan hipotesis fisis kopling magneto-mekanik atau magneto-elastis:
  1. *Steric Hindrance & Nanofiber Swelling/Shrinkage*: Pembentukan ikatan hidrazon kovalen mengubah konformasi rantai polimer PVA/ADH, menyebabkan pengerutan atau pembengkakan mikro matriks serat. Perubahan volume ini menggeser jarak rata-rata nanopartikel $\text{Fe}_3\text{O}_4$ relatif terhadap permukaan sensor TMR (jarak $z$ berkurang/bertambah), yang secara eksponensial memodulasi fluks medan magnet bocor (*stray field*) yang menembus MTJ sesuai hukum Biot-Savart / dipol magnetik ($B \propto 1/z^3$).
  2. *Surface Charge & Dipole Redistribution*: Transfer muatan lokal pada permukaan nanopartikel yang terlapisi sitrat akibat interaksi hidrazon memodifikasi anisotropi magnetik permukaan partikel $\text{Fe}_3\text{O}_4$.
  
  *Tindakan*: Tegaskan hipotesis mekanisme ini pada Subbab 2.1.10 dan Subbab 3.4.4 agar tidak dianggap sebagai "lompatan logika gaib" oleh penguji fisika material.

### 4.2 Latar Belakang Diamagnetik Tetesan Cairan (*Aqueous Droplet Artifact*)
- **Masalah**: Sampel bakso diteteskan dalam bentuk larutan/ekstrak cair. Air murni memiliki suseptibilitas diamagnetik $\chi_v \approx -9{,}0 \times 10^{-6}$. Penetesan droplet cairan di atas sensor TMR dalam medan Helmholtz dapat membiaskan fluks magnetik secara lokal semata-mata karena keberadaan medium air, terlepas dari keberadaan formalin.
- **Rekomendasi**: Tambahkan penjelasan kontrol negatif: pengujian harus membandingkan tetesan akuades murni (tanpa formalin) terhadap tetesan ekstrak bakso berformalin untuk membuktikan bahwa $\Delta V$ berasal dari interaksi analit-reseptor, bukan semata efek pembiasan cairan (*liquid loading effect*).

---

## 5. Audit Operasionalisasi Konstruk, Metrologi & Rantai Perangkat Keras

### 5.1 Oposisi Nilai Resistor Gain $R_G$ pada AD623
- **Lokasi Masalah**: Bab III, Tabel 3.3 (Bahan) baris 3-5, dan Subbab 3.3.2 butir c (persamaan $G = 1 + 100\,\text{k}\Omega / R_G$).
- **Temuan**: Tabel 3.3 mencantumkan "Resistor 1k $\Omega$ (4 buah)", "Resistor 10k $\Omega$ (1 buah)", dan "Resistor 4,7k $\Omega$ (2 buah)". Teks menyebutkan bahwa $R_G$ dipasang pada jumper, tetapi **tidak ada nilai nominal pasti yang dinyatakan untuk $R_G$**.
- **Konsekuensi Metrologis**: 
  - Jika $R_G = 1{,}0\,\text{k}\Omega$, maka $G = 1 + 100/1 = 101$.
  - Sensitivitas sensor TMR adalah $\sim 200\,\text{mV/V/mT} \times 5\,\text{V} = 1000\,\text{mV/mT} = 1{,}0\,\text{V/mT}$.
  - Dengan penguatan $G = 101$, perubahan medan sebesar $0{,}01\,\text{mT}$ ($10\,\mu\text{T}$) akan menghasilkan perubahan tegangan $\Delta V = 1{,}01\,\text{V}$! Rentang dinamis sensor akan sangat cepat jenuh (*saturated*) pada catu 5 V.
  - Jika $R_G$ tidak dipasang (pin 1 dan 8 terbuka), $G = 1$.
- **Rekomendasi Perbaikan**: Tuliskan secara eksplisit nilai nominal $R_G$ yang digunakan (misalnya $R_G = 10\,\text{k}\Omega$ untuk $G = 11$, atau nilai presisi lainnya) dan hitung anggaran rentang dinamik tegangan keluaran ($V_{out} = 2{,}50\,\text{V} \pm \Delta V_{max}$) agar dewan penguji melihat kalkulasi instrumentasi yang presisi.

### 5.2 Pengaturan Medan Kumparan Helmholtz: Manual vs. Otomatis
- **Lokasi Masalah**: Bab III Subbab 3.4.1 dan GUI software.
- **Temuan**: Sesuai dengan spesifikasi *Ground Truth* sistem, kumparan Helmholtz dicatu oleh power supply DC eksternal dengan kenop putar manual di meja lab. Parameter $V_{helm}, I_{helm}$, dan $B_{teslameter}$ pada GUI dimasukkan secara manual sebagai data *ground truth*.
- **Rekomendasi**: Pastikan teks Bab III tidak memberi impresi palsu bahwa mikrokontroler atau Raspberry Pi mengontrol arus kumparan Helmholtz secara otomatis via DAC/PWM. Nyatakan secara lugas bahwa medan acuan disapu secara manual melalui power supply DC terkalibrasi.

---

## 6. Audit Pemodelan Komputasi, QML (QSVC), dan Metodologi Machine Learning

### 6.1 Inkonsistensi Ruang Lingkup Algoritma (Judul vs Bab I vs Bab III)
- **Lokasi Masalah**: 
  - Judul: "...Menggunakan Komparasi Model SVM dan QSVC"
  - Bab I (Tujuan butir 4): "...antara model SVM klasik dan QSVC kuantum..."
  - Bab III (Subbab 3.4.6 & 3.4.7): Tiba-tiba memasukkan **Random Forest (RF)** (Subbab 3.4.6 butir 1) dan **Variational Quantum Classifier (VQC)** (Subbab 3.4.7 butir 2), serta mengevaluasi 4 model sekaligus pada Subbab 3.4.8!
- **Analisis Kritis**: Ketidaksinkronan ini merupakan ciri khas draft yang mengalami tambal-sulam (*scope creep*). Jika penulis ingin membandingkan 4 model, judul dan tujuan di Bab I harus diubah. Namun, jika fokus skripsi adalah SVM vs QSVC (yang memiliki padanan matematis setara karena QSVC pada dasarnya adalah SVM dengan kernel kuantum), maka keberadaan RF dan VQC di Bab III menjadi redundan dan mengaburkan fokus penelitian.
- **Rekomendasi Perbaikan**: **Pangkas RF dan VQC dari Bab III**. Pertahankan fokus ketat pada SVM (klasik) versus QSVC (kuantum). Hal ini menjaga konsistensi mutlak dari Judul, Rumusan Masalah, Batasan Masalah, Tujuan, hingga Metodologi.

### 6.2 Kontradiksi Ekstraksi Fitur Sinyal Sensor
- **Lokasi Masalah**: 
  - Bab I Halaman 2 Paragraf 6: Menjanjikan **5 fitur domain waktu**: tegangan puncak ($V_{peak}$), tegangan tunak rata-rata ($\overline{V}_{steady}$), delta respons ($\Delta V$), laju perubahan transien ($dV/dt$), dan integral area sinyal.
  - Bab III Subbab 3.4.5: Hanya merinci **3 fitur**: $V_{mean}$, $\Delta V$, dan $\sigma_V$.
- **Rekomendasi Perbaikan**: Sinkronkan kedua bagian ini! Mengingat QSVC disimulasikan pada komputer klasik menggunakan $ZZ\text{FeatureMap}$, jumlah fitur $d$ menentukan jumlah qubit $n$ yang disimulasikan ($n = d$). 
  - Jika menggunakan 3 fitur ($V_{mean}, \Delta V, \sigma_V$), sirkuit kuantum membutuhkan 3 qubit ($2^3 = 8$ dimensi ruang Hilbert). Ini sangat ringan, cepat disimulasikan di Raspberry Pi 5 / PC, dan stabil.
  - Jika menggunakan 5 fitur, dibutuhkan 5 qubit ($2^5 = 32$ dimensi ruang Hilbert).
  - *Saran*: Putuskan secara definitif untuk menggunakan 3 fitur atau 5 fitur, lalu terapkan secara konsisten di Bab I, Bab II, dan Bab III.

### 6.3 Pustaka Software Komputasi Kuantum Hilang dari Tabel 3.2
- **Lokasi Masalah**: Bab III Tabel 3.2 (*Software yang Digunakan*).
- **Temuan**: Tabel memuat scikit-learn, pandas, numpy, scipy, matplotlib, tetapi **sama sekali tidak memuat pustaka Quantum Machine Learning** seperti `qiskit` (dan `qiskit-machine-learning`) atau `pennylane`.
- **Rekomendasi**: Wajib menambahkan baris `Qiskit 1.x / Qiskit Machine Learning` ke dalam Tabel 3.2 sebagai legalitas komputasi implementasi QSVC.

---

## 7. Audit Penjelasan Alternatif, Faktor Perancu (*Confounders*), dan Efek Matriks

Reviewer analitik kimia dan sensor keamanan pangan pasti akan menguji aspek selektivitas dan faktor perancu pangan nyata (*real meat matrix*):

1. **Interferensi Asam Asetat dan Senyawa Volatil Bumbu Bakso**:
   Bakso mengandung bawang putih (senyawa sulfur volatil seperti allisin/dialil disulfida), cuka/asam asetat, garam ($NaCl$), dan monosodium glutamat (MSG). Gugus hidrazida ADH memang sangat selektif terhadap gugus karbonil, tetapi senyawa keton alami atau aldehida endogen pangan dapat menjadi kompetitor minor.
   - *Rekomendasi*: Tambahkan penjelasan di Bab I dan Bab III bahwa penelitian ini menetapkan uji selektivitas menggunakan senyawa interferen bumbu (asam asetat, glukosa/sukrosa) sebagai pengujian pembanding, atau nyatakan secara jujur di Batasan Masalah sebagai asumsi pengujian awal.

2. **Daya Tahan Hidrolitik Nanofiber PVA terhadap Air Matriks Bakso**:
   Meskipun telah di-*curing* asam sitrat pada suhu $130^\circ\text{C}$, perendaman berulang atau kontak langsung dengan tetesan filtrat bakso berlemak dapat menyebabkan pembengkakan membran (*swelling*) atau pelapisan lemak (*lipid fouling*).
   - *Rekomendasi*: Tegaskan bahwa membran nanofiber pada sensor TMR ini dirancang sebagai *disposable sensing strip* (sekali pakai per strip uji) atau dapat dibersihkan dengan pembilasan akuades/etanol terkontrol.

---

## 8. Audit Desain Eksperimental, Rencana Sampling, dan Validitas Statistik

1. **Rencana Pengambilan Sampel ($N$) dan Ukuran Data untuk ML**:
   - Berapa jumlah bakso kontrol dan bakso berformalin yang diuji?
   - Berapa konsentrasi formalin standar? (Di Bab III: 1, 5, 10, 25, 50, dan 100 mg/L = 6 titik konsentrasi).
   - Berapa replikasi per titik? (Disarankan minimal 5--10 kali replikasi per konsentrasi).
   - *Peringatan Data Leakage*: Jika 500 sampel tegangan per detik diambil dari satu tetesan yang sama, itu adalah *autocorrelated time series*, bukan sampel independen. Melatih SVM/QSVC pada potongan-potongan jendela dari tetesan yang sama tanpa *group-splitting* akan menyebabkan kebocoran data (*data leakage*) dan akurasi semu 100%. Penulis harus menegaskan bahwa unit data yang masuk ke model ML adalah **satu vektor fitur per tetesan pengujian independen**, atau menggunakan *GroupKFold* berdasarkan nomor sampel pengujian.

2. **Perhitungan Limit of Detection (LOD)**:
   - Sesuai kaidah IUPAC, rumus LOD adalah:
     $$\text{LOD} = \frac{3 \times \sigma_{\text{blank}}}{m}$$
     dengan $\sigma_{\text{blank}}$ adalah simpangan baku dari respons blanko (konsentrasi 0 mg/L) dan $m$ adalah gradien sensitivitas kurva kalibrasi ($\Delta V / \Delta C$).
   - Pastikan rumus ini dituliskan secara eksplisit di Bab II atau Bab III sebagai landasan matematis penentuan LOD.

---

## 9. Section-by-Section Sweep (Penyisiran Menyeluruh Per Bagian)

### 9.1 Bab I: Pendahuluan
- **Paragraf 1 (Latar Belakang)**: Sangat tajam dan terdata baik (mengutip kasus Padang, Pekanbaru 4,506 ppm, Yogyakarta, serta ambang EFSA 100 ppm).
- **Paragraf 2--3 (State-of-the-Art Sensor)**: Transisi dari laboratorium (HPLC/spektro) ke sensor MOS, elektrokimia, dan optik sangat runtut. Keterbatasan enzim FDH dijelaskan secara akurat.
- **Paragraf 4 (Inovasi Material Nanofiber)**: Narasi pemisahan peran asam sitrat dan ADH sangat baik dan orisinal.
- **Paragraf 5--6 (TMR & Komputasi Cerdas)**: Kontras TMR terhadap GMR terdahulu jelas. Catatan: samakan jumlah fitur (3 fitur vs 5 fitur) dengan Bab III.
- **Rumusan & Batasan Masalah**: Rumusan nomor 4 menyebutkan SVM vs QSVC; batasan masalah nomor 6 konsisten dengan SVM vs QSVC.

### 9.2 Bab II: Tinjauan Pustaka
- **Subbab 2.1.2 (TMR)**: Persamaan Julliere (Persamaan 2.1) dan persamaan tegangan keluaran jembatan (Persamaan 2.2) tepat.
- **Subbab 2.1.3 (Helmholtz)**: Penurunan Biot-Savart hingga rumus medan di pusat kumparan (Persamaan 2.4) sangat akademis dan elegan.
- **Subbab 2.1.4 (In-Amp)**: Persamaan gain AD623 dituliskan dengan konstanta internal $100\,\text{k}\Omega$ yang tepat.
- **Subbab 2.1.8--2.1.10 (Material Nanofiber)**: Rincian reaksi esterifikasi asam sitrat ($130^\circ\text{C}$) dan reaksi pembentukan ikatan hidrazon ADH sangat mendalam.
- **Subbab 2.1.11 & 2.1.12 (SVM & QSVC)**: Penjelasan pemetaan ruang Hilbert melalui gerbang $ZZ\text{FeatureMap}$ dan estimasi kernel kuantum $K_Q$ ditulis dengan notasi braket Dirac yang presisi.
- **Tabel 2.1 (Matriks Penelitian Terdahulu)**: Komparasi studi Wang (2021), Singhal (2024), Sun (2023), Gilang (2026), dan Fahry (2026) sangat informatif dan memetakan gap dengan tegas.

### 9.3 Bab III: Metode Penelitian
- **Tabel 3.1 (Alat)**: Lengkap.
- **Tabel 3.2 (Software)**: Perlu menambahkan baris `Qiskit` / simulator kuantum.
- **Tabel 3.3 (Bahan)**: Tambahkan nilai nominal $R_G$ pada rangkaian pengkondisi sinyal.
- **Gambar 3.1 (Diagram Alir Penelitian)**: Blok alir langkah 1--8 telah mencakup seluruh spektrum penelitian secara komprehensif.
- **Gambar 3.4 (Skematik Rangkaian)**: Skematik `babIII_skematik_TMR_grounding_fix.png` telah menerapkan pembagi tegangan $V_{REF}=2,50$ V dengan baik.
- **Subbab 3.4.6 & 3.4.7 (Model Machine Learning)**: Pangkas Random Forest dan VQC agar konsisten dengan fokus utama SVM vs QSVC.

---

## 10. Audit Sitasi & Konsistensi Referensi Dua Arah (*Bidirectional Citation Audit*)

Berdasarkan audit komputasional terprogram terhadap seluruh berkas naskah aktif (`Header/`, `Isi/Pendahuluan.tex`, `Isi/Tinjauan Pustaka.tex`, `Isi/Metode Penelitian.tex`, dan `references.bib`):

### 10.1 Sitasi dalam Naskah vs Entri BibTeX
- **Total Sitasi Aktif dalam Naskah**: 44 sitasi unik.
- **Total Entri dalam `references.bib`**: 73 entri.
- **Sitasi dalam Teks yang Hilang dari `.bib` (*Orphaned in Text*)**: **0 entri (NIHIL / BERSIH 100%)**. Seluruh 44 referensi yang dipanggil dalam teks proposal aktif memiliki entri sah di `references.bib`.
- **Entri dalam `.bib` yang Tidak Disitasi dalam Teks Aktif (*Unused in Text*)**: **29 entri**.
  - Rincian entri yang tidak terpakai: `Au2018`, `Breiman2001`, `Scornet2015`, `Tyralis2019`, `antarnusa2018`, `antarnusa2025TEOS`, `ardiyanti2023new`, `arduino2022`, `calixto2025`, `dey2025`, `difilippo2023`, `ennen2016giant`, `giaretta2024`, `kushwaha2023`, `literatureGlucose`, `mohanty2021`, `nainggolan2023`, `nve2025`, `piekarz2024`, `pythonorg`, `ricci2023smart`, `rifai2016giant`, `sanaeifar2017`, `sun2023`, `ti_lm358_datasheet`, `ti_lm358_guidelines`, `touil2022simple`, `vitayaya2024magnetoresistance`, `wibowo2023gmr`.
  - *Catatan Kurasi*: Entri `Breiman2001`, `Scornet2015`, `Tyralis2019` adalah referensi *Random Forest*. Karena RF dipangkas dari metodologi, tidak disitasinya entri ini adalah normal. Entri `ti_lm358_*` adalah peninggalan rangkaian GMR lama sebelum beralih ke AD623.

### 10.2 Berkas Tidak Aktif (`Isi/Profil Industri.tex`)
- File `Isi/Profil Industri.tex` memuat sitasi numerik mentah `\cite{15}` dan `\cite{6}`. Berkas ini merupakan artefak lama yang tidak disertakan dalam `skripsi.tex`. Direkomendasikan untuk dihapus atau diarsipkan ke folder scratch agar tidak menimbulkan kebingungan di masa depan.

---

## 11. Antisipasi Keberatan Penguji & Reviewer Kritis (*Anticipating the Room*)

Berikut adalah 7 sanggahan/pertanyaan tajam yang paling mungkin dilontarkan oleh dewan penguji seminar proposal atau reviewer jurnal, beserta strategi argumentasi pertahanannya:

1. **Keberatan 1 (Mekanika Transduksi)**:
   > *"Formalin dan ADH adalah molekul non-magnetik. Bagaimana Anda bisa mengklaim bahwa reaksi keduanya mengubah tegangan sensor magnetik TMR?"*
   - **Tanggapan/Pertahanan**: Tegaskan bahwa transduksi bekerja secara tidak langsung melalui modulasi medan magnetik bocor (*stray field perturbation*) dari nanopartikel superparamagnetik $\text{Fe}_3\text{O}_4$. Reaksi pembentukan ikatan hidrazon kovalen menginduksi pergeseran konformasi atau distorsi jarak mekanis nanopartikel $\text{Fe}_3\text{O}_4$ dalam matriks nanofiber PVA-sitrat relatif terhadap permukaan sensor MTJ di bawahnya, yang memodulasi gradien fluks magnetik bias kumparan Helmholtz.

2. **Keberatan 2 (Skalabilitas & Relevansi Quantum Machine Learning)**:
   > *"Mengapa harus menggunakan QSVC yang rumit dan berat jika fitur sinyal Anda hanya 3 buah dan data Anda dapat dipisahkan dengan mudah oleh regresi linear atau SVM biasa?"*
   - **Tanggapan/Pertahanan**: Akui secara objektif bahwa untuk data linear murni, SVM klasik sudah cukup. Namun, respons biosensor pada matriks pangan nyata (bakso) memiliki efek derau matriks biologis dan fluktuasi non-linear yang kompleks. Penggunaan QSVC dalam penelitian ini bukan untuk klaim *quantum supremacy*, melainkan pengujian komparatif eksploratif mengenai apakah pemetaan ruang Hilbert kuantum ($ZZ\text{FeatureMap}$) memberikan batas keputusan (*decision boundary*) yang memiliki ketahanan derau (*noise resilience*) lebih tinggi terhadap derau biologis pangan dibandingkan kernel RBF klasik.

3. **Keberatan 3 (Selektivitas Reseptor Pangan)**:
   > *"Di dalam bakso terdapat senyawa volatil lain seperti cuka (asam asetat) dan bumbu. Apakah ADH tidak bereaksi dengan senyawa-senyawa tersebut?"*
   - **Tanggapan/Pertahanan**: Asam asetat memiliki gugus karboksilat ($-COOH$), bukan gugus aldehida bebas ($-CHO$). Reaktivitas gugus hidrazida ADH terhadap aldehida jauh lebih cepat dan spontan pada suhu ruang membentuk ikatan hidrazon dibandingkan terhadap asam karboksilat atau ester, sehingga memberikan keunggulan spesifisitas termodinamika yang tinggi.

4. **Keberatan 4 (Stabilitas Nanofiber Terhadap Air)**:
   > *"PVA adalah polimer yang larut air. Saat ekstrak bakso cair diteteskan, bukankah seratnya akan hancur dan membubarkan partikel besi?"*
   - **Tanggapan/Pertahanan**: PVA murni memang larut air, tetapi nanofiber dalam penelitian ini telah melalui proses *thermal curing* dengan asam sitrat pada suhu $130^\circ\text{C}$ selama 1,5 jam. Reaksi esterifikasi kovalen antara gugus karboksil asam sitrat dan gugus hidroksil PVA membentuk jejaring tiga dimensi tak larut air (*water-insoluble crosslinked network*) yang terbukti mempertahankan integritas morfologi serat dalam media berair.

5. **Keberatan 5 (Metrologi & Pengaturan Medan Helmholtz)**:
   > *"Apakah kumparan Helmholtz ini dikontrol otomatis oleh Arduino untuk menyapu medan magnet?"*
   - **Tanggapan/Pertahanan**: Tidak. Kumparan Helmholtz dicatu oleh power supply DC terkalibrasi eksternal dengan pengaturan arus manual presisi di meja lab. Parameter medan dicatat menggunakan teslameter referensi sebagai *ground truth* metrologis untuk mengalibrasi respons dasar sensor TMR sebelum pengujian analit.

6. **Keberatan 6 (Resistor Gain $R_G$ pada AD623)**:
   > *"Berapa penguatan tegangan sebenarnya pada rangkaian analog AD623 Anda?"*
   - **Tanggapan/Pertahanan**: Tunjukkan skema perhitungan gain $G = 1 + 100\,\text{k}\Omega / R_G$ dengan nilai nominal resistor $R_G$ yang telah dipilih, membuktikan bahwa tegangan keluaran sensor tidak mengalami saturasi (*clipping*) pada batas catu 0--5 V.

7. **Keberatan 7 (Ukuran Sampel & Validitas Statistik ML)**:
   > *"Berapa banyak sampel bakso yang Anda latih ke dalam model? Apakah model Anda tidak mengalami overfitting atau data leakage?"*
   - **Tanggapan/Pertahanan**: Tunjukkan skema validasi *5-fold cross-validation* dengan pembagian data berbasis sampel independen (*independent trial-level splits*), bukan potongan sampel berurutan dari satu tetesan yang sama, guna memastikan validitas metrik akurasi dan generalisasi model.

---

## 12. Rencana Tindakan Perbaikan Berdasarkan Prioritas (*Actionable Revision Plan*)

### 12.1 Prioritas 1: Wajib Diperbaiki (*Must-Fix / Non-Negotiable*)
1. **Pangkas Inkonsistensi Model di Bab III**:
   Hapus subbab *Random Forest* (RF) dan *Variational Quantum Classifier* (VQC) pada Subbab 3.4.6 dan 3.4.7 di file `Isi/Metode Penelitian.tex`. Kembalikan fokus murni ke komparasi **SVM Klasik vs QSVC Kuantum** agar selaras 100% dengan Judul, Bab I, dan Bab II.
2. **Sinkronkan Jumlah Fitur Sinyal**:
   Pilih secara definitif apakah menggunakan 3 fitur ($V_{mean}, \Delta V, \sigma_V$) atau 5 fitur. Disarankan menggunakan **3 fitur domain waktu** agar pemetaan QSVC pada ruang Hilbert $2^3 = 8$ dimensi dapat dieksekusi secara efisien dan deterministik. Perbarui teks di Bab I (§1.1 ¶6) agar selaras dengan Bab III.
3. **Tambahkan Qiskit ke Tabel Software (Tabel 3.2)**:
   Masukkan pustaka `qiskit` dan `qiskit-machine-learning` ke dalam Tabel 3.2.
4. **Cantumkan Nilai Nominal Resistor $R_G$**:
   Tuliskan nilai nominal resistor $R_G$ pada Tabel 3.3 dan Subbab 3.3.2 butir c untuk menjamin replikabilitas perangkat keras.

### 12.2 Prioritas 2: Penting untuk Penguatan Ilmiah (*Important but Non-Fatal*)
1. **Pertajam Hipotesis Transduksi Magneto-Mekanik**:
   Tambahkan 1--2 paragraf penjelasan fisis pada Subbab 2.1.10 dan 3.4.4 mengenai bagaimana ikatan hidrazon kovalen memodifikasi jarak atau kerapatan fluks bocor partikel $\text{Fe}_3\text{O}_4$ ke elemen MTJ TMR.
2. **Rinci Rencana Replikasi Sampel ($N$)**:
   Nyatakan secara eksplisit jumlah ulangan per konsentrasi (misalnya 10 kali ulangan pada 6 variasi konsentrasi = 60 titik data independen) di Subbab 3.4.4 dan 3.4.5.
3. **Rumus Formal LOD di Metodologi**:
   Tuliskan rumus $\text{LOD} = 3\sigma/m$ secara eksplisit di Subbab 3.4.3.

### 12.3 Prioritas 3: Penyempurnaan Format & Kosmetik (*Refinements*)
1. **Arsipkan File Sampah**:
   Pindahkan `Isi/Profil Industri.tex` ke folder arsip agar tidak terbaca sebagai berkas aktif.
2. **Pembersihan Entri BibTeX yang Tidak Terpakai**:
   Entri-entri yang tidak terpakai di `references.bib` (seperti `Breiman2001`, `ti_lm358_*`) dapat dibersihkan atau dibiarkan sebagai basis data sekunder.

---

## 13. Memo Praktis: Cut / Rewrite / Keep

### Yang Harus Dipotong Segera (*CUT*):
- Narasi mengenai *Random Forest* (RF) dan *Variational Quantum Classifier* (VQC) pada Subbab 3.4.6, 3.4.7, dan 3.4.8 di file `Isi/Metode Penelitian.tex`.
- Penyebutan 5 fitur yang kontradiktif di Bab I jika yang digunakan secara definitif adalah 3 fitur.

### Yang Harus Ditulis Ulang / Ditambahkan (*REWRITE / EXPAND*):
- Subbab 3.4.5 (*Ekstraksi Fitur*): Tegaskan keterkaitan antara 3 fitur ($d=3$) dengan jumlah qubit pada $ZZ\text{FeatureMap}$ QSVC ($n=3$ qubit).
- Tabel 3.2 dan 3.3 di Bab III: Tambahkan Qiskit dan nilai nominal $R_G$.
- Subbab 2.1.10: Perjelas mekanisme magneto-mekanik perturbasi medan bocor $\text{Fe}_3\text{O}_4$ akibat formasi hidrazon.

### Yang Harus Dipertahankan & Ditonjolkan (*KEEP & EMPHASIZE*):
- Penjelasan rantai pengkondisi sinyal diferensial AD623 dengan penggeser level tegangan $V_{REF} = 2,50$ V.
- Pemisahan peran fungsional asam sitrat (*green crosslinker* & *capping agent*) dan ADH (*chemo-receptor* bebas glutaraldehida).
- Mekanisme akuisisi berbasis durasi waktu 5.0 detik dengan pembuangan *settling time* 1.0 detik.
- Matriks perbandingan penelitian terdahulu (Tabel 2.1) yang memposisikan kebaruan sistem secara kokoh.

---
*Laporan diagnostik ini disusun secara objektif dan komprehensif mengikuti standar peer review akademik tertinggi guna memastikan naskah proposal lulus seminar dan siap dipublikasikan pada jurnal bereputasi tinggi.*
