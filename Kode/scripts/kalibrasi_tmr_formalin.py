"""
=========================================================================
Kode/scripts/kalibrasi_tmr_formalin.py
=========================================================================
Akuisisi data kalibrasi konsentrasi formalin dengan sensor TMR ALT023-10E
Berbasis DURASI WAKTU (Lama Detik) & Settling Time.
=========================================================================
"""

import os
import sys
import csv
import time
import statistics
from datetime import datetime

import numpy as np
import matplotlib.pyplot as plt

# Resolusi path direktori
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

for d in [DATA_DIR, OUTPUT_DIR]:
    os.makedirs(d, exist_ok=True)

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

# ---------------------- KONFIGURASI ----------------------
import platform

DEFAULT_PORT = "COM3" if platform.system() == "Windows" else "/dev/ttyUSB0"
SERIAL_PORT = DEFAULT_PORT
BAUD_RATE = 115200

RAW_LOG_FILE = os.path.join(DATA_DIR, "data_mentah_kalibrasi.csv")
SUMMARY_FILE = os.path.join(DATA_DIR, "ringkasan_kalibrasi.csv")
PLOT_FILE = os.path.join(OUTPUT_DIR, "kurva_kalibrasi.png")

# Parameter akuisisi berbasis LAMA DETIK
DEFAULT_DURATION_S = 5.0   # Pengambilan data selama 5 detik per konsentrasi
DEFAULT_SETTLE_S = 1.0     # 1 detik pertama dibuang untuk stabilisasi larutan


class SimulatedSerialFormalin:
    """Mock serial stream for testing TMR formalin calibration without physical hardware."""
    def __init__(self, baud=115200):
        self.conc_current = 0.0
        self.sample_idx = 0

    def write(self, data):
        try:
            self.conc_current = float(data.decode().strip())
        except ValueError:
            pass

    def reset_input_buffer(self):
        self.sample_idx = 0

    def readline(self):
        self.sample_idx += 1
        time.sleep(0.001)
        # Respons sensor TMR terhadap konsentrasi formalin (sensitivitas ~0.024 V/(mg/L))
        v_true = 2.50 + 0.0245 * self.conc_current
        noise = np.random.normal(0, 0.0028)
        v = v_true + noise
        adc_raw = int((v / 6.144) * 32767)
        millis = self.sample_idx * 8
        line = f"{millis},{self.conc_current},{adc_raw},{v:.6f},{v:.6f}\n"
        return line.encode()

    def close(self):
        pass


def connect_serial(force_simulasi=False):
    if force_simulasi or "--simulasi" in sys.argv or "--sim" in sys.argv:
        print("[*] Menggunakan Mode Simulasi Kalibrasi Formalin (Dummy Stream)...")
        return SimulatedSerialFormalin(BAUD_RATE)

    try:
        import serial
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1.5)
        time.sleep(1)
        ser.reset_input_buffer()
        print(f"[*] Menghubungkan ke port {SERIAL_PORT}...")
        test_line = ser.readline()
        if not test_line:
            print(f"[!] Port {SERIAL_PORT} aktif namun tidak mengirim data.")
            print("[*] Beralih otomatis ke Mode Simulasi Formalin...")
            ser.close()
            return SimulatedSerialFormalin(BAUD_RATE)
        return ser
    except Exception as e:
        print(f"[!] Port serial '{SERIAL_PORT}' tidak terdeteksi: {e}")
        print("[*] Mengalihkan otomatis ke Mode Simulasi Formalin.")
        return SimulatedSerialFormalin(BAUD_RATE)


def kirim_label(ser, label):
    ser.write(f"{label}\n".encode())


def baca_satu_baris(ser):
    raw = ser.readline()
    if not raw:
        return ""
    return raw.decode(errors="ignore").strip()


def kumpulkan_satu_titik(ser, writer_raw, f_raw, duration_s=DEFAULT_DURATION_S, settle_s=DEFAULT_SETTLE_S):
    """
    Mengambil data selama `duration_s` detik penuh.
    Membuang sampel `settle_s` detik pertama untuk settling time.
    """
    collected = []
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
        writer_raw.writerow([timestamp] + parts)
        f_raw.flush()

        v = float(parts[3])
        collected.append(v)

        if t_now - last_print >= 0.5:
            last_print = t_now
            print(f"  [{elapsed:.1f}s / {duration_s:.1f}s] V = {v:.6f} V ({len(collected)} sampel)")

    print(f"  -> Selesai: {len(collected)} sampel valid dalam {time.time()-t_start:.1f}s ({settle_count} dibuang saat settling {settle_s}s)")
    return collected


def buat_kurva(summary_rows):
    konsentrasi = np.array([r[0] for r in summary_rows])
    tegangan = np.array([r[1] for r in summary_rows])
    stdev = np.array([r[2] for r in summary_rows])

    slope, intercept = np.polyfit(konsentrasi, tegangan, 1)
    y_pred = slope * konsentrasi + intercept
    ss_res = np.sum((tegangan - y_pred) ** 2)
    ss_tot = np.sum((tegangan - np.mean(tegangan)) ** 2)
    r2 = 1 - ss_res / ss_tot if ss_tot != 0 else 0.0

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.errorbar(konsentrasi, tegangan, yerr=stdev, fmt="none", ecolor="gray", capsize=4, zorder=1)
    x_line = np.linspace(min(konsentrasi) - 0.5, max(konsentrasi) + 0.5, 200)
    ax.plot(x_line, slope * x_line + intercept, "r--", zorder=2,
            label=f"V = {slope:.6f}*C + {intercept:.6f}\nR² = {r2:.4f}")
    scatter_bola(ax, konsentrasi, tegangan, warna=WARNA_DATA, label="Data kalibrasi formalin", zorder=3)
    ax.set_xlabel("Konsentrasi formalin (mg/L)")
    ax.set_ylabel("Tegangan output AD623 (V)")
    ax.set_title("Kurva Kalibrasi Sensor TMR terhadap Konsentrasi Formalin")
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(PLOT_FILE, dpi=300)

    print(f"\nPersamaan kalibrasi : V = {slope:.6f} * C + {intercept:.6f}  (R² = {r2:.4f})")
    print(f"Sensitivitas        : {slope:.6f} V/(mg/L)")
    if slope != 0:
        print(f"Rumus prediksi      : C = (V - {intercept:.6f}) / {slope:.6f}  [mg/L]")
    print(f"Grafik disimpan ke  : {PLOT_FILE}")


def main():
    ser = connect_serial()
    print(f"Terhubung ke instrumen di {SERIAL_PORT} ({BAUD_RATE} baud)")
    print("Mode Akuisisi: BERBASIS DURASI DETIK (Default: 5 detik/titik, settling: 1 detik)\n")

    summary_rows = []

    with open(RAW_LOG_FILE, "w", newline="", encoding="utf-8") as f_raw:
        writer_raw = csv.writer(f_raw)
        writer_raw.writerow([
            "timestamp", "millis_ms", "label_konsentrasi", "raw_adc",
            "tegangan_lib_V", "tegangan_manual_V",
        ])

        while True:
            print(f"\n>> Titik ke-{len(summary_rows) + 1} (ketik 'selesai' jika sudah cukup)")
            user_input = input("   Masukkan konsentrasi larutan (mg/L): ").strip()
            if user_input.lower() == "selesai":
                break
            try:
                konsentrasi = float(user_input)
            except ValueError:
                print("   Nilai tidak valid, coba lagi.")
                continue

            dur_input = input(f"   Lama akuisisi detik [{DEFAULT_DURATION_S}s]: ").strip()
            duration_s = float(dur_input) if dur_input else DEFAULT_DURATION_S

            kirim_label(ser, konsentrasi)
            input("   Celupkan sensor, tunggu sinyal stabil di osiloskop/multimeter, lalu tekan [Enter]...")

            ser.reset_input_buffer()
            print(f"   Mengambil data {konsentrasi} mg/L selama {duration_s} detik...")
            collected = kumpulkan_satu_titik(ser, writer_raw, f_raw, duration_s=duration_s)

            if len(collected) == 0:
                print("   [!] Tidak ada sampel valid. Coba ulangi titik ini.")
                continue

            mean_v = statistics.mean(collected)
            std_v = statistics.stdev(collected) if len(collected) > 1 else 0.0
            summary_rows.append((konsentrasi, mean_v, std_v))
            print(f"   -> {konsentrasi} mg/L: rata-rata {mean_v:.6f} V (stdev {std_v*1000:.2f} mV)")

    if len(summary_rows) < 2:
        print("\nData kurang dari 2 titik, regresi tidak dapat dihitung.")
        ser.close()
        return

    with open(SUMMARY_FILE, "w", newline="", encoding="utf-8") as f_sum:
        writer_sum = csv.writer(f_sum)
        writer_sum.writerow(["konsentrasi_mg_L", "tegangan_rata_V", "tegangan_stdev_V"])
        for row in summary_rows:
            writer_sum.writerow(row)

    buat_kurva(summary_rows)
    ser.close()
    print(f"\nSelesai!\n  Data mentah : {RAW_LOG_FILE}\n  Ringkasan   : {SUMMARY_FILE}\n  Grafik      : {PLOT_FILE}")


if __name__ == "__main__":
    main()
