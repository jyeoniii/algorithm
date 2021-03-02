# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3658/


from collections import defaultdict, Counter
from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        N = len(nums)
        c, total, answer = defaultdict(int), sum(nums), []
        for num in nums:
            c[num] += 1
            if c[num] > 1:
                answer.append(num)
                answer.append(N * (N + 1) // 2 - total + num)
                break

        return answer


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c, answer = Counter(nums), [0] * 2
        for x in range(1, len(nums) + 1):
            if x not in c:
                answer[1] = x
            elif c[x] > 1:
                answer[0] = x

        return answer