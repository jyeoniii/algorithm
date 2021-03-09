# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3665/


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s: return 0
        elif s == s[::-1]: return 1
        return 2