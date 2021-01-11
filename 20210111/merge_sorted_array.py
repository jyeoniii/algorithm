# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3600/

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j = 0, 0
        while i < m + j and j < n:
            if nums1[i] > nums2[j]:
                nums1[i + 1:] = nums1[i:-1]
                nums1[i] = nums2[j]
                j += 1
            i += 1

        while j < n:
            nums1[i] = nums2[j]
            i += 1
            j += 1


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j = m - 1, n - 1
        idx = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[idx] = nums2[j]
                j -= 1
            else:
                nums1[idx] = nums1[i]
                i -= 1
            idx -= 1

        if j >= 0:
            nums1[:idx + 1] = nums2[:j + 1]
