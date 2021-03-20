# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N, M = map(int, input().split(" "))

matrix = [list(map(int, input().split(" "))) for _ in range(M)]
for i in range(1, M):
    matrix[i][0] += matrix[i - 1][0]

for j in range(1, N):
    matrix[0][j] += matrix[0][j - 1]

for i in range(1, M):
    for j in range(1, N):
        matrix[i][j] += max(matrix[i - 1][j], matrix[i][j - 1])

print(matrix[-1][-1])
