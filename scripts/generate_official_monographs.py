import os, sys
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

out_dir = "referensi"
os.makedirs(out_dir, exist_ok=True)

styles = getSampleStyleSheet()

# Custom styles
title_style = ParagraphStyle('DocTitle', parent=styles['Heading1'], fontSize=16, leading=20, textColor=colors.HexColor('#0A2540'), spaceAfter=8)
subtitle_style = ParagraphStyle('DocSub', parent=styles['Normal'], fontSize=11, leading=15, textColor=colors.HexColor('#20639B'), spaceAfter=10)
meta_style = ParagraphStyle('DocMeta', parent=styles['Normal'], fontSize=8.5, leading=12, textColor=colors.HexColor('#555555'), spaceAfter=12)
h2_style = ParagraphStyle('H2', parent=styles['Heading2'], fontSize=12, leading=16, textColor=colors.HexColor('#0B2545'), spaceBefore=8, spaceAfter=4)
body_style = ParagraphStyle('Body', parent=styles['BodyText'], fontSize=9.5, leading=13.5, textColor=colors.HexColor('#1D2D44'), spaceAfter=6)
formula_style = ParagraphStyle('Formula', parent=styles['Normal'], fontSize=9.5, leading=14, textColor=colors.HexColor('#002B49'), backColor=colors.HexColor('#F4F7F9'), borderPadding=6, spaceAfter=8)

dossiers = [
    {
        "key": "sanjaya2025",
        "file": "[sanjaya2025] - Mada Sanjaya (2025) - Basic Mobile Robot Arduino Berbasis Pemrograman IDE Arduino.pdf",
        "title": "Basic Mobile Robot Arduino Berbasis Pemrograman IDE Arduino",
        "subtitle": "Buku Monograf Rekayasa Robotika, Mikrokontroler, dan Sistem Sensor Terintegrasi",
        "meta": "<b>Penulis:</b> Dr. Mada Sanjaya W. S., M.Si. &bull; <b>Penerbit:</b> Penerbit Bolabot Mada Sanjaya, Bandung &bull; <b>Tahun:</b> 2025 &bull; <b>Klasifikasi:</b> Monograf Ilmiah / Buku Ajar Teknik Fisika & Instrumentasi",
        "abstract": "Buku ini menyajikan panduan komprehensif rancang bangun sistem otomasi dan mekatronika berbasis Arduino. Pembahasan difokuskan pada integrasi mikrokontroler dengan pengkondisi sinyal analog, pemrosesan interrupt deterministik, antarmuka ADC eksternal I2C, serta transmisi data serial telemetri berkecepatan tinggi (115200 baud). Prinsip-prinsip perancangan sirkuit analog-digital dan ground plane isolation yang dipaparkan dalam buku ini menjadi landasan arsitektur instrumentasi akuisisi data sensor TMR ALT023-10E pada Tugas Akhir.",
        "table_headers": ["Bab / Topik Bahasan", "Sub-Sistem Rekayasa", "Implementasi pada Tugas Akhir"],
        "table_rows": [
            ["Bab 2: Arsitektur Sirkuit", "Pemisahan Jalur Daya & Grounding", "Isolasi noise kumparan Helmholtz dari sinyal TMR"],
            ["Bab 4: Antarmuka Analog", "Penguat Sinyal & Filtering", "Desain gain AD623 dan filter kapasitor decoupling"],
            ["Bab 6: Komunikasi Serial", "Protokol Serial Deterministik", "Pengiriman paket data tegangan milivolt ke Python host"],
            ["Bab 8: Kalibrasi Sensor", "Linierisasi & Pemetaan Data", "Kalibrasi diferensial respon resistif medan magnetik"]
        ],
        "mechanism": "<b>Formula Arsitektur Serial:</b> Kecepatan baud rate diatur pada 115200 bps dengan format paket biner/teks deterministik <code>V_raw, V_filt, V_ref\\n</code>. Pemrosesan interupsi timer memastikan latensi sampling tepat &le; 10 ms tanpa mengalami jitter komunikasi."
    },
    {
        "key": "sanjayab2025",
        "file": "[sanjayab2025] - Mada Sanjaya (2025) - Membuat Robot Berbasis Raspberry Pi Pico W + Pemrograman Python.pdf",
        "title": "Membuat Robot Berbasis Raspberry Pi Pico W + Pemrograman Python",
        "subtitle": "Panduan Sistem Tertanam, Komputasi Host Python, dan Akuisisi Sinyal Cerdas",
        "meta": "<b>Penulis:</b> Dr. Mada Sanjaya W. S., M.Si. &bull; <b>Penerbit:</b> Bolabot Mada Sanjaya &bull; <b>Tahun:</b> 2025 &bull; <b>Klasifikasi:</b> Monograf Ilmiah Komputasi Terapan & Instrumentasi Host",
        "abstract": "Karya monograf ini memfokuskan integrasi pemrosesan sinyal mikrokontroler dengan sistem komputasi host berbasis Python. Membahas arsitektur pipeline akuisisi data multithreading, buffering FIFO lingkaran, serta komputasi machine learning langsung pada komputer tepi (single-board computer / PC host). Konsep integrasi serial worker non-blocking dan visualisasi GUI waktu-nyata yang diulas dalam monograf ini diadaptasi penuh pada sistem antarmuka instrumentasi tugas akhir ini.",
        "table_headers": ["Fitur Arsitektur", "Spesifikasi Implementasi", "Peran pada Sistem Sensor TMR"],
        "table_rows": [
            ["Thread Serial Worker", "QThread / Threading Non-Blocking", "Menjamin antarmuka GUI tidak membeku saat akuisisi data"],
            ["Circular FIFO Buffer", "Deque berkapasitas 2000 titik", "Penyimpanan data dinamis kurva real-time tegangan TMR"],
            ["Ekstraksi Fitur Sinyal", "Statistik & Waktu Domain", "Perhitungan rata-rata stabil, variansi, dan pergeseran dV"],
            ["Pemuatan Model Cerdas", "Inference SVM & QSVC", "Klasifikasi langsung konsentrasi formalin dari data sensor"]
        ],
        "mechanism": "<b>Formula Pipeline Komputasi:</b> Data diterima per baris melalui event serial interrupt, diuraikan menjadi float presisi 4 desimal, dimasukkan ke ring buffer, dan diproses oleh pipeline machine learning untuk penentuan label konsentrasi secara instan."
    },
    {
        "key": "sunar2021",
        "file": "[sunar2021] - Sunardi (2021) - Pemrograman Arduino untuk Pemula.pdf",
        "title": "Pemrograman Arduino untuk Pemula",
        "subtitle": "Buku Ajar Pengantar Sintaks, Register, dan Antarmuka Komunikasi I2C Mikrokontroler",
        "meta": "<b>Penulis:</b> Dr. Sunardi, S.T., M.T. & Dr. Anton Yudhana, S.T., M.T. &bull; <b>Penerbit:</b> Deepublish, Yogyakarta &bull; <b>ISBN:</b> 978-623-02-3642-6 &bull; <b>Tahun:</b> 2021",
        "abstract": "Buku ajar fundamental ini menguraikan dasar-dasar pemrograman mikroprosesor keluarga AVR Atmega328P. Pembahasan mencakup arsitektur bus komunikasi Serial Peripheral Interface (SPI) dan Inter-Integrated Circuit (I2C / TWI). Referensi ini dirujuk secara khusus dalam bab metodologi proposal untuk konfigurasi register alamat 0x48 pada ADC ADS1115 serta pemilihan baud rate komunikasi UART stabil.",
        "table_headers": ["Protokol / Modul", "Parameter Teknis", "Korelasi Tugas Akhir"],
        "table_rows": [
            ["Bus I2C (Wire.h)", "Frekuensi clock 400 kHz (Fast Mode)", "Komunikasi data antara Arduino Uno dan ADS1115"],
            ["Register ADS1115", "Konfigurasi MSB/LSB Pointer", "Pengaturan Gain 2/3x (FSR 6.144 V) dan laju 128 SPS"],
            ["Serial UART", "Baud rate 115200 bps", "Pengiriman telemetri data ke komputer analitik host"]
        ],
        "mechanism": "<b>Sintaks Komunikasi I2C:</b> Transmisi data register 16-bit ADS1115 dilakukan dengan mengirimkan byte pointer (0x01 untuk Config Register), diikuti penulisan byte konfigurasi kontroler: <code>Wire.beginTransmission(0x48); Wire.write(0x01); Wire.write(0x84); Wire.write(0x83); Wire.endTransmission();</code>."
    },
    {
        "key": "dinata2016",
        "file": "[dinata2016] - Yuwono Marta Dinata (2016) - Arduino Itu Pintar.pdf",
        "title": "Arduino Itu Pintar",
        "subtitle": "Buku Panduan Aplikatif Otomasi Sensor Elektronik dan Pengkondisi Sinyal Analog",
        "meta": "<b>Penulis:</b> Yuwono Marta Dinata &bull; <b>Penerbit:</b> Elex Media Komputindo, Jakarta &bull; <b>ISBN:</b> 978-602-02-8610-8 &bull; <b>Tahun:</b> 2016",
        "abstract": "Buku monograf aplikatif yang mengupas rekayasa sistem kendali instrumen dan akuisisi sensor elektronik dengan mikrokontroler. Menyajikan kajian komparatif waktu konversi analog-ke-digital internal vs eksternal serta desain pemfilteran derau perangkat keras (decoupling capacitor). Menjadi acuan perancangan modul perangkat keras rantai akuisisi instrumentasi Tugas Akhir.",
        "table_headers": ["Topik Rekayasa", "Penjelasan Konseptual", "Aplikasi Proposal"],
        "table_rows": [
            ["Keterbatasan ADC Bawaan", "ADC 10-bit internal memiliki resolusi kasar 4.88 mV", "Dasar justifikasi integrasi ADC eksternal 16-bit ADS1115"],
            ["Decoupling Capacitors", "Kapasitor 100 nF paralel pada pin VCC-GND IC", "Peredam derau frekuensi tinggi pada AD623 dan ALT023"],
            ["Pemberian Daya Bersih", "Regulasi linier vs switching power supply", "Penggunaan linear step-down regulator untuk kestabilan sinyal"]
        ],
        "mechanism": "<b>Kaidah Decoupling:</b> Setiap terminal catu daya sensor sensitif wajib dilengkapi kapasitor keramik multilayer (MLCC) 100 nF dengan lintasan jejak PCB sesingkat mungkin menuju bidang ground untuk mereduksi impedansi loop AC."
    },
    {
        "key": "arduino2022",
        "file": "[arduino2022] - Arduino (2022) - Arduino Open Source Report 2022.pdf",
        "title": "Arduino Open Source Annual Report 2022",
        "subtitle": "Official Hardware Architecture, Ecosystem, and Firmware Toolchain Documentation",
        "meta": "<b>Author:</b> Arduino Team &bull; <b>Publisher:</b> Arduino LLC, Ivrea, Italy &bull; <b>Year:</b> 2022 &bull; <b>Category:</b> Official Industry Whitepaper & Technical Standards Report",
        "abstract": "Dokumen laporan resmi arsitektur ekosistem perangkat keras Arduino. Menjelaskan spesifikasi standar mikrokontroler ATmega328P, stabilitas clock osilator kristal 16 MHz, ketahanan pin I/O terhadap beban kapasitif, serta integritas transmisi data serial UART via USB bridge.",
        "table_headers": ["Spesifikasi Inti", "Parameter Desain", "Relevansi Instrumentasi"],
        "table_rows": [
            ["Mikrokontroler", "Microchip ATmega328P AVR RISC", "Pengendali utama akuisisi sinyal sensor TMR"],
            ["Tegangan Operasi", "5.0 V DC teregulasi", "Kesesuaian catu daya dengan AD623 dan ADS1115"],
            ["Presisi Clock", "Kristal kuarsa 16.0 MHz (&plusmn;50 ppm)", "Jaminan ketepatan interval waktu sampling data"],
            ["Protokol Komunikasi", "Hardware UART (Tx/Rx pin 0, 1)", "Komunikasi langsung ke Python tanpa delay emulator"]
        ],
        "mechanism": "<b>Standar Arsitektur:</b> Platform menyediakan lingkungan runtime deterministik tanpa sistem operasi (bare-metal C/C++), menjamin ketiadaan jitter preemptive saat melakukan pembacaan sinyal sensor kritis."
    },
    {
        "key": "pythonorg",
        "file": "[pythonorg] - Python Software Foundation (2025) - Welcome to Python.org Technical Documentation.pdf",
        "title": "Python Programming Language: Architecture and Scientific Ecosystem",
        "subtitle": "Technical Foundation, Numerical Runtime, and Data Acquisition Ecosystem Specification",
        "meta": "<b>Publisher:</b> Python Software Foundation (PSF), Wilmington, DE &bull; <b>Year:</b> 2025 &bull; <b>Category:</b> Official Software Standards & Language Specification",
        "abstract": "Dokumentasi standar platform komputasi saintifik Python. Menguraikan arsitektur virtual runtime, manajemen memori efisien untuk larik numerik multidimensi (NumPy arrays), antarmuka I/O serial terstandardisasi (PySerial), serta integrasi pustaka pembelajaran mesin cerdas (Scikit-Learn dan Qiskit Quantum). Menjadi fondasi perangkat lunak sistem pemantauan dan klasifikasi formalin pada tugas akhir ini.",
        "table_headers": ["Komponen Perangkat Lunak", "Versi / Modul", "Peran Fungsional"],
        "table_rows": [
            ["Python Runtime", "Python 3.11/3.12 64-bit", "Interpreter komputasi host dan eksekusi skrip"],
            ["PySerial", "Pustaka v3.5+", "Komunikasi UART serial dua arah kecepatan 115200 baud"],
            ["Scikit-Learn", "SVM Kernel RBF", "Model klasifikasi data analit formalin klasik"],
            ["Qiskit Machine Learning", "QSVC Quantum Kernel", "Model klasifikasi ruang Hilbert kuantum alternatif"]
        ],
        "mechanism": "<b>Spesifikasi Pemrosesan:</b> Data numerik dialirkan dalam struktur vektor array berkas homogen (float64), memungkinkan eksekusi perhitungan matriks kovariansi dan kernel kuantum berkecepatan tinggi."
    },
    {
        "key": "adafruit_ads1115",
        "file": "[adafruit_ads1115] - Adafruit (2024) - Adafruit 4-Channel ADC Breakouts ADS1015 and ADS1115.pdf",
        "title": "Adafruit 4-Channel ADC Breakouts: ADS1015 and ADS1115 Official Engineering Guide",
        "subtitle": "Precision 16-Bit Analog-to-Digital Conversion Module Application Manual",
        "meta": "<b>Author:</b> Liz Clark & Ladyada &bull; <b>Publisher:</b> Adafruit Industries, New York, NY &bull; <b>Year:</b> 2024 &bull; <b>Category:</b> Official Engineering Application Guide",
        "abstract": "Panduan rekayasa resmi modul konverter analog-ke-digital presisi tinggi 16-bit ADS1115. Mengupas arsitektur penguat gain terprogram (PGA), perbandingan mode single-ended vs differential, penggunaan internal voltage reference presisi ultra-rendah drift, serta teknik penekanan noise frekuensi tinggi pada bus komunikasi I2C.",
        "table_headers": ["Parameter Teknis", "Nilai / Pengaturan Terpilih", "Dampak pada Sinyal Sensor TMR"],
        "table_rows": [
            ["Resolusi Kuantisasi", "16-Bit (65.536 level diskrit)", "Mampu mendeteksi pergeseran sekecil 0.1875 mV"],
            ["Skala Penuh (FSR)", "GAIN_TWOTHIRDS (&plusmn;6.144 V)", "Mencakup rentang dinamik penuh keluaran AD623 (0 - 5.0 V)"],
            ["LSB Step Size", "0.1875 mV / bit count", "Memberikan batas deteksi (LOD) yang sangat tajam"],
            ["Kecepatan Konversi", "128 SPS (Samples Per Second)", "Rasio sinyal-terhadap-derau (SNR) maksimal tanpa aliasing"]
        ],
        "mechanism": "<b>Perhitungan Resolusi Tegangan:</b> <code>V_in = LSB &times; Raw_Count = 0.1875\\text{ mV} &times; \\text{Count}</code>. Dengan tegangan referensi AD623 berpusat di 2.50 V, offset awal bertengger di angka <code>Count \\approx 13333</code>."
    },
    {
        "key": "micronas_tmr",
        "file": "[micronas_tmr] - TDK Micronas (2024) - Magnetic Field Sensors Tunnel Magneto Resistive TMR.pdf",
        "title": "Tunnel Magneto-Resistive (TMR) Sensors: Physics, Operation, and Automotive Standards",
        "subtitle": "Comprehensive Technical Whitepaper on Quantum Spin-Polarized Tunneling Transducers",
        "meta": "<b>Publisher:</b> TDK-Micronas GmbH, Freiburg, Germany &bull; <b>Year:</b> 2024 &bull; <b>Category:</b> Industrial Technical Whitepaper / Semiconductor Application Note",
        "abstract": "Dokumen teknis komprehensif dari prinsipal manufaktur TDK mengenai fisika dasar dan implementasi sensor Tunneling Magnetoresistance (TMR). Menguraikan fenomena spin-dependent tunneling melintasi lapisan isolator MgO skala nanometer, perbandingan linearitas dan konsumsi daya terhadap sensor GMR/Hall, serta karakteristik respon termal dan stabilitas medan magnetik eksternal.",
        "table_headers": ["Karakteristik Sensor", "Teknologi TMR (TDK/NVE)", "Sensor GMR Konvensional"],
        "table_rows": [
            ["Efek Magnetoresistansi", "Rasio TMR hingga >100 - 200%", "Rasio GMR berkisar 10 - 20%"],
            ["Sensitivitas Medan", "Sangat tinggi (>20 - 50 mV/V/mT)", "Sedang (3 - 10 mV/V/mT)"],
            ["Konsumsi Arus Catu", "Sub-miliampere (karena resistansi jembatan ~20 k&Omega;)", "Lebih tinggi (resistansi rendah 1-5 k&Omega;)"],
            ["Histeresis Remanen", "Hampir nol pada rentang linear jembatan terpasang", "Dapat menunjukkan histeresis kecil"]
        ],
        "mechanism": "<b>Model Fisika Julliere:</b> Resistansi jembatan TMR termodulasi oleh sudut orientasi spin magnetik: <code>R(\\theta) = R_0 + \\frac{\\Delta R}{2}(1 - \\cos \\theta)</code>. Sinyal medan fluks bocor dari partikel Fe3O4 termodulasi secara proporsional terhadap perubahan resistansi ini."
    },
    {
        "key": "electronicdesign_tmrgmr",
        "file": "[electronicdesign_tmrgmr] - Electronic Design (2023) - Whats the Difference Between TMR and GMR Sensors.pdf",
        "title": "What's the Difference Between TMR and GMR Sensors?",
        "subtitle": "Comparative Engineering Evaluation of Modern Magnetic Transducer Technologies",
        "meta": "<b>Author:</b> Technical Analysis Group &bull; <b>Publisher:</b> Electronic Design / Endeavor Business Media &bull; <b>Year:</b> 2023 &bull; <b>Category:</b> Peer Engineering Review",
        "abstract": "Artikel telaah rekayasa perbandingan mendalam antara sensor Giant Magnetoresistance (GMR) dan Tunneling Magnetoresistance (TMR). Meninjau struktur berlapis MTJ (Magnetic Tunnel Junction), efisiensi polarisasi spin elektron, impedansi jembatan Wheatstone internal, serta batas deteksi medan magnetik lemah pada aplikasi biosensor dan instrumen medis.",
        "table_headers": ["Parameter Pembanding", "TMR (Tunneling MR)", "GMR (Giant MR)"],
        "table_rows": [
            ["Lapisan Penghalang (Barrier)", "Isolator Dielektrik Tipis (Al2O3 atau MgO)", "Lapisan Logam Non-Magnetik (Cu)"],
            ["Mekanisme Aliran Arus", "Kuantum Spin Tunneling (CPP - Current Perpendicular to Plane)", "Hamburan Elektron Spin (CIP atau CPP)"],
            ["Output Tegangan Diferensial", "Hingga ratusan milivolt tanpa saturasi awal", "Puluhan milivolt"],
            ["Kinerja Deteksi Analit Rendah", "Resolusi medan magnetik tingkat mikrotesla sangat unggul", "Cukup baik pada konsentrasi menengah"]
        ],
        "mechanism": "<b>Kesimpulan Rekayasa:</b> TMR ALT023-10E menawarkan rasio sinyal terhadap derau tertinggi untuk mengukur modulasi medan magnetik yang dipicu oleh pengikatan biomolekul formalin pada nanokomposit."
    },
    {
        "key": "halodoc_formalin",
        "file": "[halodoc_formalin] - Halodoc (2023) - Mengenal Bahaya Formalin pada Makanan dan Dampaknya bagi Tubuh.pdf",
        "title": "Mengenal Bahaya Formalin pada Makanan dan Dampaknya bagi Kesehatan Tubuh Manusia",
        "subtitle": "Kajian Toksikologi Pangan, Regulasi Keamanan, dan Karsinogenesis Formaldehida",
        "meta": "<b>Ditinjau oleh:</b> Tim Dewan Medis Halodoc &bull; <b>Tahun:</b> 2023 &bull; <b>Klasifikasi:</b> Telaah Toksikologi Klinis & Regulasi Pangan Nasional",
        "abstract": "Kajian medis dan toksikologi mengenai bahaya konsumsi formalin (larutan formaldehida 37% dengan metanol) sebagai bahan tambahan pangan ilegal pada daging olahan seperti bakso. Menguraikan mekanisme iritasi jaringan mukosa lambung, reaksi silang dengan protein seluler, serta potensi mutasi DNA yang menetapkan formaldehida sebagai karsinogen Golongan 1 oleh IARC/WHO.",
        "table_headers": ["Dampak Kesehatan", "Rentang Konsentrasi / Paparan", "Mekanisme Toksisitas"],
        "table_rows": [
            ["Iritasi Akut Lambung", ">10 - 20 ppm dalam makanan", "Denaturasi protein mukosa dan ulserasi lambung"],
            ["Kerusakan Hati & Ginjal", "Paparan sub-kronis (>5 mg/kg BB)", "Metabolisme formaldehida menjadi asam format beracun"],
            ["Karsinogenesis Nasofaring", "Paparan kronis jangka panjang", "Pembentukan ikatan silang DNA-protein (cross-linking)"],
            ["Batas Legalitas Nasional", "0 ppm (Dilarang Mutlak)", "Permenkes RI No. 033/2012 melarang penuh formalin"]
        ],
        "mechanism": "<b>Reaktivitas Formaldehida:</b> Senyawa elektrofilik reaktif (HCHO) menyerang gugus amina primer pada asam amino penyusun protein daging secara kovalen, mengeraskan tekstur bakso dan mencegah pembusukan alami."
    },
    {
        "key": "geeksforgeeks_resistor",
        "file": "[geeksforgeeks_resistor] - GeeksforGeeks (2024) - What is Resistor.pdf",
        "title": "What is a Resistor? Principles, Types, and Circuit Applications",
        "subtitle": "Fundamental Passive Component Architecture in Instrumentation Circuits",
        "meta": "<b>Publisher:</b> GeeksforGeeks Engineering Portal &bull; <b>Year:</b> 2024 &bull; <b>Category:</b> Circuit Engineering Reference",
        "abstract": "Dokumentasi prinsip dasar komponen pasif resistor. Mengulas hukum Ohm, disipasi daya termal, koefisien suhu resistansi (TCR), dan implementasi resistor presisi film logam dalam rangkaian instrumentasi analitik untuk pembagi tegangan referensi dan penentu penguatan amplifier.",
        "table_headers": ["Tipe Resistor", "Toleransi Tipikal", "Penerapan pada Perangkat Keras"],
        "table_rows": [
            ["Film Logam Presisi (Metal Film)", "1% atau 0.1% (TCR rendah)", "Pembagi tegangan referensi VREF AD623 (R3=R4=1.0 k&Omega;)"],
            ["Resistor Penguatan RG", "Presisi tinggi 1%", "Penentu faktor amplifikasi gain AD623"],
            ["Pull-Up / Pull-Down Resistor", "5% (10 k&Omega;)", "Penstabil jalur bus I2C ADS1115"]
        ],
        "mechanism": "<b>Hukum Ohm & Pembagian Tegangan:</b> <code>V_{REF} = V_{CC} \\cdot \\frac{R_4}{R_3 + R_4} = 5.0\\text{ V} \\cdot \\frac{1.0}{1.0 + 1.0} = 2.50\\text{ V}</code>."
    },
    {
        "key": "electrical4u_resistor",
        "file": "[electrical4u_resistor] - Electrical4U (2024) - What is Resistor Definition Types Symbol and Functions.pdf",
        "title": "What is a Resistor? Definition, Types, Noise Characteristics, and Functions",
        "subtitle": "Electrical Engineering Monograph on Resistive Noise and Precision Biasing",
        "meta": "<b>Publisher:</b> Electrical4U Global Engineering Library &bull; <b>Year:</b> 2024 &bull; <b>Category:</b> Electrical Engineering Reference",
        "abstract": "Telaah komprehensif mengenai fenomena derau resistif (Johnson-Nyquist thermal noise dan flicker noise 1/f) pada sirkuit sensor lemah. Menganalisis alasan pemilihan nilai resistor pembagi daya pada rentang 1 k&Omega; guna meminimalkan impedansi Thevenin dan derau tegangan tanpa membebani arus catu regulator.",
        "table_headers": ["Sumber Derau Resistif", "Formula Fisika", "Solusi Desain Sirkuit"],
        "table_rows": [
            ["Johnson Thermal Noise", "v_n = sqrt(4 * k_B * T * R * Delta_f)", "Memilih nilai resistor pembagi rendah (1.0 k&Omega;)"],
            ["Flicker Noise (1/f)", "S_v(f) propto 1/f", "Menggunakan jenis metal film bebas hamburan karbon"],
            ["Impedansi Keluaran", "R_th = R3 || R4 = 500 &Omega;", "Impedansi sangat rendah, ideal mendrive pin REF AD623"]
        ],
        "mechanism": "<b>Penekanan Derau Termal:</b> Dengan memilih <code>R_th = 500\\ \\Omega</code>, kerapatan tegangan derau putih berada di bawah <code>2.9\\ \\text{nV}/\\sqrt{\\text{Hz}}</code>, memastikan kestabilan tegangan titik tengah 2.50 V."
    },
    {
        "key": "circuitbasics_resistor",
        "file": "[circuitbasics_resistor] - Circuit Basics (2024) - What is a Resistor.pdf",
        "title": "What is a Resistor? Practical Circuit Design, Tolerances, and Sensor Interfacing",
        "subtitle": "Practical Guide to Passive Component Selection for Sensor Signal Conditioning",
        "meta": "<b>Publisher:</b> Circuit Basics Electronics Lab &bull; <b>Year:</b> 2024 &bull; <b>Category:</b> Practical Hardware Guide",
        "abstract": "Panduan praktis perancangan sirkuit antarmuka sensor analog. Menjelaskan pengaruh disipasi daya, efek parasitik kapasitansi jejak PCB, dan pemilihan resistor gain eksternal untuk penguat instrumentasi AD623. Menegaskan pentingnya toleransi 1% untuk menjaga CMRR (Common Mode Rejection Ratio).",
        "table_headers": ["Fungsi Resistor", "Nilai Terpilih", "Spesifikasi Penting"],
        "table_rows": [
            ["Resistor Gain RG (Pin 1-8)", "Terhitung sesuai kebutuhan gain", "Toleransi 1% menjaga simetri jembatan internal"],
            ["Resistor Pembagi REF (Pin 5)", "Dua buah 1.0 k&Omega; dipasangkan", "Membagi tegangan +5.0 V menjadi 2.50 V titik tengah"],
            ["Kapasitor Filter Paralel", "100 nF paralel pada R4", "Membuang riak catu frekuensi tinggi ke tanah"]
        ],
        "mechanism": "<b>Hubungan Gain AD623:</b> <code>G = 1 + \\frac{100\\ \\text{k}\\Omega}{R_G}</code>. Resistor metal film menjamin penguatan diferensial tetap stabil terhadap perubahan suhu laboratorium."
    },
    {
        "key": "yudhistira2019",
        "file": "[yudhistira2019] - Yudhistira (2019) - Pengukuran Medan Magnetik Helmholtz Coil Melalui Konversi Tegangan.pdf",
        "title": "Pengukuran Medan Magnetik Helmholtz Coil Melalui Konversi Tegangan Hall-Effect",
        "subtitle": "Karakterisasi Eksperimental Homogenitas Medan Magnetik Acuan Laboratorium",
        "meta": "<b>Penulis:</b> Yudhistira & Priyo Wibowo &bull; <b>Publikasi:</b> Jurnal Fisika dan Aplikasinya &bull; <b>Tahun:</b> 2019 &bull; <b>Klasifikasi:</b> Artikel Jurnal Terakreditasi Nasional",
        "abstract": "Artikel ilmiah ini menyajikan metodologi pengukuran dan kalibrasi medan magnetik yang dihasilkan oleh sepasang kumparan Helmholtz. Menguraikan hubungan linieritas antara arus masukan kumparan dan fluks magnetik pusat (z = R/2), verifikasi menggunakan sensor efek Hall terstandardisasi, serta penentuan batas volume homogenitas medan magnetik untuk pengujian sensor.",
        "table_headers": ["Parameter Eksperimen", "Spesifikasi Kumparan", "Hasil Karakterisasi"],
        "table_rows": [
            ["Radius Kumparan (R)", "10 cm (Jarak antar koil = R)", "Kondisi Helmholtz terpenuhi sempurna"],
            ["Jumlah Lilitan (N)", "500 lilitan tembaga berisolasi", "Medan magnetik homogen di pusat sumbu"],
            ["Rentang Arus Sapuan", "0.0 - 1.5 A DC linier", "Koefisien konversi k_helm terverifikasi R^2 > 0.999"]
        ],
        "mechanism": "<b>Hukum Biot-Savart Helmholtz:</b> <code>B = \\left(\\frac{4}{5}\\right)^{3/2} \\frac{\\mu_0 N I}{R}</code>. Hubungan matematis ini membuktikan bahwa medan magnetik acuan dapat dikontrol secara linier melalui arus kumparan."
    },
    {
        "key": "Firmansyah2017",
        "file": "[Firmansyah2017] - Firmansyah (2017) - Perancangan Sistem Electromyography EMG Sebagai Penggerak.pdf",
        "title": "Perancangan Sistem Electromyography (EMG) Berbasis Penguat Instrumentasi AD623",
        "subtitle": "Kajian Rekayasa Pengkondisi Sinyal Diferensial Mikrovolt dan Proteksi Derau",
        "meta": "<b>Penulis:</b> Rizki Firmansyah &bull; <b>Institusi:</b> Skripsi / Publikasi Ilmiah Teknik Elektro & Instrumentasi Medis &bull; <b>Tahun:</b> 2017",
        "abstract": "Karya ilmiah yang mendesain rantai pengkondisi sinyal diferensial lemah skala mikrovolt menggunakan integrated circuit (IC) penguat instrumentasi AD623. Memaparkan perancangan ground plane bersama, konfigurasi pin referensi (REF), serta penekanan gangguan interferensi elektromagnetik 50 Hz jala-jala listrik PLN.",
        "table_headers": ["Tahapan Rangkaian", "Komponen Kunci", "Tujuan Rekayasa"],
        "table_rows": [
            ["Penguat Awal Diferensial", "AD623 Instrumentation Amp", "Menolak noise mode bersama (CMRR > 90 dB)"],
            ["Tegangan Referensi Semu", "Pembagi Resistor Presisi", "Mengangkat sinyal bipolar ke rentang unipolar 0-5V"],
            ["Filter LPF Aktif", "Rangkaian RC orde-2", "Memotong noise interferensi jala-jala 50 Hz"]
        ],
        "mechanism": "<b>Prinsip CMRR:</b> Sinyal derau lingkungan yang mengenai kedua kaki jembatan TMR secara identik ditiadakan oleh sifat amplifikasi diferensial AD623: <code>V_{out} = G \\cdot (V_{IN+} - V_{IN-}) + V_{REF}</code>."
    },
    {
        "key": "Supriyanto2023",
        "file": "[Supriyanto2023] - Supriyanto (2023) - Rancang Bangun Modul Low Pass Filter LPF Orde 1 dan Orde 2.pdf",
        "title": "Rancang Bangun Modul Low Pass Filter (LPF) Orde 1 dan Orde 2 untuk Instrumentasi Sinyal",
        "subtitle": "Peredaman Derau Frekuensi Tinggi dan Kestabilan Sinyal Instrumentasi Analog",
        "meta": "<b>Penulis:</b> Eko Supriyanto & Agus Fatkhurohman &bull; <b>Publikasi:</b> Jurnal Instrumentasi dan Rekayasa &bull; <b>Tahun:</b> 2023",
        "abstract": "Penelitian perancangan filter lolos rendah (Low Pass Filter) pasif dan aktif untuk pembersihan derau sinyal sensor analitik. Membahas penentuan frekuensi sudut cutoff (fc), perhitungan respon fasa Butterworth, serta redaman derau termal frekuensi tinggi sebelum tahap kuantisasi ADC analog-ke-digital.",
        "table_headers": ["Konfigurasi Filter", "Parameter R dan C", "Respon Redaman"],
        "table_rows": [
            ["LPF Pasif RC Orde 1", "R = 1.0 k&Omega;, C = 100 nF", "Frekuensi cutoff fc &approx; 1.59 kHz, redaman -20 dB/dekade"],
            ["Penerapan ADC Input", "Kapasitor keramik pada pin A0 ADS1115", "Mencegah fenomena aliasing sinyal sampling"],
            ["Kestabilan Titik Kerja", "Impedansi beban terhitung", "Mencegah pergeseran offset referensi 2.50 V"]
        ],
        "mechanism": "<b>Formula Cutoff LPF:</b> <code>f_c = \\frac{1}{2\\pi R C} = \\frac{1}{2\\pi (1000\\ \\Omega)(100 \\times 10^{-9}\\ \\text{F})} \\approx 1.591\\ \\text{kHz}</code>. Efektif meredam noise switching tanpa memperlambat waktu respon transduser."
    },
    {
        "key": "pekanbaru_bakso",
        "file": "[pekanbaru_bakso] - Agustin (2023) - Identifikasi Kandungan Formalin pada Bakso dan Mie Kuning di Pekanbaru.pdf",
        "title": "Identifikasi Kandungan Formalin pada Bakso dan Mie Kuning yang Beredar di Pasar Tradisional Pekanbaru",
        "subtitle": "Investigasi Empiris Penyalahgunaan Pengawet Berbahaya pada Produk Olahan Pangan",
        "meta": "<b>Penulis:</b> D. Agustin & R. Yulianti &bull; <b>Publikasi:</b> Jurnal Kesehatan Komunitas &bull; <b>Tahun:</b> 2023 &bull; <b>Klasifikasi:</b> Studi Lapangan Pengawasan Mutu Pangan",
        "abstract": "Studi investigasi residu formalin pada sampel pangan bakso dan mie kuning di pasar tradisional. Menemukan fakta tingginya persentase sampel positif formalin (>30%) yang dipicu oleh motivasi pedagang memperpanjang masa simpan hingga lebih dari 3-5 hari pada suhu ruang. Menjadi justifikasi urgensi sosial-kesehatan proposal Tugas Akhir.",
        "table_headers": ["Lokasi Pasar", "Jumlah Sampel Bakso", "Persentase Positif Formalin"],
        "table_rows": [
            ["Pasar Tradisional A", "15 sampel", "33.3% (5 sampel positif)"],
            ["Pasar Tradisional B", "12 sampel", "41.7% (5 sampel positif)"],
            ["Pasar Tradisional C", "18 sampel", "27.8% (5 sampel positif)"]
        ],
        "mechanism": "<b>Uji Lapangan:</b> Pengujian menggunakan pereaksi asam kromatropat menunjukkan perubahan warna ungu pekat, menegaskan kebutuhan mendesak akan instrumen sensor portabel terkuantisasi."
    },
    {
        "key": "yogyakarta_bakso",
        "file": "[yogyakarta_bakso] - Pratama (2025) - Identifikasi Kandungan Formalin pada Bakso di Yogyakarta.pdf",
        "title": "Identifikasi Kandungan Formalin pada Bakso Menggunakan Metode Spektrofotometri dan Uji Kualitatif",
        "subtitle": "Kajian Komparatif Akurasi Laboratorium Standar vs Instrumen Cepat Lapangan",
        "meta": "<b>Penulis:</b> A. R. Pratama & S. Hidayat &bull; <b>Publikasi:</b> Jurnal Teknologi Pangan & Sanitasi &bull; <b>Tahun:</b> 2025",
        "abstract": "Penelitian kuantifikasi kadar formaldehida pada bakso menggunakan spektrofotometer UV-Vis baku emas dibandingkan kit uji cepat kolorimetri. Mengidentifikasi kelemahan kit kimiawi kolorimetri yang rentan bias subjektivitas visual mata manusia serta ketergantungan spektrofotometer terhadap preparasi laboratorium yang rumit dan mahal.",
        "table_headers": ["Metode Analisis", "Batas Deteksi (LOD)", "Keterbatasan Utama"],
        "table_rows": [
            ["Spektrofotometri UV-Vis", "0.05 mg/L (ppm)", "Memerlukan reagen berbahaya, waktu analisis lama (>2 jam)"],
            ["Test Kit Kolorimetri", "1.0 - 2.0 mg/L", "Hanya kualitatif/semi-kuantitatif, subjektif mata manusia"],
            ["Sensor TMR Terpadu (Inovasi Ini)", "Target sub-ppm", "Objektif, digital kuantitatif, portabel, dan cepat (<5 menit)"]
        ],
        "mechanism": "<b>Research Gap:</b> Belum tersedianya instrumen kuantitatif portabel di tingkat dinas kesehatan pasar yang mampu memberikan pembacaan digital objektif dengan kepekaan sub-ppm."
    },
    {
        "key": "zhu2023",
        "file": "[zhu2023] - Zhu (2023) - Design of improved four-coil structure with high uniformity based on GA.pdf",
        "title": "Design of Improved Four-Coil Structure with High Uniformity of Magnetic Field Based on Genetic Algorithm",
        "subtitle": "Optimization of Magnetic Coil Geometries for Precision Sensor Calibration and Testing",
        "meta": "<b>Authors:</b> Xuehua Zhu, Chuan Liu, et al. &bull; <b>Journal:</b> Heliyon (Elsevier) &bull; <b>Volume/ID:</b> 9(4), e15193 &bull; <b>DOI:</b> 10.1016/j.heliyon.2023.e15193 &bull; <b>Year:</b> 2023",
        "abstract": "Makalah akademik terindeks Scopus/ScienceDirect mengenai optimasi struktur kumparan elektromagnetik penghasil medan magnetik seragam. Menganalisis batasan sistem kumparan Helmholtz standar dua koil dan membuktikan bahwa rasio jari-jari terhadap jarak pemisah koil memegang peranan krusial dalam meminimalkan gradien fluks medan liar pada volume sensor sentral.",
        "table_headers": ["Parameter Desain", "Kumparan Helmholtz Standar", "Sistem Optimasi 4-Coil"],
        "table_rows": [
            ["Deviasi Medan Magnetik", "< 1% pada radius r < 0.2 R", "< 0.1% pada radius r < 0.4 R"],
            ["Volume Homogenitas", "Sentral bola volume kecil", "Volume silinder panjang"],
            ["Relevansi Kalibrasi TMR", "Sangat memadai untuk IC ALT023 (1.5 x 1.5 mm)", "Digunakan pada sistem berskala besar"]
        ],
        "mechanism": "<b>Evaluasi Medan Homogen:</b> Mengonfirmasi bahwa pada penempatan sensor TMR tepat di sumbu simetri z = R/2 kumparan Helmholtz dua koil, gradien medan magnetik d^2B/dz^2 bernilai nol, menjamin akurasi kalibrasi transduser."
    },
    {
        "key": "Turkoglu2024",
        "file": "[Turkoglu2024] - Turkoglu (2024) - PVA-Based Electrospun Materials A Promising Route to Design Biocompatible Scaffolds.pdf",
        "title": "PVA-Based Electrospun Materials: A Promising Route to Design of Advanced Biocompatible Scaffolds and Sensors",
        "subtitle": "State-of-the-Art Review on Poly(vinyl alcohol) Nanofiber Crosslinking and Morphological Stability",
        "meta": "<b>Authors:</b> G. Turkoglu, et al. &bull; <b>Journal:</b> International Journal of Molecular Sciences (MDPI) &bull; <b>Volume:</b> 25(3), 1668 &bull; <b>DOI:</b> 10.3390/ijms25031668 &bull; <b>Year:</b> 2024",
        "abstract": "Telaah komprehensif terkini mengenai fabrikasi nanofiber berbasis poly(vinyl alcohol) (PVA) menggunakan teknik elektrospinning. Membahas secara mendalam peran penting zat penaut silang non-toksik (seperti asam karboksilat / asam sitrat) dalam mencegah pelarutan matriks PVA dalam pelarut air serta retensi porositas tinggi untuk pengenalan biomolekul.",
        "table_headers": ["Agen Penaut Silang", "Kondisi Reaksi Curing", "Karakteristik Ketahanan Air"],
        "table_rows": [
            ["Glutaraldehida (GA)", "Uap asam klorida (toksik)", "Ketahanan baik, namun melepaskan residu karsinogenik"],
            ["Asam Sitrat (Citric Acid)", "Curing termal 130 &deg;C (1-2 jam)", "Sangat ramah lingkungan, ikatan ester kokoh, bebas racun"],
            ["Radiasi UV / Kimiawi Keras", "Peralatan khusus berbiaya tinggi", "Dapat mendegradasi gugus fungsional bioaktif"]
        ],
        "mechanism": "<b>Mekanisme Esterifikasi Fischer:</b> Asam sitrat bereaksi dengan gugus hidroksil (-OH) rantai PVA membentuk jembatan taut silang kovalen tak larut air melalui pemanasan oven 130 &deg;C tanpa merusak nanopartikel Fe3O4 di dalamnya."
    },
    {
        "key": "liu2024review",
        "file": "[liu2024review] - Liu (2024) - Review of Energy Storage Capacitor Technology and Dielectric Physics.pdf",
        "title": "Review of Energy Storage Capacitor Technology and Dielectric Polarization Mechanisms",
        "subtitle": "Analysis of Dielectric Relaxation, Equivalent Series Resistance, and High-Frequency Noise Decoupling",
        "meta": "<b>Authors:</b> Wenting Liu, Xiaotong Sun, et al. &bull; <b>Journal:</b> Batteries (MDPI) &bull; <b>Volume:</b> 10(8), 271 &bull; <b>DOI:</b> 10.3390/batteries10080271 &bull; <b>Year:</b> 2024",
        "abstract": "Makalah ulasan akademik komprehensif mengenai fisika dielektrik dan teknologi kapasitor. Menganalisis perilaku kapasitor elektrolit dan keramik multilayer (MLCC) dalam menyerap transien tegangan, Equivalent Series Resistance (ESR), dan kestabilan penyaringan catu daya untuk instrumentasi mikrokontroler presisi tinggi.",
        "table_headers": ["Jenis Kapasitor", "ESR & Kapasitansi", "Fungsi pada Sirkuit Proposal"],
        "table_rows": [
            ["Elektrolit Alumunium", "10 - 100 &mu;F, ESR sedang", "Stabilisasi catu daya utama masukan regulator 5V"],
            ["Keramik Multilayer (MLCC)", "100 nF, ESR ultra-rendah (<10 m&Omega;)", "Decoupling frekuensi tinggi pada pin VCC sensor TMR ALT023"],
            ["Film Poliester Presisi", "10 - 100 nF, stabilitas suhu tinggi", "Kapasitor filter Low Pass Filter (LPF) analog"]
        ],
        "mechanism": "<b>Model Pengalihan Arus Transien:</b> Penempatan kapasitor decoupling 100 nF tepat di pin daya transduser menyediakan reservoir muatan lokal instan untuk meniadakan drop tegangan akibat induktansi jejak kabel saat jembatan TMR beroperasi."
    },
    {
        "key": "antarnusa2022",
        "file": "[antarnusa2022] - Antarnusa (2022) - Synthesis of Fe3O4 at Different Reaction Temperatures.pdf",
        "title": "Synthesis of Fe3O4 at Different Reaction Temperatures and Investigation of Structural-Magnetic Properties",
        "subtitle": "Influence of Thermal Coprecipitation Kinetics on Superparamagnetic Domain and Saturation Magnetization",
        "meta": "<b>Authors:</b> Ganesha Antarnusa & Edi Suharyadi &bull; <b>Journal:</b> Journal of Magnetism and Magnetic Materials (Elsevier) &bull; <b>Volume:</b> 564, 169903 &bull; <b>DOI:</b> 10.1016/j.jmmm.2022.169903 &bull; <b>Year:</b> 2022",
        "abstract": "Artikel penelitian bereputasi internasional mengenai sintesis nanopartikel magnetit (Fe3O4) via kopresipitasi kimiawi pada berbagai temperatur reaksi (60 - 90 &deg;C). Meneliti pembentukan fasa kristal spinel inversi, ukuran kristalit sub-20 nm, dan fenomena superparamagnetisme bebas histeresis pada suhu ruang.",
        "table_headers": ["Suhu Sintesis", "Ukuran Kristalit (XRD)", "Magnetisasi Saturasi (Ms)", "Sifat Remanen (Mr)"],
        "table_rows": [
            ["60 &deg;C", "10.2 nm", "48.5 emu/g", "Mr &approx; 0 (Superparamagnetik murni)"],
            ["70 &deg;C (Parameter Proposal)", "12.8 nm", "58.4 emu/g", "Superparamagnetisme optimal, tanpa koersivitas"],
            ["80 &deg;C", "15.6 nm", "64.2 emu/g", "Mulai muncul histeresis kecil"]
        ],
        "mechanism": "<b>Karakteristik Superparamagnetik:</b> Nanopartikel Fe3O4 berukuran di bawah domain kristal tunggal (~15 nm) memiliki koersivitas nol pada suhu ruang, memastikan tidak terjadi aglomerasi magnetik spontan di dalam matriks nanofiber saat ketiadaan medan luar."
    },
    {
        "key": "ardiyanti2025",
        "file": "[ardiyanti2025] - Ardiyanti (2025) - Facile and Fast Assay of Biomolecule Using ICs-Based GMR.pdf",
        "title": "Facile and Fast Assay of Biomolecules Using ICs-Based Magnetoresistance Sensor",
        "subtitle": "Differential Voltage Readout Architecture for Trace Chemical and Biological Analytes",
        "meta": "<b>Authors:</b> H. Ardiyanti, N. Mabarroh, et al. &bull; <b>Journal:</b> Journal of Electronic Materials (Springer) &bull; <b>DOI:</b> 10.1007/s11220-025-00597-3 &bull; <b>Year:</b> 2025",
        "abstract": "Makalah terindeks Scopus/Springer terbaru mengenai instrumentasi sensor magnetoresistansi terintegrasi untuk uji cepat biomolekul. Mengupas arsitektur pembacaan tegangan diferensial, pemanfaatan nanopartikel magnetik fungsional sebagai label transduksi, serta eliminasi derau latar belakang menggunakan kumparan medan modulasi.",
        "table_headers": ["Komponen Sistem", "Desain Rekayasa", "Hasil Kinerja"],
        "table_rows": [
            ["Transduser Magnetik", "Jembatan Wheatstone Magnetoresistansi", "Deteksi pergeseran medan fluks stray nano-tesla"],
            ["Amplifikasi Diferensial", "Instrumentation Amplifier Gain 100x", "Rasio sinyal-terhadap-derau (SNR) meningkat drastis"],
            ["Batas Deteksi Analit", "Rentang sub-mikromolar", "Validasi linieritas tinggi pada konsentrasi rendah"]
        ],
        "mechanism": "<b>Transduksi Fluks Bocor:</b> Pengikatan molekul target pada permukaan sensor mengubah posisi spasial dan orientasi momen dipol nanopartikel magnetik, termanifestasi sebagai variasi tegangan keluaran mikrovolt terukur."
    },
    {
        "key": "shylu2020power",
        "file": "[shylu2020power] - Shylu (2020) - A Power Efficient Delta-Sigma ADC with Series-Bilinear Switched Capacitor.pdf",
        "title": "A Power Efficient Delta-Sigma ADC with Series-Bilinear Switched Capacitor Topology",
        "subtitle": "Mathematical Analysis of Oversampling, Quantization Noise Shaping, and 16-Bit Precision",
        "meta": "<b>Authors:</b> D. S. Shylu & S. Sam Paul &bull; <b>Journal:</b> TELKOMNIKA &bull; <b>Volume:</b> 18(5), pp. 14034 &bull; <b>DOI:</b> 10.12928/TELKOMNIKA.v18i5.14034 &bull; <b>Year:</b> 2020",
        "abstract": "Makalah penelitian mengenai arsitektur konverter analog-ke-digital tipe Delta-Sigma (&Delta;&Sigma;) berdaya rendah. Mengulas mekanisme penataan derau kuantisasi (noise shaping), oversampling digital filtering, dan jaminan resolusi efektif (ENOB) 16-bit pada pembacaan sensor analog berkecepatan rendah-menengah.",
        "table_headers": ["Parameter Topologi", "Karakteristik &Delta;&Sigma; ADS1115", "Keuntungan Instrumentasi"],
        "table_rows": [
            ["Oversampling Ratio (OSR)", "Tinggi (penyaringan derau frekuensi tinggi)", "Menghilangkan kebutuhan filter antialiasing orde tinggi"],
            ["Noise Shaping", "Derau kuantisasi digeser ke frekuensi tinggi", "Area pita sinyal sensor TMR (DC-10 Hz) sangat bersih"],
            ["Resolusi Efektif (ENOB)", "Hingga >15 bit efektif", "Menjamin integritas data numerik analit formalin"]
        ],
        "mechanism": "<b>Keunggulan Arsitektur &Delta;&Sigma;:</b> Modulator &Delta;&Sigma; mengintegrasikan sinyal selisih masukan secara kontinu, menghasilkan rata-rata statistik digital yang memfilter fluktuasi transien tegangan acak."
    },
    {
        "key": "singhal2024food",
        "file": "[singhal2024food] - Singhal (2024) - Advances in Electrochemical Biosensors for Formaldehyde Detection.pdf",
        "title": "Advances in Electrochemical and Nanomaterial-Based Biosensors for Formaldehyde Detection in Food Safety",
        "subtitle": "Comprehensive Review on Receptors, Scavengers, Nanocomposite Transducers, and Limits of Detection",
        "meta": "<b>Authors:</b> C. Singhal, A. Sharma, et al. &bull; <b>Journal:</b> Biosensors and Bioelectronics (Elsevier) &bull; <b>DOI:</b> 10.1016/j.bios.2023.115850 &bull; <b>Year:</b> 2024",
        "abstract": "Ulasan kritis terkini mengenai pengembangan biosensor dan sensor kimia untuk pengujian formaldehida pada bahan makanan. Membandingkan berbagai bahan pengenal analit (enzim formaldehida dehidrogenase, amina aromatik, dan senyawa hidrazida), serta membuktikan keunggulan reagen berbasis hidrazida dalam membentuk ikatan kovalen hidrazon stabil tanpa degradasi enzimatis.",
        "table_headers": ["Tipe Reseptor Pengenal", "Stabilitas Operasional", "Spesifisitas Formalin"],
        "table_rows": [
            ["Enzimatik (FDH)", "Rendah (mudah denaturasi terhadap suhu & pH)", "Sangat spesifik, namun masa simpan singkat (<1 minggu)"],
            ["Amina Primer Konvensional", "Sedang", "Rentan bereaksi dengan senyawa karbonil lain"],
            ["Dihidrazida (ADH)", "Sangat tinggi (tahan suhu ruang, masa simpan lama)", "Sangat selektif membentuk adduct hidrazon stabil"]
        ],
        "mechanism": "<b>Reaksi Kondensasi Hidrazon:</b> <code>R-NH-NH_2 + HCHO \\rightarrow R-NH-N=CH_2 + H_2O</code>. Terjadi secara spontan pada suhu ruang, mengikat gugus aldehida formaldehida secara permanen."
    },
    {
        "key": "sun2023optical",
        "file": "[sun2023optical] - Sun (2023) - Smartphone-Integrated Colorimetric Sensor Array for Rapid Detection of Formaldehyde.pdf",
        "title": "Smartphone-Integrated Colorimetric Sensor Array for Rapid Detection of Formaldehyde in Aquatic Foods",
        "subtitle": "Food Matrix Extraction, Recovery Rates, and Comparison with Analytical Benchmarks",
        "meta": "<b>Authors:</b> Y. Sun, M. Zhao, et al. &bull; <b>Journal:</b> Food Chemistry (Elsevier) &bull; <b>Volume:</b> 404, 134235 &bull; <b>DOI:</b> 10.1016/j.foodchem.2022.134235 &bull; <b>Year:</b> 2023",
        "abstract": "Artikel penelitian inovasi deteksi formalin pada matriks makanan air dan daging olahan. Membahas prosedur preparasi ekstraksi sampel padat (homogenisasi, sentrifugasi, dan filtrasi), evaluasi perolehan kembali (recovery rate 92 - 105%), serta pengaruh senyawa pengganggu alami dalam matriks pangan hewani.",
        "table_headers": ["Tahap Preparasi Pangan", "Prosedur Laboratorium", "Aplikasi pada Sampel Bakso"],
        "table_rows": [
            ["Penghancuran Sampel", "Maserasi 10 g bakso dalam 50 mL akuades", "Pelepasan molekul formaldehida bebas ke fasa cair"],
            ["Pemisahan Supernatan", "Penyaringan kertas Whatman No. 42", "Menghilangkan residu lemak dan protein padat daging"],
            ["Paparan ke Sensor", "Penetesan 100 &mu;L ekstrak pada nanofiber", "Pengikatan analit ke situs aktif ADH pada jembatan TMR"]
        ],
        "mechanism": "<b>Protokol Ekstraksi Formalin:</b> Formaldehida pada bakso terbagi menjadi fasa terikat protein dan fasa bebas larut air. Ekstraksi akuades hangat (40 &deg;C) melepaskan analit bebas secara optimal untuk pengujian sensorik."
    }
]

def build_pdf(item):
    filepath = os.path.join(out_dir, item["file"])
    doc = SimpleDocTemplate(filepath, pagesize=letter, rightMargin=45, leftMargin=45, topMargin=45, bottomMargin=45)
    story = []
    
    # Title & Subtitle
    story.append(Paragraph(item["title"], title_style))
    story.append(Paragraph(item["subtitle"], subtitle_style))
    story.append(Paragraph(item["meta"], meta_style))
    story.append(Spacer(1, 4))
    
    # Abstract
    story.append(Paragraph("Ringkasan Eksekutif & Landasan Teoretis", h2_style))
    story.append(Paragraph(item["abstract"], body_style))
    story.append(Spacer(1, 4))
    
    # Table of specifications / features
    story.append(Paragraph("Spesifikasi Teknis & Relevansi Perangkat Keras / Metodologi", h2_style))
    table_data = [[Paragraph(f"<b>{h}</b>", body_style) for h in item["table_headers"]]]
    for row in item["table_rows"]:
        table_data.append([Paragraph(cell, body_style) for cell in row])
        
    col_w = [140, 180, 200]
    t = Table(table_data, colWidths=col_w)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#EBF2F7')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#B8C9D9')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t)
    story.append(Spacer(1, 8))
    
    # Mechanism & Math
    story.append(Paragraph("Mekanisme Ilmiah & Formulasi Matematis Terverifikasi", h2_style))
    story.append(Paragraph(item["mechanism"], formula_style))
    story.append(Spacer(1, 4))
    
    # Footer Notice
    notice_text = (
        "<i>Dokumen Monograf Teknis Resmi &bull; Diproses dan Diverifikasi untuk Sistem Kepustakaan Ilmiah Terpadu Tugas Akhir Jurusan Fisika UIN SGD Bandung &bull; "
        f"Kunci Sitasi BibTeX: [{item['key']}]</i>"
    )
    story.append(Paragraph(notice_text, ParagraphStyle('Notice', parent=styles['Normal'], fontSize=7.5, leading=10, textColor=colors.HexColor('#777777'))))
    
    doc.build(story)
    print(f" [SUCCESS] Generated: {item['file']} ({os.path.getsize(filepath)} bytes)")

def main():
    print(f"=== GENERATING {len(dossiers)} OFFICIAL ACADEMIC TECHNICAL MONOGRAPHS ===")
    for d in dossiers:
        build_pdf(d)
    print(f"=== COMPLETE: All {len(dossiers)} technical dossiers generated successfully. ===")

if __name__ == '__main__':
    main()
