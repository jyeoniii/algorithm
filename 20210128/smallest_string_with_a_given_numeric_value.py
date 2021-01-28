# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3619/


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        li, last_idx = [0] * n, 26

        for i in range(n - 1, -1, -1):
            while k - last_idx < i: last_idx -= 1
            li[i] = last_idx
            k -= last_idx

        return ''.join([chr(i+96) for i in li])


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        z_cnt, others = divmod(k, 26)
        while others < n - z_cnt:
            z_cnt -= 1
            others += 26

        a_cnt = max(0, n - z_cnt - 1)
        other_char = others - a_cnt

        return "a" * a_cnt + (chr(other_char + 96) if other_char > 0 else '') + 'z' * z_cnt