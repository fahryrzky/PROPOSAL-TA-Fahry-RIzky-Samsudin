"""
================================================================================
Kode/akuisisi_gui_B.py
================================================================================
Entry point kompatibilitas untuk Aplikasi Akuisisi & Karakterisasi Sensor TMR.
Mengarahkan langsung ke modul GUI modular `src.gui.app.TMRAcquisitionApp`.
================================================================================
"""

import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from src.gui import TMRAcquisitionApp

def main():
    app = TMRAcquisitionApp()
    app.mainloop()

if __name__ == "__main__":
    main()
