"""
Soal    : 20. Valid Parentheses
Tanggal : 2026-11-10
Pola    : Stack (list sebagai tumpukan kurung buka)
Ide     : Baca s dari kiri. Kurung buka -> append ke note. Kurung tutup ->
          bandingkan dengan note[-1] (kurung yang terakhir dibuka) lewat
          dictionary pair {tutup: buka}. Cocok -> pop, tidak cocok -> False.
          Di akhir, note harus kosong (semua sudah ditutup).
Buntu   : - Menghitung jumlah kurung saja tidak cukup: "([)]" lolos hitungan
            padahal salah. Yang perlu diingat itu URUTAN, bukan jumlah.
          - Bingung: i (karakter yang dibaca, bisa buka/tutup) beda dengan
            note (hanya berisi kurung buka).
          - KeyError '(': dua if terpisah, jadi kurung buka ikut dicari di
            pair. Solusi: pakai else.
          - note kosong saat ada kurung tutup (")") -> cek note == [] dulu
            sebelum note[-1].
Waktu   : O(n), setiap karakter dibaca sekali; append/pop/[-1]/dict O(1)
Memori  : O(n), terburuk semua kurung buka masuk ke note
Status  : Selesai
"""

from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        pair = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        note = []

        for i in s:
            if i == "(" or i == "[" or i == "{":
                note.append(i)
            else:
                if note == []:
                    return False
                if note[-1] == pair[i]:
                    note.pop()
                else:
                    return False

        if note == []:
            return True
        else:
            return False

if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()"))  # True
    print(s.isValid("()[]{}"))  # True
    print(s.isValid("(]"))  # False
    print(s.isValid("([])"))  # True
    print(s.isValid("([)]"))  # False

# karakter :  (   )   (   )
# hitungan :  1   0   1
