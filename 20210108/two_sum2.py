# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {num: i for i, num in enumerate(numbers)}

        for i, num in enumerate(numbers):
            if target - num in d and d[target - num] != i:
                return [i + 1, d[target - num] + 1]


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while l < r:
            sum = numbers[l] + numbers[r]
            if sum < target: l += 1
            elif sum > target: r -=1
            else: return [l+1, r+1]