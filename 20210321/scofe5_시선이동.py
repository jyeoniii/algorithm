
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from collections import deque

N, M = map(int, input().split(" "))
screen = [list(input()) for _ in range(M)]

diff = [[1, 0], [0, -1], [0, 1]]


def solution(j):  # [0,j]에서 출발했을 때
    q = deque([(0, j, 0, 0)])
    visited = {(0, j)}
    while q:
        i, j, dist, cnt = q.popleft()
        if i == M - 1:
            return dist, cnt

        for di, dj in diff:
            new_i, new_j = i + di, j + dj
            if 0 <= new_i < M and 0 <= new_j < N and (new_i, new_j) not in visited and screen[new_i][new_j] == '.':
                visited.add((new_i, new_j))
                q.append((new_i, new_j, dist + 1, cnt + 1 if new_i == i else cnt))

    return float("inf"), float("inf")


dist, cnt = min((solution(j) for j in range(N) if screen[0][j] == 'c'), key=lambda x: x[0])
print(cnt if cnt != float("inf") else -1)





import functools

N, M = map(int, input().split(" "))
screen = [list(input()) for _ in range(M)]
inf = (float("inf"), float("inf"))

@functools.lru_cache(None)
def solution(i, j, is_from):  # screen[i][j]에서 시작했을 때 최
    if i == M:
        return 0, 0
    elif not 0 <= j < N or screen[i][j] == 'x':
        return inf

    current = (i, j)
    d1, c1 = solution(i + 1, j, current) if (i + 1, j) != is_from else inf
    d2, c2 = solution(i, j - 1, current) if (i, j - 1) != is_from else inf
    d3, c3 = solution(i, j + 1, current) if (i, j + 1) != is_from else inf

    if d1 <= d2 and d1 <= d3:
        return d1 + 1, c1
    elif d2 <= d3 and d2 <= d1:
        return d2 + 1, c2 + 1
    else:
        return d3 + 1, c3 + 1


d, c = min((solution(0, j, None) for j in range(N) if screen[0][j] == 'c'), key=lambda x: x[0])

print(c if c != float("inf") else -1)