---
name: academic-slides
description: Menyusun presentasi/slide deck yang minimalis, rapi, dan bergaya akademik — bukan tampilan "khas AI" (gradient norak, ikon generik, bullet menumpuk). WAJIB dipakai setiap kali diminta membuat/merevisi presentasi, PPT, slide deck, atau materi sidang/seminar/laporan (KKN, KMT, skripsi, dsb), bahkan jika user cuma bilang "bikinin PPT" tanpa detail desain. Juga dipakai kalau user komplain hasil slide "keliatan AI banget" atau minta versi lebih clean/profesional.
---

# Academic Minimalist Slides (Anti-Slop)

Tujuan skill ini: menghasilkan `.pptx` yang (a) enak dilihat, minimalis, konsisten,
(b) terasa akademik — bukan template pitch-deck startup, dan (c) TIDAK terlihat seperti
"output AI generik" (lihat checklist larangan di bawah).

Prinsip inti: **desain dulu di HTML/CSS, verifikasi visual pakai browser tool, baru
replikasikan ke `.pptx` asli yang teks-nya tetap editable.** Jangan langsung nulis
`python-pptx` tanpa pernah "melihat" hasilnya — itu penyebab utama hasil kelihatan slop.

## Alur kerja

1. **Kumpulkan konten & struktur**
   - Ambil dari user: topik, audiens (dosen penguji? tim? umum?), poin-poin utama,
     data/gambar yang harus masuk, jumlah slide kira-kira, bahasa (ID/EN), deadline.
   - Susun outline dulu sebagai teks (judul tiap slide + 1 kalimat inti per slide).
     Konfirmasi ke user SEBELUM masuk ke desain kalau outline-nya panjang/ambigu.

2. **Bangun mockup HTML/CSS**
   - Satu file HTML, tiap slide = satu `<div>` ukuran tetap `1280x720px` (rasio 16:9),
     `page-break-after: always` supaya bisa di-print/screenshot per slide.
   - Terapkan aturan desain di bawah (grid, tipografi, palet).
   - Ini BUKAN untuk dikirim ke user sebagai hasil akhir — ini working draft internal.

3. **Verifikasi visual (wajib, jangan skip)**
   - Render tiap slide ke screenshot (browser tool Antigravity / Playwright headless,
     viewport 1280x720, `deviceScaleFactor: 2` biar tajam).
   - Cek satu-satu: teks kepotong/overflow? spacing nggak konsisten antar slide?
     alignment miring? terlalu padat/kosong? warna kontras cukup?
   - Perbaiki HTML, render ulang, sampai bersih. Ini loop, bukan sekali jalan.

4. **Bangun `.pptx` final (python-pptx)**
   - Replikasikan PERSIS layout yang sudah disetujui di step 3: posisi (konversi
     px→EMU: `EMU = px * 9525` pada asumsi 96dpi), ukuran font, warna (hex sama),
     jenis font.
   - Teks harus jadi text box asli (editable), BUKAN screenshot yang ditempel sebagai
     gambar — ini yang bikin dosen/tim masih bisa edit setelahnya.
   - Chart/diagram: generate sebagai gambar (matplotlib/vega/dst) dengan style yang
     senada (lihat aturan warna), lalu embed. Foto/dokumentasi lapangan: crop rapi,
     jangan stretch/distorsi rasio.
   - Slide master: buat satu master/layout yang dipakai konsisten ke semua slide
     (posisi header, footer, nomor halaman) — jangan re-set posisi manual tiap slide.

5. **QA akhir**
   - Convert `.pptx` balik ke gambar (`soffice --headless --convert-to png` per slide,
     atau `--convert-to pdf` lalu rasterize) dan screenshot-diff terhadap mock HTML.
   - Kalau ada slide yang mismatch (font fallback beda, posisi geser), perbaiki
     `python-pptx`-nya, bukan mock HTML-nya.
   - Baru setelah ini dianggap selesai dan dikirim ke user.

## Aturan desain ("anti-slop" checklist)

**Palet warna**
- Maksimal 3 warna: 1 warna dasar (putih/off-white/charcoal gelap), 1 warna teks,
  1 warna aksen. Aksen dipakai hemat (garis, judul section, highlight satu angka
  penting) — bukan buat background penuh.
- DILARANG: gradient sebagai background, warna neon/saturasi tinggi, kombinasi
  ungu-pink-biru khas "AI generated" yang tanpa alasan brand/konteks.

**Tipografi**
- Maksimal 2 typeface: satu untuk heading, satu untuk body (boleh sama, beda weight).
  Pilih font yang tersedia cross-platform (Inter, IBM Plex Sans/Serif, Source Sans,
  Georgia, atau font institusi kalau ada) — bukan default Calibri/Arial polos.
- Tetapkan type scale tetap dan pakai konsisten, contoh:
  judul slide 32-36px, subjudul 20-22px, body 16-18px, caption/footnote 11-12px.
- Body text: maksimal ±35-40 kata per slide. Kalau lebih, pecah jadi 2 slide atau
  ringkas jadi poin kunci — jangan perkecil font supaya muat.

**Layout**
- Pakai grid (kolom 12 atau margin konsisten kiri-kanan-atas-bawah) di semua slide.
- Satu ide inti per slide. Hindari bullet bertumpuk 6-8 poin — pecah, atau ubah
  jadi diagram/tabel kalau memang perbandingan data.
- Header (judul slide) dan footer (nomor halaman, nama kegiatan/tanggal) di posisi
  identik di semua slide — bikin deck terasa satu kesatuan, bukan tempelan.

**Elemen yang DILARANG (ciri khas "AI slop")**
- Ikon generik dari clipart set default (kotak-kotak dengan ikon 3D/flat gradient
  yang nggak nyambung ke konten).
- Emoji sebagai bullet point atau dekorasi.
- Drop shadow tebal / efek glassmorphism berlebihan pada kartu/kotak.
- Kotak/card dengan border-radius besar dan bayangan di semua sisi, ditumpuk
  tanpa hierarki (ciri khas dashboard template generik).
- Foto stock generik yang tidak relevan hanya untuk mengisi ruang kosong.
- Teks rata tengah untuk paragraf/body copy (rata tengah hanya untuk judul singkat).

**Ciri akademik yang harus ADA**
- Slide judul: judul lengkap, nama penulis/tim, institusi (mis. nama universitas/
  jurusan/kelompok KKN), tanggal.
- Sitasi/sumber data dicantumkan kecil di footer slide yang relevan, bukan cuma
  di slide terakhir.
- Penomoran gambar/tabel konsisten ("Gambar 1", "Tabel 2") kalau ada beberapa.
- Slide penutup: kesimpulan ringkas (bukan "Terima Kasih" polos tanpa isi) dan/atau
  daftar referensi kalau relevan (skripsi, laporan KMT, dsb).

## Struktur konten referensi (sidang skripsi/tugas akhir sains-teknik)

Pola urutan & isi slide di bawah ini diambil dari contoh sidang skripsi bidang
sains/instrumentasi yang solid secara akademik. **Pakai ini sebagai acuan STRUKTUR
& JENIS INFORMASI per slide — bukan acuan visual.** Rendering tetap wajib ikut
"Aturan desain" di atas (tanpa gradient banner, tanpa ikon clipart, tanpa drop
shadow, tanpa garis dekoratif) — ganti semua elemen dekoratif itu dengan
tipografi bersih, garis tipis (1px) sebagai pemisah, dan whitespace.

1. **Slide judul** — judul penelitian lengkap (istilah teknis/asing dimiringkan),
   nama penulis + NIM, dosen pembimbing I & II, jurusan/fakultas/institusi,
   jenis sidang (jika ada), tanggal. Logo institusi kecil di pojok, bukan
   dominan.
2. **Latar belakang** — dibangun sebagai rantai argumen, bukan bullet lepas:
   masalah besar (data/statistik + sitasi) → pendekatan/metode yang relevan
   (dengan sitasi tiap klaim) → celah penelitian (gap) yang jadi alasan riset
   ini dilakukan. Satu ide per blok, blok dipisah garis tipis atau whitespace,
   bukan kotak berwarna dengan shadow.
3. **Rumusan masalah & tujuan penelitian** — dua kolom sejajar, masing-masing
   list bernomor, dan urutannya 1:1 berkorespondensi (rumusan masalah #1 dijawab
   tujuan #1, dst). Ini pola yang bagus, pertahankan korespondensinya.
4. **Landasan teori** — satu konsep/topik per slide (atau per section jelas),
   tiap klaim disitasi, gambar/rumus pendukung diberi caption bernomor
   ("Gambar N", "Persamaan N") dan direferensikan di teks.
5. **Metode** — tempat & waktu penelitian (paragraf singkat), tabel alat & bahan
   (tabel bersih, tanpa warna baris berselang-seling yang mencolok), diagram
   rangkaian/desain sistem dengan caption.
6. **Perancangan perangkat keras/lunak** — diagram alir (flowchart) per tahap
   (akuisisi data, pelatihan model, implementasi, dst), tiap flowchart diberi
   caption dan referensi ke bagian a/b/c-nya di teks.
7. **Hasil per pengujian** (slide ini biasanya berulang beberapa kali, satu per
   eksperimen/variabel yang diuji) — pola tetapnya:
   - Judul slide spesifik ke pengujian tsb (bukan "Hasil" generik).
   - Satu kalimat kesimpulan kuantitatif di bagian atas (bukan kotak warna
     tebal — cukup dibedakan lewat bobot font atau garis pembatas tipis).
   - Data pendukung: tabel angka + grafik (scatter/line dengan fit & R²) +
     bila relevan persamaan regresi. Tabel dan grafik diberi caption bernomor.
8. **Komparasi kondisi** — kalau ada perbandingan (dengan vs tanpa perlakuan,
   metode A vs B), sandingkan dalam satu slide: tabel/grafik berdampingan,
   satu kalimat kesimpulan yang eksplisit menyebut angka pembanding.
9. **Kesimpulan** — poin bernomor sesuai jumlah rumusan masalah (korespondensi
   1:1 lagi), angka/istilah kunci ditebalkan (bold), bukan warna-warni. Sertakan
   juga keterbatasan penelitian di poin terakhir kalau ada.
10. **Daftar pustaka** — gaya sitasi konsisten (mis. APA), alfabetis, boleh
    beberapa slide berturut-turut kalau panjang, tanpa dekorasi tambahan.
11. **Lampiran** (opsional) — bukti pendukung: publikasi, sertifikat, paten,
    dokumentasi kegiatan — foto asli (bukan clipart) dengan caption ringkas.
12. **Slide penutup** — ucapan penutup singkat; boleh pakai foto dokumentasi
    asli sebagai latar dengan overlay gelap tipis untuk keterbacaan teks, tapi
    tanpa elemen dekoratif tambahan (panah, garis melengkung, dst).

Kalau user memberi contoh deck lain sebagai referensi, terapkan logika yang sama:
pisahkan dulu apa yang STRUKTUR/KONTEN (biasanya layak ditiru untuk akademik) vs
apa yang VISUAL/DEKORASI (biasanya ini sumber "slop" dan harus diganti sesuai
checklist di atas) — jangan asumsikan seluruh contoh harus direplikasi mentah.

## Dependencies
- `python-pptx` (generate file akhir)
- Browser/headless render untuk verifikasi (Playwright, atau browser tool bawaan
  Antigravity)
- `libreoffice`/`soffice` untuk QA render balik `.pptx` → gambar (opsional tapi
  sangat direkomendasikan sebelum deliver)

## Catatan pemasangan di Antigravity
Simpan folder ini di:
- Per-workspace: `[project]/.agent/skills/academic-slides/SKILL.md`
- Global (semua project): `~/.gemini/antigravity/skills/academic-slides/SKILL.md`

Skill ini ter-trigger otomatis (semantic triggering) tiap ada permintaan yang
menyentuh presentasi/slide/PPT — nggak perlu dipanggil manual.
