# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/571/week-3-december-15th-december-21st/3571/

from typing import List
import functools


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])

        @functools.lru_cache(None)
        def max_cherries(col1, col2, row) -> int: # 현재 robot1, robot2가 각각 (row, col1), (ro2, col2)에 있을 때의 max cherries
            if row >= N: return 0
            curr_cherries = grid[row][col1] + grid[row][col2]
            after_cherries = []
            for c1 in [col1-1, col1, col1+1]:
                for c2 in [col2-1, col2, col2+1]:
                    if 0 <= c1 < M and c1 < c2 < M:
                        after_cherries.append(max_cherries(c1, c2, row + 1))
            return curr_cherries + max(after_cherries)

        return max_cherries(0, M - 1, 0)
