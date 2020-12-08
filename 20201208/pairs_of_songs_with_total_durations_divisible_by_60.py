# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3559/

from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = [0] * 60
        for t in time: count[t % 60] += 1

        answer = 0
        for i in range(1, 30): answer += count[i] * count[60-i]
        answer += count[0] * (count[0]-1) // 2
        answer += count[30] * (count[30]-1) // 2

        return answer