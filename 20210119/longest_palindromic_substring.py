# https://leetcode.com/problems/longest-palindromic-substring/


# TLE
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        dp = [[False] * N for _ in range(N)]

        start, end = 0, 0
        for l in range(0, N):
            for i in range(0, N - l):
                if l > 1: dp[i][i + l] = dp[i + 1][i + l - 1] and s[i] == s[i + l]
                elif l == 1: dp[i][i + 1] = s[i] == s[i + 1]
                else: dp[i][i + l] = True

                if dp[i][i + l]: start, end = i, i + l

        return s[start:end + 1]


# Time Complexity: O(n^2)
# Space Complexity: O(1)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while l - 1 >= 0 and r + 1 < len(s):
                if s[l - 1] != s[r + 1]:
                    break
                else:
                    l -= 1
                    r += 1
            return l, r

        start, end = 0, 0
        for i in range(len(s)):
            l, r = expand(i, i)
            if end - start < r - l:
                start, end = l, r

            if i + 1 < len(s) and s[i] == s[i + 1]:
                l, r = expand(i, i + 1)
                if end - start < r - l:
                    start, end = l, r

        return s[start:end + 1]


