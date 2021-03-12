# https://leetcode.com/problems/sliding-window-median/

from typing import List
import bisect
import heapq

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = sorted(nums[:k])
        def getMedian(window):
            return (window[k // 2] + window[k // 2 - 1]) / 2 if k % 2 == 0 else window[k // 2]

        answer = [getMedian(window)]
        for r in range(k, len(nums)):
            bisect.insort(window, nums[r])
            i = bisect.bisect_left(window, nums[r-k])
            del window[i]
            answer.append(getMedian(window))

        return answer


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        left, right, answer = [], [], []

        for i, num in enumerate(nums):
            heapq.heappush(right, -heapq.heappushpop(left, -num))
            if len(left) < len(right):
                heapq.heappush(left, -heapq.heappop(right))

            if i >= k-1:
                answer.append((-left[0] + right[0]) / 2 if k % 2 == 0 else -left[0])

                # Remove
                h = left if nums[i-k+1] <= -left[0] else right
                idx = h.index(nums[i-k+1] if h == right else -nums[i-k+1])
                h[idx] = h[-1]
                del h[-1]
                heapq.heapify(h)

        return answer
