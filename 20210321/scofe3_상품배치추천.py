# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from collections import Counter

N = int(input())
place = [list(map(int, input())) for _ in range(N)]

diff = [[0, -1], [-1, -1], [-1, 0]]
c = Counter()
total = 0
for i in range(N):
    for j in range(N):
        if place[i][j] == 1:
            if i >= 1 and j >= 1:
                min_val = min(place[i + di][j + dj] for di, dj in diff)
                if min_val >= place[i][j]:
                    place[i][j] = min_val + 1

            for k in range(1, place[i][j] + 1):
                c[k] += 1
                total += 1

print(f"total: {total}")
for k, v in c.items():
    print(f"size[{k}]: {v}")






