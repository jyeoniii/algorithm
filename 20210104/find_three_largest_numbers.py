# https://www.algoexpert.io/questions/Find%20Three%20Largest%20Numbers


def findThreeLargestNumbers(array):
    array.append(float("-inf"))
    result = [-1] * 3
    for i, x in enumerate(array):
        if x > array[result[2]]:
            result[2], result[1], result[0] = i, result[2], result[1]
        elif x > array[result[1]]:
            result[1], result[0] = i, result[1]
        elif x > array[result[0]]:
            result[0] = i

    return list(map(lambda x: array[x], result))



