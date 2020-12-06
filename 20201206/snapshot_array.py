# https://leetcode.com/problems/snapshot-array/

class SnapshotArray:
    def __init__(self, length: int):
        self.arr = [(-1, 0)] * length
        self.history = {}
        self.snap_id = -1

    def set(self, index: int, val: int) -> None:
        if self.snap_id >= 0:
            prev_snap_id, prev_value = self.arr[index]
            tmp = self.snap_id
            while prev_snap_id < tmp:
                self.history[(index, tmp)] = prev_value
                tmp -= 1

        self.arr[index] = (self.snap_id, val)

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id

    def get(self, index: int, snap_id: int) -> int:
        if (index, snap_id) in self.history:
            return self.history[(index, snap_id)]
        else:
            return self.arr[index][1]


import bisect


# Make self.arr[index] short by overwriting value of self snap_id
# set: O(logK), where K is number of snap()
# get: O(logK), where K is number of snap()
class SnapshotArray:
    def __init__(self, length: int):
        self.arr = [[(0, 0)] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        idx = bisect.bisect_left(self.arr[index], (self.snap_id, 0))
        if idx == len(self.arr[index]):
            self.arr[index].append((self.snap_id, val))
        else:
            self.arr[index][idx] = (self.snap_id, val)

    def snap(self) -> int:
        answer, self.snap_id = self.snap_id, self.snap_id + 1
        return answer

    def get(self, index: int, snap_id: int) -> int:
        if snap_id > self.snap_id: return 0

        li = self.arr[index]
        found_index = bisect.bisect_left(li, (snap_id, 0))
        if found_index >= len(li):
            return li[-1][1]

        return li[found_index][1] if li[found_index][0] == snap_id else li[found_index-1][1]


# Simply append every value whenever set() is called
# set: O(1)
# get: O(logK), where K is number of set() is called
class SnapshotArray:
    def __init__(self, length: int):
        self.arr = [[(0, 0)] for _ in range(length)]
        self.snap_id = 0
        self.MAX_INT = float("inf")

    def set(self, index: int, val: int) -> None:
        self.arr[index].append((self.snap_id, val))

    def snap(self) -> int:
        answer, self.snap_id = self.snap_id, self.snap_id + 1
        return answer

    def get(self, index: int, snap_id: int) -> int:
        if snap_id > self.snap_id: return 0

        li = self.arr[index]
        found_index = bisect.bisect_right(li, (snap_id, self.MAX_INT))

        return li[found_index-1][1]


# Does not use bisect, Implement binary search
class SnapshotArray:
    def __init__(self, length: int):
        self.arr = [[(0, 0)] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.arr[index].append((self.snap_id, val))

    def snap(self) -> int:
        answer, self.snap_id = self.snap_id, self.snap_id + 1
        return answer

    def get(self, index: int, snap_id: int) -> int:
        if snap_id >= self.snap_id: return 0

        li = self.arr[index]
        lo, hi = 0, len(li)
        while lo < hi:
            mid = (lo + hi) // 2
            if li[mid][0] <= snap_id:
                lo = mid + 1
            else:
                hi = mid

        return li[lo-1][1]
