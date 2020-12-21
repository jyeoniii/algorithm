# https://leetcode.com/problems/first-unique-character-in-a-string/

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        unique = dict(filter(lambda x: x[1] == 1, counter.items()))
        for i, c  in enumerate(s):
            if c in unique: return i
        return -1
