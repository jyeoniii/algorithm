# https://www.algoexpert.io/questions/Number%20Of%20Ways%20To%20Make%20Change


def numberOfWaysToMakeChange(n, denoms):
    dp = [0] * (n + 1)  # dp[x]: numberOfWaysToMakeChange(x)
    dp[0] = 1

    for denom in denoms:
        for x in range(n, -1, -1):
            amount = x - denom
            while amount >= 0:
                dp[x] += dp[amount]
                amount -= denom

    return dp[-1]


def numberOfWaysToMakeChange(n, denoms):
    dp = [0] * (n + 1)  # dp[x]: numberOfWaysToMakeChange(x)
    dp[0] = 1

    for denom in denoms:
        for x in range(1, n + 1):
            if denom <= x:
                dp[x] += dp[x - denom]

    return dp[-1]