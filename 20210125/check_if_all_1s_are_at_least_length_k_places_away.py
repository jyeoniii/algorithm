# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/#

from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_idx = float("-inf")
        for i, num in enumerate(nums):
            if num == 1:
                if i - last_idx <= k: return False
                else: last_idx = i
        return True