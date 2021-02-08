# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3633/

from collections import deque


class PeekingIterator:
    def __init__(self, iterator):
        self.q = deque()
        while iterator.hasNext():
            self.q.append(iterator.next())

    def peek(self):
        return self.q[0]

    def next(self):
        return self.q.popleft()

    def hasNext(self):
        return len(self.q) > 0


class PeekingIterator:
    def __init__(self, iterator):
        self.iter = iterator
        self.last_peek = self.iter.next() if self.iter.hasNext() else None

    def peek(self):
        return self.last_peek

    def next(self):
        tmp = self.last_peek
        self.last_peek = self.iter.next() if self.iter.hasNext() else None
        return tmp

    def hasNext(self):
        return self.last_peek is not None