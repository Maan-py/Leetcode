# 704. Binary Search

- Tanggal: 2026-11-11
- Level: Easy
- Kode: [0704-binary-search.py](0704-binary-search.py)

## Pahami soal
<!-- input, output, batasan, kasus aneh, dengan kata-kataku sendiri -->
- Input: list `nums` yang **sudah terurut naik**, semua angkanya berbeda, dan sebuah `target`.
- Output: **indeks** `target` di `nums`, atau `-1` kalau tidak ada.
- Syarat penting: **harus O(log n)**. Mengecek satu per satu (O(n)) tidak memenuhi syarat soal.
- Kata kunci yang membuat binary search bisa dipakai: **sudah terurut**.
- Kasus aneh:
  - `nums` hanya 1 elemen (`[5]`).
  - Target ada di ujung kiri atau kanan.
  - Target tidak ada.

## Ide
<!-- cara menyelesaikannya dalam 1–3 kalimat, seperti menjelaskan ke teman -->
Seperti main tebak angka 1–100: selalu tebak **tengahnya**, lalu **buang separuh** yang pasti salah.
`left` dan `right` adalah batas **area pencarian**, dan kedua ujungnya ikut dihitung.
Cek `nums[mid]`. Kalau terlalu kecil, buang kiri (`left = mid + 1`). Kalau terlalu besar, buang kanan (`right = mid - 1`). Ulangi sampai ketemu atau areanya kosong.

## Proses & buntu
<!-- apa yang dicoba, di mana salah, kode yang salah, kenapa salah -->
1. **Versi 1: linear search dengan `while ... or found == False`** menghasilkan `IndexError` kalau target tidak ada.
   - `or` membuat loop tetap jalan selama `found` masih False, walaupun `i` sudah melewati ujung list.
   - Seharusnya `and`. Variabel `found` juga sebenarnya tidak perlu, karena langsung `return i`.
2. **Versi 2: `return -1` di dalam `while`** membuat hasilnya selalu `-1`.
   - Fungsi langsung keluar di putaran pertama.
   - Pelajaran indentasi lagi (seperti Valid Anagram): `return -1` harus **sejajar** dengan `while`, supaya jalan setelah loop selesai.
3. Linear search itu O(n), sedangkan soal minta **O(log n)**, jadi harus binary search.
4. **Bingung dengan kode binary search**: kenapa `left <= right`, kenapa `mid + 1`, dan kenapa `mid - 1`?
   - `mid + 1` / `mid - 1`: `mid` sudah dicek dan **bukan** target, jadi ikut dibuang.
     Kalau ditulis `left = mid`, loop bisa macet selamanya. Contoh: cari 12, `left = 4`, `right = 5`, `mid = 4`, lalu `left` tetap 4.
   - `else` hanya terjadi untuk `nums[mid] > target`, karena kasus `==` sudah di-`return` lebih dulu.
   - `left <= right`: saat `left == right` area masih berisi **1 elemen** yang belum dicek.
     Kalau ditulis `<`, contoh `[5]` dengan target 5 akan salah menghasilkan `-1`.
     `left > right` artinya area kosong, jadi `-1`.
5. Versi akhir lolos 2 Example, dan juga target di ujung kanan (12 → 5), ujung kiri (-1 → 0), `[5]` target 5 → 0, dan `[5]` target 3 → -1.

## Kompleksitas
- Waktu: O(log n) karena setiap putaran membuang separuh area. Untuk n = 10⁴ paling banyak sekitar 14 putaran, sedangkan linear search bisa sampai 10.000.
- Memori: O(1) karena hanya `left`, `right`, dan `mid`.

## Pelajaran Python
<!-- sintaks atau konsep baru yang dipelajari -->
- `//` adalah pembagian bulat (floor division): `5 // 2 = 2`. Dipakai untuk `mid`, karena indeks harus integer (`nums[2.5]` error).
  Jangan tertukar dengan bahasa lain, di mana `//` itu komentar. Di Python, komentar memakai `#`.
- `or` berarti jalan kalau **salah satu** benar, sedangkan `and` berarti jalan kalau **semua** benar. Untuk kondisi loop "masih ada elemen DAN belum ketemu" pakai `and`.
- Indentasi `return`:
  - menjorok di bawah `while` berarti jalan setiap putaran,
  - sejajar dengan `while` berarti jalan sekali setelah loop selesai.
- Pola binary search (area **inklusif**): `left = 0`, `right = len - 1`, `while left <= right`, `mid = (left + right) // 2`, lalu `mid ± 1`.

## Refleksi
- Tingkat kesulitan setelah paham: mudah / sedang / susah
- Bisa ditulis ulang tanpa melihat kode? ya / belum

## Review
| Tanggal | Hasil | Catatan |
|---|---|---|
