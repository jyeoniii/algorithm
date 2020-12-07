# https://leetcode.com/problems/partition-equal-subset-sum/

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0: return False
        target = s // 2
        dp = [[False] * (target+1) for _ in range(len(nums))] # dp[i][s]: dp[:i+1]에 sum == s 인 subset이 있다

        for i, num in enumerate(nums):
            if num > target: return False
            dp[i][num] = True

        for i in range(1, len(nums)):
            for s in range(target+1):
                dp[i][s] = dp[i-1][s] or dp[i-1][s-nums[i]]

        return dp[-1][-1]

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0: return False
        target = s // 2
        dp = [False] * (target+1) # dp[s]: sum == s 인 subset이 있다

        for num in nums:
            for s in range(target, -1, -1):
                dp[s] = True if s == num else dp[s] or (s-num >= 0 and dp[s-num])

        return dp[-1]