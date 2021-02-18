# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3644/

from typing import List


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        N, cnt = len(A), 0
        for i in range(N-2):
            d = A[i]-A[i+1]
            j = i+1
            while j < N-1 and A[j]-A[j+1] == d:
                cnt += 1
                j += 1
        return cnt


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        N, result, i = len(A), 0, 0
        while i < N - 2:
            diff, j = A[i] - A[i + 1], i + 1
            while j < N - 1 and A[j] - A[j + 1] == diff: j += 1

            if j > i + 1:
                result += (j - i - 1) * (j - i) // 2
                i = j + 1
            else:  # no arithmetic slices starts with A[i]
                i += 1

        return result
