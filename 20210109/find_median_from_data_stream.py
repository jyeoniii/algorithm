# https://leetcode.com/problems/find-median-from-data-stream/

# Time Complexity: O(n)
class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        if not self.arr:
            self.arr.append(num)
            return

        lo, hi = 0, len(self.arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if self.arr[mid] > num: hi = mid
            else: lo = mid+1
        self.arr.insert(lo, num)

    def findMedian(self) -> float:
        l = len(self.arr)
        if l % 2 == 0: return (self.arr[l//2-1] + self.arr[l//2]) / 2
        else: return self.arr[l//2]


import heapq

# Time Complexity: O(logn)
class MedianFinder:

    def __init__(self):
        self.left = []  # max heap
        self.right = []  # min heap

    def addNum(self, num: int) -> None:
        if not self.left:
            heapq.heappush(self.left, -num)
            return

        if len(self.left) <= len(self.right): # left length should be increased
            if num > self.right[0]:
                heapq.heappush(self.left, -heapq.heappop(self.right))
                heapq.heappush(self.right, num)
            else:
                heapq.heappush(self.left, -num)
        else: # right length should be increased
            if num < -self.left[0]:
                heapq.heappush(self.right, -heapq.heappop(self.left))
                heapq.heappush(self.left, -num)
            else:
                heapq.heappush(self.right, num)

    def findMedian(self) -> float:
        l = len(self.left) + len(self.right)
        if l % 2 == 0:
            return (-self.left[0] + self.right[0]) / 2
        else: # left length is always bigger than right length
            return -self.left[0]


class MedianFinder:

    def __init__(self):
        self.left = []  # max heap
        self.right = []  # min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)
        heapq.heappush(self.right, -heapq.heappop(self.left))
        if len(self.left) < len(self.right):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        l = len(self.left) + len(self.right)
        if l % 2 == 0:
            return (-self.left[0] + self.right[0]) / 2
        else: # left length is always bigger than right length
            return -self.left[0]