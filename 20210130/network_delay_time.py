# https://leetcode.com/problems/network-delay-time/

from typing import List
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = [[] for _ in range(n+1)]
        for u, v, w in times: edges[u].append((v, w))

        dist = [float("inf")] * (n+1)
        h = [(0, k)]
        visited = set()

        while h:
            time, v = heapq.heappop(h)
            visited.add(v)
            if len(visited) == n: return time
            for adj_v, w in edges[v]:
                if time + w < dist[adj_v]:
                    dist[adj_v] = time + w
                    heapq.heappush(h, (dist[adj_v], adj_v))

        return -1




