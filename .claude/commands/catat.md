---
description: Catat soal LeetCode baru (buat file template + update README)
argument-hint: <nomor> <nama soal> <easy|medium>
---

Catat soal LeetCode baru ke jurnal ini. Input: `$ARGUMENTS`

## Parsing input

Format: `<nomor> <nama soal> <easy|medium>`

- Token **pertama** = nomor soal (angka).
- Token **terakhir** = level, harus `easy` atau `medium` (tidak peka huruf besar/kecil).
- Semua token **di antaranya** = nama soal (boleh lebih dari satu kata).

Contoh: `/catat 1 Two Sum easy` → nomor `1`, nama `Two Sum`, level `easy`.

Jika input tidak lengkap, nomor bukan angka, atau level bukan `easy`/`medium`,
hentikan dan beri tahu formatnya yang benar. Jangan menebak.

## Langkah

1. **Tentukan nama file**: nomor di-pad jadi 4 digit + nama soal dalam kebab-case
   (huruf kecil, spasi → `-`, hapus karakter selain huruf/angka/`-`, lalu rapatkan
   `-` yang berurutan jadi satu dan buang `-` di awal/akhir).
   Contoh: `0001-two-sum.py`, `0167-two-sum-ii-input-array-is-sorted.py`.
   Path: `<level>/<nama-file>`.

2. **Cek duplikat**: jika file itu sudah ada, atau nomor tersebut sudah ada di tabel
   README, hentikan dan beri tahu saya. Jangan menimpa apa pun.

3. **Buat file soal** dengan template persis seperti ini (isi Tanggal dengan
   tanggal hari ini format `YYYY-MM-DD`):

   ```python
   """
   Soal    : <nomor>. <Nama Soal>
   Tanggal : <YYYY-MM-DD>
   Pola    :
   Ide     :
   Buntu   :
   Waktu   : O()
   Memori  : O()
   Status  : Belum
   """

   from typing import List


   class Solution:
       def <namaMethod>(self, <parameter>) -> <tipe>:
           pass


   if __name__ == "__main__":
       s = Solution()
       print(s.<namaMethod>(<input contoh 1>))  # <output contoh 1>
       print(s.<namaMethod>(<input contoh 2>))  # <output contoh 2>
   ```

   - **Blok test** berisi satu baris `print` untuk setiap **Example resmi** di soal
     LeetCode, dengan output yang diharapkan sebagai komentar di ujung baris.
     Hanya pakai contoh yang memang tertulis di soal, jangan menambah kasus sendiri
     (kasus tambahan bisa jadi petunjuk; itu bagian saya). Jika tidak yakin dengan
     contoh resminya, tulis `# TODO: salin Example dari soal` dan sebutkan dalam laporan.
   - Jika input/output memakai `ListNode`/`TreeNode`, jangan buat helper; tulis
     contohnya sebagai komentar saja (`# Example 1: head = [1,2,3] -> [3,2,1]`)
     ditambah `# TODO: buat input-nya`.

   - `<namaMethod>` = nama method resmi LeetCode untuk soal itu (camelCase),
     beserta parameter dan type hint-nya sesuai signature resmi jika kamu tahu pasti.
     Jika tidak yakin, gunakan nama soal dalam camelCase dengan `self, *args`,
     dan sebutkan bahwa signature perlu disesuaikan.
   - Tambahkan import lain (mis. `Optional`) hanya jika diperlukan oleh signature.
   - Jika soal memakai struktur seperti `ListNode`/`TreeNode`, sertakan definisinya
     sebagai komentar seperti di LeetCode.
   - **PENTING: JANGAN tulis solusi, petunjuk, atau ide penyelesaian.** Isi method
     hanya `pass`. Saya mau mengerjakan sendiri.

   **Buat juga file jurnal** di folder yang sama dengan nama yang sama tapi
   berekstensi `.md` (mis. `easy/0001-two-sum.md`), dengan template persis ini.
   Semua bagian dibiarkan kosong untuk saya isi sendiri, jangan diisi apa pun:

   ```markdown
   # <nomor>. <Nama Soal>

   - Tanggal: <YYYY-MM-DD>
   - Level: <Easy|Medium>
   - Kode: [<nama-file>.py](<nama-file>.py)

   ## Pahami soal
   <!-- input, output, batasan, kasus aneh, dengan kata-kataku sendiri -->

   ## Ide
   <!-- cara menyelesaikannya dalam 1–3 kalimat, seperti menjelaskan ke teman -->

   ## Proses & buntu
   <!-- apa yang dicoba, di mana salah, kode yang salah, kenapa salah -->

   ## Kompleksitas
   - Waktu: O() karena
   - Memori: O() karena

   ## Pelajaran Python
   <!-- sintaks atau konsep baru yang dipelajari -->

   ## Refleksi
   - Tingkat kesulitan setelah paham: mudah / sedang / susah
   - Bisa ditulis ulang tanpa melihat kode? ya / belum

   ## Review
   | Tanggal | Hasil | Catatan |
   |---|---|---|
   ```

4. **Update README.md**:
   - Tambahkan baris baru di tabel "Daftar Soal", dengan tabel tetap terurut
     berdasarkan nomor soal:
     `| <nomor 4 digit> | [<Nama Soal>](<level>/<nama-file>.py) | <Easy|Medium> | - | Belum | [jurnal](<level>/<nama-file>.md) |`
   - Perbarui bagian "Progres": hitung ulang jumlah file `.py` di `easy/` dan
     `medium/`, lalu tulis `Easy: <n> / 26` dan `Medium: <n> / 73`.

5. **Sinkronkan antrian**: jika nomor soal ini ada di `antrian.txt`, hapus barisnya
   supaya tidak muncul lagi lewat `/harian`.

6. Jangan commit. Cukup laporkan singkat: path file `.py` dan `.md` yang dibuat
   dan progres terbaru.
