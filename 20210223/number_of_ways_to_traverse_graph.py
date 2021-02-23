# https://www.algoexpert.io/questions/Number%20Of%20Ways%20To%20Traverse%20Graph


def numberOfWaysToTraverseGraph(width, height):
    dp = [[0] * width for _ in range(height)]
    for i in range(height): dp[i][0] = 1
    for j in range(width): dp[0][j] = 1
    for j in range(1, width):
        for i in range(1, height):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[-1][-1]
