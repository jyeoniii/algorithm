# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3607/

import itertools
import functools


class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[0] * 5 for _ in range(n + 1)]
        for x in range(5): dp[1][x] = 1

        for i in range(2, n + 1):
            for x in range(5):
                dp[i][x] = sum(dp[i - 1][j] for j in range(x, 5))

        return sum(dp[-1])


class Solution:
    def countVowelStrings(self, n: int) -> int:
        @functools.lru_cache(None)
        # number of strings that starts with vowels[vowel_idx] and having length=str_idx
        def helper(vowel_idx: int, str_idx: int) -> int:
            if str_idx == 0 or vowel_idx == 4: return 1
            return helper(vowel_idx, str_idx-1) + helper(vowel_idx+1, str_idx)

        return helper(0, n)


class Solution:
    def countVowelStrings(self, n: int) -> int:
        @functools.lru_cache(None)
        # number of strings that starts with vowels[vowel_idx] and having length=str_idx
        def helper(vowel_idx: int, str_idx: int) -> int:
            if str_idx == 0 or vowel_idx == 4: return 1
            return sum(helper(i, str_idx-1) for i in range(vowel_idx, 5))

        return helper(0, n)


class Solution:
    def countVowelStrings(self, n: int) -> int:
        return len(list(itertools.combinations_with_replacement(range(5), n)))
