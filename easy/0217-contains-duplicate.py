"""
Soal    : 217. Contains Duplicate
Tanggal : 2026-11-05
Pola    :
Ide     :
Buntu   :
Waktu   : O()
Memori  : O()
Status  : Belum
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
