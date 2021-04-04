# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/593/week-1-april-1st-april-7th/3692/

from typing import List
from collections import Counter


class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        answer, c = -1, Counter(A)
        for x in c:
            if c[x] == 1:
                answer = max(answer, x)
        return answer