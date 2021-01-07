# https://leetcode.com/problems/word-ladder/

from typing import List
from collections import deque, defaultdict
from functools import reduce

# TLE when calculating edges
class Solution:
    def is_adjacent(self, word1: str, word2: str) -> bool:
        return len(word1) == len(word2) and sum(int(c1 != c2) for c1, c2 in zip(word1, word2)) == 1

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0

        N = len(wordList)
        edges = [[] for _ in range(N)]
        for i in range(N):
            for j in range(i + 1, N):
                if self.is_adjacent(wordList[i], wordList[j]):
                    edges[i].append(j)
                    edges[j].append(i)

        queue = deque([(i, 2) for i, word in enumerate(wordList) if self.is_adjacent(beginWord, word)])
        visited = set()
        while queue:
            i, dist = queue.popleft()
            if wordList[i] == endWord: return dist

            for j in edges[i]:
                if j not in visited:
                    visited.add(j)
                    queue.append((j, dist+1))

        return 0


class Solution:

    def get_regex_exprs(self, word: str):
        return [word[:i] + '*' + word[i+1:] for i in range(len(word))]

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0

        regex_match = defaultdict(list)
        def get_adjacent_words(word: str):
            return reduce(lambda l1, l2: l1 + l2, [regex_match[expr] for expr in self.get_regex_exprs(word)])

        for i, word in enumerate(wordList):
            for expr in self.get_regex_exprs(word):
                regex_match[expr].append(i)

        queue = deque([(i, 2) for i in get_adjacent_words(beginWord)])
        visited = set()
        while queue:
            i, dist = queue.popleft()
            if wordList[i] == endWord: return dist

            for j in get_adjacent_words(wordList[i]):
                if j not in visited:
                    visited.add(j)
                    queue.append((j, dist+1))

        return 0