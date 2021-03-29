# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/591/week-4-march-22nd-march-28th/3684/

from typing import List
from collections import deque


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix: return
        M, N = len(matrix), len(matrix[0])
        d = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        def bfs(edges):
            q, result, visited = deque(edges), set(), set(edges)
            while q:
                i, j = q.popleft()
                for di, dj in d:
                    t = (i + di, j + dj)
                    if 0 <= t[0] < M and 0 <= t[1] < N and matrix[i][j] <= matrix[t[0]][t[1]] and t not in visited:
                        q.append(t)
                        visited.add(t)
                    else:
                        result.add((i, j))
            return result

        pacific = bfs([(i, 0) for i in range(M)] + [(0, j) for j in range(N)])
        atlantic = bfs([(i, N - 1) for i in range(M)] + [(M - 1, j) for j in range(N)])

        return [list(x) for x in pacific if x in atlantic]