# https://leetcode.com/problems/interleaving-string/

from collections import Counter


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False

        dp = [[False] * (len(s2)+1) for _ in range(len(s1)+1)]  # dp[i][j]: inInterleave(s1[:i], s2[:j]로 s3[:i+j])
        dp[0][0] = True
        for i in range(1, len(s1)+1): dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1, len(s2)+1): dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]

        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                dp[i][j] = (dp[i-1][j] and s3[i+j-1] == s1[i-1]) or (dp[i][j-1] and s3[i+j-1] == s2[j-1])

        return dp[-1][-1]


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if Counter(s1) + Counter(s2) != Counter(s3): return False

        dp = [False] * (len(s2)+1)  # dp[j]: inInterleave(s1[:i], s2[:j]로 s3[:i+j]) at ith iteration
        dp[0] = True
        for j in range(1, len(s2)+1): dp[j] = dp[j-1] and s2[j-1] == s3[j-1]

        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                dp[j] = (dp[j] and s3[i+j-1] == s1[i-1]) or (dp[j-1] and s3[i+j-1] == s2[j-1])

        return dp[-1]



