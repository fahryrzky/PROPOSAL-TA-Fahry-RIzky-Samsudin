/*
  WiFi Connect Test - ESP32-C3 Super Mini
  Fokus cuma buat nyoba & debug koneksi WiFi doang.

  Fitur:
  - Scan network dulu, cek SSID target ketemu atau nggak
  - Auto-print REASON CODE kalau disconnect (nggak perlu ubah Core Debug Level)
  - Retry connect terus dengan info jelas, TANPA auto-restart ESP
    (biar Serial Monitor nggak keputus & reason code kebaca)

  ISI SSID & PASSWORD di bawah sebelum upload.
*/

#include <WiFi.h>

const char* WIFI_SSID     = "Robotkidz";
const char* WIFI_PASSWORD = "ISI_PASSWORD_DISINI";

unsigned long lastRetry = 0;
const unsigned long RETRY_INTERVAL_MS = 10000; // coba connect ulang tiap 10 detik kalau gagal

// ---- Dipanggil otomatis tiap ada event WiFi ----
void WiFiEventHandler(WiFiEvent_t event, WiFiEventInfo_t info) {
  switch (event) {
    case ARDUINO_EVENT_WIFI_STA_START:
      Serial.println("[EVENT] STA mode started");
      break;

    case ARDUINO_EVENT_WIFI_STA_CONNECTED:
      Serial.println("[EVENT] Terhubung ke AP (asosiasi berhasil)");
      break;

    case ARDUINO_EVENT_WIFI_STA_GOT_IP:
      Serial.print("[EVENT] Dapat IP: ");
      Serial.println(WiFi.localIP());
      Serial.println(">>> WiFi CONNECTED & SIAP DIPAKAI <<<");
      break;

    case ARDUINO_EVENT_WIFI_STA_DISCONNECTED:
      Serial.print("[EVENT] DISCONNECTED! Reason code: ");
      Serial.println(info.wifi_sta_disconnected.reason);
      printReasonMeaning(info.wifi_sta_disconnected.reason);
      break;

    default:
      break;
  }
}

// ---- Terjemahan reason code paling umum ----
void printReasonMeaning(uint8_t reason) {
  Serial.print("      Artinya: ");
  switch (reason) {
    case 2:   Serial.println("AUTH_EXPIRE - sesi otentikasi expired"); break;
    case 3:   Serial.println("AUTH_LEAVE"); break;
    case 4:   Serial.println("ASSOC_EXPIRE"); break;
    case 5:   Serial.println("ASSOC_TOOMANY - AP penuh, terlalu banyak device"); break;
    case 6:   Serial.println("NOT_AUTHED"); break;
    case 7:   Serial.println("NOT_ASSOCED"); break;
    case 8:   Serial.println("ASSOC_LEAVE - AP aktif mutusin koneksi kita"); break;
    case 15:  Serial.println("4WAY_HANDSHAKE_TIMEOUT - hampir pasti PASSWORD SALAH"); break;
    case 200: Serial.println("BEACON_TIMEOUT - sinyal terlalu lemah / hilang"); break;
    case 201: Serial.println("NO_AP_FOUND - SSID tidak ditemukan saat connect"); break;
    case 202: Serial.println("AUTH_FAIL - gagal autentikasi (cek password & tipe keamanan)"); break;
    case 203: Serial.println("ASSOC_FAIL"); break;
    case 204: Serial.println("HANDSHAKE_TIMEOUT"); break;
    default:  Serial.println("(reason code lain, cek dokumentasi esp_wifi_types.h)"); break;
  }
}

void scanAndCheckSSID() {
  Serial.println("\nScanning WiFi networks...");
  int n = WiFi.scanNetworks();
  if (n == 0) {
    Serial.println("Gak ada WiFi kedetect sama sekali!");
    return;
  }

  Serial.printf("Ditemukan %d network:\n", n);
  bool found = false;
  for (int i = 0; i < n; i++) {
    String ssid = WiFi.SSID(i);
    wifi_auth_mode_t enc = WiFi.encryptionType(i);
    Serial.printf("  [%d] %-25s RSSI:%4d Ch:%2d  Enc:%s\n",
                  i, ssid.c_str(), WiFi.RSSI(i), WiFi.channel(i),
                  authModeToStr(enc));
    if (ssid == String(WIFI_SSID)) {
      found = true;
      Serial.println("       ^-- SSID target, ketemu!");
    }
  }

  if (!found) {
    Serial.println("\n!! SSID target TIDAK ketemu di hasil scan !!");
    Serial.println("Cek lagi: 5GHz? salah ketik? sinyal ketutup jarak/dinding?");
  }
  Serial.println();
}

const char* authModeToStr(wifi_auth_mode_t mode) {
  switch (mode) {
    case WIFI_AUTH_OPEN:            return "OPEN";
    case WIFI_AUTH_WEP:             return "WEP";
    case WIFI_AUTH_WPA_PSK:         return "WPA-PSK";
    case WIFI_AUTH_WPA2_PSK:        return "WPA2-PSK";
    case WIFI_AUTH_WPA_WPA2_PSK:    return "WPA/WPA2-PSK";
    case WIFI_AUTH_WPA2_ENTERPRISE: return "WPA2-Enterprise";
    case WIFI_AUTH_WPA3_PSK:        return "WPA3-PSK";
    case WIFI_AUTH_WPA2_WPA3_PSK:   return "WPA2/WPA3-PSK";
    default:                        return "UNKNOWN";
  }
}

void startConnect() {
  Serial.printf("Mencoba connect ke: %s\n", WIFI_SSID);
  WiFi.disconnect(true);
  delay(200);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
}

void setup() {
  Serial.begin(115200);
  delay(1000);

  Serial.println("\n======================================");
  Serial.println("   ESP32-C3 WiFi Connect Test");
  Serial.println("======================================");

  WiFi.mode(WIFI_STA);
  WiFi.setSleep(false);
  WiFi.onEvent(WiFiEventHandler);

  scanAndCheckSSID();
  startConnect();
  lastRetry = millis();
}

void loop() {
  // Kalau belum connect & udah lewat interval, coba connect lagi
  if (WiFi.status() != WL_CONNECTED && millis() - lastRetry > RETRY_INTERVAL_MS) {
    Serial.println("\n--- Retry connect ---");
    startConnect();
    lastRetry = millis();
  }

  // Tiap 5 detik print status ringkas biar tau ESP masih hidup & mantau progress
  static unsigned long lastPrint = 0;
  if (millis() - lastPrint > 5000) {
    lastPrint = millis();
    Serial.printf("[status check] WiFi.status() = %d | IP: %s\n",
                  WiFi.status(), WiFi.localIP().toString().c_str());
  }
}
