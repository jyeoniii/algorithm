# https://leetcode.com/problems/unique-binary-search-trees/

import functools


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1) # dp[i]: unqiue element i개가 있을 때 가능한 BST의 갯수
        dp[0], dp[1] = 1, 1
        for x in range(2, n+1):
            dp[x] = sum(dp[i][x-1-i] for i in range(0, x))
        return dp[n]


class Solution:
    def numTrees(self, n: int) -> int:
        @functools.lru_cache(None)
        def recursive(x: int) -> int:
            if x == 0 or x == 1: return 1
            answer = 0
            for i in range(x):
                answer += recursive(i) * recursive(x-1-i)
            return answer

        return recursive(n)


class Solution:
    def numTrees(self, n: int) -> int:
        @functools.lru_cache(None)
        def recursive(x: int) -> int:
            if x == 0 or x == 1: return 1
            return sum([recursive(i) * recursive(x - 1 - i) for i in range(x)])

        return recursive(n)

