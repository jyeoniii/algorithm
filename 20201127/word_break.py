# https://leetcode.com/problems/word-break/

from typing import List
from collections import defaultdict


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s))]
        word_d = defaultdict(list)
        for word in wordDict:
            word_d[word[0]].append(word)

        for i in reversed(range(len(s))):
            if s[i] in word_d:
                for word in word_d[s[i]]:
                    if s[i:].startswith(word):
                        if i + len(word) == len(s):
                            dp[i] = True
                        elif i + len(word) < len(s):
                            dp[i] = dp[i + len(word)]
                        else:
                            dp[i] = False
                        if dp[i]:
                            break
        return dp[0]
