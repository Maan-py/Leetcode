"""
Soal    : 217. Contains Duplicate
Tanggal : 2026-11-05
Pola    : Hashing (set)
Ide     : Telusuri angka satu per satu, simpan yang sudah dilihat di set.
          Kalau angka sekarang sudah ada di set -> ada duplikat (True).
Buntu   : - Nested loop cek semua pasangan -> TLE. Early return tidak menolong
            di kasus terburuk (semua angka beda, sekitar 1,5 miliar
            perbandingan untuk 54.500 angka).
          - nums.count() di dalam comprehension tetap O(n^2) -> TLE juga.
          - Alternatif: sort lalu cek tetangga, O(n log n) waktu, O(1) memori.
Waktu   : O(n), cek in / add di set rata-rata O(1)
Memori  : O(n), terburuk semua angka masuk set
Status  : Selesai
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # duplicates = [i for i in set(nums) if nums.count(i) > 1]

        # if duplicates != []:
        #     return True
        # else:
        #     return False

        seen = set()
        duplicates = []

        for i in nums:
            if i in seen:
                duplicates.append(i)
            else:
                seen.add(i)

        if duplicates != []:
            return True
        else:
            return False

if __name__ == "__main__":
    s = Solution()
    print(s.containsDuplicate([1, 2, 3, 1]))  # True
    print(s.containsDuplicate([1, 2, 3, 4]))  # False
    print(s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True
    print(s.containsDuplicate([2, 14, 18, 22, 22]))  # True
