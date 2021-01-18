# https://leetcode.com/submissions/detail/444511084/

from typing import List
from collections import defaultdict, Counter


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        cnt = 0
        for num in nums:
            if d[k - num] > 0:
                d[k - num] -= 1
                cnt += 1
            else:
                d[num] += 1

        return cnt


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        cnt = 0
        for x in c.keys():
            if x > k // 2: continue
            if x == k // 2 and k % 2 == 0: cnt += c[x] // 2
            else: cnt += min(c[x], c[k-x])
        return cnt