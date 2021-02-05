# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def helper(l: int, r: int):
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target or nums[l] == target or nums[r] == target: return True
                if nums[l] <= nums[mid]:  # nums[l:mid] is sorted
                    return helper(l, mid - 1) or helper(mid + 1, r)
                else:  # nums[mid+1:r+1] is sorted
                    return helper(mid + 1, r) or helper(l, mid - 1)

        return helper(0, len(nums) - 1)


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target: return True
            while l < mid and nums[l] == nums[mid]: l += 1
            if nums[mid] < nums[l]:
                if nums[mid] < target <= nums[r]: l = mid + 1
                else: r = mid - 1
            else:
                if nums[l] <= target < nums[mid]: r = mid - 1
                else: l = mid + 1

        return False