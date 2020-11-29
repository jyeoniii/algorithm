# https://leetcode.com/problems/rotate-array/

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        if k == 0: return

        def reverse(arr: List[int], start: int, end: int):
            for i in range(0, (end - start + 1) // 2):
                arr[start + i], arr[end - i] = arr[end - i], arr[start + i]

        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)

