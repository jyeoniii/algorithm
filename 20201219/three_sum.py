# https://leetcode.com/problems/3sum/

from typing import List

# Backtracking - Time Limit Exceeded
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(idx: int, curr: List[int]):
            if len(curr) == 3:
                if sum(curr) == 0:
                    sorted_curr = sorted(curr)
                    if sorted_curr not in result:
                        result.append(sorted_curr)
                return

            for i in range(idx, len(nums)+len(curr)-2):
                curr.append(nums[i])
                dfs(i+1, curr)
                curr.pop()

        dfs(0, [])
        return result

import bisect

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        result = set()

        nums.sort()
        for i in range(N - 2):
            for j in range(i + 1, N):
                two_sum = nums[i] + nums[j]
                k = bisect.bisect_left(nums, -two_sum, lo=j + 1)
                if k < len(nums) and nums[k] == -two_sum:
                    li = (nums[i], nums[j], nums[k])
                    result.add(li)
        return list(result)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        result = []
        lookup = {num: idx for idx, num in enumerate(nums)}

        for i in range(N - 2):
            for j in range(i + 1, N):
                two_sum = nums[i] + nums[j]
                if -two_sum in lookup and lookup[-two_sum] > j:
                    comb = sorted((nums[i], nums[j], -two_sum))
                    if comb not in result: result.append(comb)
        return result


# Fastest
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        lookup = {num: idx for idx, num in enumerate(nums)}

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]: continue
            for j in range(i + 1, len(nums) - 1):
                if j > i+1 and nums[j] == nums[j-1]: continue
                two_sum = nums[i] + nums[j]
                if -two_sum in lookup and lookup[-two_sum] > j:
                    result.append([nums[i], nums[j], -two_sum])

        return result