# https://leetcode.com/problems/n-queens/

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        queen_idx = [0 for _ in range(n)] # queen_idx[i] = x -> matrix[i][x]에 queen이 놓여있다
        answer = []

        def isValid(i: int) -> bool:
            for k in range(i):
                if queen_idx[k] == queen_idx[i] or abs(k-i) == abs(queen_idx[k]-queen_idx[i]): return False
            return True

        # i-1번째 행까지 queen이 놓여있다는 가정 하에 i번째 행에 queen을 놓는다.
        def dfs(i: int):
            if i == n:
                answer.append(list(map(lambda x: "".join(["Q" if x == idx else "." for idx in range(n)]), queen_idx)))
                return

            for j in range(n):
                queen_idx[i] = j
                if isValid(i):
                    dfs(i+1)

        dfs(0)
        return answer
