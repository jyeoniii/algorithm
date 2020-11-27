# https://leetcode.com/problems/maximum-product-subarray/
# O(n) time complexity, O(1) space complexity

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        answer = nums[0]
        prev_min = nums[0]
        prev_max = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            prev_min, prev_max = min(num, min(prev_min * num, prev_max * num)), max(num,
                                                                                    max(prev_min * num, prev_max * num))
            answer = max(answer, max(prev_min, prev_max))
        return answer
