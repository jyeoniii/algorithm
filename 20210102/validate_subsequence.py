# https://www.algoexpert.io/questions/Validate%20Subsequence


# Time: O(n^2), Space: O(n^2)
def isValidSubsequence(array, sequence):
    dp = [[False] * len(sequence) for _ in range(len(array))] # dp[i][j]: sequence[:j+1]가 array[:i+1]의 subsequence
    dp[0][0] = array[0] == sequence[0]
    for x in range(1, len(array)):
        dp[x][0] = dp[x-1][0] or array[x] == sequence[0]

    for j in range(1, len(sequence)):
        for i in range(j, len(array)):
            dp[i][j] = dp[i-1][j] or (dp[i-1][j-1] and array[i] == sequence[j])

    return dp[-1][-1]


# Time: O(n), Space: O(1)
def isValidSubsequence(array, sequence):
    seq_idx = 0
    array_idx = 0
    while seq_idx < len(sequence):
        for i in range(array_idx, len(array)):
            if array[i] == sequence[seq_idx]:
                seq_idx += 1
                array_idx = i+1
                break
        else: return False
    return True
