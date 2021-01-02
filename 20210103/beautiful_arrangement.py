# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3591/

from typing import Set


class Solution:
    def countArrangement(self, n: int) -> int:
        nums = [set() for _ in range(n)]
        for i in range(1, n + 1):
            for x in range(1, n + 1):
                if x % i == 0 or i % x == 0: nums[i - 1].add(x)

        def dfs(i: int, used: Set[int]):
            if i == n: return 1
            answer = 0
            for x in nums[i]:
                if x not in used:
                    used.add(x)
                    answer += dfs(i + 1, used)
                    used.remove(x)
            return answer

        return dfs(0, set())
