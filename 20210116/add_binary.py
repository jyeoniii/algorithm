# https://leetcode.com/problems/add-binary/


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a)-1, len(b)-1
        carry = 0
        result = ''
        while i >= 0 or j >= 0:
            a_bit = int(a[i]) if i >= 0 else 0
            b_bit = int(b[j]) if j >= 0 else 0
            sum = a_bit + b_bit + carry
            carry = 1 if sum >= 2 else 0
            result += str(sum % 2)
            i -= 1
            j -= 1

        if carry: result += '1'
        return result[::-1]


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = list(a), list(b)
        carry = 0
        result = ''
        while a or b:
            if a: carry += int(a.pop())
            if b: carry += int(b.pop())
            result += str(carry % 2)
            carry = carry // 2

        if carry: result += '1'
        return result[::-1]