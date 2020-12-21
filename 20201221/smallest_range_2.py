# https://leetcode.com/problems/smallest-range-ii/

from typing import List


class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        N = len(A)
        A.sort()
        ans = A[N - 1] - A[0]

        for i in range(N - 1):
            a, b = A[i], A[i + 1]
            high = max(A[N - 1] - K, a + K)
            low = min(A[0] + K, b - K)
            ans = min(ans, high - low)
        return ans