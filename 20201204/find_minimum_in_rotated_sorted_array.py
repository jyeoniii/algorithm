# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

from typing import List


class Solution:

    def findMin(self, nums: List[int]) -> int:
        prev = float("-inf")
        for num in nums:
            if prev > num: return num
            prev = num
        return nums[0]