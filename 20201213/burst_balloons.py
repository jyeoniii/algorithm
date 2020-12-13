# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3564/

from typing import List
from functools import lru_cache

# https://leetcode.com/problems/burst-balloons/discuss/970727/Python-5-lines-dp-explained
# dp[i][j]: the maximum number of coins we can get, popping balls from i to j, not including i and j
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        A = [1] + nums + [1]

        @lru_cache(None)
        def dfs(i, j):
            return max([A[i] * A[k] * A[j] + dfs(i, k) + dfs(k, j) for k in range(i + 1, j)] or [0])

        return dfs(0, len(A) - 1)
