# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3651/


# Divide And Conquer
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        if not S: return 0

        open_cnt, score, start = 0, 0, 0
        for i, c in enumerate(S):
            if c == '(':
                open_cnt += 1
            else:
                open_cnt -= 1
                if open_cnt == 0:
                    score += 1 if S[i-1] == '(' else 2 * self.scoreOfParentheses(S[start+1:i])
                    start = i+1

        return score


# Stack
class Solution:
    def scoreOfParentheses(self, S):
        stack = [0] # The score of the current frame

        for i, c in enumerate(S):
            if c == '(':
                stack.append(0)
            else:
                frame_score = stack.pop()
                stack[-1] += 1 if S[i-1] == '(' else 2 * frame_score

        return stack.pop()


# Use x*(a+b)= xa+xb
class Solution:
    def scoreOfParentheses(self, S):
        score = depth = 0
        for i, c in enumerate(S):
            if c == '(':
                depth += 1
            else:
                depth -= 1
                if S[i-1] == '(':
                    score += 1 << depth
        return score

