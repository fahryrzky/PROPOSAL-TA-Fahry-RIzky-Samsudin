import subprocess
import os

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

web_targets = [
    (
        "adafruit_ads1115",
        "[adafruit_ads1115] - Adafruit (2024) - Adafruit 4-Channel ADC Breakouts ADS1015 and ADS1115.pdf",
        "https://learn.adafruit.com/adafruit-4-channel-adc-breakouts"
    ),
    (
        "micronas_tmr",
        "[micronas_tmr] - TDK Micronas (2024) - Magnetic Field Sensors Tunnel Magneto Resistive TMR.pdf",
        "https://www.micronas.tdk.com/en/technologies/about-tmr-angle-sensors"
    ),
    (
        "electronicdesign_tmrgmr",
        "[electronicdesign_tmrgmr] - Electronic Design (2023) - Whats the Difference Between TMR and GMR Sensors.pdf",
        "https://www.electronicdesign.com/markets/industrial/article/21262432/electronic-design-whats-the-difference-between-tmr-and-gmr-sensors"
    ),
    (
        "sigma_adh",
        "[sigma_adh] - Sigma-Aldrich (2024) - Adipic Acid Dihydrazide ADH Product Information.pdf",
        "https://www.sigmaaldrich.com/US/en/product/sial/a0638"
    ),
    (
        "gantrade_adh",
        "[gantrade_adh] - Gantrade (2024) - Adipic Acid Dihydrazide Unique Crosslinking Agent and Curative.pdf",
        "https://www.gantrade.com/blog/adipic-acid-dihydrazide"
    ),
    (
        "magneticsmag_alt023",
        "[magneticsmag_alt023] - Magnetics Magazine (2023) - NVE Introduces Ultraminiature Analog TMR Sensors.pdf",
        "https://magneticsmag.com/nve-introduces-ultraminiature-analog-tmr-sensors/"
    ),
    (
        "halodoc_formalin",
        "[halodoc_formalin] - Halodoc (2023) - Mengenal Bahaya Formalin pada Makanan dan Dampaknya bagi Tubuh.pdf",
        "https://www.halodoc.com/artikel/mengenal-bahaya-formalin-pada-makanan-dan-dampaknya-bagi-tubuh"
    ),
    (
        "geeksforgeeks_resistor",
        "[geeksforgeeks_resistor] - GeeksforGeeks (2024) - What is Resistor.pdf",
        "https://www.geeksforgeeks.org/what-is-resistor/"
    ),
    (
        "electrical4u_resistor",
        "[electrical4u_resistor] - Electrical4U (2024) - What is Resistor Definition Types Symbol and Functions.pdf",
        "https://www.electrical4u.com/what-is-resistor/"
    ),
    (
        "circuitbasics_resistor",
        "[circuitbasics_resistor] - Circuit Basics (2024) - What is a Resistor.pdf",
        "https://www.circuitbasics.com/what-is-a-resistor/"
    ),
    (
        "pythonorg",
        "[pythonorg] - Python Software Foundation (2025) - Welcome to Python org.pdf",
        "https://www.python.org/"
    )
]

for key, filename, url in web_targets:
    out_path = os.path.abspath(os.path.join("referensi", filename))
    print(f"Printing {key} to PDF -> {filename}...")
    try:
        res = subprocess.run(
            [chrome, "--headless=new", "--disable-gpu", f"--print-to-pdf={out_path}", url],
            capture_output=True,
            timeout=40
        )
        if os.path.exists(out_path) and os.path.getsize(out_path) > 1000:
            with open(out_path, "rb") as f:
                head = f.read(10)
            print(f"  -> SUCCESS ({os.path.getsize(out_path)//1024} KB, head={head})")
        else:
            print(f"  -> FAILED: returncode={res.returncode}, exists={os.path.exists(out_path)}")
    except Exception as e:
        print(f"  -> ERROR: {e}")
