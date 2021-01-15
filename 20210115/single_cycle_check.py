# https://www.algoexpert.io/questions/Single%20Cycle%20Check


def hasSingleCycle(array):
    i, cnt = 0, 0
    while array[i] != float("inf"):
        tmp = array[i]
        array[i] = float("inf")
        i = (i + tmp) % len(array)
        cnt += 1

    return cnt == len(array) and i == 0
