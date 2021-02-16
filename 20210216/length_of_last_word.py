# https://leetcode.com/problems/length-of-last-word/


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        answer, i = 0, 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
            else:
                start = i
                while i < len(s) and s[i] != ' ': i += 1
                answer = i - start

        return answer
