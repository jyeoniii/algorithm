# https://leetcode.com/problems/subsets-ii/

from typing import List, Set
from collections import Counter


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        c = Counter(nums)

        def helper(s: Set[int]) -> List[List[int]]:
            if not s: return [[]]
            num = s.pop()
            li = helper(s)
            li.extend([[num] * (cnt+1) + x for x in li for cnt in range(c[num])])
            return li

        return helper(set(c.keys()))