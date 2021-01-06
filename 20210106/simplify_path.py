# https://leetcode.com/problems/simplify-path/


class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        stack = []

        for p in paths:
            if p == '.':
                continue
            elif p == '..':
                if stack: stack.pop()
            elif p:
                stack.append(p)
        return '/' + '/'.join(stack)