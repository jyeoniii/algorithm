# https://leetcode.com/problems/permutation-in-string/

from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, c1 = 0, Counter(s1)

        for r in range(len(s2)):
            if s2[r] not in c1:
                if c1 != Counter(s2[l:r]): l = r + 1
                else: return True
            elif r-l+1 == len(s1):
                if c1 != Counter(s2[l:r+1]): l += 1
                else: return True

        return c1 == Counter(s2[l:])


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, c1, c2 = 0, Counter(s1), Counter(s2[:len(s1) - 1])

        for r in range(len(s1) - 1, len(s2)):
            c2[s2[r]] += 1
            if c1 == c2:
                return True
            else:
                c2[s2[l]] -= 1
                if c2[s2[l]] == 0:
                    del c2[s2[l]]
                l += 1

        return False