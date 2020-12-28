# https://leetcode.com/problems/last-stone-weight/

from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while stones:
            y = heapq.heappop(stones)
            if not stones: return -y
            x = heapq.heappop(stones)

            if x != y:
                heapq.heappush(stones, y - x)
        return 0

