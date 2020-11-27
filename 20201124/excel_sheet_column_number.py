# https://leetcode.com/problems/excel-sheet-column-number/
# 26진법

class Solution:
    def titleToNumber(self, s: str) -> int:
        base_ord = ord('A') - 1
        answer = 0
        for i, x in enumerate(s):
            code = ord(x) - base_ord
            answer += 26 ** (len(s)-i-1) * code
        return answer