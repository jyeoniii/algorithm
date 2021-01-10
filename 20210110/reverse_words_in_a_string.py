# https://leetcode.com/problems/reverse-words-in-a-string/


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))


class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        i = len(s) - 1
        while i >= 0:
            while i >= 0 and s[i] == ' ': i -= 1
            word_start_idx = i
            while i >= 0 and s[i] != ' ': i -= 1
            word = s[i + 1:word_start_idx + 1]

            if result and word: result += ' '
            result += word

        return result

