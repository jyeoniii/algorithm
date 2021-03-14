# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3670/

from collections import defaultdict
from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        d = defaultdict(set)
        arr.sort()
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[j] % arr[i] == 0:
                    d[arr[j]].add(arr[i])

        dp = defaultdict(lambda: 1)
        answer = 0
        for num in arr:
            dp[num] += sum(dp[n] * dp[num // n] for n in d[num] if num // n in d[num])
            answer += dp[num]

        return answer % (10 ** 9 + 7)

