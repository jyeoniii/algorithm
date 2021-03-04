# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3656/


class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        pos = { c: i for i, c in enumerate(keyboard) }
        cost, currPos = 0, 0
        for c in word:
            cost += abs(pos[c] - currPos)
            currPos = pos[c]
        return cost