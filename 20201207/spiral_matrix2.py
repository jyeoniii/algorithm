# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3557/

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        arr = [[0] * n for _ in range(n)]
        di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
        i, j, cnt, d_idx = 0, 0, 0, 0

        while True:
            if cnt == n * n: break
            cnt += 1
            arr[i][j] = cnt

            new_i = i + di[d_idx]
            new_j = j + dj[d_idx]
            if new_i < 0 or new_i >= n or new_j < 0 or new_j >= n or arr[new_i][new_j] != 0:
                d_idx = (d_idx + 1) % 4
                i, j = i + di[d_idx], j + dj[d_idx]
            else:
                i, j = new_i, new_j

        return arr
