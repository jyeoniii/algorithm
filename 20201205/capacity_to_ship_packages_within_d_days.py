# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        max_weight = max(weights)
        lo, hi = max_weight, max_weight * len(weights) // D + 1

        def find_days_to_ship(capacity: int) -> int:
            nonlocal D
            day_count = 1
            curr_weight = 0
            for weight in weights:
                if curr_weight + weight <= capacity:
                    curr_weight += weight
                else:
                    day_count += 1
                    if day_count > D: break
                    curr_weight = weight
            return day_count

        capacity = 0
        while True:
            new_capacity = (lo + hi) // 2
            if capacity == new_capacity: break
            else: capacity = new_capacity

            day_count = find_days_to_ship(capacity)

            if day_count > D: lo = capacity + 1
            elif day_count <= D: hi = capacity
            else: break

        tmp = capacity - 1
        while tmp >= max_weight and day_count <= D:
            day_count = find_days_to_ship(tmp)
            if day_count <= D:
                capacity = tmp
                tmp = capacity - 1

        return capacity


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        max_weight = max(weights)
        lo, hi = max_weight, max_weight * len(weights) // D + 1

        def find_days_to_ship(capacity: int) -> int:
            nonlocal D
            day_count = 1
            curr_weight = 0
            for weight in weights:
                if curr_weight + weight <= capacity:
                    curr_weight += weight
                else:
                    day_count += 1
                    if day_count > D: break
                    curr_weight = weight
            return day_count

        capacity = 0
        while True:
            new_capacity = (lo + hi) // 2
            if capacity == new_capacity: break
            else: capacity = new_capacity

            day_count = find_days_to_ship(capacity)

            if day_count > D: lo = capacity + 1
            else: hi = capacity

        return capacity


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        max_weight = max(weights)
        lo, hi = max_weight, max_weight * len(weights) // D + 1

        def can_ship(capacity: int) -> bool:
            nonlocal D
            day_count = 1
            curr_weight = 0
            for weight in weights:
                if curr_weight + weight <= capacity:
                    curr_weight += weight
                else:
                    day_count += 1
                    if day_count > D: break
                    curr_weight = weight
            return day_count <= D

        while lo < hi:
            capacity = (lo + hi) // 2

            if can_ship(capacity): hi = capacity
            else: lo = capacity + 1

        return lo