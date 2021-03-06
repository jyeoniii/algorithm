# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3662/

from typing import List
from collections import defaultdict


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        subWords = set()
        words = set(words)
        for word in words:
            for i in range(1, len(word)):
                subWords.add(word[i:])

        return sum(len(word)+1 for word in words if word not in subWords)


class TrieNode:
    def __init__(self, c: chr):
        self.c = c
        self.children = {}

class Trie:
    def __init__(self):
        self.trie = TrieNode('*')

    def add(self, s: str):
        node = self.trie
        for c in reversed(s):
            if c in node.children:
                node = node.children[c]
            else:
                node.children[c] = TrieNode(c)
                node = node.children[c]

    def isSuffix(self, s: str):
        node = self.trie
        for c in reversed(s):
            node = node.children[c]
        return len(node.children) > 0

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = Trie()
        words = set(words)
        for word in words:
            trie.add(word)

        return sum(len(word) + 1 for word in words if not trie.isSuffix(word))
