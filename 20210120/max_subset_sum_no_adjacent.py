# https://www.algoexpert.io/questions/Max%20Subset%20Sum%20No%20Adjacent


def maxSubsetSumNoAdjacent(array):
    if not array: return 0
    elif len(array) == 1: return max(array[i] for i in range(len(array)))

    dp = [0] * len(array)  # dp[i]: ith element까지 봤을 때의 최댓값
    dp[0], dp[1] = array[0], max(array[0], array[1])
    for i in range(2, len(array)):
        dp[i] = max(dp[i-1], dp[i-2] + array[i])

    return dp[-1]


def maxSubsetSumNoAdjacent(array):
    if not array: return 0
    elif len(array) == 1: return array[0]

    second_last, last = array[0], max(array[0], array[1])
    for i in range(2, len(array)):
        max_sum = max(last, second_last + array[i])
        second_last, last = last, max_sum

    return last