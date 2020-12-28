# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

from typing import List
from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        M, N = len(grid), len(grid[0])
        di, dj = [0, 0, 1, -1], [-1, 1, 0, 0]
        visited = [set() for _ in range(k+1)] # visited[k][i][j]: k개의 장애물을 삭제했을 때 grid[i][j]의 visit 여부
        q = deque([(0, 0, 0, 0)])

        visited[0].add(0)
        while q:
            i, j, dist, kk = q.popleft()
            if i == M - 1 and j == N - 1:
                return dist
            for x in range(4):
                new_i, new_j = i + di[x], j + dj[x]
                val = new_i * N + new_j
                if 0 <= new_i < M and 0 <= new_j < N:
                    if grid[new_i][new_j] == 0 and val not in visited[kk]:
                        visited[kk].add(val)
                        q.append((new_i, new_j, dist + 1, kk))
                    elif kk < k and grid[new_i][new_j] == 1 and val not in visited[kk+1]:  # eliminate obstacle
                        visited[kk+1].add(val)
                        q.append((new_i, new_j, dist + 1, kk + 1))
        return -1


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        M, N = len(grid), len(grid[0])
        di, dj = [0, 0, 1, -1], [-1, 1, 0, 0]
        visited = {}
        q = deque([(0, 0, 0, 0)])

        visited[(0,0)] = 0
        while q:
            i, j, dist, kk = q.popleft()
            if i == M - 1 and j == N - 1:
                return dist
            for x in range(4):
                new_i, new_j = i + di[x], j + dj[x]
                if 0 <= new_i < M and 0 <= new_j < N:
                    if grid[new_i][new_j] == 0 and ((new_i, new_j) not in visited or visited[(new_i, new_j)] > kk):
                        visited[(new_i, new_j)] = kk
                        q.append((new_i, new_j, dist + 1, kk))
                    elif kk < k and grid[new_i][new_j] == 1 and ((new_i, new_j) not in visited or visited[(new_i, new_j)] > kk+1):  # eliminate obstacle
                        visited[(new_i, new_j)] = kk+1
                        q.append((new_i, new_j, dist + 1, kk + 1))
        return -1