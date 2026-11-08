"""
Soal    : 121. Best Time to Buy and Sell Stock
Tanggal : 2026-11-09
Pola    :
Ide     :
Buntu   :
Waktu   : O()
Memori  : O()
Status  : Belum
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # list_profit = []
        # maximum_profit = 0

        # for i in range(len(prices) - 1):
        #     for j in range(i + 1, len(prices)):
        #         list_profit.append(prices[j] - prices[i])

        # maximum_profit = max(list_profit)

        # if(maximum_profit > 0):
        #     return maximum_profit
        # else:
        #     return 0

        cheapest = prices[0]
        highest_profit = 0

        for price in prices:
            cheapest = min(cheapest, price)
            profit_today = price - cheapest
            highest_profit = max(highest_profit, profit_today)
        return highest_profit


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))  # 5
    print(s.maxProfit([7, 6, 4, 3, 1]))  # 0
    print(s.maxProfit([2,4,1]))  # 2

# Hari: 0
# Harga: 7
# Termurah sejauh ini: 7
# Untung kalau jual hari ini: 0
# Untung terbesar sejauh ini: 0
# ────────────────────────────────────────
# Hari: 1
# Harga: 1
# Termurah sejauh ini: 1
# Untung kalau jual hari ini: 0
# Untung terbesar sejauh ini: 0
# ────────────────────────────────────────
# Hari: 2
# Harga: 5
# Termurah sejauh ini: 1
# Untung kalau jual hari ini: 4
# Untung terbesar sejauh ini: 4
# ────────────────────────────────────────
# Hari: 3
# Harga: 3
# Termurah sejauh ini: 1
# Untung kalau jual hari ini: 2
# Untung terbesar sejauh ini: 4
# ────────────────────────────────────────
# Hari: 4
# Harga: 6
# Termurah sejauh ini: 1
# Untung kalau jual hari ini: 5
# Untung terbesar sejauh ini: 5
# ────────────────────────────────────────
# Hari: 5
# Harga: 4
# Termurah sejauh ini: 1
# Untung kalau jual hari ini: 3
# Untung terbesar sejauh ini: 5
