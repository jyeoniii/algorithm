# https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/

from typing import List


# https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/discuss/987607/O(n)-explanation-with-picture
class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        pos = [i for i, x in enumerate(nums) if x == 1]
        prefix_sum = [0] * (len(pos) + 1)
        for i, n in enumerate(pos): prefix_sum[i + 1] = prefix_sum[i] + pos[i]  # prefix_sum[i]: nums[0]+..+nums[i-1]

        l, r, answer = 0, k - 1, float("inf")
        while r < len(pos):
            mid = (l + r) // 2
            left = prefix_sum[mid] - prefix_sum[l]
            right = prefix_sum[r + 1] - prefix_sum[mid + 1]

            dist = (k - 1) // 2
            if k % 2 == 1:
                answer = min(answer, right - left - dist * (dist + 1))
            else:
                answer = min(answer, right - left - dist * (dist + 1) - pos[mid] - (dist + 1))

            l += 1
            r += 1

        return answer
