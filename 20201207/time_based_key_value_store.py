# https://leetcode.com/problems/time-based-key-value-store/

from collections import defaultdict
import bisect

class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = defaultdict(list)
        self.MAX_STRING = "z" * 100

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d: return ""
        li = self.d[key]
        idx = bisect.bisect_right(li, (timestamp, self.MAX_STRING))
        return li[idx-1][1] if idx > 0 else ""


class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d: return ""
        li = self.d[key]
        lo, hi = 0, len(li)
        while lo < hi:
            mid = (lo + hi) // 2
            if li[mid][0] <= timestamp:
                lo = mid + 1
            else:
                hi = mid

        return li[lo-1][1] if lo > 0 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
