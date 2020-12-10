# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3561/

from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 or arr[0] >= arr[1]: return False
        increasing = True
        for i in range(1, len(arr)):
            if arr[i-1] < arr[i]:
                if not increasing: return False
            elif arr[i-1] == arr[i]:
                return False
            else:
                if increasing: increasing = False
        return increasing == False
