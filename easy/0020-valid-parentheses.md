# 20. Valid Parentheses

- Tanggal: 2026-11-10
- Level: Easy
- Kode: [0020-valid-parentheses.py](0020-valid-parentheses.py)

## Pahami soal
<!-- input, output, batasan, kasus aneh, dengan kata-kataku sendiri -->
- Input: string `s` yang **hanya** berisi `( ) [ ] { }`. Panjangnya 1 sampai 10⁴.
- Output: `True` kalau susunan kurungnya valid. Ada 3 aturan:
  1. Setiap kurung buka ditutup oleh kurung yang **jenisnya sama** (`"(]"` salah).
  2. Urutan tutupnya benar: yang **dibuka terakhir ditutup duluan**, seperti kotak di dalam kotak (`"([)]"` salah, `"([])"` benar).
  3. Tidak ada kurung tutup tanpa pasangan bukanya (`")"` salah), dan tidak ada kurung buka yang tersisa (`"(("` salah).
- Kasus aneh:
  - Diawali kurung tutup (`")"`, `"]["`).
  - Kurung tutup kelebihan (`"())"`).
  - Kurung buka kelebihan (`"(()"`).

## Ide
<!-- cara menyelesaikannya dalam 1–3 kalimat, seperti menjelaskan ke teman -->
Baca string dari kiri sambil memegang "buku catatan" (list) berisi kurung buka yang **belum ditutup**.
Kurung buka ditulis di ujung buku. Kurung tutup dicocokkan dengan **ujung buku** (kurung yang terakhir dibuka): kalau cocok, coret; kalau tidak cocok atau bukunya kosong, `False`.
Di akhir, buku harus kosong.

## Proses & buntu
<!-- apa yang dicoba, di mana salah, kode yang salah, kenapa salah -->
1. **Awalnya tidak ada ide sama sekali.** Mencoba nested loop dengan `s[:1]`, tapi tidak jelas arahnya.
2. **Disederhanakan dulu: hanya `(` dan `)`.** Cukup **menghitung**: `(` berarti +1, `)` berarti −1. Akhirnya harus 0 dan tidak boleh minus.
   Contoh `"()()"`: hitungannya 1, 0, 1, 0, jadi valid.
3. **Kenapa menghitung tidak cukup untuk 3 jenis kurung:** `"([)]"` dengan tiga hitungan terpisah berakhir semuanya 0, jadi dianggap "valid", padahal salah.
   Hitungan hanya tahu **berapa banyak**, tidak tahu **urutannya**. Jadi yang dibutuhkan adalah list untuk mengingat urutan kurung buka, yaitu **stack**.
4. **Sempat bingung skenarionya**: kenapa "memegang kurung tutup", padahal isi catatan selalu kurung buka?
   Ternyata itu dua hal berbeda:
   - `i` adalah karakter yang **sedang dibaca** dari `s`, bisa buka atau tutup,
   - `note` hanya berisi kurung **buka**.
   Kurung tutup tidak pernah masuk ke `note`. Ia hanya **dibandingkan** dengan `note[-1]`.
   Yang membantu: membayangkan **pita** (`s`) dan **buku catatan** (`note`) lalu menelusurinya langkah demi langkah.
5. **`KeyError: '('`**: dua `if` berdiri sendiri-sendiri, jadi setelah kurung buka di-`append`, `if` kedua tetap jalan dan mencari `pair["("]`. Padahal key-nya hanya kurung tutup.
   - Perbaikannya: pakai `else`, supaya pengecekan hanya untuk kurung tutup.
6. **Buku kosong saat ada kurung tutup** (`")"`): `note[-1]` akan `IndexError`.
   - Perbaikannya: cek `note == []` dulu **sebelum** `note[-1]`.
7. Versi akhir lolos 5 Example dan juga `")"`, `"(("`, `"())"`, `"{[()()]}"`, `"]["`.

## Kompleksitas
- Waktu: O(n) karena setiap karakter dibaca sekali, dan `append`, `pop`, `[-1]`, serta pencarian di dictionary semuanya O(1).
- Memori: O(n) karena di kasus terburuk (semuanya kurung buka) seluruh karakter masuk ke `note`.

## Pelajaran Python
<!-- sintaks atau konsep baru yang dipelajari -->
- **Stack** dengan list: `append(x)` menambah di ujung, `[-1]` melihat ujung, `pop()` menghapus ujung. Yang terakhir masuk, pertama keluar (LIFO).
- **Dictionary** untuk pasangan: `{")": "(", ...}`. Key-nya kurung tutup karena yang dicari adalah "kurung tutup ini pasangan bukanya apa?".
  Bisa juga dibalik (key = kurung buka) dengan cara cek `pair[note[-1]] == i`.
- `KeyError` muncul kalau key-nya tidak ada di dictionary. `IndexError` muncul kalau `[-1]` dipakai pada list kosong.
- `if` + `if` itu **dua pengecekan terpisah**, keduanya bisa jalan. `if` + `else` artinya **hanya salah satu** yang jalan.
- Kode yang sama (`note == []`) bisa punya arti berbeda tergantung letaknya:
  - di dalam loop artinya "ada yang bisa ditutup?",
  - setelah loop artinya "semua sudah ditutup?".
- Kalau soal terasa terlalu sulit, **sederhanakan dulu** (satu jenis kurung), lalu lihat kenapa versi sederhananya gagal di soal asli.

## Refleksi
- Tingkat kesulitan setelah paham: mudah / sedang / susah
- Bisa ditulis ulang tanpa melihat kode? ya / belum

## Review
| Tanggal | Hasil | Catatan |
|---|---|---|
