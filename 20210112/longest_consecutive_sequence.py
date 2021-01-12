# https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List


# Time Complexity: O(nlogn)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        cnt = 1
        answer = 1 if nums else 0
        print(nums)
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]: continue
            elif nums[i - 1] + 1 == nums[i]: cnt += 1
            else: cnt = 1
            answer = max(answer, cnt)

        return answer


# Time Complexity: O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for num in nums: s.add(num)

        answer = 0
        for num in s:
            if num - 1 not in s:
                curr_num = num
                len = 1
                while curr_num + 1 in s:
                    len += 1
                    curr_num += 1
                answer = max(answer, len)

        return answer
