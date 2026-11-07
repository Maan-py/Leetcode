# 268. Missing Number

- Tanggal: 2026-11-07
- Level: Easy
- Kode: [0268-missing-number.py](0268-missing-number.py)

## Pahami soal
<!-- input, output, batasan, kasus aneh, dengan kata-kataku sendiri -->
- Input: list `nums` berisi `n` angka **berbeda**, semuanya di rentang `0` sampai `n`.
- Output: satu angka di rentang itu yang **tidak ada** di `nums`.
- Rentangnya punya `n + 1` angka (`0, 1, …, n`), sedangkan isi list hanya `n`, jadi pasti tepat satu yang hilang.
- Batasan: `n` sampai 10⁴.
- Kasus aneh: yang hilang bisa angka **terbesar**, `n` itu sendiri. Contohnya `[0, 1]` menghasilkan `2`. Karena itu loop harus sampai `n`, bukan berhenti di `n - 1`.

## Ide
<!-- cara menyelesaikannya dalam 1–3 kalimat, seperti menjelaskan ke teman -->
Cek setiap angka dari `0` sampai `n`. Angka pertama yang tidak ada di `nums` adalah jawabannya.

## Proses & buntu
<!-- apa yang dicoba, di mana salah, kode yang salah, kenapa salah -->
- Dikerjakan sendiri. Kode akhirnya: `for i in range(0, len(nums) + 1)` lalu `if i not in nums: return i`.
- `+ 1` di `range` itu penting supaya angka `n` ikut dicek (kasus `[0, 1]` menghasilkan `2`).
- <!-- tambahkan sendiri: ada yang sempat bikin bingung? -->

## Kompleksitas
- Waktu: O(n²) karena loop berjalan `n + 1` kali, dan di setiap putaran `i not in nums` menelusuri list (sampai n).
  Di kasus terburuk (n = 10⁴, yang hilang angka terakhir) butuh sekitar 0,6 detik di laptop. Masih cukup untuk batasan ini, tapi tidak untuk n yang jauh lebih besar.
- Memori: O(1) karena tidak membuat struktur data baru, hanya variabel `i`.

Follow-up dari soal: bisakah **O(n) waktu dan O(1) memori**? Belum dicoba.

## Pelajaran Python
<!-- sintaks atau konsep baru yang dipelajari -->
- `not in` adalah kebalikan `in`: `True` kalau elemennya **tidak ada**.
- `range(a, b)` berhenti **sebelum** `b`. Jadi untuk mencakup `n`, tulis `range(0, n + 1)`, atau cukup `range(n + 1)`, karena `0` adalah nilai awal default.
- `in` pada **list** itu O(n), sedangkan pada **set** O(1). Ini pelajaran yang sama dengan Contains Duplicate.

## Refleksi
- Tingkat kesulitan setelah paham: mudah / sedang / susah
- Bisa ditulis ulang tanpa melihat kode? ya / belum

## Review
| Tanggal | Hasil | Catatan |
|---|---|---|
