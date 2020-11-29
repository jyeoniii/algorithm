# https://leetcode.com/problems/word-break-ii/

from typing import List
from collections import defaultdict


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_d = defaultdict(list)
        for word in wordDict:
            word_d[word[0]].append(word)

        dp = [[] for _ in range(len(s))] # dp[i]: i번째 index가 word break 가능한 경우, 해당 word들의 모음
        for i in reversed(range(len(s))):
            for word in word_d[s[i]]:
                if s[i:].startswith(word):
                    if i + len(word) == len(s):
                        dp[i].append(word)
                    elif i + len(word) < len(s) and dp[i+len(word)]:
                        dp[i].append(word)

        def dfs(idx: int) -> List[List[str]]:
            result = []
            for word in dp[idx]:
                if idx+len(word) == len(s):
                    result.append([word])
                else:
                    for next_words in dfs(idx+len(word)):
                        result.append([word] + next_words)
            return result

        return map(lambda x: " ".join(x), dfs(0))
