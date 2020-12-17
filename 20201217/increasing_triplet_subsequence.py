# https://leetcode.com/problems/increasing-triplet-subsequence/

from typing import List
import bisect


# Use LIS
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        dp = []
        for num in nums:
            idx = bisect.bisect_left(dp, num)
            if idx == len(dp):
                dp.append(num)
                if len(dp) == 3: return True
            else:
                dp[idx] = num

        return False
