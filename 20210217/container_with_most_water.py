# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3643/

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        area, l, r = 0, 0, len(height) - 1
        while l < r:
            area = max(area, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]: l += 1
            else: r -= 1

        return area

