"""
================================================================================
src/acquisition.py
================================================================================
Mesin Akuisisi Data Berbasis DURASI WAKTU (Detik) & Penyangga Aliran Real-Time
================================================================================
"""

import time
from datetime import datetime
import numpy as np


class StreamBuffer:
    """Buffer geser (rolling buffer) untuk memvisualisasikan aliran real-time."""
    def __init__(self, max_points=150):
        self.max_points = max_points
        self.times = []
        self.voltages = []
        self.b_fields = []
        self.start_time = None

    def reset(self):
        self.times.clear()
        self.voltages.clear()
        self.b_fields.clear()
        self.start_time = None

    def add_sample(self, v_val, b_val):
        if self.start_time is None:
            self.start_time = time.time()
        t_now = time.time() - self.start_time

        self.times.append(t_now)
        self.voltages.append(v_val)
        self.b_fields.append(b_val)

        if len(self.times) > self.max_points:
            self.times.pop(0)
            self.voltages.pop(0)
            self.b_fields.pop(0)

        return t_now


class DurationAcquisitionEngine:
    """
    Eksekutor pengambilan titik kalibrasi berdasarkan DURASI WAKTU (Lama Detik).
    Memisahkan waktu stabilisasi awal (settling time) dan waktu pencuplikan data valid.
    """
    def __init__(self, serial_mgr):
        self.serial_mgr = serial_mgr
        self.is_running = False
        self.cancel_requested = False

    def acquire_point(
        self,
        v_helm,
        i_helm,
        b_teslameter,
        duration_seconds=5.0,
        settle_seconds=1.0,
        progress_callback=None,
        log_callback=None,
    ):
        """
        Mengambil sampel selama `duration_seconds` detik penuh.
        Data pada `settle_seconds` pertama dibuang untuk stabilisasi transien.
        """
        self.is_running = True
        self.cancel_requested = False

        if log_callback:
            log_callback(
                f"Mulai akuisisi titik B={b_teslameter:.3f} mT (Durasi: {duration_seconds:.1f}s, Settle: {settle_seconds:.1f}s)..."
            )

        # Beritahu Arduino / Simulator target medan B
        self.serial_mgr.write_label(b_teslameter)
        time.sleep(0.1)

        valid_samples = []
        settle_samples_count = 0

        t_start = time.time()
        t_end = t_start + duration_seconds

        last_progress_update = 0

        while time.time() < t_end and not self.cancel_requested:
            line = self.serial_mgr.read_line()
            t_now = time.time()
            elapsed = t_now - t_start

            if line and not line.startswith("#"):
                parts = line.split(",")
                if len(parts) >= 5:
                    try:
                        v_val = float(parts[3])
                        if elapsed < settle_seconds:
                            settle_samples_count += 1
                        else:
                            valid_samples.append(v_val)
                    except ValueError:
                        pass

            # Update progress callback tiap 50ms
            if t_now - last_progress_update >= 0.05:
                last_progress_update = t_now
                fraction = min(1.0, elapsed / duration_seconds)
                if progress_callback:
                    progress_callback(fraction, elapsed, duration_seconds, len(valid_samples))

            # Sleep mikro agar CPU tidak 100%
            time.sleep(0.001)

        self.is_running = False

        if self.cancel_requested:
            if log_callback:
                log_callback("Akuisisi titik dibatalkan oleh pengguna.")
            return None

        # Hitung statistik akhir
        if len(valid_samples) == 0:
            if log_callback:
                log_callback("[PERINGATAN] Tidak ada sampel valid yang terbaca.")
            return None

        v_mean = float(np.mean(valid_samples))
        v_std = float(np.std(valid_samples, ddof=1)) if len(valid_samples) > 1 else 0.0
        actual_duration = time.time() - t_start

        point_data = {
            "v_helm": v_helm,
            "i_helm": i_helm,
            "b_teslameter": b_teslameter,
            "v_sensor": v_mean,
            "std_v": v_std,
            "n_samples": len(valid_samples),
            "settle_discarded": settle_samples_count,
            "duration_s": round(actual_duration, 2),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        if log_callback:
            log_callback(
                f"Selesai: B={b_teslameter:.3f} mT -> V={v_mean:.5f} V (±{v_std*1000:.2f} mV) "
                f"[{len(valid_samples)} sampel dalam {actual_duration:.1f}s]"
            )

        return point_data

    def cancel(self):
        self.cancel_requested = True
