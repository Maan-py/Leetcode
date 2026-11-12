# 35. Search Insert Position

- Tanggal: 2026-11-12
- Level: Easy
- Kode: [0035-search-insert-position.py](0035-search-insert-position.py)

## Pahami soal
<!-- input, output, batasan, kasus aneh, dengan kata-kataku sendiri -->
- Input: list `nums` yang **sudah terurut naik**, semua angkanya berbeda, dan sebuah `target`.
- Output:
  - kalau `target` ada, return **indeksnya**;
  - kalau tidak ada, return **posisi tempat target harus disisipkan** supaya `nums` tetap terurut.
- Syarat: **O(log n)**. Ditambah kata *sorted*, ini tanda pakai binary search.
- Bedanya dengan 0704 hanya satu: kalau tidak ketemu, jawabannya bukan `-1`.
- Kasus aneh:
  - target lebih kecil dari semua angka, jadi disisipkan di depan (indeks `0`);
  - target lebih besar dari semua angka, jadi disisipkan di belakang (indeks `len(nums)`).

## Ide
<!-- cara menyelesaikannya dalam 1–3 kalimat, seperti menjelaskan ke teman -->
Pakai binary search 0704 persis. Hanya `return -1` di akhir diganti **`return left`**.
Saat loop berhenti (`left > right`), `left` berdiri tepat di angka pertama yang lebih besar dari target, dan di situlah target harus disisipkan.

## Proses & buntu
<!-- apa yang dicoba, di mana salah, kode yang salah, kenapa salah -->
1. Sadar soal ini bisa pakai binary search karena ada kata *sorted* dan syarat *O(log n)*, sama seperti 0704.
2. **Bingung** apa yang harus di-return kalau target tidak ketemu.
3. Telusuri Example 2 (`[1, 3, 5, 6]`, target `2`) dengan tangan:
   - `left=0, right=3`, `mid=1`, `nums[1]=3`: `2 > 3` False, jadi `right=0`.
   - `left=0, right=0`, `mid=0`, `nums[0]=1`: `2 > 1` True, jadi `left=1`.
   - `left=1, right=0`: loop berhenti. Jawabannya `1`, sama dengan `left`.
4. Cek ulang di Example 3 (target `7`): loop berhenti di `left=4`, sama dengan jawabannya.
5. Kenapa `left`:
   - `left` hanya bergeser melewati angka yang **lebih kecil** dari target.
   - `right` hanya bergeser melewati angka yang **lebih besar**.
   - Jadi setelah bersilangan, `left` ada di angka pertama yang lebih besar.
6. Ubah satu baris (`return -1` menjadi `return left`), dan semua Example lolos.
   Sudah dicek juga untuk target di depan (`0` → `0`), `[1]` target `0` → `0`, `[1]` target `2` → `1`, dan target `4` → `2`.

## Kompleksitas
- Waktu: O(log n) karena setiap putaran membuang separuh area.
- Memori: O(1) karena hanya `left`, `right`, dan `mid`.

## Pelajaran Python
<!-- sintaks atau konsep baru yang dipelajari -->
- Tidak ada sintaks baru. Pelajarannya ada di cara berpikir:
  - **Cari soal lama yang mirip**: 0035 adalah 0704 dengan modifikasi kecil.
  - **Telusuri dengan tangan** dan catat nilai variabel di setiap langkah, terutama **saat loop berhenti**. Jawabannya sering sudah ada di salah satu variabel.
- Saat menelusuri, tulis kondisinya persis seperti di kode (`target > nums[mid]`), jangan dibalik di kepala.
- Binary search punya dua bentuk akhir:
  - "cari persis" → `return -1`;
  - "cari posisi" → `return left`.

## Refleksi
- Tingkat kesulitan setelah paham: mudah / sedang / susah
- Bisa ditulis ulang tanpa melihat kode? ya / belum

## Review
| Tanggal | Hasil | Catatan |
|---|---|---|
