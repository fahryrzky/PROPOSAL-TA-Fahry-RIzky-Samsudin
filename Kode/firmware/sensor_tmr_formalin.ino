/*
  =====================================================================
  Akuisisi Data Sensor TMR - Formalin Detector
  (ALT023-10E -> AD623 -> ADS1115 -> Arduino -> Raspberry Pi)
  =====================================================================
  Signal chain fisik (sesuai skematik):
    Sensor TMR (ALT023-10E)
      -> filter RFI (R1/R2 1k + C1/C2 10nF + C3 100nF)
      -> AD623 instrumentation amplifier
         (gain diatur via RG jumper, VBIAS/REF ~2.5V dari divider R3=R4=1k)
      -> filter anti-alias (R5 10k + socket C4, lihat tabel cutoff yang sudah dihitung)
      -> ADS1115 16-bit ADC, channel AIN0
         (AIN1-AIN3 sudah di-ground, ADDR->GND => alamat I2C default 0x48)
      -> Arduino Uno (I2C hardware: SDA=A4, SCL=A5)
      -> Raspberry Pi lewat Serial/USB, 115200 baud, format CSV

  Sebelum upload:
    1. Install library "Adafruit ADS1X15" lewat Arduino Library Manager
    2. Isi AD623_GAIN di bawah sesuai RG yang benar-benar dipasang
       (Gain = 1 + (100000 / RG_ohm), lihat datasheet AD623)
    3. Cek ulang VBIAS_VOLT kalau nilai R3/R4 diganti dari 1k

  Catatan desain: Arduino di sini CUMA streaming sampel MENTAH satu-satu,
  tidak ada averaging/oversampling di firmware -- itu sengaja dipindah
  semua ke sisi Python (lebih ringan buat Arduino, dan lebih gampang diubah-ubah
  parameter statistiknya tanpa upload ulang sketch). Kecepatan streaming
  mengikuti data rate ADS1115 (128 SPS default, sekitar 1 baris/7,8 ms).

  Cara pakai saat kalibrasi:
    - Buka Serial Monitor, atau biarkan dikontrol script Python (115200 baud)
    - Kirim angka (boleh desimal) lalu Enter setiap kali titik kalibrasi berganti.
      "label" ini generik, artinya tergantung eksperimen yang lagi jalan:
        * kalibrasi formalin -> label = konsentrasi (mg/L)
        * karakterisasi sensor -> label = pembacaan teslameter (uT/mT, medan B riil)
      -> label ikut tercatat di setiap baris data sampai diganti lagi
    - Data mengalir terus-menerus secepat ADS1115 selesai konversi, siap dibaca
      Raspberry Pi/Python lewat pyserial; averaging & stdev dihitung di sana

  Format satu baris output:
    millis_ms,label,raw_adc,tegangan_lib_V,tegangan_manual_V
    (tegangan_lib_V dari ads.computeVolts(), tegangan_manual_V dari LSB hitung manual
    ala kode kating di proyek GMR -- dua-duanya harus sama persis, buat validasi silang)
  =====================================================================
*/

#include <Wire.h>
#include <Adafruit_ADS1X15.h>

Adafruit_ADS1115 ads;

// ---------------------- KONFIGURASI (sesuaikan sebelum pakai) ----------------------
const uint8_t   ADS1115_ADDR     = 0x48;  // ADDR pin -> GND
const uint8_t   ADS1115_CHANNEL  = 0;     // AIN0, satu-satunya channel yang dipakai
// PGA: +-6.144V, lebih longgar dari GAIN_ONE (+-4.096V) supaya output AD623 yang
// mendekati batas 0-5V tidak clipping. INI SATU-SATUNYA TEMPAT untuk ganti PGA
// (dipakai juga oleh perhitungan LSB manual di bawah, supaya selalu konsisten).
const adsGain_t PGA_GAIN         = GAIN_TWOTHIRDS;

// Dipakai untuk dicatat di header saja / referensi perhitungan lanjutan di Python:
// tidak mengubah cara ADC dibaca, hanya dokumentasi nilai rangkaian saat ini.
const float AD623_GAIN = 100.0;  // GANTI sesuai RG yang dipasang
const float VBIAS_VOLT = 2.5;    // dari divider R3=R4=1k (5V/2)

// ---------------------- VARIABEL INTERNAL ----------------------
float    currentLabel = -1;  // label titik kalibrasi aktif (mg/L formalin ATAU B dalam uT/mT,
                              // tergantung eksperimen); -1 = belum diset. Pakai float karena
                              // nilainya sering desimal (mis. 0,30 mg/L atau pembacaan teslameter).
float    lsb;                // Volt per count, dihitung manual di setup() (gaya kode kating)

void setup() {
  Serial.begin(115200);
  while (!Serial) { ; }

  Wire.begin();

  if (!ads.begin(ADS1115_ADDR)) {
    Serial.println(F("# ERROR: ADS1115 tidak terdeteksi. Cek wiring I2C (SDA/SCL) dan alamat 0x48."));
    while (1) { delay(1000); }
  }

  ads.setGain(PGA_GAIN);

  // 128 SPS = kompromi kecepatan vs noise bawaan ADS1115.
  // Untuk presisi maksimal (lebih lambat per sampel), ganti ke RATE_ADS1115_8SPS.
  ads.setDataRate(RATE_ADS1115_128SPS);

  // Hitung LSB secara manual (gaya kode kating di proyek GMR) sebagai pembanding
  // independen terhadap ads.computeVolts(). Hasilnya harus sama; kalau beda,
  // berarti ada yang salah setting gain di salah satu sisi.
  float vfsr;
  switch (PGA_GAIN) {
    case GAIN_TWOTHIRDS: vfsr = 6.144; break;
    case GAIN_ONE:       vfsr = 4.096; break;
    case GAIN_TWO:       vfsr = 2.048; break;
    case GAIN_FOUR:      vfsr = 1.024; break;
    case GAIN_EIGHT:     vfsr = 0.512; break;
    case GAIN_SIXTEEN:   vfsr = 0.256; break;
    default:              vfsr = 6.144; break;
  }
  lsb = vfsr / 32768.0;  // ADS1115 single-ended, LSB dalam Volt per count

  Serial.print(F("# LSB manual = "));
  Serial.print(lsb, 8);
  Serial.println(F(" V/count"));
  Serial.print(F("# AD623_GAIN="));
  Serial.print(AD623_GAIN);
  Serial.print(F(" VBIAS_VOLT="));
  Serial.println(VBIAS_VOLT);
  Serial.println(F("# Ketik angka (mg/L) lalu Enter untuk menandai label konsentrasi saat ini."));
  Serial.println(F("millis_ms,label,raw_adc,tegangan_lib_V,tegangan_manual_V"));
}

void loop() {
  handleSerialLabel();
  takeAndPrintReading();
}

void handleSerialLabel() {
  if (Serial.available() > 0) {
    float val = Serial.parseFloat();
    while (Serial.available() > 0 && (Serial.peek() == '\n' || Serial.peek() == '\r')) {
      Serial.read();
    }
    // Tidak difilter val>=0: sensor TMR ini bipolar, jadi label B boleh negatif
    // (medan dengan polaritas berlawanan) saat karakterisasi.
    currentLabel = val;
    Serial.print(F("# Label titik kalibrasi diset ke "));
    Serial.println(currentLabel, 4);
  }
}

void takeAndPrintReading() {
  int16_t raw = ads.readADC_SingleEnded(ADS1115_CHANNEL);  // blocking, nunggu 1 konversi ADS1115 selesai

  float voltLib    = ads.computeVolts(raw);  // metode 1: library
  float voltManual = raw * lsb;              // metode 2: LSB manual (gaya kating), buat validasi silang

  Serial.print(millis());
  Serial.print(',');
  Serial.print(currentLabel, 4);
  Serial.print(',');
  Serial.print(raw);
  Serial.print(',');
  Serial.print(voltLib, 6);
  Serial.print(',');
  Serial.println(voltManual, 6);
}
