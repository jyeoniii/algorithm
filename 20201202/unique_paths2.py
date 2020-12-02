# https://leetcode.com/problems/unique-paths-ii/

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid: return 0

        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(N)] for _ in range(M)]
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(1, M):
            dp[i][0] = 1 if obstacleGrid[i][0] == 0 and dp[i-1][0] == 1 else 0
        for j in range(1, N):
            dp[0][j] = 1 if obstacleGrid[0][j] == 0 and dp[0][j-1] == 1 else 0

        for i in range(1, M):
            for j in range(1, N):
                dp[i][j] = 0 if obstacleGrid[i][j] == 1 else dp[i-1][j] + dp[i][j-1]
        return dp[M-1][N-1]
