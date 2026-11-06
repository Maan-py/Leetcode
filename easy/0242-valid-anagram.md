# 242. Valid Anagram

- Tanggal: 2026-11-06
- Level: Easy
- Kode: [0242-valid-anagram.py](0242-valid-anagram.py)

## Pahami soal
<!-- input, output, batasan, kasus aneh, dengan kata-kataku sendiri -->
- Input: dua string, `s` dan `t`.
- Output: `True` kalau `t` adalah susunan ulang huruf-huruf `s`, yaitu **huruf yang sama dengan jumlah yang sama**. Kalau tidak, `False`.
- Batasan: panjang `s` dan `t` sampai 5 × 10⁴, isinya hanya huruf kecil a–z.
- Kasus aneh:
  - Panjangnya beda (`"a"`, `"ab"`), jadi pasti `False`.
  - Hurufnya sama tapi jumlahnya beda (`"aab"`, `"abb"` atau `"aacc"`, `"ccac"`). Kasus ini menjebak.

## Ide
<!-- cara menyelesaikannya dalam 1–3 kalimat, seperti menjelaskan ke teman -->
Salin `t` ke list `huruf_t` sebagai "kertas coretan".
Untuk setiap huruf di `s`: kalau ada di `huruf_t`, coret satu. Kalau tidak ada, langsung `False`.
Setelah semua huruf `s` habis, `huruf_t` harus kosong. Kalau masih ada sisa, berarti `t` punya huruf lebih.

## Proses & buntu
<!-- apa yang dicoba, di mana salah, kode yang salah, kenapa salah -->
1. **Versi 1: nested loop, cek "hurufnya ada di `t`?", lalu hitung jumlah `True`.**
   - Salah, karena hanya mengecek **keberadaan** huruf, bukan **jumlahnya**.
   - `"aab"`, `"abb"` menjadi `True`, karena `a` kedua memakai `a` yang sama di `t`.
   - Pelajaran: pasangan yang sudah dipakai harus **dicoret**.
2. **Versi 2: `if huruf_t[i] in s: huruf_t.remove(huruf_t[i])`.**
   - Perannya **tertukar**: huruf diambil dari `t`, dicari di `s`, tapi yang dicoret `t`.
   - `s` tidak pernah dicoret, jadi `c` di `s` bisa dipakai tiga kali. Akibatnya `"aacc"`, `"ccac"` menjadi `True`.
   - `return` juga masih di dalam `for`, jadi fungsi berhenti setelah huruf pertama.
3. **Versi 3: `if s[i] in huruf_t: huruf_t.remove(huruf_t[i])`.**
   - Pengecekannya sudah benar, tapi **huruf yang dicoret salah**.
   - `huruf_t[i]` berarti huruf apa pun di posisi `i`, bukan huruf yang dicari.
   - `for j` masih ada, jadi satu huruf mencoret berkali-kali.
   - Kondisi `return`-nya juga terbalik (`!= []` diberi `True`).
4. **Versi akhir:** `for huruf in s`, cek `huruf in huruf_t`, lalu `huruf_t.remove(huruf)`. Kalau tidak ada, `return False`. Setelah loop, cek `huruf_t == []`. Semua test lolos.

Aturan yang dipegang:
- **Daftar yang dicek dengan `in` harus sama dengan daftar yang dicoret.**
- Satu string dibaca, string lainnya dicoret.

## Kompleksitas
- Waktu: O(n²) karena loop `s` berjalan n kali, dan di setiap putaran `in` serta `.remove()` menelusuri `huruf_t` (sampai n).
- Memori: O(n) karena `huruf_t` adalah salinan `t`.

Belum optimal. Langkah berikutnya: **hitung** setiap huruf muncul berapa kali (dictionary), supaya tidak perlu mencari dan mencoret satu per satu.

## Pelajaran Python
<!-- sintaks atau konsep baru yang dipelajari -->
- String itu **immutable** (tidak bisa diubah). `t.remove()` dan `del t[0]` error, jadi ubah ke list dulu dengan `list(t)`.
- `list.remove(x)` menghapus **satu** `x` yang pertama, dan error kalau `x` tidak ada. Karena itu cek dulu dengan `in`.
- `t.replace('a', '', 1)` membuat **string baru** tanpa `a` pertama. Ini bukan mengubah string lama.
- `for huruf in s` langsung memberi hurufnya, jadi lebih jelas daripada `for i in range(len(s))` lalu `s[i]`.
- `range(len(s))` hanya memberi angka. Hurufnya diambil dari list yang mana ditentukan oleh nama list sebelum `[i]`.
- **Jangan mengubah list yang sedang di-loop**, karena ada elemen yang akan terlewat.
- Indentasi `return` menentukan apakah ia berjalan di dalam atau setelah loop.

## Refleksi
- Tingkat kesulitan setelah paham: mudah / sedang / susah
- Bisa ditulis ulang tanpa melihat kode? ya / belum

## Review
| Tanggal | Hasil | Catatan |
|---|---|---|
