"""
Generator Pratinjau HTML Presentasi Seminar Proposal Tugas Akhir - Fahry Rizky Samsudin
Format Standar Akademik Fisika UIN Sunan Gunung Djati Bandung (16 Slide Bebas AI Slop)
"""

import os

HTML_OUTPUT = "presentation_preview.html"

def generate_html_preview():
    html_content = """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pratinjau Presentasi Seminar Proposal — Fahry Rizky Samsudin</title>
  <style>
    :root {
      --navy-dark: #0f172a;
      --navy-mid: #1e3a8a;
      --blue-accent: #0284c7;
      --emerald: #059669;
      --gold: #d97706;
      --bg-light: #f8fafc;
      --card-bg: #ffffff;
      --card-border: #cbd5e1;
      --text-main: #0f172a;
      --text-muted: #475569;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      background: #0b1120;
      color: var(--text-main);
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 24px;
      gap: 24px;
    }
    .header-bar {
      max-width: 1200px;
      width: 100%;
      background: rgba(30, 41, 59, 0.8);
      backdrop-filter: blur(12px);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 12px;
      padding: 16px 24px;
      color: #fff;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .header-title { font-size: 16px; font-weight: 700; color: #38bdf8; }
    .header-subtitle { font-size: 13px; color: #94a3b8; }
    .slide-deck {
      display: flex;
      flex-direction: column;
      gap: 32px;
      max-width: 1200px;
      width: 100%;
    }
    .slide {
      background: var(--bg-light);
      width: 100%;
      aspect-ratio: 16 / 9;
      border-radius: 12px;
      border: 1px solid #334155;
      box-shadow: 0 20px 25px -5px rgba(0,0,0,0.5), 0 8px 10px -6px rgba(0,0,0,0.5);
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      padding: 28px 36px 36px 36px;
    }
    .slide-top-line {
      position: absolute;
      top: 0; left: 0; right: 0; height: 6px;
      background: var(--navy-mid);
    }
    .slide-badge {
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 1px;
      color: var(--blue-accent);
      text-transform: uppercase;
      margin-bottom: 2px;
    }
    .slide-title {
      font-size: 20px;
      font-weight: 800;
      color: var(--navy-dark);
      margin-bottom: 16px;
    }
    .slide-title span {
      font-weight: 500;
      font-size: 15px;
      color: var(--text-muted);
    }
    .slide-content {
      flex: 1;
      display: flex;
      gap: 20px;
      min-height: 0;
    }
    .card {
      background: var(--card-bg);
      border: 1.5px solid var(--card-border);
      border-radius: 10px;
      padding: 16px 20px;
      display: flex;
      flex-direction: column;
    }
    .card-title {
      font-size: 14px;
      font-weight: 700;
      color: var(--navy-mid);
      margin-bottom: 8px;
    }
    .card-body {
      font-size: 12.5px;
      line-height: 1.45;
      color: var(--text-main);
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    .bullet-item { display: flex; gap: 8px; align-items: flex-start; }
    .bullet-dot { color: var(--blue-accent); font-weight: bold; }
    .citation { font-weight: bold; color: var(--navy-mid); }
    .slide-footer {
      position: absolute;
      bottom: 12px; left: 36px; right: 36px;
      display: flex;
      justify-content: space-between;
      font-size: 10.5px;
      color: var(--text-muted);
      border-top: 1px solid var(--card-border);
      padding-top: 6px;
    }
    table { width: 100%; border-collapse: collapse; font-size: 11px; }
    th { background: var(--navy-dark); color: #fff; padding: 8px 10px; text-align: left; }
    td { padding: 8px 10px; border-bottom: 1px solid #e2e8f0; }
    tr:nth-child(even) td { background: #f1f5f9; }
    tr.highlight td { background: #f0fdfa; font-weight: 600; color: var(--navy-mid); }
    img { max-width: 100%; height: auto; object-fit: contain; }
  </style>
</head>
<body>

  <div class="header-bar">
    <div>
      <div class="header-title">PRATINJAU DECK PRESENTASI SEMINAR PROPOSAL</div>
      <div class="header-subtitle">Fahry Rizky Samsudin (1237030018) — Bebas AI Slop (16 Slide Padat)</div>
    </div>
    <div style="font-size: 12px; background: #0284c7; padding: 6px 12px; border-radius: 6px; font-weight: 700;">
      16 Slide Standar Gilang Pratama
    </div>
  </div>

  <div class="slide-deck">

    <!-- SLIDE 1: COVER -->
    <div class="slide" id="slide-1">
      <div class="slide-top-line"></div>
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
        <img src="Gambar/Logo/Logo UIN.png" style="height: 56px;" alt="UIN">
        <div style="text-align: center; font-size: 12px; font-weight: bold; color: var(--navy-mid);">
          SEMINAR PROPOSAL TUGAS AKHIR | JURUSAN FISIKA<br>
          FAKULTAS SAINS DAN TEKNOLOGI - UIN SUNAN GUNUNG DJATI BANDUNG
        </div>
        <img src="Gambar/Logo/Logo Fisika UIN.png" style="height: 56px;" alt="Fisika">
      </div>
      <div class="card" style="border-color: var(--blue-accent); text-align: center; padding: 24px 20px; margin-bottom: 16px;">
        <div style="font-size: 16px; font-weight: 800; color: var(--navy-dark); line-height: 1.35;">
          RANCANG BANGUN INSTRUMENTASI SENSOR TUNNELING MAGNETORESISTANCE BERBASIS NANOFIBER Fe3O4/PVA-SITRAT-ADH UNTUK DETEKSI FORMALIN PADA BAKSO MENGGUNAKAN KOMPARASI MODEL KLASIK (SVM, RANDOM FOREST) DAN KUANTUM (QSVC, VQC)
        </div>
      </div>
      <div style="display: flex; justify-content: center; margin-bottom: 16px;">
        <div style="background: var(--navy-dark); color: #fff; padding: 8px 32px; border-radius: 8px; text-align: center;">
          <div style="font-size: 11px; color: #93c5fd;">DISUSUN OLEH:</div>
          <div style="font-size: 15px; font-weight: bold;">FAHRY RIZKY SAMSUDIN</div>
          <div style="font-size: 12px; color: #cbd5e1;">NIM: 1237030018</div>
        </div>
      </div>
      <div style="display: flex; gap: 16px;">
        <div class="card" style="flex: 1;">
          <div style="font-size: 10px; font-weight: bold; color: var(--blue-accent);">DOSEN PEMBIMBING I:</div>
          <div style="font-size: 13px; font-weight: bold; color: var(--navy-dark);">Mada Sanjaya W.S., M.Si., Ph.D.</div>
          <div style="font-size: 10px; color: var(--text-muted);">NIP. 19851101 200912 1005</div>
        </div>
        <div class="card" style="flex: 1;">
          <div style="font-size: 10px; font-weight: bold; color: var(--emerald);">DOSEN PEMBIMBING II / PENGUJI:</div>
          <div style="font-size: 13px; font-weight: bold; color: var(--navy-dark);">Dr. Yudha Satya Perkasa, M.Si.</div>
          <div style="font-size: 10px; color: var(--text-muted);">NIP. 19780512 200801 1 009</div>
        </div>
      </div>
      <div class="slide-footer">
        <span>Proposal Tugas Akhir — Fisika UIN SGD Bandung</span>
        <span>Slide 1 / 16</span>
      </div>
    </div>

    <!-- SLIDE 2: LATAR BELAKANG -->
    <div class="slide" id="slide-2">
      <div class="slide-top-line"></div>
      <div class="slide-badge">Bab I: Pendahuluan</div>
      <div class="slide-title">Latar Belakang: Alur Masalah, Urgensi, & Solusi Riset</div>
      <div class="slide-content" style="justify-content: center; align-items: center;">
        <img src="output/diagrams/latar_belakang_flowchart.png" style="width: 100%; max-height: 90%; object-fit: contain; border-radius: 8px;" alt="Flowchart Latar Belakang">
      </div>
      <div class="slide-footer">
        <span>Proposal Tugas Akhir — Fisika UIN SGD Bandung</span>
        <span>Slide 2 / 16</span>
      </div>
    </div>

    <!-- SLIDE 3: RUMUSAN & BATASAN MASALAH -->
    <div class="slide" id="slide-3">
      <div class="slide-top-line"></div>
      <div class="slide-badge">Bab I: Pendahuluan</div>
      <div class="slide-title">Perumusan Masalah & Batasan Masalah Penelitian</div>
      <div class="slide-content">
        <div class="card" style="flex: 1;">
          <div class="card-title" style="color: var(--blue-accent);">RUMUSAN MASALAH PENELITIAN</div>
          <div class="card-body">
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>1. Rancang Bangun Hardware:</strong> Bagaimana merancang rantai instrumentasi sensor TMR ALT023-10E terintegrasi dengan in-amp AD623 dan ADC ADS1115 untuk deteksi formalin?</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>2. Karakteristik Metrologis:</strong> Bagaimana sensitivitas, linearitas (R²), limit of detection (LOD), dan limit of quantification (LOQ) sensor TMR berlabel nanofiber Fe3O4/PVA-Sitrat-ADH?</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>3. Komparasi 4 Model Cerdas:</strong> Bagaimana perbandingan akurasi, presisi, recall, F1, dan ROC-AUC antara model klasik (SVM, RF) vs model kuantum (QSVC, VQC)?</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>4. Ketahanan Derau & Kelayakan:</strong> Bagaimana tingkat ketahanan derau (noise robustness) dan latensi komputasi model kuantum dibanding model klasik untuk implementasi embedded?</div></div>
          </div>
        </div>
        <div class="card" style="flex: 1;">
          <div class="card-title" style="color: var(--emerald);">BATASAN MASALAH PENELITIAN</div>
          <div class="card-body">
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>Transduser:</strong> Sensor TMR ALT023-10E (NVE Corporation), rentang linier ±1.0 mT, catu 5.0 V tunggal.</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>Material Reseptor:</strong> Nanofiber Fe3O4/PVA-Sitrat-ADH via electrospinning & thermal curing 130 °C.</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>Pengkondisi Sinyal:</strong> AD623 (VREF = 2.50 V, G = 11) & filter pasif anti-aliasing RC (fc ≈ 159 Hz).</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>ADC & Komunikasi:</strong> ADS1115 16-bit (GAIN_TWOTHIRDS, 128 SPS), I2C ke Arduino Uno R3.</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>Sampel Analit:</strong> Formalin standar (0–100 ppm) dan ekstrak bakso riil (kontrol vs berformalin).</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>Komparasi Model:</strong> 4 Model: SVM (RBF), Random Forest, QSVC (ZZFeatureMap), dan VQC (Ansatz).</div></div>
          </div>
        </div>
      </div>
      <div class="slide-footer">
        <span>Proposal Tugas Akhir — Fisika UIN SGD Bandung</span>
        <span>Slide 3 / 16</span>
      </div>
    </div>

    <!-- SLIDE 4: TUJUAN & MANFAAT PENELITIAN -->
    <div class="slide" id="slide-4">
      <div class="slide-top-line"></div>
      <div class="slide-badge">Bab I: Pendahuluan</div>
      <div class="slide-title">Tujuan Penelitian & Kontribusi Manfaat Riset</div>
      <div class="slide-content">
        <div class="card" style="flex: 1;">
          <div class="card-title" style="color: var(--blue-accent);">TUJUAN PENELITIAN</div>
          <div class="card-body">
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>1. Rancang Bangun Sistem:</strong> Merealisasikan prototipe instrumen sensor TMR dengan modul pengkondisi sinyal AD623 dan ADC 16-bit ADS1115.</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>2. Karakterisasi Metrologis:</strong> Menentukan kurva kalibrasi V-B, sensitivitas rasiometrik, batas deteksi (LOD), dan LOQ sensor terhadap formalin standar.</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>3. Komparasi 4 Model ML:</strong> Mengevaluasi dan membandingkan performa akurasi, presisi, recall, F1, dan ROC-AUC antara SVM, Random Forest, QSVC, dan VQC.</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>4. Evaluasi Ketahanan Derau:</strong> Menguji ketahanan derau (noise robustness) model klasik vs kuantum dan latensi inferensi untuk kesiapan deployment.</div></div>
          </div>
        </div>
        <div class="card" style="flex: 1;">
          <div class="card-title" style="color: var(--gold);">MANFAAT & DAMPAK RISET</div>
          <div class="card-body">
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>Aspek Ilmiah & Spintronika:</strong> Memberikan kontribusi orisinal dalam penggabungan transduser spintronika TMR dengan material komposit nanofiber hijau dan komputasi kuantum (Qiskit).</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>Aspek Teknologi Instrumentasi:</strong> Menghasilkan alat uji formalin portabel bersuhu ruang yang cepat, murah, tidak destruktif, dan tidak membutuhkan reagen beracun di lapangan.</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>Aspek Keamanan Pangan Nasional:</strong> Menyediakan instrumen skrining kuantitatif bagi BPOM dan dinas pasar untuk melindungi masyarakat dari bahaya karsinogenik pangan.</div></div>
          </div>
        </div>
      </div>
      <div class="slide-footer">
        <span>Proposal Tugas Akhir — Fisika UIN SGD Bandung</span>
        <span>Slide 4 / 16</span>
      </div>
    </div>

    <!-- SLIDE 5: LANDASAN TEORI I -->
    <div class="slide" id="slide-5">
      <div class="slide-top-line"></div>
      <div class="slide-badge">Bab II: Tinjauan Pustaka</div>
      <div class="slide-title">Transduser Spintronik TMR & Reseptor Kovalen Nanofiber <span>| Transduksi Magneto-Mekanik</span></div>
      <div class="slide-content">
        <div class="card" style="flex: 1;">
          <div class="card-title">1. Transduser TMR ALT023-10E</div>
          <div class="card-body">
            <div class="bullet-item"><span class="bullet-dot">•</span><div>Efek Quantum Tunneling melintasi isolator tipis MgO pada struktur Magnetic Tunnel Junction (MTJ).</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div>Persamaan Julliere: <em>TMR = [2P1P2 / (1 - P1P2)] x 100%</em> (&gt; 200% pada suhu ruang).</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div>Sensitivitas 15–25 mV/V/mT pada medan rendah ±1.0 mT (6x lebih peka dari sensor GMR).</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div class="citation">Sitasi: (Julliere, 1975; Pannetier et al., 2022; NVE Corp., 2023)</div></div>
            <div style="display: flex; gap: 8px; margin-top: 6px;">
              <img src="Gambar/Bab2/babII_ALT023.png" style="height: 90px; border-radius: 4px; border: 1px solid #e2e8f0;" alt="TMR">
              <img src="Gambar/Bab2/babII_TMR_Layer.png" style="height: 90px; border-radius: 4px; border: 1px solid #e2e8f0;" alt="Layer">
            </div>
          </div>
        </div>
        <div class="card" style="flex: 1;">
          <div class="card-title" style="color: var(--emerald);">2. Nanofiber Fe3O4/PVA-Sitrat-ADH</div>
          <div class="card-body">
            <div class="bullet-item"><span class="bullet-dot">•</span><div>Partikel superparamagnetik Fe3O4 disintesis via ekstrak daun kelor (green synthesis ramah lingkungan).</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div>Thermal curing asam sitrat 130 °C membentuk taut silang ester yang tahan air (insoluble).</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div>Reseptor ADH mengikat formalin spesifik membentuk ikatan hidrazon kovalen (R-C=N-NH-R').</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div>Modulasi stray field magnetik: <em>B_stray ∝ 1/z³</em> menggeser tegangan sensor secara presisi.</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div class="citation">Sitasi: (Hermanson, 2013; Antarnusa et al., 2022; Türkoğlu, 2024)</div></div>
            <div style="margin-top: 6px;">
              <img src="Gambar/Bab2/babII_ikatan_formalin.png" style="height: 90px; border-radius: 4px; border: 1px solid #e2e8f0;" alt="Formalin Reaction">
            </div>
          </div>
        </div>
      </div>
      <div class="slide-footer">
        <span>Proposal Tugas Akhir — Fisika UIN SGD Bandung</span>
        <span>Slide 5 / 16</span>
      </div>
    </div>

    <!-- SLIDE 6: LANDASAN TEORI II -->
    <div class="slide" id="slide-6">
      <div class="slide-top-line"></div>
      <div class="slide-badge">Bab II: Tinjauan Pustaka</div>
      <div class="slide-title">Rantai Pengkondisi Sinyal AD623, ADC ADS1115, & Metrologi <span>| Presisi Sinyal Rendah Derau</span></div>
      <div class="slide-content">
        <div class="card" style="flex: 1;">
          <div class="card-title">1. Penguat Instrumentasi AD623 & LPF</div>
          <div class="card-body">
            <div class="bullet-item"><span class="bullet-dot">•</span><div>In-Amp rail-to-rail catu tunggal +5.0 V dengan CMRR tinggi meredam derau common-mode.</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div>Resistor gain RG = 10.0 kΩ menghasilkan penguatan tetap <em>G = 1 + (100 kΩ / RG) = 11</em>.</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div>Tegangan bias referensi VREF = 2.50 V (R3 = R4 = 1.0 kΩ) menjaga sinyal bipolar pada rentang 1.40–3.60 V (anti-clipping).</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div>Filter pasif RC (R=10 kΩ, C=100 nF, fc ≈ 159 Hz) membatasi frekuensi di bawah batas Nyquist.</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div class="citation">Sitasi: (Analog Devices, 2020; Pallàs-Areny & Webster, 2001)</div></div>
            <div style="margin-top: 6px;">
              <img src="Gambar/Bab2/babII_AD623_Pinout.png" style="height: 85px; border-radius: 4px; border: 1px solid #e2e8f0;" alt="AD623">
            </div>
          </div>
        </div>
        <div class="card" style="flex: 1;">
          <div class="card-title" style="color: var(--gold);">2. ADC 16-Bit ADS1115 & Metrologi IUPAC</div>
          <div class="card-body">
            <div class="bullet-item"><span class="bullet-dot">•</span><div>ADC Delta-Sigma 16-bit antarmuka I2C (alamat 0x48, laju konversi 128 SPS).</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div>PGA internal GAIN_TWOTHIRDS (FSR = ±6.144 V) menghasilkan resolusi 0.1875 mV/count.</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>Rumus LOD & LOQ Standar IUPAC:</strong><br><em>LOD = (3.3 x σ_blank) / m &nbsp;|&nbsp; LOQ = (10 x σ_blank) / m</em></div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div>Sensitivitas: <em>m = ΔV / ΔC</em> (kemiringan kurva respon kalibrasi sensor).</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div class="citation">Sitasi: (Texas Instruments, 2018; Mocak et al., 1997; IUPAC, 2014)</div></div>
            <div style="margin-top: 6px;">
              <img src="Gambar/Bab2/babII_ADS-1115-c.jpg" style="height: 85px; border-radius: 4px; border: 1px solid #e2e8f0;" alt="ADS1115">
            </div>
          </div>
        </div>
      </div>
      <div class="slide-footer">
        <span>Proposal Tugas Akhir — Fisika UIN SGD Bandung</span>
        <span>Slide 6 / 16</span>
      </div>
    </div>

    <!-- SLIDE 7: LANDASAN TEORI III -->
    <div class="slide" id="slide-7">
      <div class="slide-top-line"></div>
      <div class="slide-badge">Bab II: Tinjauan Pustaka</div>
      <div class="slide-title">Fondasi Matematis Komparasi 4 Model Machine Learning <span>| Klasik vs Kuantum</span></div>
      <div class="slide-content" style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
        <div class="card">
          <div class="card-title" style="color: var(--blue-accent);">1. Support Vector Machine (SVM) — Klasik</div>
          <div class="card-body" style="font-size: 11.5px;">
            <div>• Maksimasi marjin optimal dual problem: <em>max_α ∑ α_i - 0.5 ∑ α_i α_j y_i y_j K(x_i, x_j)</em></div>
            <div>• Kernel RBF Gauss: <em>K(x_i, x_j) = exp(-γ ||x_i - x_j||²)</em></div>
            <div>• Tuning hyperparameter C dan γ via Grid Search & 5-Fold CV.</div>
            <div class="citation">Sitasi: (Cortes & Vapnik, 1995; Schölkopf et al., 2002)</div>
          </div>
        </div>
        <div class="card">
          <div class="card-title" style="color: var(--navy-mid);">2. Random Forest (RF) — Klasik</div>
          <div class="card-body" style="font-size: 11.5px;">
            <div>• Ensemble Bagging dari B pohon keputusan acak mandiri.</div>
            <div>• Prediksi agregat mayoritas: <em>y_pred = mode{h_b(x)}</em> untuk b=1..B.</div>
            <div>• Tuning: n_estimators (50–200) dan max_depth (3–10). Evaluasi Gini Impurity.</div>
            <div class="citation">Sitasi: (Breiman, 2001; Tyralis et al., 2019)</div>
          </div>
        </div>
        <div class="card">
          <div class="card-title" style="color: var(--emerald);">3. Quantum Support Vector (QSVC) — Kuantum</div>
          <div class="card-body" style="font-size: 11.5px;">
            <div>• Pemetaan ke ruang Hilbert 8D 3-qubit: <em>|Φ(x)⟩ = U_Φ(x)|0⟩^⊗3</em> via ZZFeatureMap.</div>
            <div>• Quantum Kernel Matrix: <em>K_ij^Q = |⟨Φ(x_i)|Φ(x_j)⟩|²</em> dihitung pada simulator kuantum.</div>
            <div>• Optimasi marjin klasik diterapkan pada ruang berdimensi tinggi.</div>
            <div class="citation">Sitasi: (Havlíček et al., 2019; Schuld & Killoran, 2019)</div>
          </div>
        </div>
        <div class="card">
          <div class="card-title" style="color: var(--gold);">4. Variational Quantum Classifier (VQC) — Kuantum</div>
          <div class="card-body" style="font-size: 11.5px;">
            <div>• Sirkuit kuantum parametrik: <em>|ψ(x, θ)⟩ = W(θ) U_Φ(x) |0⟩^⊗3</em> (Ansatz RealAmplitudes).</div>
            <div>• Optimasi sudut θ gerbang rotasi secara iteratif via optimizer COBYLA/SPSA.</div>
            <div>• Prediksi kelas melalui pembacaan nilai ekspektasi Hamiltonian: <em>⟨Z_0⟩</em>.</div>
            <div class="citation">Sitasi: (Cerezo et al., 2021; Qiskit Machine Learning, 2024)</div>
          </div>
        </div>
      </div>
      <div class="slide-footer">
        <span>Proposal Tugas Akhir — Fisika UIN SGD Bandung</span>
        <span>Slide 7 / 16</span>
      </div>
    </div>

    <!-- SLIDE 8: MATRIKS PENELITIAN TERDAHULU -->
    <div class="slide" id="slide-8">
      <div class="slide-top-line"></div>
      <div class="slide-badge">Bab II: Tinjauan Pustaka</div>
      <div class="slide-title">Matriks Komparasi Penelitian Terdahulu & Kebaruan Riset</div>
      <div class="slide-content">
        <div class="card" style="width: 100%; padding: 10px;">
          <table>
            <thead>
              <tr>
                <th>Peneliti & Tahun</th>
                <th>Target Analit</th>
                <th>Transduser</th>
                <th>Material Reseptor</th>
                <th>Model Cerdas</th>
                <th>Limitasi / Keterbatasan</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Wang et al. (2021)</td>
                <td>Formalin</td>
                <td>MOS Gas Sensor</td>
                <td>ZnO Nanorod</td>
                <td>Tanpa ML</td>
                <td>Suhu operasi 300 °C, boros daya, interferensi aroma bumbu tinggi.</td>
              </tr>
              <tr>
                <td>Singhal et al. (2024)</td>
                <td>Formalin</td>
                <td>Elektrokimia</td>
                <td>Grafena-Kitosan</td>
                <td>Tanpa ML</td>
                <td>Destruktif, preparasi elektroda rumit, rentan fouling analit organik.</td>
              </tr>
              <tr>
                <td>Sun et al. (2023)</td>
                <td>Formalin</td>
                <td>Biosensor Enzim</td>
                <td>Enzim FDH Imobil</td>
                <td>KNN Klasik</td>
                <td>Stabilitas enzim rendah (&lt; 2 minggu), denaturasi cepat pada suhu ruang.</td>
              </tr>
              <tr>
                <td>Gilang Pratama (2026)</td>
                <td>Glukosa Saliva</td>
                <td>GMR Spintronik</td>
                <td>Fe3O4/PVA-GOx</td>
                <td>Random Forest</td>
                <td>Rasio MR rendah (10–15%), terbatas pada satu model klasik saja.</td>
              </tr>
              <tr class="highlight">
                <td>Fahry R. S. (2026)<br>[Penelitian Ini]</td>
                <td>Formalin Bakso</td>
                <td>TMR Spintronik<br>(ALT023-10E)</td>
                <td>Nanofiber Hijau<br>Fe3O4/PVA-Sitrat-ADH</td>
                <td>Komparasi 4 Model<br>(SVM, RF, QSVC, VQC)</td>
                <td>Kebaruan: MR &gt; 200%, ikatan kovalen spesifik, analisis komparatif ruang Hilbert & uji ketahanan derau.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      <div class="slide-footer">
        <span>Proposal Tugas Akhir — Fisika UIN SGD Bandung</span>
        <span>Slide 8 / 16</span>
      </div>
    </div>

    <!-- SLIDE 9: DIAGRAM ALIR PENELITIAN -->
    <div class="slide" id="slide-9">
      <div class="slide-top-line"></div>
      <div class="slide-badge">Bab III: Metode Penelitian</div>
      <div class="slide-title">Diagram Alir Tahapan Penelitian Menyeluruh <span>| 8 Tahapan Sistematis</span></div>
      <div class="slide-content">
        <div class="card" style="flex: 1.1;">
          <div class="card-title" style="color: var(--blue-accent);">8 TAHAPAN EKSEKUSI RISET</div>
          <div class="card-body">
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>1. Studi Literatur:</strong> Kajian transduser TMR, nanofiber kovalen, dan Quantum ML.</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>2. Desain Hardware:</strong> Rantai sinyal ALT023-10E → AD623 → LPF → ADS1115 → Arduino.</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>3. Desain Software:</strong> Firmware mikrokontroler dan GUI Python Raspberry Pi 5.</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>4. Sintesis Material:</strong> Elektrospinning Fe3O4/PVA, curing sitrat 130 °C, fungsionalisasi ADH.</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>5. Karakterisasi Medan:</strong> Pengujian V-B dan dV/dB terhadap acuan kumparan Helmholtz.</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>6. Pengujian Formalin:</strong> Uji respon larutan standar (0–100 ppm) dan ekstrak bakso pasar.</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>7. Pemodelan Cerdas:</strong> Pelatihan & validasi komparasi 4 model (SVM, RF, QSVC, VQC).</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>8. Evaluasi & Laporan:</strong> Analisis noise robustness, penyusunan naskah, dan publikasi.</div></div>
          </div>
        </div>
        <div class="card" style="flex: 0.9;">
          <div class="card-title" style="color: var(--emerald);">PENJAMINAN MUTU DATA RISET</div>
          <div class="card-body">
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>Ground Truth Metrologis:</strong> Pengukuran medan magnet Helmholtz menggunakan teslameter terkalibrasi sebagai acuan absolut.</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>Replikasi Pengukuran:</strong> Setiap titik konsentrasi diukur secara berulang (triplo) untuk mendapatkan simpangan baku presisi.</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>Protokol Stabilisasi:</strong> Akuisisi 5.0 detik mengabaikan 1.0 detik pertama (settling time) untuk membuang efek transien awal.</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>Pencegahan Data Leakage:</strong> Standarisasi fitur dan pembagian dataset dilakukan berbasis sampel tetesan independen, bukan irisan waktu yang sama.</div></div>
          </div>
        </div>
      </div>
      <div class="slide-footer">
        <span>Proposal Tugas Akhir — Fisika UIN SGD Bandung</span>
        <span>Slide 9 / 16</span>
      </div>
    </div>

    <!-- SLIDE 10: MEKATRONIKA & SKEMATIK HARDWARE -->
    <div class="slide" id="slide-10">
      <div class="slide-top-line"></div>
      <div class="slide-badge">Bab III: Metode Penelitian</div>
      <div class="slide-title">Desain Mekatronika & Rangkaian Perangkat Keras <span>| Integrasi Fisik & Elektronik</span></div>
      <div class="slide-content">
        <div class="card" style="flex: 1;">
          <div class="card-title">1. Mekatronika Casing & Kumparan Helmholtz</div>
          <div class="card-body">
            <div>Kit terintegrasi dengan layar sentuh Raspberry Pi 5, mikrokontroler Arduino Uno, kumparan Helmholtz (0–16 V DC), dan slot sensor TMR.</div>
            <div style="display: flex; gap: 8px; margin-top: 8px;">
              <img src="Gambar/Bab3/babIII_desainluar.jpg" style="height: 150px; border-radius: 4px; border: 1px solid #e2e8f0;" alt="Casing Luar">
              <img src="Gambar/Bab3/babIII_desaindalam.jpg" style="height: 150px; border-radius: 4px; border: 1px solid #e2e8f0;" alt="Casing Dalam">
            </div>
          </div>
        </div>
        <div class="card" style="flex: 1;">
          <div class="card-title" style="color: var(--navy-mid);">2. Rantai Sinyal Presisi & Grounding</div>
          <div class="card-body">
            <div>Filter RFI diferensial, AD623 (G=11, VREF=2.50 V), LPF pasif RC (fc=159 Hz), ADS1115 16-bit, serta pemisahan ground AGND dan DGND.</div>
            <div style="margin-top: 8px;">
              <img src="Gambar/Bab3/babIII_skematik_TMR_grounding_fix.png" style="max-height: 150px; border-radius: 4px; border: 1px solid #e2e8f0;" alt="Skematik">
            </div>
          </div>
        </div>
      </div>
      <div class="slide-footer">
        <span>Proposal Tugas Akhir — Fisika UIN SGD Bandung</span>
        <span>Slide 10 / 16</span>
      </div>
    </div>

    <!-- SLIDE 11: DIAGRAM ALIR SOFTWARE -->
    <div class="slide" id="slide-11">
      <div class="slide-top-line"></div>
      <div class="slide-badge">Bab III: Metode Penelitian</div>
      <div class="slide-title">Diagram Alir Perangkat Lunak Mikrokontroler & Python Host</div>
      <div class="slide-content">
        <div class="card" style="flex: 1; align-items: center;">
          <div class="card-title" style="width: 100%;">1. Firmware Arduino Uno (sensor_tmr_formalin.ino)</div>
          <div style="font-size: 11px; color: var(--text-muted); margin-bottom: 8px; width: 100%;">
            Akuisisi deterministik 128 SPS, pembacaan I2C pin AIN0, streaming serial CSV murni tanpa rata-rata.
          </div>
          <img src="Gambar/Bab3/babIII_AlurSoftwareArduino.drawio.png" style="max-height: 220px; object-fit: contain;" alt="Flowchart Arduino">
        </div>
        <div class="card" style="flex: 1.1; align-items: center;">
          <div class="card-title" style="color: var(--emerald); width: 100%;">2. Host Python GUI (kalibrasi_tmr_formalin.py)</div>
          <div style="font-size: 11px; color: var(--text-muted); margin-bottom: 8px; width: 100%;">
            Engine berbasis durasi 5.0 detik (buang settling time 1.0 detik), regresi linier otomatis, dan plot 300 DPI.
          </div>
          <img src="Gambar/Bab3/babIII_DiagramAlirPython.drawio.png" style="max-height: 220px; object-fit: contain;" alt="Flowchart Python">
        </div>
      </div>
      <div class="slide-footer">
        <span>Proposal Tugas Akhir — Fisika UIN SGD Bandung</span>
        <span>Slide 11 / 16</span>
      </div>
    </div>

    <!-- SLIDE 12: DIAGRAM ALIR PEMODELAN & DEPLOYMENT -->
    <div class="slide" id="slide-12">
      <div class="slide-top-line"></div>
      <div class="slide-badge">Bab III: Metode Penelitian</div>
      <div class="slide-title">Diagram Alir Pemodelan 4 Model & Deployment Realtime</div>
      <div class="slide-content">
        <div class="card" style="flex: 1.2; align-items: center;">
          <div class="card-title" style="width: 100%;">Pelatihan Komparatif 4 Model (SVM, RF vs QSVC, VQC)</div>
          <div style="font-size: 11px; color: var(--text-muted); margin-bottom: 8px; width: 100%;">
            Ekstraksi 3 Fitur (V_mean, ΔV, σ_V), split 80:20, validasi 5-fold CV, dan uji noise robustness.
          </div>
          <img src="Gambar/Bab3/babIII_ModelBuilding.drawio.png" style="max-height: 220px; object-fit: contain;" alt="Flowchart Model Building">
        </div>
        <div class="card" style="flex: 1; align-items: center;">
          <div class="card-title" style="color: var(--emerald); width: 100%;">Deployment Sistem Inferensi Realtime</div>
          <div style="font-size: 11px; color: var(--text-muted); margin-bottom: 8px; width: 100%;">
            Penerapan model optimal pada Raspberry Pi 5 GUI untuk klasifikasi status keamanan pangan bakso.
          </div>
          <img src="Gambar/Bab3/babIII_ModelDeploy.drawio.png" style="max-height: 220px; object-fit: contain;" alt="Flowchart Model Deploy">
        </div>
      </div>
      <div class="slide-footer">
        <span>Proposal Tugas Akhir — Fisika UIN SGD Bandung</span>
        <span>Slide 12 / 16</span>
      </div>
    </div>

    <!-- SLIDE 13: SINTESIS & PREPARASI BAKSO -->
    <div class="slide" id="slide-13">
      <div class="slide-top-line"></div>
      <div class="slide-badge">Bab III: Metode Penelitian</div>
      <div class="slide-title">Sintesis Nanofiber Kovalen & Preparasi Sampel Bakso Riil</div>
      <div class="slide-content">
        <div class="card" style="flex: 1;">
          <div class="card-title" style="color: var(--blue-accent);">SINTESIS NANOFIBER Fe3O4/PVA-SITRAT-ADH</div>
          <div class="card-body">
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>1. Sintesis Fe3O4 Hijau:</strong> Kopresipitasi garam besi dengan ekstrak daun kelor sebagai agen pereduksi ramah lingkungan.</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>2. Larutan Polimer Doping:</strong> Pencampuran PVA 10% w/v dengan 2% w/v nanopartikel Fe3O4 dan 5% w/v asam sitrat.</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>3. Proses Electrospinning:</strong> Tegangan tinggi 15 kV, jarak jarum-kolektor 12 cm, laju alir syringe pump 0.8 mL/jam.</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>4. Thermal Curing 130 °C:</strong> Pemanasan oven 130 °C selama 2 jam untuk reaksi esterifikasi penaut silang anti-air.</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>5. Imobilisasi ADH:</strong> Fungsionalisasi gugus hidrazida terminal bebas sebagai chemo-receptor spesifik formaldehida.</div></div>
          </div>
        </div>
        <div class="card" style="flex: 1;">
          <div class="card-title" style="color: var(--emerald);">PREPARASI & PENGUJIAN SAMPEL BAKSO</div>
          <div class="card-body">
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>1. Sampling Pasar:</strong> Pengambilan sampel bakso sapi dari pasar tradisional dan pasar modern di wilayah Bandung.</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>2. Pembuatan Sampel Kontrol:</strong> Bakso higienis buatan laboratorium tanpa penambahan bahan pengawet sintetik.</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>3. Preparasi Sampel Spiked:</strong> Injeksi larutan formalin dengan variasi konsentrasi terukur (10, 20, 50, 100 ppm) untuk validasi.</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>4. Ekstraksi Filtrat:</strong> Penghancuran mekanik sampel bakso, penambahan aquades steril, sonikasi 15 menit, dan sentrifugasi.</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div><strong>5. Prosedur Uji Sensor TMR:</strong> Penetesan 50 µL filtrat ke atas reseptor nanofiber, perekaman sinyal 5.0 detik, dan inferensi ML.</div></div>
          </div>
        </div>
      </div>
      <div class="slide-footer">
        <span>Proposal Tugas Akhir — Fisika UIN SGD Bandung</span>
        <span>Slide 13 / 16</span>
      </div>
    </div>

    <!-- SLIDE 14: GANTT CHART -->
    <div class="slide" id="slide-14">
      <div class="slide-top-line"></div>
      <div class="slide-badge">Bab III: Metode Penelitian</div>
      <div class="slide-title">Jadwal & Tempat Pelaksanaan Penelitian (Gantt Chart)</div>
      <div class="slide-content" style="flex-direction: column; gap: 12px;">
        <div class="card" style="background: var(--navy-dark); color: #fff; border-color: var(--navy-mid); padding: 12px 18px;">
          <div style="font-size: 12px; font-weight: bold; color: #93c5fd; margin-bottom: 2px;">
            LOKASI & PERIODE RISET: BOLABOT TECHNO ROBOTIC INSTITUTE BANDUNG
          </div>
          <div style="font-size: 11.5px; color: #cbd5e1;">
            Jl. Sauyunan VI No. 10 Blok F6, Kelurahan Cipadung, Kecamatan Panyileukan, Kota Bandung, Jawa Barat 40614.<br>
            Periode Riset Efektif: Bulan September – Desember 2026 (Durasi: 16 Pekan Kerja Efektif).
          </div>
        </div>
        <div class="card" style="padding: 6px;">
          <table>
            <thead>
              <tr>
                <th style="width: 40px; text-align: center;">No</th>
                <th>Tahapan Kegiatan Penelitian</th>
                <th style="width: 120px; text-align: center;">Bulan 1 (Sep)</th>
                <th style="width: 120px; text-align: center;">Bulan 2 (Okt)</th>
                <th style="width: 120px; text-align: center;">Bulan 3 (Nov)</th>
                <th style="width: 120px; text-align: center;">Bulan 4 (Des)</th>
              </tr>
            </thead>
            <tbody>
              <tr><td style="text-align: center;">1</td><td>Studi literatur & perancangan desain rantai sinyal hardware</td><td style="text-align: center; font-weight: bold; color: var(--blue-accent);">[ X ]</td><td style="text-align: center; color: var(--text-muted);">[   ]</td><td style="text-align: center; color: var(--text-muted);">[   ]</td><td style="text-align: center; color: var(--text-muted);">[   ]</td></tr>
              <tr><td style="text-align: center;">2</td><td>Sintesis material nanofiber Fe3O4/PVA-Sitrat-ADH kovalen</td><td style="text-align: center; font-weight: bold; color: var(--blue-accent);">[ X ]</td><td style="text-align: center; font-weight: bold; color: var(--blue-accent);">[ X ]</td><td style="text-align: center; color: var(--text-muted);">[   ]</td><td style="text-align: center; color: var(--text-muted);">[   ]</td></tr>
              <tr><td style="text-align: center;">3</td><td>Perakitan instrumen TMR, kalibrasi Helmholtz, & firmware</td><td style="text-align: center; color: var(--text-muted);">[   ]</td><td style="text-align: center; font-weight: bold; color: var(--blue-accent);">[ X ]</td><td style="text-align: center; font-weight: bold; color: var(--blue-accent);">[ X ]</td><td style="text-align: center; color: var(--text-muted);">[   ]</td></tr>
              <tr><td style="text-align: center;">4</td><td>Pengujian larutan formalin standar & ekstrak sampel bakso</td><td style="text-align: center; color: var(--text-muted);">[   ]</td><td style="text-align: center; color: var(--text-muted);">[   ]</td><td style="text-align: center; font-weight: bold; color: var(--blue-accent);">[ X ]</td><td style="text-align: center; color: var(--text-muted);">[   ]</td></tr>
              <tr><td style="text-align: center;">5</td><td>Pelatihan & komparasi model klasik vs kuantum (Qiskit)</td><td style="text-align: center; color: var(--text-muted);">[   ]</td><td style="text-align: center; color: var(--text-muted);">[   ]</td><td style="text-align: center; font-weight: bold; color: var(--blue-accent);">[ X ]</td><td style="text-align: center; font-weight: bold; color: var(--blue-accent);">[ X ]</td></tr>
              <tr><td style="text-align: center;">6</td><td>Evaluasi noise robustness, analisis metrologis, & skripsi</td><td style="text-align: center; color: var(--text-muted);">[   ]</td><td style="text-align: center; color: var(--text-muted);">[   ]</td><td style="text-align: center; color: var(--text-muted);">[   ]</td><td style="text-align: center; font-weight: bold; color: var(--blue-accent);">[ X ]</td></tr>
            </tbody>
          </table>
        </div>
      </div>
      <div class="slide-footer">
        <span>Proposal Tugas Akhir — Fisika UIN SGD Bandung</span>
        <span>Slide 14 / 16</span>
      </div>
    </div>

    <!-- SLIDE 15: DAFTAR PUSTAKA -->
    <div class="slide" id="slide-15">
      <div class="slide-top-line"></div>
      <div class="slide-badge">Daftar Pustaka</div>
      <div class="slide-title">Pustaka Rujukan Utama Berbobot Internasional</div>
      <div class="slide-content">
        <div class="card" style="width: 100%;">
          <div class="card-title" style="color: var(--navy-mid);">DAFTAR REFERENSI KUNCI PROPOSAL</div>
          <div class="card-body" style="font-size: 11.5px; gap: 6px;">
            <div class="bullet-item"><span class="bullet-dot">•</span><div>Analog Devices. (2020). <em>AD623: Single-Supply, Rail-to-Rail, Low Cost Instrumentation Amplifier Data Sheet (Rev. E)</em>. Norwood: Analog Devices, Inc.</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div>Antarnusa, G., Suharyadi, E., & Kato, T. (2022). Giant Magnetoresistance Biosensor Based on Fe3O4 Magnetic Nanoparticles for Biomedical Applications. <em>Sensors</em>, 22(14), 5120.</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div>Breiman, L. (2001). Random Forests. <em>Machine Learning</em>, 45(1), 5–32.</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div>Cerezo, M., Arrasmith, A., Babbush, R., Benjamin, S. C., Endo, S., Fujii, K., ... & Coles, P. J. (2021). Variational Quantum Algorithms. <em>Nature Reviews Physics</em>, 3(9), 625–644.</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div>Cortes, C., & Vapnik, V. (1995). Support-Vector Networks. <em>Machine Learning</em>, 20(3), 273–297.</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div>Havlíček, V., Córcoles, A. D., Temme, K., Harrow, A. W., Kandala, A., Chow, J. M., & Gambetta, J. M. (2019). Supervised Learning with Quantum-Enhanced Feature Spaces. <em>Nature</em>, 567(7747), 209–212.</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div>Hermanson, G. T. (2013). <em>Bioconjugate Techniques</em> (3rd ed.). Boston: Academic Press.</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div>Mocak, J., Bond, A. M., Mitchell, S., & Scollary, G. (1997). A Statistical Overview of Limit of Detection and Limit of Quantification in Analytical Chemistry. <em>Pure and Applied Chemistry</em>, 69(2), 297–328.</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div>NVE Corporation. (2023). <em>TMR ALT023-10E High Sensitivity Analog Magnetometer Sensor Catalog</em>. Eden Prairie: NVE Corporation.</div></div>
            <div class="bullet-item"><span class="bullet-dot">•</span><div>Pannetier, M., Fermon, C., Le Goff, G., Simola, J., & Kerr, E. (2022). High-Sensitivity TMR Sensors for Biomagnetic Applications. <em>Journal of Magnetism and Magnetic Materials</em>, 548, 168920.</div></div>
          </div>
        </div>
      </div>
      <div class="slide-footer">
        <span>Proposal Tugas Akhir — Fisika UIN SGD Bandung</span>
        <span>Slide 15 / 16</span>
      </div>
    </div>

    <!-- SLIDE 16: PENUTUP -->
    <div class="slide" id="slide-16" style="justify-content: center; align-items: center; text-align: center;">
      <div class="slide-top-line"></div>
      <div class="card" style="border-color: var(--blue-accent); padding: 40px 60px; max-width: 800px; width: 100%;">
        <div style="display: flex; justify-content: center; gap: 20px; margin-bottom: 20px;">
          <img src="Gambar/Logo/Logo UIN.png" style="height: 64px;" alt="UIN">
          <img src="Gambar/Logo/Logo Fisika UIN.png" style="height: 64px;" alt="Fisika">
        </div>
        <div style="font-size: 32px; font-weight: 800; color: var(--navy-dark); margin-bottom: 8px;">
          SEKIAN & TERIMA KASIH
        </div>
        <div style="font-size: 18px; font-weight: 700; color: var(--blue-accent); margin-bottom: 24px;">
          Sesi Diskusi & Tanya Jawab Seminar Proposal Tugas Akhir
        </div>
        <div style="font-size: 15px; font-weight: bold; color: var(--navy-mid); margin-bottom: 4px;">
          Fahry Rizky Samsudin (NIM: 1237030018)
        </div>
        <div style="font-size: 12px; color: var(--text-muted); line-height: 1.4;">
          Jurusan Fisika, Fakultas Sains dan Teknologi<br>
          Universitas Islam Negeri Sunan Gunung Djati Bandung<br>
          Tahun 2026
        </div>
      </div>
      <div class="slide-footer">
        <span>Proposal Tugas Akhir — Fisika UIN SGD Bandung</span>
        <span>Slide 16 / 16</span>
      </div>
    </div>

  </div>

</body>
</html>
"""
    with open(HTML_OUTPUT, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"[SUKSES] Pratinjau HTML diperbarui: {HTML_OUTPUT} (16 Slide Bebas AI Slop)")

if __name__ == "__main__":
    generate_html_preview()
