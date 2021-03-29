# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/591/week-4-march-22nd-march-28th/3685/

from typing import List
from collections import Counter
import functools


# TLE
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        B = set(B)
        @functools.lru_cache(None)
        def isSubset(a, b):  # b is subset of a
            ca, cb = Counter(a), Counter(b)
            return all(c in ca and ca[c] >= cnt for c, cnt in cb.items())

        return [a for a in A if all(isSubset(a, b) for b in B)]


# https://leetcode.com/problems/word-subsets/discuss/1128187/Python-Simple-counter-solution-explained
class Solution:
    def wordSubsets(self, A, B):
        cnt = Counter()
        for b in B:
            cnt |= Counter(b)

        return [a for a in A if not cnt - Counter(a)]