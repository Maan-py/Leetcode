"""
Soal    : 1. Two Sum
Tanggal : 2026-11-04
Pola    : Brute force (nested loop, cek semua pasangan)
Ide     : Untuk setiap angka di indeks i, pasangkan dengan setiap angka SETELAHNYA
          (j mulai dari i + 1). Kalau nums[i] + nums[j] == target, return [i, j].
          Mulai dari i + 1 supaya tidak ada pasangan dobel dan indeks yang sama
          tidak dipakai dua kali.
Buntu   : - Yang di-return itu indeks, bukan angkanya.
          - "Tidak boleh pakai elemen yang sama dua kali" = indeks yang sama,
            bukan angka yang sama ([3, 3] tetap boleh).
          - return i, j menghasilkan tuple (i, j), bukan list -> pakai [i, j].
          - Cara menghitung Big-O dari loop bersarang.
Waktu   : O(n²), cek semua pasangan (sekitar n²/2)
Memori  : O(1), hanya i dan j
Status  : Selesai (brute force). Versi lebih cepat (hash map) belum.
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))  # [0, 1]
    print(s.twoSum([3, 2, 4], 6))  # [1, 2]
    print(s.twoSum([3, 3], 6))  # [0, 1]
    print(s.twoSum([1, 5, 3, 8], 11))  # [2, 3]
