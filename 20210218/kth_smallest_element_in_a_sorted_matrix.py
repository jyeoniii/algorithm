# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

from typing import List
import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        h, cnt = [(matrix[0][0], 0, 0)], 0
        matrix[0][0] = visited = float("inf")
        while h:
            val, i, j = heapq.heappop(h)
            cnt += 1
            if k == cnt: return val

            if i + 1 < len(matrix) and matrix[i + 1][j] != visited:
                heapq.heappush(h, (matrix[i + 1][j], i + 1, j))
                matrix[i + 1][j] = visited
            if j + 1 < len(matrix[0]) and matrix[i][j + 1] != visited:
                heapq.heappush(h, (matrix[i][j + 1], i, j + 1))
                matrix[i][j + 1] = visited


