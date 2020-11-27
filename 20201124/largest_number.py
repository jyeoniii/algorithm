# https://leetcode.com/problems/largest-number/

from typing import List
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp_number(n1: str, n2: str) -> int:
            min_len = min(len(n1), len(n2))
            for i in range(min_len):
                if n1[i] != n2[i]:
                    return ord(n2[i]) - ord(n1[i])

            if len(n1) > min_len:
                return cmp_number(n1[min_len:], n2)
            elif len(n2) > min_len:
                return cmp_number(n1, n2[min_len:])
            else:
                return 0

        str_nums = map(str, nums)
        sorted_list = sorted(str_nums, key=cmp_to_key(cmp_number))
        return "0" if sorted_list[0] == "0" else "".join(sorted_list)


# https://leetcode.com/submissions/detail/423537502/
class Solution:
    class LargestNumber(str):
        def __lt__(x, y):
            return x + y > y + x

    def largestNumber(self, nums: List[int]) -> str:
        str_nums = map(str, nums)
        sorted_list = sorted(str_nums, key=self.LargestNumber)
        return "0" if sorted_list[0] == "0" else "".join(sorted_list)
