# https://leetcode.com/problems/longest-increasing-subsequence/

from typing import List
import bisect


# O(n^2)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums) # dp[i]: nums[i]를 마지막 수로 가지는, LIS의 길이
        answer = 0
        for i, n in enumerate(nums):
            dp[i] = 1
            for j in range(i-1, -1, -1):
                if nums[j] < n:
                    dp[i] = max(dp[i], dp[j]+1)
            answer = max(answer, dp[i])
        return answer

# https://leetcode.com/problems/longest-increasing-subsequence/discuss/901573/O(n-log-n)-Solution-in-Python
# Time Complexity: O(nlogn)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for num in nums:
            i = bisect.bisect_left(dp, num)
            if i == len(dp):
                dp.append(num)
            else:
                dp[i] = num

        return len(dp)
    