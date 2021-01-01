# https://leetcode.com/problems/sum-of-subarray-minimums/

from typing import List


# https://leetcode.com/problems/sum-of-subarray-minimums/discuss/170750/C%2B%2BJavaPython-Stack-Solution
# https://leetcode.com/problems/sum-of-subarray-minimums/discuss/178876/stack-solution-with-very-detailed-explanation-step-by-step
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        s1, s2 = [], []
        left, right = [0] * len(arr), [0] * len(arr)

        for i in range(len(arr)):
            cnt = 1
            while s1 and s1[-1][0] > arr[i]: cnt += s1.pop()[1]
            s1.append((arr[i], cnt))
            left[i] = cnt

        for i in range(len(arr)-1, -1, -1):
            cnt = 1
            while s2 and s2[-1][0] >= arr[i]: cnt += s2.pop()[1]
            s2.append((arr[i], cnt))
            right[i] = cnt

        return sum(x * l * r for x, l, r in zip(arr, left, right)) % (10**9 + 7)