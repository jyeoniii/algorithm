# https://leetcode.com/problems/distant-barcodes/

from typing import List
from collections import Counter


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counter = sorted(Counter(barcodes).items(), key=lambda x: x[1])
        answer = [0] * len(barcodes)
        idx = 0
        while counter:
            num, cnt = counter.pop()
            for _ in range(cnt):
                answer[idx] = num
                idx = idx+2 if idx+2 < len(barcodes) else 1
        return answer