"""
Soal    : 125. Valid Palindrome
Tanggal : 2026-11-08
Pola    : Two Pointers (indeks kiri i, kanan len(res) - 1 - i)
Ide     : Bersihkan dulu: hanya huruf/angka (isalnum), lalu lower().
          Bandingkan res[i] dengan res[len(res) - 1 - i]. Ada yang beda ->
          bukan palindrom.
Buntu   : - Nested loop (for i in res / for j in res[::-1]) membandingkan
            SEMUA pasangan (21 x 21), padahal tiap huruf cuma punya 1 pasangan.
          - Menulis pasangan indeks manual (0->20, 1->19, ...) -> jumlahnya
            selalu len(res) - 1, jadi kanan = len(res) - 1 - i.
          - Two Pointers itu dua variabel indeks, bukan linked list.
          - Bisa dirapikan: loop cukup setengah, langsung return False.
Waktu   : O(n), membersihkan string + satu loop
Memori  : O(n), string res dan list output
Status  : Selesai
"""

from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        output = []
        res = "".join([char for char in s if char.isalnum()]).lower()

        for i in range(len(res)):
            kanan = len(res) - 1 - i
            if res[i] == res[kanan]:
                output.append(True)
            else:
                output.append(False)

        if False in output:
            return False
        else:
            return True

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))  # True
    print(s.isPalindrome("race a car"))  # False
    print(s.isPalindrome(" "))  # True
