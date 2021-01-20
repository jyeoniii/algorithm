# https://leetcode.com/problems/word-ladder-ii/

from typing import List
from collections import defaultdict, deque


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for idx, word in enumerate(wordList):
            for i in range(len(word)):
                d[word[:i] + '*' + word[i+1:]].append(idx)

        wordList.append(beginWord)
        s, q = set(), deque([(len(wordList)-1, [len(wordList)-1])])
        answer = []
        while q:
            idx, li = q.popleft()
            word = wordList[idx]
            if word == endWord:
                if not answer or len(answer[0]) == len(li):
                    answer.append(li)
                    continue
                else:
                    break

            s.add(idx)
            for i in range(len(word)):
                for word_idx in d[word[:i] + '*' + word[i+1:]]:
                    if word_idx not in s:
                        new_li = li[:]
                        new_li.append(word_idx)
                        q.append((word_idx, new_li))

        return list(map(lambda li: [wordList[x] for x in li], answer))
