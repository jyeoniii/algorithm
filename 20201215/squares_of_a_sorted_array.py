# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge

from typing import List
import bisect

# O(nlogn)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(x * x for x in nums)

# Two Pointer Approach
# O(n)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = bisect.bisect_left(nums, 0)
        if i == 0:
            return [x * x for x in nums]
        elif i == len(nums):
            return reversed([x * x for x in nums])
        else:
            result = []
            left, right = i-1, i
            while left >= 0 and right < len(nums):
                if abs(nums[left]) < abs(nums[right]):
                    result.append(nums[left] * nums[left])
                    left -= 1
                else:
                    result.append(nums[right] * nums[right])
                    right += 1
            while left >= 0:
                result.append(nums[left] * nums[left])
                left -= 1
            while right < len(nums):
                result.append(nums[right] * nums[right])
                right += 1
            return result

