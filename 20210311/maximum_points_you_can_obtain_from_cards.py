# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        arr_size = len(cardPoints) - k
        l, r = 0, arr_size - 1
        answer = curr_sum = sum(cardPoints[:arr_size])
        for r in range(arr_size, len(cardPoints)):
            curr_sum += cardPoints[r] - cardPoints[l]
            answer = min(answer, curr_sum)
            l += 1

        return sum(cardPoints) - answer
