# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3565/

from typing import List
import functools

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        dp = [[False] * N for _ in range(N)]

        for i in range(N):
            dp[i][i] = True
        for i in range(N - 1):
            dp[i][i + 1] = s[i] == s[i + 1]

        for i in range(N - 1, -1, -1):
            for j in range(i + 2, N):
                dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]

        @functools.lru_cache(None)
        def dfs(i: int) -> List[List[str]]: # dfs(i): s[i:]에서 찾을 수 있는 모든 palindrome 조합
            answer = []
            for x in range(i, N):
                if dp[i][x]:
                    p = [s[i:x+1]]
                    next_palindromes = dfs(x+1)
                    if next_palindromes:
                        for li in next_palindromes:
                            tmp = p + li
                            answer.append(tmp)
                    else:
                        answer.append(p)
            return answer

        return dfs(0)


class Solution:
    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]

    def partition(self, s: str) -> List[List[str]]:
        result = []

        def dfs(s: str, partitions: List[str]):
            if not s:
                result.append(partitions[:])
                return

            for i in range(len(s)):
                pre, post = s[:i+1], s[i+1:]
                if self.is_palindrome(pre):
                    dfs(post, partitions + [pre])

        dfs(s, [])
        return result
