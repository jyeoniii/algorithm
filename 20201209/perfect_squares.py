# https://leetcode.com/problems/perfect-squares/
import functools


class Solution:
    @functools.lru_cache(None)
    def numSquares(self, n: int) -> int:
        if n == 0: return 0

        sqrt = int(n ** (0.5))
        if sqrt * sqrt == n: return 1
        return min(self.numSquares(n - x * x) + 1 for x in range(sqrt, 0, -1))


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)

        def recursive(x: int) -> int:
            if x == 0:
                return 0
            elif dp[x] != 0:
                return dp[x]

            sqrt = int(x ** (0.5))
            if sqrt == x ** (0.5): return 1
            dp[x] = min(recursive(x - i * i) + 1 for i in range(sqrt, 0, -1))

            return dp[x]

        return recursive(n)
