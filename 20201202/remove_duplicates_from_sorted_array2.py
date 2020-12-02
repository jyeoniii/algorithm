# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# [0, 0, 1, 1, 1, 1, 2, 3, 3] -> [0,0,1,1,2,3,3]

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = float("-inf")
        cnt, idx = 0, 0
        for num in nums:
            cnt = 1 if prev != num else cnt + 1
            if cnt <= 2:
                nums[idx] = num
                idx += 1
            prev = num
        return idx