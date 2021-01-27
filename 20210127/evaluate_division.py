# https://leetcode.com/problems/evaluate-division/

from typing import List
from collections import defaultdict, deque


# BFS
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        edges = defaultdict(list)
        for i in range(len(equations)):
            x, y = equations[i]
            edges[x].append((y, values[i]))
            edges[y].append((x, 1/values[i]))

        def calc(a, b) -> float:
            if a not in edges or b not in edges: return -1

            visited = set()
            q = deque([(a, 1)])
            while q:
                x, dist = q.popleft()
                visited.add(x)
                if x == b: return dist
                for y, v in edges[x]:
                    if y not in visited:
                        q.append((y, dist * v))
            return -1

        return [calc(x, y) for x, y in queries]


# Union Find
class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = defaultdict(int)

    def union(self, x, y, v):
        if x not in self.parent: self.parent[x] = (x, 1)
        if y not in self.parent: self.parent[y] = (y, 1)

        px, py = self.find(x), self.find(y)
        if px == py: return
        if self.rank[px[0]] >= self.rank[py[0]]:
            self.parent[py[0]] = (px[0], px[1]/py[1]*v)
            if self.rank[px[0]] == self.rank[py[0]]:
                self.rank[px[0]] += 1
        else:
            self.parent[px[0]] = (py[0], 1 / (px[1]/py[1]*v))

    def find(self, x):  # return (rootX, rootX/x)
        if x != self.parent[x][0]:
            px, v = self.parent[x]
            new_px, new_v = self.find(px)
            self.parent[x] = (new_px, new_v * v)
        return self.parent[x]

    def div(self, x, y):
        if x not in self.parent or y not in self.parent: return -1

        px, py = self.find(x), self.find(y)
        if px[0] != py[0]: return -1
        else: return py[1] / px[1]


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        uf = UnionFind()
        for i in range(len(equations)):
            x, y = equations[i]
            uf.union(x, y, values[i])

        return [uf.div(x, y) for x, y in queries]