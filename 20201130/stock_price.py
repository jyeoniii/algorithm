# https://programmers.co.kr/learn/courses/30/lessons/42584?language=python3

def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = []
    for i in range(len(prices)):
        while stack and prices[i] < stack[-1][1]:
            (idx, last_price) = stack.pop()
            answer[idx] = i - idx
        stack.append((i, prices[i]))

    while stack:
        (idx, last_price) = stack.pop()
        answer[idx] = len(prices) - 1 - idx

    return answer