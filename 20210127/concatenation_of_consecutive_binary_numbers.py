# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3618/


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        answer = ""
        for num in range(1, n+1):
            answer += bin(num)[2:]

        return int(answer, 2) % 1000000007


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        def helper(x: int) -> str:
            if x == 0: return ''
            return helper(x-1) + bin(x)[2:]
        return int(helper(n), 2) % 1000000007


