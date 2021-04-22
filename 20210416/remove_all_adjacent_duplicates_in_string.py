# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/


class Solution:
    def removeDuplicates(self, S: str) -> str:
        s = []
        for c in S:
            if s and c == s[-1]:
                s.pop()
            else:
                s.append(c)
        return ''.join(s)