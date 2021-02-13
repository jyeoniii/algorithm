# https://leetcode.com/problems/combination-sum-iii/

from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        answer = []
        def helper(kk: int, nn: int, li: List[int]):
            nonlocal answer
            if kk == 0:
                if nn == 0: answer.append(li[:])
                return

            last_num = li[-1] if li else 0
            for x in range(last_num + 1, 10):
                if n - x >= 0:
                    li.append(x)
                    helper(kk - 1, nn - x, li)
                    li.pop()

        helper(k, n, [])
        return answer
