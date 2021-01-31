#https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/583/week-5-january-29th-january-31st/3623/

from typing import List
import bisect


# Time Complexity: O(nlogn)
# Space Complexity: O(n)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        tmp = []
        for i in range(len(nums) - 1, 0, -1):
            tmp.append(nums[i])
            if nums[i - 1] < nums[i]:
                tmp.append(nums[i-1])
                break
        else:
            nums.sort()
            return

        tmp.sort()
        idx = bisect.bisect_right(tmp, nums[i-1])
        if idx == len(tmp): idx -= 1
        nums[i-1], nums[i:] = tmp[idx], tmp[:idx] + tmp[idx+1:]


# Monotone Stack
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            if stack and stack[-1] > nums[i]:
                j = len(nums)-1
                while len(stack) > 1 and stack[-2] > nums[i]:
                    nums[j] = stack.pop()
                    j -= 1
                tmp, nums[i] = nums[i], stack.pop()
                stack.append(tmp)
                while stack:
                    nums[j] = stack.pop()
                    j -= 1
                break
            else:
                stack.append(nums[i])
        else:
            for i in range(len(nums)-1, -1, -1):
                nums[i] = stack.pop()


# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def reverseList(self, li: List[int], l: int, r: int):
        while l < r:
            li[l], li[r] = li[r], li[l]
            l += 1
            r -= 1

    def nextPermutation(self, nums: List[int]) -> None:
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                idx = i
                break
        else:
            self.reverseList(nums, 0, len(nums)-1)
            return

        idx_to_swap = idx
        for j in range(idx, len(nums)):
            if nums[j] > nums[idx-1]: idx_to_swap = j
            else: break

        nums[idx-1], nums[idx_to_swap] = nums[idx_to_swap], nums[idx-1]
        self.reverseList(nums, idx, len(nums)-1)