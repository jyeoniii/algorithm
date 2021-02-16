# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3642/

from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def helper(i: int, curr: List[str]) -> List[str]:
            if i == len(S): return curr
            return helper(
                i + 1,
                [s + S[i] for s in curr] if S[i].isdigit() else
                [s + S[i].upper() for s in curr] + [s + S[i].lower() for s in curr]
            )

        return helper(0, [''])