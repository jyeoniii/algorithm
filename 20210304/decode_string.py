# https://leetcode.com/problems/decode-string/


# Time Complexity: Worst case O(n^2)
# Space Complexity: O(number of brackets)
class Solution:
    def decodeString(self, s: str) -> str:
        answer, stack, k = "", [], -1
        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit() and not stack:
                digit_start = i
                while i + 1 < len(s) and s[i + 1].isdigit():
                    i += 1
                k = int(s[digit_start:i + 1])
            elif c == '[':
                stack.append(i)
            elif c == ']':
                idx = stack.pop()
                if not stack:
                    answer += k * self.decodeString(s[idx + 1:i])
            elif c.isalpha() and not stack:
                answer += c
            i += 1

        return answer if k >= 0 else s

