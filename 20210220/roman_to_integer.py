# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3646/


class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        i, answer = 0, 0
        while i < len(s):
            if i + 1 < len(s) and (
                    (s[i] == 'I' and (s[i + 1] == 'V' or s[i + 1] == 'X')) or
                    (s[i] == 'X' and (s[i + 1] == 'L' or s[i + 1] == 'C')) or
                    (s[i] == 'C' and (s[i + 1] == 'D' or s[i + 1] == 'M'))):
                answer += d[s[i + 1]] - d[s[i]]
                i += 1
            else:
                answer += d[s[i]]
            i += 1

        return answer
