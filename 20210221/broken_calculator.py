# https://leetcode.com/problems/broken-calculator/

class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        cnt = 0
        while Y > X:
            if Y % 2 == 1:
                Y += 1
            else:
                Y //= 2
            cnt += 1
        return cnt + X - Y
