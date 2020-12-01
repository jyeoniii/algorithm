# https://leetcode.com/problems/spiral-matrix-ii/

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        i, j = 0, 0
        di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
        dir_idx, count = 0, 0
        while count < n * n:
            count += 1
            matrix[i][j] = count
            if i + di[dir_idx] not in range(0, n) or j + dj[dir_idx] not in range(0, n) or matrix[i+di[dir_idx]][j+dj[dir_idx]] != 0:
                dir_idx = (dir_idx + 1) % 4

            i = i + di[dir_idx]
            j = j + dj[dir_idx]

        return matrix