# https://leetcode.com/problems/different-ways-to-add-parentheses/

from typing import List
from functools import lru_cache


class Solution:
    @lru_cache(None)
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isnumeric(): return [int(input)]
        res = []
        for i, c in enumerate(input):
            if c in "+-*":
                res += [l + r if c == "+" else l - r if c == "-" else l * r
                        for l in self.diffWaysToCompute(input[:i])
                        for r in self.diffWaysToCompute(input[i + 1:])]
        return res


class Solution:
    @lru_cache(None)
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isnumeric(): return [int(input)]
        return [l + r if c == "+" else l - r if c == "-" else l * r
                for i, c in enumerate(input) if c in "+-*"
                for l in self.diffWaysToCompute(input[:i])
                for r in self.diffWaysToCompute(input[i + 1:])]
