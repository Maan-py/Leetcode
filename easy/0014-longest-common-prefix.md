# 14. Longest Common Prefix

- Tanggal: 2026-11-03
- Level: Easy
- Kode: [0014-longest-common-prefix.py](0014-longest-common-prefix.py)

## Pahami soal
<!-- input, output, batasan, kasus aneh, dengan kata-kataku sendiri -->

## Ide
Jadikan string pertama patokan. Cek huruf ke-i di semua string lain (vertical
scanning, kolom per kolom). Berhenti kalau ada string yang sudah habis
(`i >= len(s)`) atau hurufnya beda. Huruf baru dicatat setelah SEMUA string lolos
di kolom itu.

## Proses & buntu
- Memakai `i` untuk dua hal sekaligus (nomor kolom dan nomor string) →
  `strs[i+1][i]` → `IndexError`.
- Bingung bedanya `range(1, len(strs))` (memberi angka) dan `strs[1:]` (memberi
  string-nya langsung).
- `append` sempat ditaruh di dalam loop dalam, jadi huruf tercatat sebelum semua
  string dicek.
- Lupa cek string yang lebih pendek → bisa `IndexError`. Urutan kondisi penting:
  `i >= len(s)` harus di depan supaya `s[i]` tidak diakses (short-circuit `or`).

## Kompleksitas
- Waktu: O(n * m) karena ada paling banyak m kolom (panjang string pertama), dan
  di tiap kolom paling banyak n string dicek.
- Memori: O(m) karena list `hasil` bisa berisi sampai m huruf.

## Pelajaran Python
<!-- sintaks atau konsep baru yang dipelajari -->

## Refleksi
- Tingkat kesulitan setelah paham: mudah / sedang / susah
- Bisa ditulis ulang tanpa melihat kode? ya / belum

## Review
| Tanggal | Hasil | Catatan |
|---|---|---|
