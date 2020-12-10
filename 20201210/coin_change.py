# https://leetcode.com/problems/coin-change/

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0

        num_coins = len(coins)
        max_val = float("inf")
        dp = [[max_val] * (amount + 1) for _ in range(num_coins)]  # dp[i][c]: i번째 coin까지만 사용했을 때 c를 만들 수 있는 최소 갯수

        for i in range(num_coins):
            if coins[i] <= amount: dp[i][coins[i]] = 1

        for i in range(num_coins):
            coin = coins[i]
            for x in range(amount + 1):
                if x == coin: continue
                dp[i][x] = min(dp[i - 1][x], dp[i][x - coin] + 1) if x-coin >= 0 else dp[i - 1][x]

        return dp[-1][-1] if dp[-1][-1] < max_val else -1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0

        max_val = float("inf")
        dp = [max_val] * (amount + 1) # dp[c]: c를 만들 수 있는 최소 갯수

        for coin in coins:
            if coin <= amount: dp[coin] = 1

        for coin in coins:
            for x in range(amount + 1):
                dp[x] = min(dp[x], dp[x-coin]+1) if x - coin >= 0 else dp[x]

        return dp[-1] if dp[-1] < max_val else -1