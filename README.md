# PROPOSAL TUGAS AKHIR — FAHRY RIZKY SAMSUDIN

> **Rancang Bangun Instrumentasi Sensor *Tunneling Magnetoresistance* Berbasis Nanofiber $\text{Fe}_3\text{O}_4$/PVA-Sitrat-ADH untuk Deteksi Formalin pada Bakso Menggunakan Komparasi Model SVM dan QSVC**

[![LaTeX Proposal](https://img.shields.io/badge/LaTeX-PDF%20Compiled-emerald?style=flat-square)](Proposal%20Fahry%20Rizky%20Samsudin.pdf)
[![Python Version](https://img.shields.io/badge/Python-3.13.15-blue?style=flat-square)](requirements.txt)
[![GUI Framework](https://img.shields.io/badge/GUI-CustomTkinter%206.0-teal?style=flat-square)](Kode/main_gui.py)
[![Repo Status](https://img.shields.io/badge/Access-Private-rose?style=flat-square)](#)

---

## 📌 Identitas Penelitian
- **Peneliti**: Fahry Rizky Samsudin
- **NIM**: 1237030018
- **Dosen Pembimbing**: Mada Sanjaya W.S., M.Si., Ph.D.
- **Institusi**: Jurusan Fisika, Fakultas Sains dan Teknologi, UIN Sunan Gunung Djati Bandung
- **Tahun**: 2026

---

## 🛠️ Kebutuhan Sistem & Spesifikasi Library

Sistem instrumentasi dan akuisisi data ini dibangun menggunakan lingkungan **Python 3.13.15** (sepenuhnya kompatibel dengan **Python $\ge$ 3.10** pada Windows, macOS, maupun Linux).

### Daftar Library & Versi Terpasang

| Library | Versi Terpasang | Keterangan Fungsi |
|---|---|---|
| **Python** | `3.13.15` | Runtime bahasa utama |
| **`customtkinter`** | `6.0.0` | Antarmuka grafis (GUI) modern bernuansa *academic dark-slate* |
| **`matplotlib`** | `3.11.2` | Visualisasi kurva real-time $B(t)$, plot kalibrasi $V$ vs $B$, dan kurva sensitivitas |
| **`numpy`** | `2.5.3` | Komputasi numerik, regresi polinomial, dan matriks sensor |
| **`scipy`** | `1.18.1` | Interpolasi *cubic spline* dan diferensiasi sensitivitas $dV/dB$ |
| **`pandas`** | `3.0.6` | Manajemen tabel data kalibrasi dan dataframe analitik |
| **`openpyxl`** | `3.1.5` | Mesin ekspor laporan kalibrasi multi-sheet Excel (.xlsx) |
| **`pyserial`** | `3.5` | Komunikasi serial UART dengan mikrokontroler Arduino Uno |
| **`pypdf`** | `6.19.0` | Utilitas verifikasi dan inspeksi berkas keluaran naskah PDF |

### Cara Instalasi Cepat Dependensi
Buka terminal pada direktori repositori ini dan jalankan:
```bash
pip install -r requirements.txt
```

---

## 📂 Struktur Direktori Repositori

```
Proposal/
├── Header/                     # Halaman preliminer naskah LaTeX (sampul, keaslian, pengesahan, kata pengantar, daftar isi)
├── Isi/                        # Naskah inti bab proposal skripsi:
│   ├── Pendahuluan.tex         # Bab I: Latar Belakang, Rumusan Masalah, Tujuan Penelitian, Batasan Masalah
│   ├── Tinjauan Pustaka.tex    # Bab II: Teori TMR, AD623, ADS1115, Nanofiber, SVM & QSVC
│   └── Metode Penelitian.tex   # Bab III: Desain Hardware, Software, Sintesis Nanofiber, Diagram Alir ML
├── Gambar/                     # Gambar dan diagram terstruktur per bab:
│   ├── Bab1/                   # Ilustrasi dan bagan Bab I
│   ├── Bab2/                   # Gambar teori & komponen Bab II (prefix: babII_*)
│   ├── Bab3/                   # Gambar desain 3D, skematik PCB & diagram alir Bab III (prefix: babIII_*)
│   ├── Lampiran/               # Foto fisik alat, statif, casing, dan layar GUI (prefix: lampiran_*)
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
├── skripsi.pdf                 # Output PDF hasil kompilasi
├── Proposal Fahry Rizky Samsudin.pdf # Salinan resmi naskah PDF
├── AGENTS.md                   # Dokumen panduan sistem & batasan perangkat keras untuk agen AI
└── GEMINI.md                   # Pedoman aturan agen kecerdasan buatan ruang kerja
```

---

## ⚡ Spesifikasi Rantai Sinyal & Perangkat Keras

1. **Sensor Magnetik**: TMR ALT023-10E (*Tunneling Magnetoresistance*, NVE Corporation). Karakteristik bipolar, resistansi jembatan $\approx 20\ \text{k}\Omega$, rentang linear $\pm 1.0\ \text{mT}$, dicatu tegangan tunggal $5.0\ \text{V}$ dengan kapasitor decoupling $100\ \text{nF}$.
2. **Pengkondisi Sinyal (*In-Amp*)**: AD623. Menggunakan catu daya tunggal $+5.0\ \text{V}$. Pin 5 (`REF`) dihubungkan ke pembagi tegangan resistor presisi $R_3 = R_4 = 1.0\ \text{k}\Omega$ sehingga **$V_{\text{REF}} = 2.50\ \text{V}$**. Pada $B=0$, tegangan keluaran bertengger di $\approx 2.50\ \text{V}$.
3. **ADC**: ADS1115 16-Bit pada catu $5.0\ \text{V}$ dengan penguatan internal `GAIN_TWOTHIRDS` ($\text{FSR} = \pm 6.144\ \text{V}$), memberikan resolusi $0.1875\ \text{mV/count}$.
4. **Kumparan Helmholtz & Power Supply**: Catu daya DC variabel dengan rentang tegangan **$0.0 - 16.0\ \text{V}$**. Resistansi kumparan $R \approx 10\ \Omega$, arus maksimal $\approx 1.6\ \text{A}$, rentang medan magnet yang dihasilkan $\approx 0 - 11.5\ \text{mT}$ (dapat dibalik polaritasnya untuk sapuan medan negatif hingga $-4\ \text{mT}$).
5. **Pengaturan Helmholtz**: Diatur secara **EKSTERNAL** menggunakan knob fisik meja laboratorium. Parameter $V_{\text{helm}}$, $I_{\text{helm}}$, dan $B_{\text{teslameter}}$ pada GUI berfungsi murni sebagai pencatatan data (*ground truth manual*), bukan pengontrol tegangan hardware.
6. **Akuisisi Data**: Berbasis **DURASI WAKTU (Lama Detik)** (default: 5.0 detik) dengan pembuangan waktu stabilisasi awal (*settling time*, default: 1.0 detik).

---

## 🚀 Panduan Menjalankan Perangkat Lunak

### 1. Menjalankan Aplikasi Antarmuka GUI
```bash
# Dari root repositori
python Kode/main_gui.py

# Atau dari dalam folder Kode/
cd Kode
python main_gui.py
```

### 2. Menjalankan Skrip Pengolahan Kalibrasi Mandiri (CLI)
```bash
# Olah data regresi linear & sensitivitas spline
python Kode/scripts/olah_data_kalibrasi_B.py

# Membuat dataset simulasi dummy
python Kode/scripts/generate_dummy_tmr_data.py
```

### 3. Mengompilasi Naskah Proposal LaTeX ke PDF
Untuk mengompilasi naskah proposal secara otomatis dalam 4 tahap (`pdflatex` $\to$ `bibtex` $\to$ `pdflatex` $\to$ `pdflatex`):
- Pada Windows:
  ```cmd
  build.bat
  ```
- Atau menggunakan Python:
  ```bash
  python scripts/build_proposal.py
  ```
Hasil PDF resmi otomatis diperbarui pada berkas `Proposal Fahry Rizky Samsudin.pdf` dan seluruh berkas sampah log dibersihkan ke folder `build_logs/`.

---

## 🤖 Portabilitas Asisten AI (Agent Skills & Anti-Slop)

Repositori ini telah dibekali dengan **49 Keterampilan Asisten AI (*Installed Agent Skills*)** di dalam folder `.agents/skills/`, termasuk modul **Anti-Slop AI** (`antislop`, `antislop-ui`, `antislop-copywriting`, `antislop-human`, `antislop-layoutmobile`, `antislop-code`). Saat repositori ini di-*clone* ke komputer atau laptop lain:
- Lingkungan AI / Antigravity akan otomatis mendeteksi kustomisasi ruang kerja dari folder `.agents/`.
- Aturan anti-slop (`.agents/rules/antislop.md`) memastikan kode, UI, dan naskah yang dihasilkan terbebas dari pola generik AI (*slop*).
- Seluruh pedoman arsitektur pada `AGENTS.md` dan `GEMINI.md` otomatis menjadi acuan kerja tanpa perlu konfigurasi ulang.

