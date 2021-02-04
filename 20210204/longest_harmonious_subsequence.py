# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3628/

from typing import List
from collections import defaultdict


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1

        answer = 0
        for i, x in d.items():
            if i - 1 in d:
                answer = max(answer, x + d[i - 1])
        return answer