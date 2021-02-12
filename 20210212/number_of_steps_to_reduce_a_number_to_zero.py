# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3637/


class Solution:
    def numberOfSteps(self, num: int) -> int:
        cnt = 0
        while num > 0:
            if num % 2 == 0: num //= 2
            else: num -= 1
            cnt += 1
        return cnt