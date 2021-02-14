# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3639/

from typing import List
from collections import deque


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        group = {}

        q = deque()
        for i in range(len(graph)):
            if i in group: continue

            q.append(i)
            group[i] = 1
            while q:
                x = q.popleft()
                for e in graph[x]:
                    if e not in group:
                        group[e] = group[x] * -1
                        q.append(e)
                    elif group[e] == group[x]:
                        return False

        return True


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        parent = [x for x in range(len(graph))]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for x in range(len(graph)):
            px = find(x)
            pys = [find(y) for y in graph[x]]

            for py in pys:
                if px == py: return False

            for py in pys[1:]:
                parent[py] = pys[0]

        return True