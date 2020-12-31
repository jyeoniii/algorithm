# https://leetcode.com/problems/task-scheduler/description/

from typing import List
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0: return len(tasks)

        d = sorted(Counter(tasks).items(), key=lambda x: x[1])
        _, first_cnt = d.pop()
        idle = (first_cnt - 1) * n

        while d:
            task, cnt = d.pop()
            idle -= cnt - 1 if first_cnt == cnt else cnt

        return max(idle, 0) + len(tasks)
