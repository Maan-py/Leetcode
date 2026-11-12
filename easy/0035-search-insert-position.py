"""
Soal    : 35. Search Insert Position
Tanggal : 2026-11-12
Pola    : Binary Search (area inklusif, return left)
Ide     : Kode 0704 dipakai lagi, hanya return -1 diganti return left.
          Saat loop berhenti (left > right), left berdiri tepat di angka
          pertama yang lebih besar dari target = posisi sisip.
Buntu   : - Bingung mencari idenya. Telusuri Example 2 dengan tangan:
            loop berhenti di left=1, right=0, dan jawabannya 1 = left.
          - Cek ulang di Example 3: berhenti di left=4 = jawabannya.
          - Kenapa left: left hanya melompati angka yang < target,
            right hanya melompati angka yang > target.
Waktu   : O(log n), tiap putaran area tinggal separuh
Memori  : O(1), hanya left, right, mid
Status  : Selesai
"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid

            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return left

if __name__ == "__main__":
    s = Solution()
    print(s.searchInsert([1, 3, 5, 6], 5))  # 2
    print(s.searchInsert([1, 3, 5, 6], 2))  # 1
    print(s.searchInsert([1, 3, 5, 6], 7))  # 4

# 0  1  2  3
# 1, 3, 5, 6 -> 0 <= 3 -> mid = (0+3) // 2 = 1 -> 7 != 3 -> 7 > 3 -> left = 1 + 1 = 2
