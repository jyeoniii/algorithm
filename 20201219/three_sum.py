# https://leetcode.com/problems/3sum/

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        result = []

        nums.sort()
        for i in range(N - 2):
            for j in range(i + 1, N):
                two_sum = nums[i] + nums[j]
                k = bisect.bisect_left(nums, -two_sum, lo=j + 1)
                if k < len(nums) and nums[k] == -two_sum:
                    li = [nums[i], nums[j], nums[k]]
                    if li not in result: result.append(li)
        return result
