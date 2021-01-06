# https://leetcode.com/problems/basic-calculator/

class Solution:
    def calculate(self, s: str) -> int:
        def calcParenthesis(idx: int):  # return [computed value in parenthesis, idx of ')']
            stack = []
            op, last_op_idx = '+', idx - 1
            while idx < len(s) and s[idx] != ')':
                if s[idx] == '(':
                    val, next_idx = calcParenthesis(idx + 1)
                    idx = next_idx
                    stack.append(val if op == '+' else -val)
                elif s[idx].isdigit():  # number
                    if idx == len(s) - 1 or not s[idx + 1].isdigit():
                        num = int(s[last_op_idx + 1:idx + 1])
                        stack.append(num if op == '+' else -num)
                elif s[idx] != ' ':  # operator
                    op, last_op_idx = s[idx], idx
                idx += 1

            return sum(stack), idx

        return calcParenthesis(0)[0]


from typing import List

# For Further Implementation
# Division: https://stackoverflow.com/questions/5535206/negative-integer-division-surprising-result
class GenericCalculator:

    def _calc(self, stack: List[int], num: int, op: str):
        if op == '+': stack.append(num)
        elif op == '-': stack.append(-num)
        elif op == '*': stack.append(stack.pop() * num)
        else: stack.append(int(float(stack.pop()) / num))

    def calculate(self, s: str) -> int:
        def calcParenthesis(idx: int):  # return [computed value in parenthesis, idx of ')']
            stack = []
            op, last_op_idx = '+', idx - 1
            while idx < len(s) and s[idx] != ')':
                if s[idx] == '(':
                    num, next_idx = calcParenthesis(idx + 1)
                    idx = next_idx
                    self._calc(stack, num, op)
                elif s[idx].isdigit():  # number
                    if idx == len(s) - 1 or not s[idx + 1].isdigit():
                        num = int(s[last_op_idx + 1:idx + 1])
                        self._calc(stack, num, op)
                elif s[idx] != ' ':  # operator
                    op, last_op_idx = s[idx], idx
                idx += 1
            return sum(stack), idx

        return calcParenthesis(0)[0]

if __name__ == "__main__":
    s = GenericCalculator()
    assert -31 == s.calculate("(6+2)/2 + (3+4) *(2-7)")
    assert 22 == s.calculate("((6+2)/2 + (3+4) *(7-7/3))/2 + 3")
    assert 6 == s.calculate("3 + 4-3/2 + (3*4)/(1-3*5)+2/3")
    assert -162 == s.calculate("3 + 4-3/2 + (3*4)*(1-3*5)+2/3")