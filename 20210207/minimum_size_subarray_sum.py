# https://leetcode.com/problems/minimum-size-subarray-sum/

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r, curr_sum, answer = 0, 0, 0, float("inf")
        while r < len(nums):
            if curr_sum >= target:
                answer = min(answer, r - l)
                curr_sum -= nums[l]
                l += 1
            else:
                curr_sum += nums[r]
                r += 1

        while l < len(nums) and curr_sum >= target:
            answer = min(answer, r - l)
            curr_sum -= nums[l]
            l += 1

        return answer if answer < float("inf") else 0


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, curr_sum, answer = 0, 0, float("inf")

        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum >= target:
                answer = min(answer, r-l+1)
                curr_sum -= nums[l]
                l += 1

        return answer if answer < float("inf") else 0