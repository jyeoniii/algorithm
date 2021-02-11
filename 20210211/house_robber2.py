# https://leetcode.com/problems/house-robber-ii/

from typing import List
from collections import deque


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3: return max(nums)

        answer = max(nums[0], nums[1])
        x1, x2, x3 = float("-inf"), nums[0], 0
        for i in range(2, len(nums) - 1):
            x1, x2, x3 = x2, x3, max(x1, x2) + nums[i]
            answer = max(answer, x3)

        x1, x2, x3 = float("-inf"), 0, nums[1]
        for i in range(2, len(nums)):
            x1, x2, x3 = x2, x3, max(x1, x2) + nums[i]
            answer = max(answer, x3)

        return answer


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3: return max(nums)

        answer = max(nums[0], nums[1])
        dp = deque([float("-inf"), nums[0], 0])
        for i in range(2, len(nums) - 1):
            x = dp.popleft()
            dp.append(max(x, dp[0]) + nums[i])
            answer = max(answer, dp[-1])

        dp = deque([float("-inf"), 0, nums[1]])
        for i in range(2, len(nums)):
            x = dp.popleft()
            dp.append(max(x, dp[0]) + nums[i])
            answer = max(answer, dp[-1])

        return answer