# https://leetcode.com/problems/distinct-subsequences/submissions/


# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        M, N = len(s), len(t)
        if M < N: return 0

        dp = [[0] * N for _ in range(M)]  # dp[i][j]: number of ds of s[:i] and t[:j]
        dp[0][0] = 1 if s[0] == t[0] else 0
        for i in range(1, M):
            dp[i][0] = dp[i - 1][0] + (1 if s[i] == t[0] else 0)

        for i in range(1, M):
            for j in range(1, min(i + 1, N)):
                dp[i][j] = dp[i - 1][j] + (dp[i - 1][j - 1] if s[i] == t[j] else 0)

        return dp[-1][-1]


# Time Complexity: O(n^2)
# Space Complexity: O(n)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        M, N = len(s), len(t)
        if M < N: return 0

        dp = [0] * N  # dp[j]: number of subsequece=t[:j] in s
        for i in range(0, M):
            for j in range(min(N-1, i), -1, -1):
                dp[j] += 0 if s[i] != t[j] else (1 if j == 0 else dp[j-1])

        return dp[-1]