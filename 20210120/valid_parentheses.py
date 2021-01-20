# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3610/


class Solution:
    def isValid(self, s: str) -> bool:
        pair = { ')': '(', '}': '{', ']': '[' }
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if not stack: return False
                if stack[-1] == pair[c]: stack.pop()
                else: return False

        return not stack
