# https://www.algoexpert.io/questions/Four%20Number%20Sum


# Time Complexity: O(n^3)
def fourNumberSum(array, targetSum):
    array.sort()
    answer = []
    for first in range(len(array) - 3):
        for fourth in range(len(array) - 1, first + 2, -1):
            second, third = first + 1, fourth - 1
            while second < third:
                s = array[first] + array[second] + array[third] + array[fourth]
                if s == targetSum:
                    answer.append([array[first], array[second], array[third], array[fourth]])
                    second += 1
                    third -= 1
                elif s < targetSum:
                    second += 1
                else:
                    third -= 1

    return answer


from collections import defaultdict


# Time Complexity: O(n^2)
def fourNumberSum(array, targetSum):
    d = defaultdict(list)
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            d[array[i] + array[j]].append([i, j])

    answer = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            target = targetSum - array[i] - array[j]
            for li in d[target]:
                if j < li[0]:
                    answer.append(list(map(lambda x: array[x], [i, j] + li)))

    return answer


