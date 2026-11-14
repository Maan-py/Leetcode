# 21. Merge Two Sorted Lists

- Tanggal: 2026-11-14
- Level: Easy
- Kode: [0021-merge-two-sorted-lists.py](0021-merge-two-sorted-lists.py)

## Pahami soal
<!-- input, output, batasan, kasus aneh, dengan kata-kataku sendiri -->
- Input: dua linked list `list1` dan `list2`, masing-masing **sudah terurut naik**.
- Output: satu linked list gabungan yang tetap terurut, dibentuk dari **menyambung ulang node-node yang sudah ada**.
- Kasus aneh:
  - dua-duanya kosong → `[]`;
  - salah satu kosong → hasilnya list yang lain (`[]` + `[0]` → `[0]`);
  - angka yang sama ada di dua list (`1` dan `1`).

## Ide
<!-- cara menyelesaikannya dalam 1–3 kalimat, seperti menjelaskan ke teman -->
Seperti menggabungkan dua tumpukan kartu yang sudah urut:
- **Bandingkan angka paling depan, lalu ambil yang lebih kecil.** Ulangi selama dua-duanya masih ada.
- Kalau salah satu habis, **sambung sisa yang lain langsung**, karena sisanya sudah urut.

Barisan baru dimulai dari node palsu `dummy` sebagai pengait. `tail` menandai ujungnya, dan hasilnya `dummy.next`.

## Proses & buntu
<!-- apa yang dicoba, di mana salah, kode yang salah, kenapa salah -->
1. Sempat kesal dengan DSA, jadi soal ini dikerjakan pelan-pelan dengan **dipandu**.
2. Idenya ditemukan lewat permainan kartu:
   - A `1 2 4`, B `1 3 4`. Di giliran 2 (depan A = 2, depan B = 1) aku ambil `1`, karena **lebih kecil**, supaya tetap urut.
   - Kalau A sudah habis, sisa B **langsung** disambung tanpa membandingkan lagi.
3. Bagian `else` yang aku tulis sendiri salah:
   ```python
   else:
       list1.next = list2.val   # ❌
       tail = tail.next
   ```
   - Yang harus diubah adalah `tail.next` (ujung barisan baru), bukan `list1.next`.
   - `.val` itu **angka**, padahal `next` harus menunjuk **node**. Yang benar `tail.next = list2`.
   - `list2 = list2.next` belum ada, jadi B tidak pernah maju.
   - `tail = tail.next` masuk ke dalam `else`, padahal harus **sejajar dengan `if`/`else`**, supaya jalan setiap putaran.
4. **Kode akhir dituliskan oleh Claude**, lalu dijelaskan baris per baris. Perlu ditulis ulang sendiri saat review.

### Penelusuran per baris: A = `1 → 4`, B = `2 → 3`
Notasi: `D` adalah dummy, `A1` adalah node angka 1 dari A, dan seterusnya.

| Langkah | Baris | Keadaan |
|---|---|---|
| awal | `dummy = ListNode()`, `tail = dummy` | `D`, tail di D; list1 → A1, list2 → B2 |
| P1 | `1 <= 2` True → `tail.next = list1` | `D → A1 → A4` |
| | `list1 = list1.next` | list1 → A4 |
| | `tail = tail.next` | tail di A1 |
| P2 | `4 <= 2` False → `tail.next = list2` | `D → A1 → B2 → B3` (A1 → A4 putus) |
| | `list2 = list2.next` | list2 → B3 |
| | `tail = tail.next` | tail di B2 |
| P3 | `4 <= 3` False → `tail.next = list2` | `D → A1 → B2 → B3` |
| | `list2 = list2.next` | list2 → None (B habis) |
| | `tail = tail.next` | tail di B3 |
| cek | `while`: list2 is None → berhenti | |
| sisa | `list1 is not None` → `tail.next = list1` | `D → A1 → B2 → B3 → A4` |
| hasil | `return dummy.next` | `1 → 2 → 3 → 4` ✓ |

### Penelusuran Example 3: list1 = `[]`, list2 = `[0]`
| Langkah | Baris | Keadaan |
|---|---|---|
| awal | `dummy = ListNode()`, `tail = dummy` | `D`, tail di D; list1 → None, list2 → B0 |
| cek | `while`: `list1 is not None` False → loop **tidak jalan sama sekali** | |
| sisa | `list1 is not None` False → masuk `else`: `tail.next = list2` | `D → B0` |
| hasil | `return dummy.next` | `0` ✓ |

## Kompleksitas
- Waktu: O(n + m) karena setiap node dari kedua list disambung tepat satu kali.
- Memori: O(1) karena tidak membuat node baru selain `dummy`, cuma memindah panah.

## Pelajaran Python
<!-- sintaks atau konsep baru yang dipelajari -->
- **Node dummy**: node palsu di depan supaya barisan baru punya "awal" untuk disambung. Di akhir dibuang dengan `return dummy.next`.
- **`tail`**: penunjuk ujung barisan baru. Setiap kali menyambung node, `tail` digeser ke node itu.
- `.val` adalah **angka**, sedangkan `.next` adalah **panah ke node**. Jangan isi `.next` dengan angka.
- Dua jenis baris yang beda fungsinya:
  - `x.next = ...` **mengubah sambungan**;
  - `x = ...` hanya **menggeser jari**.
- Panah lama yang "nyasar" (misalnya A1 → A4) tidak masalah, karena nanti ditimpa oleh `tail.next = ...`.
- `while a and b`: loop berhenti begitu **salah satu** False.

## Refleksi
- Tingkat kesulitan setelah paham: mudah / sedang / susah
- Bisa ditulis ulang tanpa melihat kode? ya / belum

## Review
| Tanggal | Hasil | Catatan |
|---|---|---|
