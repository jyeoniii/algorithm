# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3629/


class Solution:
    def simplifyPath(self, path: str) -> str:
        tokens = path.split('/')
        stack = []
        for token in tokens:
            if not token or token == '.':
                continue
            elif token == '..':
                if stack: stack.pop()
            else:
                stack.append(token)
        return '/' + '/'.join(stack)