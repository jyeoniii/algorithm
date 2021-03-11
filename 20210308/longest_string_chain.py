# https://leetcode.com/problems/longest-string-chain/

from typing import List
import functools
from collections import defaultdict


class Solution:

    def isPredecessor(self, word1: str, word2: str) -> bool:
        if len(word1) + 1 != len(word2): return False
        i, j, skip = 0, 0, 0
        while i < len(word1) and j < len(word2):
            if word1[i] != word2[j]:
                if skip > 0: return False
                skip += 1
            else:
                i += 1
            j += 1

        return True

    def longestStrChain(self, words: List[str]) -> int:
        edges = [[] for _ in range(len(words))]
        for i in range(len(words)):
            for j in range(len(words)):
                if self.isPredecessor(words[i], words[j]):
                    edges[i].append(j)

        @functools.lru_cache(None)
        def dfs(i: int) -> int:
            if not edges[i]: return 1
            return 1 + max(dfs(j) for j in edges[i])

        return max(dfs(i) for i in range(len(words)))


class Solution:

    def isPredecessor(self, word1: str, word2: str) -> bool:
        if len(word1) + 1 != len(word2): return False
        i, j, skip = 0, 0, 0
        while i < len(word1) and j < len(word2):
            if word1[i] != word2[j]:
                if skip > 0: return False
                skip += 1
            else:
                i += 1
            j += 1

        return True

    def longestStrChain(self, words: List[str]) -> int:
        edges = [[] for _ in range(len(words))]
        d = defaultdict(list)
        for i in range(len(words)):
            d[len(words[i])].append(i)

        for l in d:
            if l + 1 in d:
                for i in d[l]:
                    for j in d[l + 1]:
                        if self.isPredecessor(words[i], words[j]):
                            edges[i].append(j)

        @functools.lru_cache(None)
        def dfs(i: int) -> int:
            if not edges[i]: return 1
            return 1 + max(dfs(j) for j in edges[i])

        return max(dfs(i) for i in range(len(words)))


class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        dp = { word: 1 for word in words }
        
        @functools.lru_cache(None)
        def dfs(word):
            if word not in dp: return 0
            dp[word] = 1 + max(dfs(word[:i] + word[i+1:]) for i in range(len(word)))
            return dp[word]

        return max(dfs(word) for word in words)
