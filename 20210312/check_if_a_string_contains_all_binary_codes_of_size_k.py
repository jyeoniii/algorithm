# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3669/

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        binSet = set()
        for r in range(k, len(s) + 1):
            binSet.add(s[r - k:r])

        return len(binSet) == 2 ** k


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        return len({s[r - k:r] for r in range(k, len(s) + 1)}) == 2 ** k
