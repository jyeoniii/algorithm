# https://leetcode.com/problems/subsets/

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        bitmasks = [bin(i)[2:].zfill(len(nums)) for i in range(2 ** len(nums))]
        answer = []
        for bitmask in bitmasks:
            answer.append([nums[idx] for idx, x in enumerate(bitmask)])

        return answer

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def dfs(subset: List[int], nums_to_add: List[int]):
            answer.append(subset)
            for idx, num in enumerate(nums_to_add):
                dfs(subset + [num], nums_to_add[idx+1:])
        dfs([], nums)
        return answer