# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/590/week-3-march-15th-march-21st/3674/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold, not_hold = float("-inf"), 0
        for price in prices:
            hold = max(not_hold - price, hold)
            not_hold = max(hold + price - fee, not_hold)
        return max(hold, not_hold)