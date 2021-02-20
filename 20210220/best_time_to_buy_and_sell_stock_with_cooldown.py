# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

from typing import List


"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75942/4-line-Python-solution-52-ms

hold -> nothing -> hold
hold -> sell -> cooldown
not_hold -> buy -> hold
not_hold -> nothing -> not_hold
cooldown -> nothing -> not_hold
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold, not_hold, cooldown = 0, float("-inf"), float("-inf")
        for price in prices:
            hold = max(hold, not_hold - price)
            not_hold = max(not_hold, cooldown)
            cooldown = hold + price

        return max(hold, not_hold, cooldown)