# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3652/

from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        min_idx, max_idx, max_val = float("inf"), float("-inf"), float("-inf")
        stack = []
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] > num:
                idx = stack.pop()
                min_idx = min(min_idx, idx)
                max_val = max(max_val, nums[idx])

            if num < max_val: max_idx = i
            stack.append(i)

        return 0 if len(stack) == len(nums) else max_idx - min_idx + 1