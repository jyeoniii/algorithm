# https://leetcode.com/problems/brick-wall/

from typing import List
from collections import defaultdict


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        cnt = defaultdict(int)
        for row in wall:
            pos = 0
            for i in range(len(row) - 1):
                pos += row[i]
                cnt[pos] += 1

        return len(wall) - max(cnt.values(), default=0)
