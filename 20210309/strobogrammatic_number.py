# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3664/


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        d = { '0': '0', '1': '1', '6': '9', '8': '8', '9': '6' }
        return ''.join(d[c] if c in d else 'x' for c in reversed(num)) == num


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        d = { '0': '0', '1': '1', '6': '9', '8': '8', '9': '6' }
        for i in range(len(num)//2+1):
            if num[i] not in d or d[num[i]] != num[len(num)-1-i]:
                return False
        return True