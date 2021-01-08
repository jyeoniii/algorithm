# https://www.algoexpert.io/questions/Three%20Number%20Sum

from collections import defaultdict
import random
import time


def threeNumberSum(array, targetSum):
    d = defaultdict(list)
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            d[array[i] + array[j]].append([i, j])

    answer = []
    for i, n in enumerate(array):
        if targetSum - n in d:
            answer.extend(sorted([array[i], array[j], array[k]]) for j, k in d[targetSum-n] if i > k)

    return sorted(answer)


def threeNumberSum2(array, targetSum):
    array.sort()
    answer = []
    for l in range(len(array)-2):
        m, r = l+1, len(array)-1
        while m < r:
            sum = array[l] + array[m] + array[r]
            if sum < targetSum: m += 1
            elif sum > targetSum: r -= 1
            else:
                answer.append([array[l], array[m], array[r]])
                m += 1
                r -= 1

    return answer


if __name__ == "__main__":
    arr = [random.randint(-100, 100) for _ in range(100)]
    start = time.time()
    result1 = threeNumberSum(arr, 24)
    print(f"elapsed {time.time() - start} ms")

    start = time.time()
    result2 = threeNumberSum2(arr, 24)
    print(f"elapsed {time.time() - start} ms")


