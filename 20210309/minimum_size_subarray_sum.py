# https://leetcode.com/problems/minimum-size-subarray-sum/

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        answer, l, curr_sum = float("inf"), 0, 0
        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum >= target:
                answer = min(answer, r-l+1)
                curr_sum -= nums[l]
                l += 1
        return answer if answer != float("inf") else 0