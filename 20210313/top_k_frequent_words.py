# https://leetcode.com/problems/top-k-frequent-words/

from typing import List
from collections import Counter, deque
import heapq


class WordCount:
    def __init__(self, word, cnt):
        self.word = word
        self.cnt = cnt

    def __lt__(self, other):
        if self.cnt != other.cnt:
            return self.cnt < other.cnt
        else:
            return self.word > other.word

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter, h = Counter(words), []
        for word, cnt in counter.items():
            heapq.heappush(h, WordCount(word, cnt))
            if len(h) > k:
                heapq.heappop(h)

        answer = deque()
        while h:
            answer.appendleft(heapq.heappop(h).word)

        return answer

