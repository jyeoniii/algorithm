# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = 0
        for i, num in enumerate(nums):
            if num == target: return i
            if nums[i - 1] > nums[i]:
                pivot = i
                break

        arr = nums[pivot:] + nums[:pivot]
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] == target: return (mid + pivot) % len(arr)
            elif arr[mid] < target: lo = mid + 1
            else: hi = mid

        return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target: return mid
            if nums[lo] <= nums[mid]: # nums[lo:mid+1] is sorted
                if nums[lo] <= target < nums[mid]: hi = mid-1
                else: lo = mid+1
            else: # nums[mid:hi+1] is sorted
                if nums[mid] < target <= nums[hi]: lo = mid+1
                else: hi = mid-1

        return -1

