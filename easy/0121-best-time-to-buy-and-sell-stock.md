# 121. Best Time to Buy and Sell Stock

- Tanggal: 2026-11-09
- Level: Easy
- Kode: [0121-best-time-to-buy-and-sell-stock.py](0121-best-time-to-buy-and-sell-stock.py)

## Pahami soal
<!-- input, output, batasan, kasus aneh, dengan kata-kataku sendiri -->
- Input: list `prices`, yaitu harga saham setiap hari.
- Output: untung terbesar dari **satu kali beli lalu satu kali jual**. Hari jual harus **setelah** hari beli. Kalau tidak bisa untung, hasilnya `0`.
- Batasan: panjang `prices` sampai **10⁵**.
- Kasus aneh:
  - Harga termurah ada di hari **terakhir** (`[2, 4, 1]`), jadi tidak bisa dijual. Jawabannya tetap 2 (beli di 2, jual di 4).
  - Harga turun terus (`[7, 6, 4, 3, 1]`), hasilnya 0.
  - Hanya satu hari (`[5]`), hasilnya 0.

## Ide
<!-- cara menyelesaikannya dalam 1–3 kalimat, seperti menjelaskan ke teman -->
Bertanya dari sisi **penjualan**: "kalau aku jual hari ini, beli terbaiknya adalah harga termurah **sebelum** hari ini."
Telusuri harga sekali sambil mengingat dua angka, yaitu **harga termurah sejauh ini** dan **untung terbesar sejauh ini**.
Setiap hari: perbarui harga termurah, hitung untung kalau jual hari ini, lalu perbarui untung terbesar.

## Proses & buntu
<!-- apa yang dicoba, di mana salah, kode yang salah, kenapa salah -->
1. **Versi 1: cari `min(prices)`, lalu cari `max` di bagian setelahnya.** Hasilnya **Wrong Answer** di `[2, 4, 1]` (keluar 0, seharusnya 2).
   - Harga termurah (1) ada di hari terakhir, jadi setelahnya tidak ada hari untuk menjual.
   - Pelajaran: harga **termurah** belum tentu hari **beli terbaik**.
2. **Versi 2: brute force, semua pasangan beli dan jual disimpan di `list_profit`, lalu diambil `max`.** Jawabannya benar, tapi **TLE**.
   - Untuk n = 10⁵ ada sekitar **5 miliar** pasangan, dan menyimpan semuanya di list juga memakan puluhan GB memori.
   - Ada bug tambahan: kalau `prices` hanya 1 hari, list-nya kosong dan `max([])` error.
3. **Membuat tabel dengan tangan** (hari, harga, termurah sejauh ini, untung hari ini, untung terbesar sejauh ini) untuk `[7, 1, 5, 3, 6, 4]`.
   - Terlihat bahwa setiap baris cukup dihitung dari **harga hari ini** dan **baris kemarin**. Tidak perlu melihat jauh ke belakang.
   - Sempat **bingung** mengubah tabel menjadi kode. Yang membantu: membuat satu kolom dulu (termurah sejauh ini) dengan satu variabel yang diperbarui terus, ibarat "kertas kecil" yang ditimpa.
4. **Versi akhir:** satu loop dengan `cheapest = min(cheapest, price)`, `profit_today = price - cheapest`, dan `highest_profit = max(highest_profit, profit_today)`.
   - Lolos semua test, termasuk `[5]`.
   - Input 100.001 hari selesai sekitar 0,01 detik di laptop.

## Kompleksitas
- Waktu: O(n) karena hanya satu loop, dan setiap hari cuma ada 3 operasi.
- Memori: O(1) karena hanya menyimpan 3 variabel (`cheapest`, `profit_today`, `highest_profit`), tanpa list.

| Cara | Waktu | Memori | Hasil |
|---|---|---|---|
| min global lalu max sesudahnya | O(n) | O(n) (slice) | Wrong Answer |
| Semua pasangan disimpan di list | O(n²) | O(n²) | TLE |
| Termurah sejauh ini (satu loop) | O(n) | O(1) | lolos |

## Pelajaran Python
<!-- sintaks atau konsep baru yang dipelajari -->
- `min(a, b)` dan `max(a, b)` bisa membandingkan **dua nilai** langsung, bukan hanya mencari isi list.
- Pola "**variabel yang diperbarui terus**" (*running min/max*): nilai kemarin tidak perlu disimpan di list. Cukup **ditimpa**, karena hanya dibutuhkan untuk menghitung hari ini.
- `max([])` dengan list kosong menghasilkan `ValueError`. Hati-hati kalau list bisa kosong.
- `prices[i:]` (slice) membuat list baru, jadi butuh memori tambahan.
- Kalau bingung mengubah ide jadi kode: **buat tabel dengan tangan**. Setiap kolom yang dihitung dari baris sebelumnya biasanya menjadi satu variabel.

## Refleksi
- Tingkat kesulitan setelah paham: mudah / sedang / susah
- Bisa ditulis ulang tanpa melihat kode? ya / belum

## Review
| Tanggal | Hasil | Catatan |
|---|---|---|
