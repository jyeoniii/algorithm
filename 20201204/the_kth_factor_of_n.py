# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3554/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        cnt = 0
        for num in range(1, n+1):
            if n % num == 0:
                cnt += 1
            if cnt == k:
                return num
        return -1