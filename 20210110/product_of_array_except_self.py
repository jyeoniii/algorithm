# https://leetcode.com/problems/product-of-array-except-self/

from typing import List
from functools import reduce


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = reduce(lambda x, y: x * y, nums)
        zero_count = nums.count(0)

        return [total_product // x if x != 0
            else 0 if zero_count > 1 else reduce(lambda x, y: x * y, filter(lambda x: x != 0, nums))
            for x in nums]


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product, right_product = [0] * len(nums), [0] * len(nums)
        left_product[0] = nums[0]
        right_product[len(nums) - 1] = nums[len(nums) - 1]

        for i in range(1, len(nums)):
            left_product[i] = left_product[i - 1] * nums[i]

        for i in range(len(nums) - 2, 0, -1):
            right_product[i] = right_product[i + 1] * nums[i]

        return [(left_product[i - 1] if i - 1 >= 0 else 1) * (right_product[i + 1] if i + 1 < len(nums) else 1) for i
                in range(len(nums))]


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1] * len(nums)
        left_running_product = 1
        for i in range(len(nums)):
            product[i] *= left_running_product
            left_running_product *= nums[i]

        right_running_product = 1
        for i in range(len(nums) - 1, -1, -1):
            product[i] *= right_running_product
            right_running_product *= nums[i]

        return product
