# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/573/week-5-december-29th-december-31st/3587/

from typing import List
import heapq
from collections import deque


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights: return 0

        h = []
        for i, x in enumerate(heights): heapq.heappush(h, (x, i))

        intervals = deque([(0, len(heights) - 1)])
        max_area = 0

        while intervals:
            start, end = intervals.popleft()

            if start <= h[0][1] <= end:
                height, i = heapq.heappop(h)
                max_area = max(max_area, (end - start + 1) * height)
                if start <= i - 1: intervals.append((start, i - 1))
                if i + 1 <= end: intervals.append((i + 1, end))
            else:
                intervals.append((start, end))

        return max_area


# Divide and conquer, but TLE
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights: return 0

        def helper(start: int, end: int) -> int:
            if start > end:
                return 0
            elif start == end:
                return heights[start]
            min_idx, min_height = float("inf"), float("inf")

            for i in range(start, end + 1):
                if heights[i] < min_height:
                    min_idx, min_height = i, heights[i]
            return max((end - start + 1) * min_height, helper(start, min_idx - 1), helper(min_idx + 1, end))

        return helper(0, len(heights) - 1)


# Monotone Stack
class Solution:
    def largestRectangleArea(self, heights):
        stack, max_area = [], 0
        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] >= h:
                height = heights[stack.pop()]
                width = i if not stack else i-stack[-1]-1
                max_area = max(max_area, height*width)
            stack.append(i)
        return max_area