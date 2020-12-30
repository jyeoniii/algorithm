# https://leetcode.com/problems/longest-valid-parentheses/


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        dp = [0] * len(s)  # dp[i]: s[i]로 끝나는 LVP의 길이, i = ')' 일 때만 > 0
        answer = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if not stack: continue
                j = stack.pop()
                dp[i] = 2 + dp[i-1] + (dp[j-1] if j-1 >= 0 else 0)
                answer = max(answer, dp[i])

        return answer