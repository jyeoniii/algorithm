# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3614/

from typing import List
from collections import defaultdict
import heapq

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        d = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                heapq.heappush(d[j-i], mat[i][j])

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = heapq.heappop(d[j-i])

        return mat





