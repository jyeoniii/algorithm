# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/590/week-3-march-15th-march-21st/3676/

from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # up[i], down[i]: nums[i]로 끝나는 wiggleMaxLength 중 up으로 끝난 / down으로 끝난
        up, down = [1] * len(nums), [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    up[i] = max(up[i], down[j] + 1)
                elif nums[j] > nums[i]:
                    down[i] = max(down[i], up[j] + 1)

        return max(up[-1], down[-1])


"""
First of all, 
up[i] := longest subsequence that uses elements in A[0], ..., A[i] and ends in an up-wiggle and 
down[i] := longest subsequence that uses elements in A[0], ..., A[i] and ends in a down-wiggle. 
Notice that neither up[i] nor down[i] require the subsequence to end on A[i].

Now, why can we always extend?

Say A[i-1] > A[i], i.e. A[i] is a down-wiggle. We know up[i-1] represents the longest subsequence to the left of A[i] that ends on an up-wiggle. 
Let the last element of that subsequence be x. There are two cases:

case 1: x > A[i]. Then obviously we can extend the subsequence by A[i] => down[i] = up[i-1] + 1.
case 2: x <= A[i]. But notice we know that A[i-1] > A[i], so we can always replace x by A[i-1], then extend the subsequence by A[i] => down[i] = up[i-1] + 1.

So no matter what, we can always extend the previous subsequence by 1. 
By symmetry the same logic can be applied for when A[i] is an up-wiggle.
"""
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up, down = [1] * len(nums), [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                up[i], down[i] = max(up[i], down[i-1] + 1), down[i-1]
            elif nums[i-1] > nums[i]:
                up[i], down[i] = up[i-1], max(down[i], up[i-1] + 1)
            else:
                up[i], down[i] = up[i-1], down[i-1]

        return max(up[-1], down[-1])


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up, down = 1, 1
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                up = max(up, down + 1)
            elif nums[i-1] > nums[i]:
                down = max(down, up + 1)

        return max(up, down)
