# https://leetcode.com/problems/ones-and-zeroes/
# 0-1 Knapsac problem

from typing import List


# O(Nmn)
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        if not strs: return 0

        zero_one_counts = [(s.count('0'), s.count('1')) for s in strs]

        # dp[i][m][n]: i번째까지의 str에 대해, 남은 사용 가능한 0, 1의 갯수가 각각 m, n개일때의 subset의 최대 갯수
        dp = [[[0] * (n+1) for _ in range(m+1)] for _ in range(len(strs))]
        for zero_count in range(zero_one_counts[0][0], m+1):
            for one_count in range(zero_one_counts[0][1], n+1):
                dp[0][zero_count][one_count] = 1

        for i in range(1, len(zero_one_counts)):
            zero_count, one_count = zero_one_counts[i]
            for z in range(0, m + 1):
                for o in range(0, n + 1):
                    if z < zero_count or o < one_count:
                        dp[i][z][o] = dp[i-1][z][o]
                    else:
                        dp[i][z][o] = max(dp[i-1][z][o], dp[i-1][z-zero_count][o-one_count] + 1)

        return dp[len(strs)-1][m][n]


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        if not strs: return 0

        # dp[m][n]: 남은 사용 가능한 0, 1의 갯수가 각각 m, n개일때의 subset의 최대 갯수
        dp = [[0] * (n+1) for _ in range(m+1)]
        for str in strs:
            one_count, zero_count = str.count('1'), str.count('0')
            for z in range(m, -1, -1):
                for o in range(n, -1, -1):
                    if z >= zero_count and o >= one_count:
                        dp[z][o] = max(dp[z][o], dp[z-zero_count][o-one_count] + 1)
        return dp[m][n]