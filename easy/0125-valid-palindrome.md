# 125. Valid Palindrome

- Tanggal: 2026-11-08
- Level: Easy
- Kode: [0125-valid-palindrome.py](0125-valid-palindrome.py)

## Pahami soal
<!-- input, output, batasan, kasus aneh, dengan kata-kataku sendiri -->
- Input: string `s` yang bisa berisi huruf, angka, spasi, dan tanda baca.
- Output: `True` kalau string-nya **palindrom**, yaitu terbaca sama dari depan dan belakang, **setelah**:
  - semua huruf diubah jadi huruf kecil,
  - semua karakter selain huruf atau angka dibuang.
- Kasus aneh:
  - `" "` setelah dibersihkan menjadi string kosong `""`. String kosong dianggap palindrom, jadi `True`.
  - Angka juga ikut dicek, karena `isalnum` mencakup huruf **dan** angka.

## Ide
<!-- cara menyelesaikannya dalam 1–3 kalimat, seperti menjelaskan ke teman -->
Bersihkan dulu string-nya (hanya huruf dan angka, semuanya huruf kecil).
Lalu cocokkan huruf pertama dengan huruf terakhir, huruf kedua dengan huruf kedua dari belakang, dan seterusnya.
Kalau ada satu pasangan yang beda, berarti bukan palindrom.

## Proses & buntu
<!-- apa yang dicoba, di mana salah, kode yang salah, kenapa salah -->
1. Membersihkan string sudah langsung benar: `"".join([char for char in s if char.isalnum()]).lower()`.
2. **Bingung membuat loop-nya.** Versi pertama memakai nested loop:
   `for i in res:` lalu `for j in res[::-1]:`.
   - Hasilnya **setiap** huruf dibandingkan dengan **setiap** huruf dari belakang: 21 × 21 = 441 perbandingan.
   - Padahal satu huruf kiri hanya punya **satu** pasangan.
3. Menulis pasangan indeksnya secara manual: `0 -> 20`, `1 -> 19`, `2 -> 18`, …
   Dari situ terlihat jumlah setiap pasangan selalu 20, yaitu `len(res) - 1`.
   Jadi `kanan = len(res) - 1 - i`, dan cukup **satu loop**.
4. Versi akhir: satu `for` dengan `kanan = len(res) - 1 - i`. Hasil setiap pasangan disimpan di list `output`, lalu dicek `if False in output`. Semua test lolos.

Bisa dirapikan lagi:
- Loop cukup sampai **setengah** (`range(len(res) // 2)`). Setengah sisanya hanya mengecek pasangan yang sama dengan arah dibalik.
- Langsung `return False` saat ketemu pasangan yang beda. Tidak perlu list `output`.
- Versi **Two Pointers**: `kiri = 0`, `kanan = len(res) - 1`, lalu `while kiri < kanan`. Kiri maju, kanan mundur.

## Kompleksitas
- Waktu: O(n) karena membersihkan string butuh satu kali jalan, dan loop pengecekan juga satu kali jalan. Tidak ada nested loop.
- Memori: O(n) karena `res` adalah salinan string yang sudah dibersihkan, dan `output` juga menyimpan n nilai.

Versi Two Pointers yang langsung bekerja di `s` (melewati karakter non-alfanumerik tanpa membuat `res`) bisa sampai **O(1)** memori.

## Pelajaran Python
<!-- sintaks atau konsep baru yang dipelajari -->
- `char.isalnum()` bernilai `True` kalau karakternya huruf **atau** angka.
- `.lower()` mengubah huruf jadi huruf kecil.
- `"".join(list)` menggabungkan list karakter menjadi string.
- `s[::-1]` adalah string yang dibalik.
- `//` adalah pembagian bulat (`21 // 2 = 10`), dipakai di `range()` yang hanya menerima bilangan bulat.
- Rumus indeks pasangan dari belakang: `len(x) - 1 - i`.
- **Two Pointers** itu teknik dua variabel indeks yang bergerak saling mendekat. Bukan linked list.
- `while` cocok dipakai kalau kondisi berhentinya "selama ..." (misalnya `kiri < kanan`), bukan "sebanyak n kali".

## Refleksi
- Tingkat kesulitan setelah paham: mudah / sedang / susah
- Bisa ditulis ulang tanpa melihat kode? ya / belum

## Review
| Tanggal | Hasil | Catatan |
|---|---|---|
