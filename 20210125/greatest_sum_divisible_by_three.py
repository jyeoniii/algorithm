# https://leetcode.com/problems/greatest-sum-divisible-by-three/

from typing import List
import heapq


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        mod_one, mod_two = [], []
        S = 0
        for num in nums:
            mod = num % 3
            if mod == 1:
                heapq.heappush(mod_one, -num)
                if len(mod_one) > 2: heapq.heappop(mod_one)
            elif mod == 2:
                heapq.heappush(mod_two, -num)
                if len(mod_two) > 2: heapq.heappop(mod_two)
            S += num

        mod = S % 3
        if mod == 0: return S
        elif mod == 1: return S - min(-mod_one[-1], -sum(mod_two) if len(mod_two) == 2 else float("inf"))
        elif mod == 2: return S - min(-mod_two[-1], -sum(mod_one) if len(mod_one) == 2 else float("inf"))


class Solution:
    def maxSumDivThree(self, N: List[int]) -> int:
        mod_one = heapq.nsmallest(2, [n for n in N if n % 3 == 1])
        mod_two = heapq.nsmallest(2, [n for n in N if n % 3 == 2])
        S = sum(N)

        if S % 3 == 0: return S
        if S % 3 == 1: return S - min(mod_one[0], sum(mod_two) if len(mod_two) == 2 else float("inf"))
        if S % 3 == 2: return S - min(mod_two[0], sum(mod_one) if len(mod_one) == 2 else float("inf"))
