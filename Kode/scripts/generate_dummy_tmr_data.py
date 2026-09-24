"""
=========================================================================
Kode/scripts/generate_dummy_tmr_data.py
=========================================================================
Generator dataset dummy realistis untuk karakterisasi & kalibrasi sensor
TMR ALT023-10E dengan pengkondisi sinyal AD623 (V_REF = 2.50V, supply 5V).
Helmholtz Power Supply: 0 - 16 V (Rentang medan B: -4.0 s.d. +12.0 mT).
=========================================================================
"""

import os
import csv
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def generate_tmr_dummy_data():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.abspath(os.path.join(script_dir, ".."))
    data_dir = os.path.join(base_dir, "data")
    os.makedirs(data_dir, exist_ok=True)

    excel_path = os.path.join(data_dir, "titik_kalibrasi_B.xlsx")
    raw_csv_path = os.path.join(data_dir, "data_mentah_karakterisasi_B.csv")

    # Rentang medan magnet B (mT) kumparan Helmholtz: -4 mT s.d. +12 mT
    b_points = np.array([-4.0, -2.5, -1.0, 0.0, 1.5, 3.0, 5.0, 7.0, 9.0, 10.5, 12.0])

    # Power supply DC Helmholtz 0 - 16 V (Resistansi kumparan ~10 Ohm)
    v_helm = np.where(b_points < 0, np.abs(b_points) / 0.72 * 1.0, (b_points / 12.0) * 16.0)
    i_helm = v_helm / 10.0

    # Model respon sensor TMR ALT023-10E + AD623 In-Amp (V_REF = 2.50 V, 5V supply)
    def sensor_model(b):
        return 2.500 + 1.80 * np.tanh(0.185 * b / 1.80)

    summary_rows = []
    raw_rows = []

    start_time = datetime.now() - timedelta(minutes=20)

    for idx, (b, v_h, i_h) in enumerate(zip(b_points, v_helm, i_helm)):
        v_true = sensor_model(b)

        # 640 sampel valid (5 detik pada ~128 SPS) dengan noise Gaussian 3.5 mV
        n_samples = 640
        noise = np.random.normal(0, 0.0035, n_samples)
        v_samples = v_true + noise

        v_mean = float(np.mean(v_samples))
        v_std = float(np.std(v_samples, ddof=1))
        point_time = (start_time + timedelta(seconds=idx * 60)).strftime("%Y-%m-%d %H:%M:%S")

        summary_rows.append({
            "v_helm_V": round(float(v_h), 2),
            "I_helm_A": round(float(i_h), 3),
            "B_mT": round(float(b), 2),
            "V_mean_V": round(v_mean, 6),
            "V_std_V": round(v_std, 6),
            "n_sampel": n_samples,
            "duration_s": 5.0,
            "timestamp": point_time
        })

        # Format log mentah: timestamp, v_helm, i_helm, millis, label, raw_adc, tegangan_lib_V, tegangan_manual_V
        for s_idx, v_s in enumerate(v_samples):
            adc_raw = int((v_s / 6.144) * 32767)
            raw_time = (start_time + timedelta(seconds=idx * 60 + s_idx * 0.008)).isoformat()
            raw_rows.append([
                raw_time,
                round(float(v_h), 2),
                round(float(i_h), 3),
                s_idx * 8,
                round(float(b), 2),
                adc_raw,
                round(float(v_s), 6),
                round(float(v_s), 6)
            ])

    # Simpan Excel
    df_summary = pd.DataFrame(summary_rows)
    df_summary.to_excel(excel_path, index=False)
    print(f"[OK] Dataset titik kalibrasi berhasil dibuat: {excel_path} ({len(df_summary)} titik)")

    # Simpan CSV mentah
    with open(raw_csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "v_helm_V", "I_helm_A", "millis", "label", "raw_adc", "tegangan_lib_V", "tegangan_manual_V"])
        writer.writerows(raw_rows)
    print(f"[OK] Dataset streaming mentah berhasil dibuat: {raw_csv_path} ({len(raw_rows)} baris)")

    # Buat juga salinan di root BASE_DIR agar kompatibel
    try:
        df_summary.to_excel(os.path.join(base_dir, "titik_kalibrasi_B.xlsx"), index=False)
    except Exception:
        pass


if __name__ == "__main__":
    generate_tmr_dummy_data()
