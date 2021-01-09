# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3598/

from typing import List
from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        regex_dict = defaultdict(list)
        for idx, word in enumerate(wordList):
            for i in range(len(word)):
                regexp = word[:i] + '*' + word[i + 1:]
                regex_dict[regexp].append(idx)

        q = deque([(beginWord, 1)])
        visited = set()
        while q:
            word, cnt = q.popleft()
            if word == endWord: return cnt

            for regexp in [word[:i] + '*' + word[i + 1:] for i in range(len(word))]:
                for word_idx in regex_dict[regexp]:
                    if word_idx not in visited:
                        visited.add(word_idx)
                        q.append((wordList[word_idx], cnt + 1))

        return 0







