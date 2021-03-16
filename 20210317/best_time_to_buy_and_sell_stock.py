# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_price, answer = float("inf"), float("-inf"), 0
        for price in prices:
            if price < min_price:
                min_price, max_price = price, float("-inf")
            elif price > max_price:
                max_price = price
                answer = max(answer, max_price - min_price)

        return answer