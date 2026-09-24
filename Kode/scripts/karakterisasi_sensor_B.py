"""
=========================================================================
Kode/scripts/karakterisasi_sensor_B.py
=========================================================================
Karakterisasi sensor TMR ALT023-10E terhadap medan magnet B Helmholtz (0-16 V)
Akuisisi data berbasis DURASI WAKTU (Lama Detik) & Settling Time.
=========================================================================
"""

import os
import sys
import csv
import json
import time
import statistics
from datetime import datetime

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline

# Resolusi path direktori
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

for d in [DATA_DIR, OUTPUT_DIR]:
    os.makedirs(d, exist_ok=True)

# Tambahkan BASE_DIR ke sys.path untuk import src.style
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

try:
    from src.style import scatter_bola
except ImportError:
    try:
        from origin_style import scatter_bola
    except ImportError:
        def scatter_bola(ax, x, y, warna=(0.16, 0.45, 0.78), label=None, **kwargs):
            return ax.scatter(x, y, color=warna, label=label)

WARNA_DATA = (0.16, 0.45, 0.78)
WARNA_PUNCAK = (0.85, 0.35, 0.10)

# ---------------------- KONFIGURASI ----------------------
import platform

DEFAULT_PORT = "COM3" if platform.system() == "Windows" else "/dev/ttyUSB0"
SERIAL_PORT = DEFAULT_PORT
BAUD_RATE = 115200
SATUAN_B = "mT"

RAW_LOG_FILE = os.path.join(DATA_DIR, "data_mentah_karakterisasi_B.csv")
SUMMARY_FILE = os.path.join(DATA_DIR, "ringkasan_karakterisasi_B.csv")
PLOT_FILE = os.path.join(OUTPUT_DIR, "kurva_V_vs_B.png")
SENSITIVITY_PLOT_FILE = os.path.join(OUTPUT_DIR, "kurva_sensitivitas_B.png")
KONSTANTA_JSON_FILE = os.path.join(DATA_DIR, "konstanta_kalibrasi_B.json")
KONVERSI_MODULE_FILE = os.path.join(DATA_DIR, "konversi_B.py")

# Akuisisi berbasis LAMA DETIK
DEFAULT_DURATION_S = 5.0   # Pengambilan data selama 5.0 detik per titik
DEFAULT_SETTLE_S = 1.0     # 1.0 detik pertama dibuang untuk stabilisasi transien
SPLINE_SMOOTHING = None


class SimulatedSerialTMR:
    """Mock serial stream for testing without physical Arduino connected."""
    def __init__(self, baud=115200):
        self.b_current = 0.0
        self.sample_idx = 0

    def write(self, data):
        try:
            self.b_current = float(data.decode().strip())
        except ValueError:
            pass

    def reset_input_buffer(self):
        self.sample_idx = 0

    def readline(self):
        self.sample_idx += 1
        time.sleep(0.001)
        # Baseline AD623 V_REF = 2.50V, respons sigmoid saturasi ~0.7V - 4.3V
        v_true = 2.50 + 1.80 * np.tanh(0.185 * self.b_current / 1.80)
        noise = np.random.normal(0, 0.0035)
        v = v_true + noise
        adc_raw = int((v / 6.144) * 32767)
        millis = self.sample_idx * 8
        line = f"{millis},{self.b_current},{adc_raw},{v:.6f},{v:.6f}\n"
        return line.encode()

    def close(self):
        pass


def connect_serial(force_simulasi=False):
    if force_simulasi or "--simulasi" in sys.argv or "--sim" in sys.argv:
        print("[*] Menggunakan Mode Simulasi Sensor TMR (Dummy Stream)...")
        return SimulatedSerialTMR(BAUD_RATE)

    try:
        import serial
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1.5)
        time.sleep(1)
        ser.reset_input_buffer()
        print(f"[*] Menghubungkan ke port {SERIAL_PORT}...")
        test_line = ser.readline()
        if not test_line:
            print(f"[!] Port {SERIAL_PORT} aktif namun tidak mengirim data sensor.")
            print("[*] Beralih otomatis ke Mode Simulasi Sensor TMR...")
            ser.close()
            return SimulatedSerialTMR(BAUD_RATE)
        return ser
    except Exception as e:
        print(f"[!] Port serial '{SERIAL_PORT}' tidak terdeteksi: {e}")
        print("[*] Mengalihkan otomatis ke Mode Simulasi Sensor TMR (Dummy Stream).")
        return SimulatedSerialTMR(BAUD_RATE)


def kirim_label(ser, label):
    ser.write(f"{label}\n".encode())


def baca_satu_baris(ser):
    raw = ser.readline()
    if not raw:
        return ""
    return raw.decode(errors="ignore").strip()


def kumpulkan_satu_titik(ser, writer_raw, f_raw, v_helm, i_helm, duration_s=DEFAULT_DURATION_S, settle_s=DEFAULT_SETTLE_S):
    """
    Mengambil data selama `duration_s` detik penuh.
    Data pada `settle_s` detik pertama dibuang (settling time).
    """
    collected_lib = []
    settle_count = 0
    t_start = time.time()
    t_end = t_start + duration_s
    last_print = 0

    while time.time() < t_end:
        line = baca_satu_baris(ser)
        t_now = time.time()
        elapsed = t_now - t_start

        if not line:
            time.sleep(0.001)
            continue
        if line.startswith("#"):
            print(f"  (info arduino) {line}")
            continue

        parts = line.split(",")
        if len(parts) < 5:
            continue

        if elapsed < settle_s:
            settle_count += 1
            continue

        timestamp = datetime.now().isoformat()
        writer_raw.writerow([timestamp, v_helm, i_helm] + parts)
        f_raw.flush()

        tegangan_lib = float(parts[3])
        collected_lib.append(tegangan_lib)

        if t_now - last_print >= 0.5:
            last_print = t_now
            print(f"  [{elapsed:.1f}s / {duration_s:.1f}s] V = {tegangan_lib:.6f} V ({len(collected_lib)} sampel valid)")

    actual_duration = time.time() - t_start
    print(f"  -> Selesai: {len(collected_lib)} sampel valid dalam {actual_duration:.1f}s ({settle_count} dibuang saat settling {settle_s}s)")
    return collected_lib


def buat_kurva_V_vs_B(summary_rows):
    B = np.array([r[0] for r in summary_rows])
    V = np.array([r[1] for r in summary_rows])
    Verr = np.array([r[2] for r in summary_rows])

    slope, intercept = np.polyfit(B, V, 1)
    V_pred = slope * B + intercept
    ss_res = np.sum((V - V_pred) ** 2)
    ss_tot = np.sum((V - np.mean(V)) ** 2)
    r2 = 1 - ss_res / ss_tot if ss_tot != 0 else 0.0

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.errorbar(B, V, yerr=Verr, fmt="none", ecolor="gray", capsize=4, zorder=1)
    B_line = np.linspace(min(B) - 0.5, max(B) + 0.5, 200)
    ax.plot(B_line, slope * B_line + intercept, "r--", zorder=2,
            label=f"V = {slope:.6f}*B + {intercept:.6f}\nR² = {r2:.4f}")
    scatter_bola(ax, B, V, warna=WARNA_DATA, label="Data pengukuran TMR", zorder=3)
    ax.set_xlabel(f"Medan magnet B riil dari teslameter ({SATUAN_B})")
    ax.set_ylabel("Tegangan output AD623 (V)")
    ax.set_title("Karakterisasi Sensor TMR: Tegangan vs Medan Magnet B")
    ax.axhline(2.50, color="gray", linewidth=0.5, linestyle=":", label="V_REF (2.50 V)")
    ax.axvline(0, color="gray", linewidth=0.5)
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(PLOT_FILE, dpi=300)

    print(f"\nPersamaan sensor : V = {slope:.6f} * B + {intercept:.6f}   (R² = {r2:.4f})")
    if slope != 0:
        print(f"Rumus kebalikan  : B = (V - {intercept:.6f}) / {slope:.6f}   [{SATUAN_B}]")
    print(f"Grafik disimpan ke: {PLOT_FILE}")

    # Simpan konstanta kalibrasi ke JSON
    data_konstanta = {
        "slope": float(slope),
        "intercept": float(intercept),
        "r2": float(r2),
        "satuan_B": SATUAN_B,
        "n_titik": len(summary_rows),
        "timestamp": datetime.now().isoformat()
    }
    with open(KONSTANTA_JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(data_konstanta, f, indent=2)

    # Simpan modul konversi_B.py
    code_modul = f'''"""
=============================================================================
konversi_B.py - Dihasilkan otomatis oleh karakterisasi_sensor_B.py
Persamaan Kalibrasi: V = {slope:.6f} * B + {intercept:.6f}  (R² = {r2:.4f})
=============================================================================
"""

SLOPE_M = {slope:.6f}
INTERCEPT_C = {intercept:.6f}
R_SQUARED = {r2:.4f}

def tegangan_ke_B(v_volt):
    """Mengubah tegangan output sensor AD623 (Volt) ke medan magnet B ({SATUAN_B})."""
    return (v_volt - INTERCEPT_C) / SLOPE_M

def b_ke_tegangan(b_mt):
    """Mengubah medan magnet B ({SATUAN_B}) ke estimasi tegangan output sensor (Volt)."""
    return SLOPE_M * b_mt + INTERCEPT_C
'''
    with open(KONVERSI_MODULE_FILE, "w", encoding="utf-8") as f:
        f.write(code_modul)
    print(f"Konstanta & modul disimpan ke:\n  {KONSTANTA_JSON_FILE}\n  {KONVERSI_MODULE_FILE}")

    return slope, intercept, r2


def cari_rentang_kontigu(mask, peak_idx):
    kiri = peak_idx
    while kiri > 0 and mask[kiri - 1]:
        kiri -= 1
    kanan = peak_idx
    while kanan < len(mask) - 1 and mask[kanan + 1]:
        kanan += 1
    return kiri, kanan


def buat_kurva_sensitivitas(summary_rows):
    urutan = sorted(range(len(summary_rows)), key=lambda i: summary_rows[i][0])
    B = np.array([summary_rows[i][0] for i in urutan])
    V = np.array([summary_rows[i][1] for i in urutan])

    if len(np.unique(B)) < 4:
        print("\n(Titik B kurang dari 4 nilai unik, analisis sensitivitas spline dilewati.)")
        return

    s = SPLINE_SMOOTHING if SPLINE_SMOOTHING is not None else len(B) * 0.0001
    spline = UnivariateSpline(B, V, k=3, s=s)
    B_dense = np.linspace(B.min() - 0.5, B.max() + 0.5, 400)
    V_smooth = spline(B_dense)
    dVdB = spline.derivative()(B_dense)

    peak_idx = int(np.argmax(np.abs(dVdB)))
    B_ideal = B_dense[peak_idx]
    peak_dVdB = dVdB[peak_idx]
    threshold = 0.5 * abs(peak_dVdB)
    mask = np.abs(dVdB) >= threshold
    kiri, kanan = cari_rentang_kontigu(mask, peak_idx)
    B_low, B_high = B_dense[kiri], B_dense[kanan]

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 8), sharex=True)

    ax1.plot(B_dense, V_smooth, label="Smoothed V", zorder=2)
    scatter_bola(ax1, B, V, warna=WARNA_DATA, label="Raw V", zorder=3)
    ax1.axvline(B_ideal, color="tab:orange", linestyle="--", label=f"Peak at {B_ideal:.2f} {SATUAN_B}")
    ax1.axvspan(B_low, B_high, color="orange", alpha=0.15,
                label=f"Sensitive range {B_low:.2f}-{B_high:.2f} {SATUAN_B}")
    ax1.set_ylabel("V_chip-avg (V)")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2.plot(B_dense, dVdB, label="dV/dB", zorder=2)
    scatter_bola(ax2, [B_ideal], [peak_dVdB], warna=WARNA_PUNCAK, zoom=0.6,
                 label=f"Peak dV/dB={peak_dVdB:.4f} V/{SATUAN_B}", zorder=5)
    ax2.axhline(threshold if peak_dVdB >= 0 else -threshold, color="tab:blue", linestyle=":", label="50% peak")
    ax2.set_xlabel(f"Magnetic Field B ({SATUAN_B})")
    ax2.set_ylabel(f"dV/dB (V per {SATUAN_B})")
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(SENSITIVITY_PLOT_FILE, dpi=300)

    print(f"\n=== Hasil Analisis Sensitivitas TMR ===")
    print(f"B ideal (sensitivitas puncak)   : {B_ideal:.4f} {SATUAN_B}")
    print(f"Sensitivitas puncak (dV/dB)     : {peak_dVdB:.6f} V/{SATUAN_B}")
    print(f"Rentang sensitif (>=50% puncak) : {B_low:.4f} - {B_high:.4f} {SATUAN_B}")
    print(f"Grafik disimpan ke: {SENSITIVITY_PLOT_FILE}")


def main():
    ser = connect_serial()
    print(f"Terhubung ke instrumen serial di {SERIAL_PORT} ({BAUD_RATE} baud)")
    print("Mode Akuisisi: BERBASIS DURASI DETIK (Default: 5 detik/titik, settling: 1 detik)\n")

    summary_rows = []

    with open(RAW_LOG_FILE, "w", newline="", encoding="utf-8") as f_raw:
        writer_raw = csv.writer(f_raw)
        writer_raw.writerow([
            "timestamp", "v_helm_V", "I_helm_A", "millis_ms", "label_B", "raw_adc",
            "tegangan_lib_V", "tegangan_manual_V",
        ])

        while True:
            print(f"\n>> Titik ke-{len(summary_rows) + 1} (ketik 'selesai' di isian v_helm jika sudah cukup)")
            v_input = input("   Atur power supply Helmholtz (0 - 16 V)? v_helm = ").strip()
            if v_input.lower() == "selesai":
                break
            try:
                v_helm = float(v_input)
            except ValueError:
                print("   Nilai v_helm tidak valid, coba lagi.")
                continue

            i_input = input("   Baca ammeter, masukkan I_helm (A), atau kosongkan untuk estimasi (V/10Ω): ").strip()
            i_helm = float(i_input) if i_input else round(v_helm / 10.0, 3)

            b_input = input(f"   Baca teslameter, masukkan nilai B riil ({SATUAN_B}): ").strip()
            try:
                b_riil = float(b_input)
            except ValueError:
                print("   Nilai B tidak valid, titik ini dilewati.")
                continue

            dur_input = input(f"   Lama akuisisi detik [{DEFAULT_DURATION_S}s]: ").strip()
            duration_s = float(dur_input) if dur_input else DEFAULT_DURATION_S

            kirim_label(ser, b_riil)
            time.sleep(0.3)
            ser.reset_input_buffer()

            print(f"   Mengumpulkan data selama {duration_s}s untuk v_helm={v_helm} V, I_helm={i_helm} A, B={b_riil} {SATUAN_B}...")
            collected = kumpulkan_satu_titik(ser, writer_raw, f_raw, v_helm, i_helm, duration_s=duration_s)

            if len(collected) == 0:
                print("   [!] Tidak ada sampel valid. Coba ulangi titik ini.")
                continue

            mean_v = statistics.mean(collected)
            std_v = statistics.stdev(collected) if len(collected) > 1 else 0.0
            summary_rows.append((b_riil, mean_v, std_v, v_helm, i_helm))
            print(f"   -> B = {b_riil} {SATUAN_B}: rata-rata {mean_v:.6f} V (stdev {std_v*1000:.2f} mV)")

    if len(summary_rows) < 2:
        print("\nData kurang dari 2 titik, regresi tidak dapat dihitung.")
        ser.close()
        return

    with open(SUMMARY_FILE, "w", newline="", encoding="utf-8") as f_sum:
        writer_sum = csv.writer(f_sum)
        writer_sum.writerow([f"B_riil_{SATUAN_B}", "tegangan_rata_V", "tegangan_stdev_V", "v_helm_V", "I_helm_A"])
        for row in summary_rows:
            writer_sum.writerow(row)

    buat_kurva_V_vs_B(summary_rows)
    buat_kurva_sensitivitas(summary_rows)

    ser.close()
    print(f"\nSelesai!\n  Data mentah : {RAW_LOG_FILE}\n  Ringkasan   : {SUMMARY_FILE}\n  Grafik      : {PLOT_FILE}")


if __name__ == "__main__":
    main()
