# https://leetcode.com/problems/search-a-2d-matrix-ii/

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = 0, len(matrix[0]) - 1
        while c >= 0 and r < len(matrix):
            if matrix[r][c] == target: return True
            elif matrix[r][c] > target: c -= 1
            elif matrix[r][c] < target: r += 1
        return False

