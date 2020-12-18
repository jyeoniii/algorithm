# https://programmers.co.kr/learn/courses/30/lessons/60058

from typing import Tuple


def find_balanced(s: str) -> Tuple[str, str]:
    cnt = 0
    for i, c in enumerate(s):
        cnt += 1 if c == '(' else -1
        if cnt == 0:
            return s[:i + 1], s[i + 1:]


def is_valid(s) -> bool:
    cnt = 0
    for c in s:
        cnt += 1 if c == '(' else -1
        if cnt < 0: return False
    return True


def solution(p):
    if not p or is_valid(p): return p

    u, v = find_balanced(p)
    if is_valid(u):
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + ''.join(['(' if c == ')' else ')' for c in u[1:len(u) - 1]])
