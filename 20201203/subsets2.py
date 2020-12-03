# https://leetcode.com/problems/subsets-ii/
from typing import List
from collections import Counter

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        num_count = Counter(nums)
        answer = []

        def dfs(subset: List[int], nums_to_add: List[int]):
            answer.append(subset)
            for i, num in enumerate(nums_to_add):
                for cnt in range(1, num_count[num]+1):
                    tmp = subset + [num] * cnt
                    dfs(tmp, nums_to_add[i+1:])

        dfs([], sorted(list(num_count.keys())))

        return answer
