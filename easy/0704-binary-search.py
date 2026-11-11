"""
Soal    : 704. Binary Search
Tanggal : 2026-11-11
Pola    : Binary Search (area inklusif left..right)
Ide     : nums sudah terurut, jadi tebak tengahnya lalu buang separuh.
          mid = (left + right) // 2. nums[mid] == target -> return mid;
          terlalu kecil -> left = mid + 1; terlalu besar -> right = mid - 1.
          Area kosong (left > right) -> -1.
Buntu   : - Linear search: while ... or found == False -> IndexError
            (harusnya and); return -1 di dalam while -> selalu -1.
          - Soal minta O(log n), linear search O(n) tidak memenuhi syarat.
          - Kenapa mid +/- 1: mid sudah dicek, ikut dibuang (left = mid
            bisa macet selamanya).
          - Kenapa left <= right: saat left == right masih ada 1 elemen
            yang belum dicek ([5], target 5).
Waktu   : O(log n), tiap putaran area tinggal separuh
Memori  : O(1), hanya left, right, mid
Status  : Selesai
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
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

        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.search([-1, 0, 3, 5, 9, 12], 9))  # 4
    print(s.search([-1, 0, 3, 5, 9, 12], 2))  # -1
