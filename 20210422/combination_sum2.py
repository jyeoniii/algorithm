# https://leetcode.com/problems/combination-sum-ii/

from typing import List
from collections import Counter


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        c = Counter(candidates)
        keys = list(c.keys())

        def recursive(curr: List[int], idx: int, curr_sum: int):
            if curr_sum == target:
                answer.append(curr[:])
                return

            for i in range(idx, len(keys)):
                num = keys[i]
                append_cnt = 0
                for cnt in range(1, c[num] + 1):
                    if curr_sum + cnt * num <= target:
                        curr.append(num)
                        append_cnt += 1
                        recursive(curr, i + 1, curr_sum + cnt * num)

                for _ in range(append_cnt):
                    curr.pop()

        recursive([], 0, 0)
        return answer
