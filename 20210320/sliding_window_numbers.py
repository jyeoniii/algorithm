# Return if 3 X 3 Sliding Window contains [1,2...,8,9]

from collections import Counter


def solution(numbers):
    answers = [False] * (len(numbers[0])-2)
    c = Counter()
    for i in range(3):
        for j in range(3):
            c[numbers[i][j]] += 1

    answers[0] = len(c.keys()) == 9
    for j in range(len(numbers[0])-3):
        for i in range(3):
            c[numbers[i][j+3]] += 1
            c[numbers[i][j]] -= 1
            if c[numbers[i][j]] <= 0:
                del c[numbers[i][j]]
        answers[j+1] = len(c.keys()) == 9

    return answers


if __name__ == "__main__":
    numbers = [[1,2,3,2,5,7],[4,5,6,1,7,6],[7,8,9,4,8,3]]
    print(solution(numbers))



