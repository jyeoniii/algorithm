# https://leetcode.com/problems/count-square-submatrices-with-all-ones/

from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0])
        answer = sum(row.count(1) for row in matrix)

        d = [(0, -1), (-1, 0), (-1, -1)]
        for l in range(2, min(M, N) + 1):
            for i in range(l - 1, M):
                for j in range(l - 1, N):
                    if matrix[i][j] != l - 1:
                        continue
                    for di, dj in d:
                        new_i, new_j = i + di, j + dj
                        if not 0 <= new_i < M or not 0 <= new_j < N or matrix[new_i][new_j] < l - 1:
                            break
                    else:
                        matrix[i][j] += 1
                        answer += 1

        return answer


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        M, N, answer = len(matrix), len(matrix[0]), 0

        d = [(0, -1), (-1, 0), (-1, -1)]
        for i in range(M):
            for j in range(N):
                if not matrix[i][j]: continue
                matrix[i][j] += min(
                    matrix[i + di][j + dj] if 0 <= i + di < M and 0 <= j + dj < N else 0
                    for di, dj in d
                )
                answer += matrix[i][j]

        return answer

