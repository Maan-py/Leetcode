"""
Soal    : 125. Valid Palindrome
Tanggal : 2026-11-08
Pola    :
Ide     :
Buntu   :
Waktu   : O()
Memori  : O()
Status  : Belum
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
