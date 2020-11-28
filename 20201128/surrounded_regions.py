# https://leetcode.com/problems/surrounded-regions/
from typing import List, Tuple

# BFS
class Solution:

    def __init__(self):
        self.di = [-1, 1, 0, 0]
        self.dj = [0, 0, -1, 1]


    def solve(self, board: List[List[str]]) -> None:
        if not board: return
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        def setArea(i: int, j: int) -> None:
            queue = [(i, j)]
            l = [(i, j)]

            is_edge = False

            while queue:
                (i, j) = queue.pop(0)

                if i == 0 or i == len(board)-1 or j == 0 or j == len(board[0])-1:
                    is_edge = True

                for x in range(4):
                    new_i = i + self.di[x]
                    new_j = j + self.dj[x]
                    if new_i < 0 or new_i >= len(board) or new_j < 0 or new_j >= len(board[0]) or visited[i][j]:
                        continue
                    elif board[new_i][new_j] == 'O': # Still, we need to check all those adjacent regions
                        queue.append((new_i, new_j))
                        l.append((new_i, new_j))

                visited[i][j] = True

            if not is_edge:
                for (i, j) in l: board[i][j] = 'X'


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X' or visited[i][j]: continue
                setArea(i, j)

# DFS
class Solution:
    def __init__(self):
        self.di = [-1, 1, 0, 0]
        self.dj = [0, 0, -1, 1]


    def solve(self, board: List[List[str]]) -> None:
        if not board: return

        visited = [[None for _ in range(len(board[0]))] for _ in range(len(board))]

        def is_surrounded(i: int, j: int, l: List[Tuple[int, int]]) -> bool:
            visited[i][j] = True
            l.append((i,j))

            need_to_set = True
            for x in range(4):
                new_i = i + self.di[x]
                new_j = j + self.dj[x]
                if new_i not in range(0, len(board)) or new_j not in range(0, len(board[0])):
                    need_to_set = False
                elif visited[new_i][new_j]:
                    continue
                elif board[new_i][new_j] == 'O':
                    need_to_set = is_surrounded(new_i, new_j, l) and need_to_set
            return need_to_set


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and not visited[i][j]:
                    l = []
                    if is_surrounded(i, j, l):
                        while l:
                            (i, j) = l.pop()
                            board[i][j] = 'X'

# DFS on edge only
class Solution:
    def __init__(self):
        self.di = [-1, 1, 0, 0]
        self.dj = [0, 0, -1, 1]


    def solve(self, board: List[List[str]]) -> None:
        if not board: return

        def check_surrounded(i: int, j: int):
            board[i][j] = 'T'
            for x in range(4):
                new_i = i + self.di[x]
                new_j = j + self.dj[x]
                if new_i in range(0, len(board)) and new_j in range(0, len(board[0])) and board[new_i][new_j] == 'O':
                    check_surrounded(new_i, new_j)

        for j in [0, len(board[0])-1]:
            for i in range(len(board)):
                if board[i][j] == 'O': check_surrounded(i, j)

        for i in [0, len(board)-1]:
            for j in range(len(board[0])):
                if board[i][j] == 'O': check_surrounded(i, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = 'O' if board[i][j] == 'T' else 'X'