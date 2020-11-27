# https://leetcode.com/problems/combinations/
# Backtracking

from typing import List


class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        tmp = []

        def _recursive(curr_idx: int, answer: List[int]):
            nonlocal k, tmp, n
            if len(tmp) == k:
                answer.append(tmp[:])
                return

            for x in range(curr_idx, n + 1):
                tmp.append(x)
                _recursive(x + 1, answer)
                tmp.pop()

        answer = []
        _recursive(1, answer)
        return answer
