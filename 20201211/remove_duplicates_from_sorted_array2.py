# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3562/

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0

        prev = float("-inf")
        cnt, idx = 0, 0
        for num in nums:
            if prev < num:
                nums[idx] = num
                cnt = 1
                idx += 1
                prev = num
            else:
                cnt += 1
                if cnt <= 2:
                    nums[idx] = num
                    idx += 1
        return idx