# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3625/


class Solution:
    def hammingWeight(self, n: str) -> int:
        return bin(n).count('1')