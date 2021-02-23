# https://www.algoexpert.io/questions/Levenshtein%20Distance


def levenshteinDistance(str1, str2):
    M, N = len(str1), len(str2)
    dp = [[0] * (N+1) for _ in range(M+1)]
    for i in range(M+1): dp[i][0] = i
    for j in range(N+1): dp[0][j] = j
    for i in range(1, M+1):
        for j in range(1, N+1):
            dp[i][j] = dp[i-1][j-1] if str1[i-1] == str2[j-1] else 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

    return dp[-1][-1]
