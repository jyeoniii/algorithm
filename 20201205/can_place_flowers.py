# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3555/

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while n and i < len(flowerbed):
            if flowerbed[i] == 1:
                i += 2
            else:
                if i+1 < len(flowerbed):
                    if flowerbed[i+1] == 0: # adjacent flowerbed is empty
                        n -= 1
                        i += 2
                    else:
                        i += 3
                else: # no adjacent flowerbed
                    n -= 1
                    i += 2

        return n == 0

