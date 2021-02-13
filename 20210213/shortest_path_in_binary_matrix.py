# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3638/

from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1: return -1
        grid[0][0] = -1

        di, dj = [0, 1, 1, 1, -1, 0, -1, -1], [1, 0, -1, 1, 1, -1, 0, -1]
        q = deque([(0, 0, 1)])
        while q:
            i, j, dist = q.popleft()
            if i == len(grid) - 1 and j == len(grid[0]) - 1: return dist

            for k in range(8):
                new_i, new_j = i + di[k], j + dj[k]
                if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]) and grid[new_i][new_j] == 0:
                    grid[new_i][new_j] = -1
                    q.append((new_i, new_j, dist + 1))

        return -1
