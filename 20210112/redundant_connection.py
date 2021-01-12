# https://leetcode.com/problems/redundant-connection/

from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}
        def find(x):
            while x in parent and parent[x] != x: x = parent[x]
            return x

        for u, v in edges:
            pu, pv = find(u), find(v)
            if pu == pv: return [u, v]
            else: parent[pv] = pu


# Path Compression and Union By Rank
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [0] * (len(edges) + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for u, v in edges:
            pu, pv = find(u), find(v)
            if pu == pv: return [u, v]
            if rank[pu] == rank[pv]:
                parent[pu] = pv
                rank[pu] += 1
            elif rank[pu] < rank[pv]:
                parent[pu] = pv
            else:
                parent[pv] = pu

