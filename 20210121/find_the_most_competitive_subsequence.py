# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3611/

from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        attempts = len(nums) - k
        stack = []
        for num in nums:
            while stack and num < stack[-1] and attempts > 0:
                stack.pop()
                attempts -= 1
            stack.append(num)

        return stack[:k]