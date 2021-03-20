# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import heapq
import sys

preference = {g: score for g, score in zip(list("ABCDE"), input().split(" "))}
N, M = map(int, input().split(" "))


class Content:
    def __init__(self, seen, genre, i, j):
        self.seen = seen
        self.genre = genre
        self.i = i
        self.j = j

    def __lt__(self, other):
        if self.genre == other.genre or preference[self.genre] == preference[other.genre]:
            return [self.i, self.j] < [other.i, other.j]
        else:
            return preference[self.genre] > preference[other.genre]


seen = [list(input()) for _ in range(N)]
genre = [list(input()) for _ in range(N)]

y, o = [], []
for i, (s, g) in enumerate(zip(seen, genre)):
    for j in range(M):
        if s[j] == 'Y':
            heapq.heappush(y, Content(s[j], g[j], i, j))
        elif s[j] == 'O':
            heapq.heappush(o, Content(s[j], g[j], i, j))

while y:
    c = heapq.heappop(y)
    sys.stdout.write(f"{c.genre} {preference[c.genre]} {c.i} {c.j}\n")

while o:
    c = heapq.heappop(o)
    sys.stdout.write(f"{c.genre} {preference[c.genre]} {c.i} {c.j}\n")

