# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3653/

from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, i, j = [], 0, 0
        while i < len(pushed) and j < len(popped):
            while not stack or (i < len(pushed) and popped[j] != stack[-1]):
                stack.append(pushed[i])
                i += 1
            if popped[j] == stack[-1]:
                stack.pop()
                j += 1
            else:
                return False

        return list(reversed(stack)) == popped[j:]


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, i = [], 0
        for x in pushed:
            stack.append(x)
            while i < len(popped) and (stack and stack[-1] == popped[i]):
                stack.pop()
                i += 1

        return i == len(popped)

