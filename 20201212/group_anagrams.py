# https://leetcode.com/problems/group-anagrams/

from typing import List
from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            key = "".join(list(map(lambda x: x[0] + str(x[1]), sorted(Counter(s).items()))))
            d[key].append(s)
        return list(map(lambda x: x[1], d.items()))

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            d["".join(sorted(s))].append(s)
        return list(map(lambda x: x[1], d.items()))