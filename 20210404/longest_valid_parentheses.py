# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/593/week-1-april-1st-april-7th/3695/


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * len(s)  # dp[i]: s[i]로 끝나는 longestValidParentheses
        answer, stack = 0, []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if stack:
                    open_idx = stack.pop()
                    dp[i] = dp[open_idx - 1] + i - open_idx + 1
                    answer = max(answer, dp[i])

        return answer