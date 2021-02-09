# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/#


class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        s, cnt = [], 0
        for c in S:
            if c == '(':
                s.append('(')
            else:
                if not s: cnt += 1
                else: s.pop()

        return cnt + len(s)