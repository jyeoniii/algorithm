# https://leetcode.com/problems/missing-ranges/

from typing import List


class Solution:

    def formatRange(self, lower: int, upper: int):
        return str(lower) if lower == upper else f"{lower}->{upper}"

    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if not nums:
            return [self.formatRange(lower, upper)]

        answer = []
        if lower < nums[0]:
            answer.append(self.formatRange(lower, nums[0]-1))

        for i in range(len(nums)-1):
            if nums[i] + 1 != nums[i+1]:
                answer.append(self.formatRange(nums[i]+1, nums[i+1]-1))

        if nums[-1] < upper:
            answer.append(self.formatRange(nums[-1]+1, upper))

        return answer