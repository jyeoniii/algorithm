# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/573/week-5-december-29th-december-31st/3586/

from typing import List


# https://leetcode.com/problems/game-of-life/discuss/993632/Python-O(mn)-time-and-O(1)-space-simple-solution
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        M, N = len(board), len(board[0])
        d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in range(M):
            for j in range(N):
                neighbor_cnt = 0
                for di, dj in d:
                    new_i, new_j = i + di, j + dj
                    if 0 <= new_i < M and 0 <= new_j < N:
                        neighbor_cnt += board[new_i][new_j] % 2

                if neighbor_cnt == 3 or (board[i][j] and neighbor_cnt == 2):
                    board[i][j] += 2

        for i in range(M):
            for j in range(N):
                board[i][j] >>= 1