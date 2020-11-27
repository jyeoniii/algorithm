# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Binary search

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        def binary_search(start: int, end: int) -> List[int]:
            nonlocal nums, target
            if start == end and nums[start] != target:
                return [-1, -1]

            mid = (start + end) // 2
            if target == nums[mid]:
                tmp1, tmp2 = mid, mid
                while tmp1 >= 0 and nums[tmp1] == target:
                    tmp1 = tmp1 - 1
                while tmp2 < len(nums) and nums[tmp2] == target:
                    tmp2 = tmp2 + 1
                return [tmp1 + 1, tmp2 - 1]
            elif target <= nums[mid]:
                return binary_search(start, mid)
            else:
                return binary_search(mid + 1, end)

        return binary_search(0, len(nums) - 1)
