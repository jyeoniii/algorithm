# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

from typing import List
import heapq
from functools import lru_cache


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        pq, di, dj = [], [-1, 1, 0, 0], [0, 0, -1, 1]
        dp = [[1] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heapq.heappush(pq, (matrix[i][j], i, j))

        answer = 0
        while pq:
            v, i, j = heapq.heappop(pq)
            tmp = dp[i][j]
            for k in range(4):
                new_i, new_j = i + di[k], j + dj[k]
                if 0 <= new_i < len(matrix) and 0 <= new_j < len(matrix[0]) and matrix[new_i][new_j] < matrix[i][j]:
                    dp[i][j] = max(dp[i][j], tmp + dp[new_i][new_j])
            answer = max(answer, dp[i][j])

        return answer


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]

        @lru_cache(None)
        def helper(i: int, j: int):
            result = 0
            for k in range(4):
                new_i, new_j = i + di[k], j + dj[k]
                if 0 <= new_i < len(matrix) and 0 <= new_j < len(matrix[0]) and matrix[new_i][new_j] < matrix[i][j]:
                    result = max(result, helper(i + di[k], j + dj[k]))
            return 1 + result

        return max(helper(i, j) for i in range(len(matrix)) for j in range(len(matrix[0])))
