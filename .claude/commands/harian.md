---
description: Ambil soal berikutnya dari antrian.txt dan buatkan template-nya
---

Siapkan soal LeetCode hari ini dari antrian.

## Langkah

1. **Baca `antrian.txt`.** Ambil baris soal **paling atas**: baris pertama yang
   tidak kosong dan tidak diawali `#`. Formatnya `<nomor> | <Nama Soal> | <easy|medium>`.
   Jika tidak ada baris soal lagi, beri tahu bahwa antrian sudah habis lalu berhenti.

2. **Cek apakah hari ini sudah dapat soal.** Cari file `.py` di `easy/` dan `medium/`
   yang docstring-nya berisi `Tanggal : <tanggal hari ini>`. Jika ada, sebutkan file
   itu dan tanya apakah tetap mau ambil soal berikutnya. Jangan lanjut sebelum dijawab.

3. **Buat soal tersebut** dengan mengikuti langkah 1–4 di `.claude/commands/catat.md`
   persis (nama file, cek duplikat, file `.py` dengan docstring + class `Solution`
   kosong + blok test dari Example resmi, file jurnal `.md` kosong, update tabel
   dan progres README). Aturan yang sama berlaku:
   **JANGAN tulis solusi, petunjuk, atau ide penyelesaian. Isi method hanya `pass`.**

4. **Hapus baris soal itu dari `antrian.txt`.** Jika sesudahnya sebuah bagian
   (`# --- ... ---`) tidak punya soal lagi, hapus juga judul bagian itu. Jika seluruh
   level habis, hapus juga penanda levelnya (`# ===== EASY =====` / `# ===== MEDIUM =====`).
   Jangan ubah baris lain.

   Antrian sengaja diurutkan semua Easy dulu baru Medium. Jangan ubah urutannya.
   Saat soal Easy terakhir diambil, beri tahu bahwa mulai besok masuk ke Medium.

5. Jangan commit. Laporkan singkat:
   - path file `.py` dan `.md` yang dibuat,
   - progres terbaru (Easy x / 26, Medium x / 73),
   - sisa soal di antrian.
