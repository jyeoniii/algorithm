# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/572/week-4-december-22nd-december-28th/3581/

import functools

# Top Down
class Solution:
    def numDecodings(self, s: str) -> int:
        @functools.lru_cache(None)
        def recursive(i: int):  # s[i:]의 numDecodings
            if i == len(s): return 1
            elif s[i] == '0': return 0

            answer = recursive(i+1)
            if i < len(s)-1 and (s[i] == '1' or (s[i] == '2' and s[i+1] <= '6')):
                answer += recursive(i+2)
            return answer

        return recursive(0)


# Bottom Up
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        dp = [0] * len(s)  # dp[i]: s[:i+1]의 numDecodings
        dp[0] = 1
        for i in range(1, len(s)):
            dp[i] = dp[i-1] if s[i] != '0' else 0
            if i-1 >= 0 and (s[i-1] == '1' or (s[i-1] == '2' and s[i] <= '6')):
                dp[i] += dp[i-2] if i-2 >= 0 else 1
        return dp[-1]

