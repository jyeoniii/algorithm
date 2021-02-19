# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3645/


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s: return s
        li, paren_idx, i = [], [], 0
        while i < len(s):
            if s[i] == '(':
                paren_idx.append(len(li))
                li.append(s[i])
            elif s[i] == ')':
                if paren_idx:
                    paren_idx.pop()
                    li.append(s[i])
            else: # alphabet
                start = i
                while i+1 < len(s) and 'a' <= s[i+1] <= 'z': i += 1
                li.append(s[start:i+1])
            i += 1

        for idx in paren_idx: li[idx] = ''
        return ''.join(li)


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        li, paren_idx, i = list(s), [], 0

        for i in range(len(li)):
            if li[i] == '(':
                paren_idx.append(i)
            elif li[i] == ')':
                if paren_idx:
                    paren_idx.pop()
                else:
                    li[i] = ''

        for idx in paren_idx: li[idx] = ''
        return ''.join(li)