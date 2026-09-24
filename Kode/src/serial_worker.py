"""
================================================================================
src/serial_worker.py
================================================================================
Manajemen Komunikasi Serial Hardware (Arduino) & Mock Simulator Sensor TMR
================================================================================
"""

import time
import numpy as np
import serial
from serial.tools import list_ports

from .config import AD623_VREF, ADS1115_LSB, DEFAULT_BAUD


def scan_serial_ports():
    """Memindai seluruh port COM yang aktif pada sistem."""
    ports = ["[SIMULASI / DUMMY]"]
    try:
        for p in list_ports.comports():
            ports.append(p.device)
    except Exception:
        pass
    return ports


class SimulatedSerialTMR:
    """Mock serial stream for testing without physical Arduino connected."""
    def __init__(self, baud=DEFAULT_BAUD):
        self.b_current = 0.0
        self.sample_idx = 0
        self.is_open = True

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
        # Respons sensor TMR ALT023-10E: V_REF = 2.50 V, G ~ 0.185 V/mT
        v_true = AD623_VREF + 1.80 * np.tanh(0.185 * self.b_current / 1.80)
        noise = np.random.normal(0, 0.0035)
        v = v_true + noise
        adc_raw = int(v / ADS1115_LSB)
        millis = self.sample_idx * 8
        line = f"{millis},{self.b_current},{adc_raw},{v:.6f},{v:.6f}\n"
        return line.encode()

    def in_waiting(self):
        return 1

    def close(self):
        self.is_open = False


class SerialManager:
    """Pengelola koneksi serial hardware Arduino atau mode simulasi."""
    def __init__(self):
        self.ser = None
        self.is_connected = False
        self.is_simulated = False
        self.current_port = ""

    def connect(self, port_name, baud=DEFAULT_BAUD):
        self.disconnect()
        if "[SIMULASI" in port_name:
            self.ser = SimulatedSerialTMR(baud)
            self.is_connected = True
            self.is_simulated = True
            self.current_port = "[SIMULASI]"
            return True, "Mode simulasi TMR ALT023-10E berhasil diaktifkan."
        else:
            try:
                self.ser = serial.Serial(port_name, baud, timeout=1.0)
                time.sleep(1.5)  # Tunggu Arduino reset
                self.ser.reset_input_buffer()
                self.is_connected = True
                self.is_simulated = False
                self.current_port = port_name
                return True, f"Berhasil terhubung ke Arduino di {port_name} ({baud} baud)."
            except Exception as e:
                self.ser = None
                self.is_connected = False
                self.is_simulated = False
                return False, str(e)

    def disconnect(self):
        if self.ser:
            try:
                self.ser.close()
            except Exception:
                pass
        self.ser = None
        self.is_connected = False
        self.is_simulated = False
        self.current_port = ""

    def read_line(self):
        if self.ser and self.is_connected:
            try:
                if self.is_simulated or (hasattr(self.ser, "in_waiting") and self.ser.in_waiting):
                    return self.ser.readline().decode(errors="ignore").strip()
            except Exception:
                pass
        return ""

    def write_label(self, label):
        if self.ser and self.is_connected:
            try:
                if hasattr(self.ser, "write"):
                    self.ser.write(f"{label}\n".encode())
                if hasattr(self.ser, "reset_input_buffer"):
                    self.ser.reset_input_buffer()
            except Exception:
                pass
