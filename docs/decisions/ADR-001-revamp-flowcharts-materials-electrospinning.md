# ADR-001: Restrukturisasi Flowchart TikZ, Parameter Elektrospinning, dan Sistematika Material Bab II & III

## Status
Proposed

## Tanggal
2026-09-24

## Konteks
Penelitian Tugas Akhir Fahry Rizky Samsudin berjudul *"Rancang Bangun Instrumentasi Sensor Tunneling Magnetoresistance Berbasis Nanofiber \ch{Fe3O4}/PVA-Sitrat-ADH untuk Deteksi Formalin pada Bakso Menggunakan Komparasi Model SVM dan QSVC"*.
Sebelumnya, draf proposal masih memuat sisa alur dan artefak dari penelitian terdahulu (Gilang - biosensor GMR glukosa saliva). Beberapa masalah kritis diidentifikasi:
1. **Gambar 3.6 -- Gambar 3.9 (Diagram Alir Perangkat Lunak)**: Masih menggunakan diagram alir lama berbasis GMR (`.drawio.png`) yang tidak merefleksikan arsitektur kode TMR terbaru (`sensor_tmr_formalin.ino`, `kalibrasi_tmr_formalin.py`, `karakterisasi_sensor_B.py`). Diagram harus dibangun ulang dari nol menggunakan kode vektor native **TikZ** di LaTeX.
2. **Kegagalan Distribusi Fe3O4 pada Nanofiber (Hasil SEM)**: Hasil uji SEM awal menunjukkan bahwa parameter elektrospinning yang diwarisi dari penelitian Gilang menghasilkan nanofiber di mana partikel Fe3O4 tidak terdistribusi merata (bahkan mendekati nol). Hal ini disebabkan oleh:
   - Partikel magnetik Fe3O4 tanpa penstabil (*capping agent*) mengalami aglomerasi cepat dan sedimentasi di dasar syringe selama proses elektrospinning yang berlangsung 2--3 jam.
   - Viskositas larutan PVA 9% (0,45 g dalam 5 mL) kurang mencukupi untuk menarik dan membungkus nanopartikel Fe3O4 ke dalam filamen serat.
   - Laju alir 15 $\mu$L/min (0,9 mL/jam) dan tegangan 15 kV pada jarak 15 cm belum dioptimasi untuk sistem komposit magnetik ini.
3. **Sistematika Material pada Tinjauan Pustaka (Bab II) dan Metodologi (Bab III)**: Subbab 2.1.8 sebelumnya langsung melompat ke *"Nanofiber Fe3O4/PVA-Sitrat-ADH"*, padahal penguji/pembimbing mensyaratkan pembahasan bertahap:
   - Polivinil Alkohol (PVA) sebagai matriks polimer pembawa.
   - Asam Sitrat (*Citric Acid*) sebagai agen penstabil dispersi Fe3O4 (*capping agent*) dan *crosslinker* termal esterifikasi tahan air.
   - *Adipic Acid Dihydrazide* (ADH) sebagai *crosslinker* komplementer dan situs pengenal (*recognition site*) formaldehida.
   - Nanofiber Komposit Fe3O4/PVA-Sitrat-ADH sebagai elemen reseptor terpadu.

## Keputusan
1. **Parameter Elektrospinning yang Direkomendasikan**:
   - **Modifikasi Prekursor**: Mengintegrasikan Asam Sitrat sebagai *capping agent* langsung saat dispersi Fe3O4 (sonikasi 30 menit) sebelum dicampur dengan PVA. Gugus karboksilat (-COO⁻) memberikan tolakan elektrostatik (potensial zeta negatif tinggi) sehingga mencegah aglomerasi dan sedimentasi Fe3O4 dalam jarum/syringe.
   - **Konsentrasi PVA**: Dinaikkan ke rentang optimal 10%--12% (b/v) guna meningkatkan *chain entanglement* polimer.
   - **Tegangan Operasi ($V$)**: 16 -- 18 kV (titik optimal: 17 kV) untuk menghasilkan medan listrik efektif ~1,13--1,20 kV/cm yang stabil menarik *Taylor cone*.
   - **Laju Alir (*Flow Rate*)**: 0,4 -- 0,8 mL/jam (sekitar 7 -- 13 $\mu$L/min, rekomendasi spesifik: 0,6 mL/jam atau 10 $\mu$L/min).
   - **Jarak Ujung Jarum ke Kolektor (TCD)**: 13 -- 15 cm.
   - **Desain Eksperimen (DoE)**: Memasukkan skema variasi parameter elektrospinning pada Metodologi Penelitian sebagai tahap optimasi formal.
2. **Penyusunan Ulang Subbab Bab II**:
   - Subbab 2.1.8: *Polyvinyl Alcohol* (PVA)
   - Subbab 2.1.9: Asam Sitrat (*Citric Acid*)
   - Subbab 2.1.10: *Adipic Acid Dihydrazide* (ADH)
   - Subbab 2.1.11: Nanofiber \ch{Fe3O4}/PVA-Sitrat-ADH sebagai Elemen Reseptor
3. **Penyusunan Ulang Subbab 3.4 Metodologi**:
   - Membahas preparasi PVA, sintesis Fe3O4 dengan capping Asam Sitrat, elektrospinning dengan rentang parameter optimal, serta perlakuan *thermal curing* & ADH fungsionalisasi secara bertahap.
4. **Implementasi Diagram Alir TikZ**:
   - Gambar 3.6: Diagram Alir Firmware Arduino (`sensor_tmr_formalin.ino`)
   - Gambar 3.7: Diagram Alir Python Akuisisi & Kalibrasi (`kalibrasi_tmr_formalin.py` dan `karakterisasi_sensor_B.py`)
   - Gambar 3.8: Diagram Alir Pemodelan Machine Learning (Klasik RF/SVM vs QML QSVC/VQC)
   - Gambar 3.9: Diagram Alir Penerapan Model Realtime (*Deployment* pada Raspberry Pi 5)
   - Seluruhnya digambar dengan sintaks TikZ modular, konsisten dengan format margin report LaTeX.

## Konsekuensi
- Dokumen LaTeX terbebas dari seluruh artefak visual GMR berbasis bitmap/PNG yang buram.
- Proposal memiliki landasan teoritis dan metodologis yang kuat terkait alasan kegagalan SEM sebelumnya serta solusi optimasinya.
- Waktu kompilasi LaTeX tetap cepat karena diagram TikZ menggunakan bentuk standar (`rectangle`, `diamond`, `rounded corners`).
