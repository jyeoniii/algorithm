# https://leetcode.com/problems/single-number-ii/submissions/

from typing import List
from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        for num in c:
            if c[num] == 1: return num


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (sum(set(nums)) * 3 - sum(nums)) // 2
