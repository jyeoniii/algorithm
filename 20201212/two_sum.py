# https://leetcode.com/problems/two-sum/

from typing import List

# Two Pass
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums): d[num] = i
        for i, num in enumerate(nums):
            if target - num in d and i != d[target-num]:
                return [i, d[target-num]]
        return

# One Pass
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            if target - num in d and i != d[target-num]:
                return [i, d[target-num]]
            d[num] = i
        return
