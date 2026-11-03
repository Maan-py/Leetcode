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
   ```

   - `<namaMethod>` = nama method resmi LeetCode untuk soal itu (camelCase),
     beserta parameter dan type hint-nya sesuai signature resmi jika kamu tahu pasti.
     Jika tidak yakin, gunakan nama soal dalam camelCase dengan `self, *args`,
     dan sebutkan bahwa signature perlu disesuaikan.
   - Tambahkan import lain (mis. `Optional`) hanya jika diperlukan oleh signature.
   - Jika soal memakai struktur seperti `ListNode`/`TreeNode`, sertakan definisinya
     sebagai komentar seperti di LeetCode.
   - **PENTING: JANGAN tulis solusi, petunjuk, atau ide penyelesaian.** Isi method
     hanya `pass`. Saya mau mengerjakan sendiri.

4. **Update README.md**:
   - Tambahkan baris baru di tabel "Daftar Soal", dengan tabel tetap terurut
     berdasarkan nomor soal:
     `| <nomor 4 digit> | [<Nama Soal>](<level>/<nama-file>) | <Easy|Medium> | - | Belum | - |`
   - Perbarui bagian "Progres": hitung ulang jumlah file `.py` di `easy/` dan
     `medium/`, lalu tulis `Easy: <n> / 26` dan `Medium: <n> / 73`.

5. **Sinkronkan antrian**: jika nomor soal ini ada di `antrian.txt`, hapus barisnya
   supaya tidak muncul lagi lewat `/harian`.

6. Jangan commit. Cukup laporkan singkat: path file yang dibuat dan progres terbaru.
