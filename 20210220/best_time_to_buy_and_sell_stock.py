# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack, answer = [], 0
        for price in prices:
            if stack and stack[-1] > price:
                answer = max(answer, stack[-1] - stack[0])
            while stack and stack[-1] > price:
                stack.pop()
            stack.append(price)

        if stack: answer = max(answer, stack[-1] - stack[0])
        return answer


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_price, answer = float("inf"), float("-inf"), 0
        for price in prices:
            if price < min_price:
                answer = max(answer, max_price - min_price)
                min_price, max_price = price, float("-inf")
            elif price > max_price:
                max_price = price
                answer = max(answer, max_price - min_price)

        return answer
