# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3602/

from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j = 0, len(people) - 1
        answer = 0
        while i <= j:
            answer += 1
            if people[i] + people[j] <= limit: i += 1
            j -= 1

        return answer