"""
Soal    : 242. Valid Anagram
Tanggal : 2026-11-06
Pola    :
Ide     :
Buntu   :
Waktu   : O()
Memori  : O()
Status  : Belum
"""

from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        output = []
        huruf_t = []

        for j in range(len(t)):
            huruf_t.append(t[j])

        for huruf in s:
            # for j in range(len(huruf_t)):
            if huruf in huruf_t:
                huruf_t.remove(huruf)
                # print(huruf_t)
                # output.append(True)
            else:
                # output.append(False)
                return False

        if huruf_t == []:
            return True
        else:
            return False
            # return output

            # # if huruf_s[i] in huruf_t:
            # #     huruf_s.remove(s[i])
            # #     output.append(True)
            # #     print(huruf_s)
            # #     break
            # else:
            #     output.append(False)
            #     # break
        # return output
        # print(huruf_s)
        # print(huruf_t)
        # print(huruf_s)
        # for i in range(len(output)):
        #     if (output[`i]) == True:
        #         jumlah += 1
        # # print(jumlah)
        # if jumlah == len(s) and len(s) == len(t):
        #     return True
        # elif jumlah != len(s) and len(s) == len(t):
        #     return False
        # elif len(s) != len(t):
        #     return False


if __name__ == "__main__":
    s = Solution()
    print(s.isAnagram("anagram", "nagaram"))  # True
    print(s.isAnagram("rat", "car"))  # False
    print(s.isAnagram("a", "ab"))  # False
    print(s.isAnagram("ab", "a"))  # False
    print(s.isAnagram("aacc", "ccac"))  # False
