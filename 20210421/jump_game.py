# https://leetcode.com/problems/jump-game/

from typing import List


# O(n^2), TLE
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True
        for i in range(len(nums) - 1, -1, -1):
            for step in range(min(nums[i] + 1, len(nums) - i)):
                if dp[i + step]:
                    dp[i] = True
                    break

        return dp[0]


# O(n)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        answer, last_idx = False, len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i < last_idx <= i + nums[i]:
                last_idx = i

        return last_idx <= nums[0]