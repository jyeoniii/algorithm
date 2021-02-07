# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3631/

from typing import List
from collections import deque


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        q, answer = deque(), []
        last_c_idx = float("-inf")
        for i, x in enumerate(s):
            if x == c:
                while q:
                    j = q.popleft()
                    answer.append(min(i - j, j - last_c_idx))
                last_c_idx = i
                answer.append(0)
            else:
                q.append(i)

        while q:
            j = q.popleft()
            answer.append(j - last_c_idx)

        return answer


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        q, answer = deque(), [0] * len(s)
        last_c_idx = float("-inf")
        for i in range(len(s)):
            if s[i] == c: last_c_idx = i
            answer[i] = i - last_c_idx

        last_c_idx = float("inf")
        for i in range(len(s)-1, -1, -1):
            if s[i] == c: last_c_idx = i
            answer[i] = min(answer[i], last_c_idx - i)

        return answer
