# https://leetcode.com/problems/number-of-closed-islands/

from typing import List
from collections import deque


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        answer, M, N = 0, len(grid), len(grid[0])
        d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for y in range(1, M - 1):
            for x in range(1, N - 1):
                if grid[y][x] != 0:
                    continue

                grid[y][x] = 1
                q = deque([(y, x)])
                isClosed = True
                while q:
                    i, j = q.popleft()
                    if i == 0 or i == M - 1 or j == 0 or j == N - 1:
                        isClosed = False
                    for di, dj in d:
                        new_i, new_j = i + di, j + dj
                        if 0 <= new_i < M and 0 <= new_j < N and grid[new_i][new_j] == 0:
                            grid[new_i][new_j] = 1
                            q.append((new_i, new_j))

                if isClosed:
                    answer += 1

        return answer
