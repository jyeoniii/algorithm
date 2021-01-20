# https://www.algoexpert.io/questions/Knapsack%20Problem


def knapsackProblem(items, capacity):
    dp = [[0, []] for _ in range(capacity+1)]  # dp[i]: capacity가 i 이하인 경우의 answer

    for i, (value, weight) in enumerate(items):
        for w in range(capacity, -1, -1):
            if w - weight < 0: continue
            if dp[w-weight][0] + value > dp[w][0]:
                dp[w][0] = dp[w-weight][0] + value
                dp[w][1] = dp[w-weight][1][:]
                dp[w][1].append(i)

    return dp[-1]


