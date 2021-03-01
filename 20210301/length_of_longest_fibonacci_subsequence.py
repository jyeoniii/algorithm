# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

from typing import List
from collections import defaultdict

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        s, answer = set(arr), 0
        for i in range(len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                x1, x2, currLength = arr[i], arr[j], 2
                while x1 + x2 in s:
                    currLength += 1
                    answer = max(answer, currLength)
                    x1, x2 = x2, x1 + x2

        return answer


class Solution(object):
    def lenLongestFibSubseq(self, A):
        index = { x: i for i, x in enumerate(A) }
        longest = defaultdict(lambda: 2)

        answer = 0
        for k in range(len(A)):
            for j in range(k):
                i = index.get(A[k] - A[j], None)
                if i is not None and i < j:
                    longest[j, k] = longest[i, j] + 1
                    answer = max(answer, longest[j, k])

        return answer
