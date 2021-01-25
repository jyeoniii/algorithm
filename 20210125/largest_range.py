# https://www.algoexpert.io/questions/Largest%20Range


def largestRange(array):
    s = set(array)
    start, end = array[0], array[0]

    for num in array:
        if num - 1 in s: continue
        l, r = num, num
        while r + 1 in s: r += 1
        if r - l > end - start: start, end = l, r

    return [start, end]
