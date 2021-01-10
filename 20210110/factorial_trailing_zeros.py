# https://leetcode.com/problems/factorial-trailing-zeroes/


class Solution:
    def trailingZeroes(self, n: int) -> int:
        two_count = 0
        five_count = 0
        for i in range(1, n + 1):
            two_count += i // 2
            five_count += i // 5

        return min(two_count, five_count)


class Solution:
    def trailingZeroes(self, n: int) -> int:
        five_count = 0
        for i in range(1, n + 1):
            while i % 5 == 0:
                i /= 5
                five_count += 1

        return five_count

# https://leetcode.com/problems/factorial-trailing-zeroes/discuss/52399/My-python-solution-in-O(1)-space-O(logN)-time
class Solution(object):
    def trailingZeroes(self, n):
        cnt = 0
        while n > 0:
            n = n // 5
            cnt += n

        return cnt