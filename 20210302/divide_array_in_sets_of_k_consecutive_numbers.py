# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

from collections import Counter, OrderedDict
from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0: return False
        nums.sort()
        counter = Counter(nums)
        for key in counter.keys():
            while counter[key] > 0:
                for x in range(k):
                    if key + x not in counter or counter[key + x] == 0:
                        return False
                    counter[key + x] -= 1
        return True


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0: return False
        counter = OrderedDict(sorted(Counter(nums).items()))
        for key in counter.keys():
            cnt = counter[key]
            if counter[key] > 0:
                for x in range(k):
                    if key + x not in counter or counter[key + x] < cnt:
                        return False
                    counter[key + x] -= cnt
        return True


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0: return False
        counter = Counter(nums)
        for num in counter.keys():
            min_num = num
            while min_num - 1 in counter and counter[min_num - 1] > 0: min_num -= 1

            for x in range(min_num, num + 1):
                while counter[x] > 0:
                    for i in range(k):
                        if x + i not in counter or counter[x + i] == 0: return False
                        counter[x + i] -= 1

        return True


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0: return False
        counter = Counter(nums)
        for num in nums:
            min_num = num
            while min_num - 1 in counter and counter[min_num - 1] > 0: min_num -= 1

            for x in range(min_num, num + 1):
                cnt = counter[x]
                if cnt == 0: continue
                for i in range(k):
                    if x + i not in counter or counter[x + i] < cnt: return False
                    counter[x + i] -= cnt

        return True