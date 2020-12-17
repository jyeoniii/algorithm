# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/571/week-3-december-15th-december-21st/3569/

from typing import List
from collections import defaultdict

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        sum1, sum2 = defaultdict(int), defaultdict(int)
        for i in range(len(A)):
            for j in range(len(B)):
                sum1[A[i] + B[j]] += 1

        for i in range(len(C)):
            for j in range(len(D)):
                sum2[C[i] + D[j]] += 1

        return sum(cnt1 * sum2[-x] for x, cnt1 in sum1.items() if -x in sum2)


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        s = defaultdict(int)
        for x in A:
            for y in B:
                s[x+y] += 1

        return sum(s[-(x+y)] for x in C for y in D if -(x+y) in s)

