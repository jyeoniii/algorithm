# https://leetcode.com/problems/basic-calculator-ii/

from collections import deque


class Solution:
    def _calc(self, op1: int, op2: int, operator: str):
        if operator == '+': return op1 + op2
        elif operator == '-': return op1 - op2
        elif operator == '*': return op1 * op2
        else: return op1 // op2

    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        queue = deque()
        last_op_idx = -1
        for i, c in enumerate(s):
            if c.isdigit():
                if i == len(s) - 1 or not s[i + 1].isdigit():
                    num = int(s[last_op_idx + 1:i + 1])
                    if queue and (queue[-1] == '*' or queue[-1] == '/'):
                        operator, operand = queue.pop(), queue.pop()
                        queue.append(self._calc(operand, num, operator))
                    else:
                        queue.append(num)
            else:
                queue.append(c)
                last_op_idx = i

        while len(queue) > 1:
            op1, operator, op2 = queue.popleft(), queue.popleft(), queue.popleft()
            queue.appendleft(self._calc(op1, op2, operator))

        return queue.pop()


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        op, last_op_idx = '+', -1
        for i, c in enumerate(s):
            if c: continue
            elif c.isdigit():
                if i == len(s) - 1 or not s[i + 1].isdigit():
                    num = int(s[last_op_idx + 1:i + 1])
                    if op == '+': stack.append(num)
                    elif op == '-': stack.append(-num)
                    elif op == '*': stack.append(stack.pop() * num)
                    elif op == '/':
                        tmp = stack.pop()
                        stack.append(tmp // num if tmp % num == 0 else tmp // num + (0 if tmp > 0 else 1))
            else:
                op, last_op_idx = c, i

        return sum(stack)
