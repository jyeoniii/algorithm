# https://www.algoexpert.io/questions/Min%20Number%20Of%20Coins%20For%20Change


def minNumberOfCoinsForChange(n, denoms):
    dp = [[float("inf")] * (n + 1) for _ in range(len(denoms))]
    for x in range(n + 1):
        dp[0][x] = x // denoms[0] if x % denoms[0] == 0 else float("inf")

    for i in range(1, len(denoms)):
        for j in range(n + 1):
            cnt = 0
            while j - cnt * denoms[i] >= 0:
                dp[i][j] = min(dp[i - 1][j - cnt * denoms[i]] + cnt, dp[i][j])
                cnt += 1

    return dp[-1][-1] if dp[-1][-1] != float("inf") else -1


def minNumberOfCoinsForChange(n, denoms):
    dp = [float("inf")] * (n + 1)
    dp[0] = 0

    for coin in denoms:
        for amount in range(n + 1):
            if coin <= amount:
                dp[amount] = min(dp[amount - coin] + 1, dp[amount])

    return dp[-1] if dp[-1] != float("inf") else -1