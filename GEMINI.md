# AGENTS.md — Panduan Sistem & Pengetahuan Proyek Proposal Tugas Akhir

Dokumen ini berisi arsitektur sistem, konvensi berkas, spesifikasi perangkat keras, dan panduan keterampilan (*skills*) untuk agen kecerdasan buatan (*AI assistant*) dan pengembang pada repositori Tugas Akhir ini.

---

## 1. Identitas Proyek
- **Judul**: *Rancang Bangun Instrumentasi Sensor Tunneling Magnetoresistance Berbasis Nanofiber $\text{Fe}_3\text{O}_4$/PVA-Sitrat-ADH untuk Deteksi Formalin pada Bakso Menggunakan Komparasi Model Klasik (SVM, Random Forest) dan Kuantum (QSVC, VQC)*
- **Peneliti**: Fahry Rizky Samsudin (NIM: 1237030018)
- **Institusi**: Jurusan Fisika, Fakultas Sains dan Teknologi, UIN Sunan Gunung Djati Bandung
- **Tahun**: 2026

---

## 2. Struktur Direktori Repositori

```
Proposal/
├── Header/                     # Halaman preliminer skripsi (sampul, persetujuan, daftar isi/gambar/tabel)
├── Isi/                        # Naskah utama bab proposal:
│   ├── Pendahuluan.tex         # Bab I: Latar Belakang, Rumusan Masalah, Tujuan, Batasan
│   ├── Tinjauan Pustaka.tex    # Bab II: Teori TMR, AD623, ADS1115, Nanofiber, SVM & QSVC
│   └── Metode Penelitian.tex   # Bab III: Desain Hardware, Software, Sintesis, Alur Model ML
├── Gambar/                     # Subfolder gambar terstruktur:
│   ├── Bab1/                   # Ilustrasi dan diagram Bab I
│   ├── Bab2/                   # Gambar teori & komponen Bab II (prefix: babII_*)
│   ├── Bab3/                   # Gambar desain 3D, skematik & diagram alir Bab III (prefix: babIII_*)
│   ├── Lampiran/               # Foto dokumentasi fisik alat, statif, casing (prefix: lampiran_*)
│   └── Logo/                   # Logo resmi institusi (Logo UIN.png)
├── Kode/                       # Sistem instrumentasi & akuisisi Python:
│   ├── main_gui.py             # Entry point utama aplikasi GUI CustomTkinter
│   ├── akuisisi_gui_B.py       # Wrapper kompatibilitas GUI
│   ├── origin_style.py         # Wrapper gaya grafik bola 3D OriginLab
│   ├── src/                    # Paket modular GUI & backend:
│   │   ├── config.py           # Konfigurasi parameter elektrik & tema
│   │   ├── style.py            # Rendering scatter_bola OriginLab
│   │   ├── serial_worker.py    # SerialManager, scanner port, SimulatedSerialTMR
│   │   ├── acquisition.py      # DurationAcquisitionEngine (Lama Detik) & StreamBuffer
│   │   ├── analysis.py         # CalibrationAnalyzer (regresi, spline dV/dB, auto-save konstanta)
│   │   ├── export_handler.py   # Ekspor laporan 2-sheet Excel, stream Excel, & plot 300 DPI
│   │   └── gui/app.py          # Antarmuka CustomTkinter TMRAcquisitionApp lengkap
│   ├── scripts/                # Skrip CLI pemrosesan mandiri:
│   │   ├── karakterisasi_sensor_B.py
│   │   ├── kalibrasi_tmr_formalin.py
│   │   ├── olah_data_kalibrasi_B.py
│   │   └── generate_dummy_tmr_data.py
│   ├── data/                   # Dataset CSV mentah, Excel kalibrasi, konstanta JSON, konversi_B.py
│   ├── output/                 # Hasil ekspor gambar kurva plot resolusi tinggi (300 DPI)
│   └── firmware/               # Firmware mikrokontroler Arduino (.ino)
├── .agents/skills/             # 43 Keterampilan Asisten AI untuk portabilitas Git lintas komputer
├── build_logs/                 # Tempat isolasi berkas sementara/sampah kompilasi LaTeX (.aux, .log, dll.)
├── scripts/build_proposal.py   # Skrip otomasi kompilasi 4-tahap LaTeX (pdflatex -> bibtex -> 2x pdflatex)
├── build.bat                   # Pintasan batch build proposal di Windows
├── skripsi.tex                 # Dokumen induk LaTeX
└── skripsi.pdf                 # Output PDF hasil kompilasi (disalin ke Proposal Fahry Rizky Samsudin.pdf)
```

---

## 3. Spesifikasi Rantai Sinyal & Perangkat Keras (Ground Truth)

Saat bekerja dengan kode atau naskah proposal, patuhi spesifikasi elektrik berikut:
1. **Sensor Magnetik**: TMR ALT023-10E (*Tunneling Magnetoresistance*, NVE Corporation). Karakteristik *bipolar*, resistansi jembatan $\approx 20\ \text{k}\Omega$, rentang linear $\pm 1.0\ \text{mT}$, dicatu tegangan tunggal $5.0\ \text{V}$ dengan kapasitor *decoupling* $100\ \text{nF}$.
2. **Penguat Sinyal (*In-Amp*)**: AD623. Menggunakan catu daya tunggal $+5.0\ \text{V}$. Pin 5 (`REF`) dihubungkan ke pembagi tegangan resistor presisi $R_3 = R_4 = 1.0\ \text{k}\Omega$ sehingga **$V_{\text{REF}} = 2.50\ \text{V}$** (bukan 1.65 V). Pada $B=0$, tegangan keluaran bertengger di $\approx 2.50\ \text{V}$.
3. **ADC**: ADS1115 16-Bit. Bekerja pada catu $5.0\ \text{V}$ dengan penguatan internal `GAIN_TWOTHIRDS` ($\text{FSR} = \pm 6.144\ \text{V}$), memberikan resolusi $0.1875\ \text{mV/count}$.
4. **Kumparan Helmholtz & Power Supply**: Catu daya DC variabel dengan rentang tegangan **$0.0 - 16.0\ \text{V}$**. Resistansi kumparan $R \approx 10\ \Omega$, arus maksimal $\approx 1.6\ \text{A}$, rentang medan magnet yang dihasilkan $\approx 0 - 11.5\ \text{mT}$ (dapat dibalik polaritasnya untuk sapuan medan negatif hingga $-4\ \text{mT}$).
5. **Pengaturan Helmholtz**: Diatur secara **EKSTERNAL** menggunakan knob fisik meja laboratorium. Parameter $V_{\text{helm}}$, $I_{\text{helm}}$, dan $B_{\text{teslameter}}$ pada GUI berfungsi murni sebagai pencatatan data (*ground truth manual*), bukan pengontrol tegangan hardware.
6. **Akuisisi Data**: Berbasis **DURASI WAKTU (Lama Detik)** (default: 5.0 detik) dengan pembuangan waktu stabilisasi awal (*settling time*, default: 1.0 detik).

---

## 4. Prosedur Kompilasi LaTeX

Untuk mengompilasi naskah proposal menjadi PDF:
- **Windows Command**:
  ```cmd
  build.bat
  ```
  atau
  ```bash
  python scripts/build_proposal.py
  ```
- **Mekanisme Otomatis**:
  1. Menjalankan 4 tahap: `pdflatex` (pass 1) -> `bibtex` -> `pdflatex` (pass 2 sinkronisasi) -> `pdflatex` (pass 3 nomor halaman).
  2. Memindahkan seluruh berkas bantu (`.aux`, `.log`, `.bbl`, `.blg`, `.toc`, `.lof`, `.lot`, `.out`) ke folder [build_logs](file:///c:/Users/Fahry%20Rizky%20S/Documents/Tugas%20Akhir%20Fahry/Proposal/build_logs).
  3. Menyalin hasil `skripsi.pdf` secara otomatis menjadi `Proposal Fahry Rizky Samsudin.pdf`.
  4. Seluruh gambar dimuat melalui `\graphicspath` di [skripsi.tex](file:///c:/Users/Fahry%20Rizky%20S/Documents/Tugas%20Akhir%20Fahry/Proposal/skripsi.tex):
     ```latex
     \graphicspath{{Gambar/}{Gambar/Bab1/}{Gambar/Bab2/}{Gambar/Bab3/}{Gambar/Lampiran/}{Gambar/Logo/}}
     ```

---

## 5. Keterampilan Asisten AI (*Installed Agent Skills*)

Folder [.agents/skills](file:///c:/Users/Fahry%20Rizky%20S/Documents/Tugas%20Akhir%20Fahry/Proposal/.agents/skills) memuat 49 keterampilan (termasuk modul Anti-Slop AI) yang otomatis aktif ketika repositori ini diakses oleh Antigravity di perangkat mana pun:

| Kategori | Nama Skill |
|---|---|
| **Alur Pikir & Desain** | `brainstorming`, `idea-refine`, `interview-me`, `spec-driven-development`, `writing-plans` |
| **Kualitas & Review** | `code-review-and-quality`, `receiving-code-review`, `requesting-code-review`, `code-simplification`, `verification-before-completion`, `doubt-driven-development` |
| **Anti-Slop AI & Estetika Desain** | `antislop`, `antislop-ui`, `antislop-copywriting`, `antislop-human`, `antislop-layoutmobile`, `antislop-code` |
| **Pengujian & Debugging** | `systematic-debugging`, `debugging-and-error-recovery`, `test-driven-development`, `superpowers-test-driven-development`, `browser-testing-with-devtools` |
| **Arsitektur & Rekayasa** | `api-and-interface-design`, `frontend-ui-engineering`, `awesome-llm-apps`, `performance-optimization`, `observability-and-instrumentation`, `security-and-hardening` |
| **Eksekusi & Otomasi** | `executing-plans`, `subagent-driven-development`, `incremental-implementation`, `dispatching-parallel-agents`, `latex-compile-clean`, `ci-cd-and-automation` |
| **Git & Versioning** | `git-workflow-and-versioning`, `using-git-worktrees`, `finishing-a-development-branch`, `shipping-and-launch` |
| **Desain CAD, CAE & Fabrikasi** | `cad`, `dfm`, `dfam-check`, `cad-constraint-kit`, `cad-physics-validation`, `multi-agent-cad`, `varen-ai-cad`, `cad-drawing-intelligence`, `dxf`, `engineering-drawing`, `step-parts`, `cad-viewer`, `urdf`, `sdf`, `srdf`, `bambu-labs`, `gcode`, `sendcutsend`, `aieng-cad-authoring`, `aieng-cad-cae-copilot`, `aieng-closed-loop-copilot`, `scad-coding`, `scad-planning`, `scad-validation-review`, `scad-repair`, `scad-library-bosl2`, `scad-library-threads`, `scad-library-round-anything` |
| **Pengetahuan & Konteks** | `context-engineering`, `claude-mem`, `documentation-and-adrs`, `source-driven-development`, `using-superpowers`, `using-agent-skills`, `writing-skills` |

### Sinkronisasi ke Perangkat Baru (GitHub)
Saat repositori ini di-*clone* ke komputer atau laptop lain:
1. Folder `.agents/skills` akan otomatis menyertakan seluruh 49 keterampilan.
2. Lingkungan Antigravity pada komputer baru akan langsung mendeteksi kustomisasi ruang kerja (*workspace customizations*) dari folder `.agents/`.
3. Aturan anti-slop otomatis ditegakkan dari `.agents/rules/antislop.md` guna mencegah output AI yang generik (*slop*).
4. Seluruh instruksi, gaya penulisan, dan batas arsitektur pada berkas ini (`AGENTS.md` & `GEMINI.md`) otomatis terbaca sebagai pedoman baku.

---

## 6. Pedoman Baku Presentasi Seminar Proposal (Anti-Slop Slide & Deck PPTX)

Berdasarkan format baku Gilang Pratama (1227030017) dan arahan peneliti, slide presentasi proposal wajib mematuhi standar berikut:
1. **Ukuran Font Wajib Besar**: Judul slide minimal 18–24 pt (Bold), heading kartu 13–15 pt (Bold), body teks materi 11.5–13 pt. Dilarang keras teks kerdil / micro-text bergumam di bawah slide latar belakang atau dasar teori.
2. **Cover Tradisi Gilang**: Logo UIN (kiri atas) & Logo Fisika UIN (kanan atas), Judul Proposal di tengah berukuran besar dan tebal, Identitas Peneliti (Nama & NIM) di tengah, Dosen Pembimbing I di kiri bawah, dan Dosen Pembimbing II di kanan bawah.
3. **Latar Belakang Berwujud Flowchart Berarah**: Wajib berwujud bagan alir diagramatis dengan panah alur penalaran (Urgensi Pangan → Limitasi Sensor → Reseptor Nanofiber → Transduser TMR → Rantai Sinyal → Komparasi ML → Target Solusi). Dilarang berupa paragraf teks atau bullet point biasa.
4. **Landasan Teori Terkonsolidasi (2 Hingga 4 Teori per Slide)**:
   - Dilarang memecah menjadi slide "Landasan Teori 1", "Landasan Teori 2" (AI slop).
   - Wajib memadukan 2–4 teori per slide dengan sitasi persis proposal dan menyertakan gambar fisik riil (ALT023-10E, MTJ, ikatan kovalen ADH, AD623, ADS1115, serta 4 Model Cerdas dalam grid 2x2).
5. **Larangan Keras Filler & Jargon Slop**:
   - Dilarang membuat slide "Profil Mitra Riset" atau "Sistematika Paparan / Agenda".
   - Dilarang jargon bisnis AI slop seperti "4 Dimensi Strategis", "Pilar Keberlanjutan", dll.
6. **Proteksi Integritas Berkas**:
   - File utama slide adalah `Proposal_TA_Fahry_Rizky_Samsudin.pptx` dan `presentation_preview.html`. Dilarang menimpa kedua berkas ini dengan generator generik AI slop.

