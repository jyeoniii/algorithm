# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/593/week-1-april-1st-april-7th/3694/

from typing import List
from collections import Counter

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counters = [Counter(s) for s in strs]
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # dp[m][n]: findMaxForm(strs, m, n) on ith iteration
        for i in range(len(strs)):
            one, zero = counters[i]['1'], counters[i]['0']
            for mm in range(m, zero - 1, -1):
                for nn in range(n, one - 1, -1):
                    dp[mm][nn] = max(dp[mm][nn], dp[mm - zero][nn - one] + 1)

        return dp[-1][-1]

