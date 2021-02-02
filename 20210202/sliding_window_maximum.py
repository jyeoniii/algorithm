# https://leetcode.com/problems/sliding-window-maximum/

from typing import List
import heapq
from collections import deque


# Time Complexity: O(nlogk)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = [float("-inf")] * (len(nums) - k + 1)
        h = [(-nums[i], i) for i in range(k)]
        heapq.heapify(h)

        ans[0] = -h[0][0]
        for i in range(1, len(ans)):  # i: start idx of sliding window
            while h and h[0][1] < i: heapq.heappop(h)
            heapq.heappush(h, (-nums[i+k-1], i+k-1))
            ans[i] = -h[0][0]

        return ans


# Time Complexity: O(n)
# Monotone Queue: https://stonejjun.tistory.com/126
class Solution:
    def maxSlidingWindow(self, nums, k):
        queue, ans = deque(), []  # queue: list of index where nums[index] is decreasing
        for i, n in enumerate(nums):
            while queue and nums[queue[-1]] < n: queue.pop()
            queue.append(i)
            if queue[0] == i - k: queue.popleft()
            if i >= k - 1: ans.append(nums[queue[0]])

        return ans

