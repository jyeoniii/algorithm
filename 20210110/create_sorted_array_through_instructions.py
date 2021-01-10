# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3599/

from typing import List
import bisect


MOD = 1000000007
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        nums = []
        costs = 0
        for n in instructions:
            left_pos = bisect.bisect_left(nums, n)
            right_pos = bisect.bisect_right(nums, n)

            costs += min(left_pos, len(nums) - right_pos)
            nums[left_pos:left_pos] = [n]  # same with insert at left_pos

        return costs % MOD


# Fenwick Tree: https://www.acmicpc.net/blog/view/21
# https://leetcode.com/problems/create-sorted-array-through-instructions/discuss/927761/Python3-Binary-Index-Tree-oror-SortedList
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        N = max(instructions)
        cc = [0] * (N + 1)

        def update(x):
            while x <= N:
                cc[x] += 1
                x += -x & x

        def query(x):
            ans = 0
            while x > 0:
                ans += cc[x]
                x -= -x & x
            return ans

        ans = 0
        for i, n in enumerate(instructions):
            ans += min(query(n - 1), i - query(n))
            update(n)
        return ans % MOD