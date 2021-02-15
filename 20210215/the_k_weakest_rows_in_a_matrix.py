# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021

from typing import List
import heapq


class Solution:

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        M, N = len(mat), len(mat[0])
        pq = []  # maxHeap. length = k
        for i in range(M):
            j = 0
            while j < N and mat[i][j] == 1: j += 1
            heapq.heappush(pq, (-j, -i))
            if len(pq) > k:
                heapq.heappop(pq)

        answer = []
        while pq:
            answer.append(-heapq.heappop(pq)[1])
        return reversed(answer)
