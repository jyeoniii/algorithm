# https://www.hackerrank.com/challenges/merging-communities/problem

import sys


class UnionFind:
    def __init__(self, N):
        self.parent = [x for x in range(N + 1)]
        self.cnt = [1] * (N + 1)
        self.rank = [0] * (N + 1)

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
            self.cnt[py] += self.cnt[px]
        elif self.rank[py] < self.rank[px]:
            self.parent[py] = px
            self.cnt[px] += self.cnt[py]
        else:
            self.parent[px] = py
            self.cnt[py] += self.cnt[px]
            self.rank[py] += 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def getCount(self, x):
        return self.cnt[self.find(x)]


N, Q = map(lambda x: int(x), sys.stdin.readline().split(" "))
uf = UnionFind(N)

for _ in range(Q):
    params = sys.stdin.readline().split(" ")
    if params[0] == 'Q':
        print(uf.getCount(int(params[1])))
    else:
        i, j = int(params[1]), int(params[2])
        uf.union(i, j)


