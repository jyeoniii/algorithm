# https://leetcode.com/problems/number-of-islands/

from typing import List

class Solution:

    def __init__(self):
        self.di = [-1, 1, 0, 0]
        self.dj = [0, 0, 1, -1]
        self.WATER, self.LAND, self.VISITED = '0', '1', '-1'

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        def dfs(i: int, j: int):
            grid[i][j] = self.VISITED
            for x in range(4):
                new_i = i + self.di[x]
                new_j = j + self.dj[x]
                if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]) and grid[new_i][new_j] == self.LAND:
                    dfs(new_i, new_j)

        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == self.LAND:
                    dfs(i, j)
                    answer += 1

        return answer