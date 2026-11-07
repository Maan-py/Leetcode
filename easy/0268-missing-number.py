"""
Soal    : 268. Missing Number
Tanggal : 2026-11-07
Pola    :
Ide     :
Buntu   :
Waktu   : O()
Memori  : O()
Status  : Belum
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
