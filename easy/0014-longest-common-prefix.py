"""
Soal    : 14. Longest Common Prefix
Tanggal : 2026-11-03
Pola    : Vertical scanning (cek kolom per kolom)
Ide     : Jadikan string pertama patokan. Cek huruf ke-i di semua string lain;
          berhenti kalau ada string yang sudah habis (i >= len(s)) atau hurufnya
          beda. Huruf baru dicatat setelah SEMUA string lolos di kolom itu.
Buntu   : - Memakai i untuk dua hal sekaligus (nomor kolom dan nomor string).
          - Bingung bedanya range(1, len(strs)) (angka) dan strs[1:] (string).
          - append sempat ditaruh di dalam loop dalam, jadi huruf tercatat
            sebelum semua string dicek.
          - Lupa cek string yang lebih pendek -> bisa IndexError.
Waktu   : O(n * m), n = jumlah string, m = panjang string pertama
Memori  : O(m), untuk list hasil
Status  : Selesai (Accepted, 1 ms)
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        hasil = []

        for i in range(len(strs[0])):
            for s in strs[1:]:
                if i >= len(s) or s[i] !=  strs[0][i]:
                    return "".join(hasil)
            hasil.append(strs[0][i])        
        return "".join(hasil)

if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))  # fl
    print(s.longestCommonPrefix(["dog", "racecar", "car"]))  # (kosong)
    print(s.longestCommonPrefix(["abc"]))  # abc
    print(s.longestCommonPrefix(["flower", "flow"]))  # flow
    print(s.longestCommonPrefix(["abc", ""]))  # (kosong)
