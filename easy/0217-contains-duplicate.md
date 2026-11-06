# 217. Contains Duplicate

- Tanggal: 2026-11-05
- Level: Easy
- Kode: [0217-contains-duplicate.py](0217-contains-duplicate.py)

## Pahami soal
<!-- input, output, batasan, kasus aneh, dengan kata-kataku sendiri -->
- Input: list angka `nums`.
- Output: `True` kalau ada angka yang muncul **minimal dua kali**, `False` kalau semua angkanya beda.
- Batasan: panjang `nums` sampai **10⁵**, nilai angkanya dari -10⁹ sampai 10⁹.
- Kasus aneh: list yang semua angkanya beda adalah **kasus terburuk**, karena tidak ada duplikat yang bikin kita bisa berhenti lebih awal.

## Ide
<!-- cara menyelesaikannya dalam 1–3 kalimat, seperti menjelaskan ke teman -->
Telusuri angka satu per satu sambil mencatat angka yang sudah pernah dilihat di sebuah `set`.
Kalau angka sekarang sudah ada di `set`, berarti dobel, jadi langsung `True`.
Kalau sampai habis tidak ketemu, hasilnya `False`.

## Proses & buntu
<!-- apa yang dicoba, di mana salah, kode yang salah, kenapa salah -->
1. **Nested loop (cek semua pasangan)**, seperti Two Sum. Hasilnya benar tapi **TLE**.
   - Sudah ditambah `return True` lebih awal, tapi tetap TLE.
   - Kenapa? Test yang gagal berisi sekitar 54.500 angka **berbeda semua**, jadi tidak pernah berhenti lebih awal.
     Itu sekitar 54.500² / 2 ≈ **1,5 miliar** perbandingan.
   - Pelajaran: early return tidak menolong di kasus terburuk.
2. **`nums.count(i)` di dalam comprehension.** Kodenya pendek tapi tetap **TLE**.
   - `count()` sendiri menelusuri seluruh list, jadi kalau dipanggil untuk setiap angka hasilnya tetap `O(n²)`.
     Loop-nya hanya tersembunyi.
3. **`set` (`seen`).** Cek `i in seen`, kalau belum ada tinggal `seen.add(i)`. Cara ini **lolos**.
   - Bisa dirapikan: langsung `return True` saat ketemu dobel, dan `return False` di akhir.
     Tidak perlu list `duplicates`.

Alternatif lain yang dibahas: **urutkan dulu, lalu cek tetangga** (`nums[i] == nums[i + 1]`).
Setelah diurutkan, angka yang sama pasti bersebelahan. Waktunya `O(n log n)`, memorinya `O(1)` dengan `nums.sort()`.
Jadi intinya bukan "harus pakai set", tapi "harus menghindari `O(n²)`".

## Kompleksitas
- Waktu: O(n) karena setiap angka dilihat sekali, dan cek `in` atau `add` di `set` rata-rata `O(1)`.
- Memori: O(n) karena di kasus terburuk (semua beda) semua angka masuk ke `set`.

| Cara | Waktu | Memori | Hasil |
|---|---|---|---|
| Nested loop | O(n²) | O(1) | TLE |
| `count()` per angka | O(n²) | O(n) | TLE |
| Urutkan + cek tetangga | O(n log n) | O(1) | lolos |
| `set` | O(n) | O(n) | lolos |

## Pelajaran Python
<!-- sintaks atau konsep baru yang dipelajari -->
- `set()` adalah kumpulan tanpa duplikat. `x in my_set` itu `O(1)`, sedangkan `x in my_list` itu `O(n)`.
- `my_set.add(x)` dipakai untuk menambah isi `set`.
- `nums.count(x)` menghitung kemunculan `x`, tapi caranya menelusuri seluruh list (`O(n)`).
- List comprehension: `[i for i in ... if ...]`.
- Membaca batasan untuk menebak kompleksitas: kalau n = 10⁵, `O(n²)` hampir pasti TLE.
- `nums.sort()` mengurutkan list itu sendiri, sedangkan `sorted(nums)` membuat list baru.

## Refleksi
- Tingkat kesulitan setelah paham: mudah / sedang / susah
- Bisa ditulis ulang tanpa melihat kode? ya / belum

## Review
| Tanggal | Hasil | Catatan |
|---|---|---|
