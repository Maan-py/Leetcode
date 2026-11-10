"""
Soal    : 268. Missing Number
Tanggal : 2026-11-07
Pola    : Cek rentang 0..n
Ide     : Cek tiap angka dari 0 sampai n (range(len(nums) + 1)). Angka
          pertama yang tidak ada di nums adalah jawabannya.
Buntu   : - + 1 di range penting supaya n ikut dicek ([0, 1] -> 2).
Waktu   : O(n^2), not in pada list O(n) untuk tiap angka
Memori  : O(1)
Status  : Selesai. Follow-up O(n) waktu + O(1) memori belum.
"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(0, len(nums) + 1):
            if i not in nums:
                return i


if __name__ == "__main__":
    s = Solution()
    print(s.missingNumber([3, 0, 1]))  # 2
    print(s.missingNumber([0, 1]))  # 2
    print(s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # 8
