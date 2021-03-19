# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/590/week-3-march-15th-march-21st/3677/

from typing import List
from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q, visited = deque([0]), {0}
        while q:
            i = q.popleft()

            for j in rooms[i]:
                if j not in visited:
                    visited.add(j)
                    q.append(j)

            if len(visited) == len(rooms):
                return True

        return False
