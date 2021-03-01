# https://leetcode.com/problems/triangle/

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j, x in enumerate(triangle[i]):
                dp[j] = min(dp[j], dp[j + 1]) + x

        return dp[0]