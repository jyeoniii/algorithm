# https://leetcode.com/problems/maximum-subarray/

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer = nums[0]
        prevMax = nums[0]
        for i in range(1, len(nums)):
            prevMax = max(nums[i], prevMax + nums[i])
            answer = max(answer, prevMax)
        return answer
