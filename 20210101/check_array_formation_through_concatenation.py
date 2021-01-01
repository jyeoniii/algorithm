# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3589/

from typing import List

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        pieces.sort(key=lambda x: x[0])
        i = 0
        while i < len(arr):
            lo, hi = 0, len(pieces)
            while lo < hi:
                mid = (lo + hi) // 2
                if pieces[mid][0] == arr[i]:
                    if pieces[mid] == arr[i:i+len(pieces[mid])]:
                        i += len(pieces[mid])
                        break
                    else: return False
                elif pieces[mid][0] < arr[i]: lo = mid+1
                else: hi = mid
            else: return False

        return i == len(arr)


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        d = {x[0]: x for x in pieces}

        result = []
        for num in arr:
            if num in d: result += d[num]
        return result == arr


