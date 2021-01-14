# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3603/

from itertools import accumulate
from typing import List

# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        cum_sum = [0] + list(accumulate(nums))
        d = {s: i for i, s in enumerate(cum_sum)}

        target = cum_sum[-1] - x
        if target < 0: return -1

        answer = float("inf")
        for num in d:
            if num + target in d:
                answer = min(answer, d[num] + len(nums) - d[num + target])

        return answer if answer != float("inf") else -1


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        cum_sum = list(accumulate(nums))
        d = {s: i for i, s in enumerate(cum_sum)}

        target = cum_sum[-1] - x
        if target < 0: return -1

        answer = len(nums)-1-d[target] if target in d else float("inf")
        for num in d:
            if num + target in d:
                answer = min(answer, d[num] + len(nums) - d[num + target])

        return answer if answer != float("inf") else -1

# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0: return -1

        l, answer = 0, float("inf")
        for r in range(len(nums)):
            target -= nums[r]
            while target < 0:
                target += nums[l]
                l += 1

            if target == 0: answer = min(answer, l + len(nums) - 1 - r)

        return answer if answer != float("inf") else -1
