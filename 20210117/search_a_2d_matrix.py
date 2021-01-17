# https://leetcode.com/problems/search-a-2d-matrix/

from typing import List
import bisect


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = bisect.bisect_right([row[0] for row in matrix], target) - 1
        if i < 0: return False

        j = bisect.bisect_left(matrix[i], target)
        return j < len(matrix[0]) and matrix[i][j] == target


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo, hi = 0, len(matrix)-1
        while lo <= hi:
            mid = (lo + hi) // 2
            if matrix[mid][0] == target: return True
            elif matrix[mid][0] < target: lo = mid + 1
            else: hi = mid - 1
        if lo == 0: return False

        row = matrix[lo - 1]
        lo, hi = 0, len(matrix[0])-1
        while lo <= hi:
            mid = (lo + hi) // 2
            if row[mid] == target: return True
            elif row[mid] < target: lo = mid + 1
            else: hi = mid - 1

        return lo < len(matrix[0]) and row[lo] == target