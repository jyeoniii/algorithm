# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3617/

from typing import List
import heapq


# Dijkstra Algorithm
# Time Complexity: O(ElogV) = O(MNlogMN)
class Solution:

    def minimumEffortPath(self, height: List[List[int]]) -> int:
        M, N, diff = len(height), len(height[0]), [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dist = [[float("inf")] * N for _ in range(M)]
        dist[0][0] = 0
        h = [(0, 0, 0)]  # cost, i, j
        while h:
            c, i, j = heapq.heappop(h)
            if i == M - 1 and j == N - 1: break

            for di, dj in diff:
                if 0 <= i + di < M and 0 <= j + dj < N:
                    cost = max(c, abs(height[i][j] - height[i + di][j + dj]))
                    if dist[i + di][j + dj] > cost:
                        dist[i + di][j + dj] = cost
                        heapq.heappush(h, (cost, i + di, j + dj))

        return dist[-1][-1]