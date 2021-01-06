# https://leetcode.com/problems/kth-missing-positive-number/

from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        num, arr_idx = 1, 0
        while k > 0 and arr_idx < len(arr):
            if arr[arr_idx] != num:
                k -= 1
            else:
                arr_idx += 1
            num += 1
        return num - 1 + k
