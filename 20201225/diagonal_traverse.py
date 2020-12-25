# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/572/week-4-december-22nd-december-28th/3580/

from typing import List
from collections import defaultdict
from functools import reduce

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        diagonals = defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                diagonals[i + j].append(matrix[i][j])
        res = []
        for i, li in diagonals.items():
            res.extend(li) if i % 2 == 1 else res.extend(li[::-1])
        return res


# Too slow
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        diagonals = defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                diagonals[i + j].append(matrix[i][j])
        return reduce(lambda x,y: x+y, [li if i % 2 == 1 else li[::-1] for i, li in diagonals.items()])
