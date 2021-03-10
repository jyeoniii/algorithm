# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3667/

class Solution:
    def intToRoman(self, num: int) -> str:
        mapping = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        answer, div = '', 1000
        while num > 0:
            q = num // div
            if not q:
                div //= 10
                continue

            if q == 4:
                answer += mapping[div * 1] + mapping[div * 5]
            elif q == 9:
                answer += mapping[div * 1] + mapping[div * 10]
            elif q < 5:
                answer += mapping[div] * q
            else:
                answer += mapping[5 * div] + (q - 5) * mapping[div]

            num -= q * div
            div //= 10

        return answer