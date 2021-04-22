# https://leetcode.com/problems/combination-sum-iv/

from typing import List
import functools

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @functools.lru_cache(maxsize=None)
        def recursive(remain: int): # recursive(x): combinationSum4(nums, x)
            return 1 if not remain else sum(recursive(remain - num) for num in nums if remain - num >= 0)

        return recursive(target)


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        nums.sort()
        for x in range(target + 1):
            for num in nums:
                if x - num >= 0:
                    dp[x] += dp[x - num]
                else:
                    break

        return dp[-1]