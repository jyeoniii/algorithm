# https://www.algoexpert.io/questions/Smallest%20Difference

def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    i, j = 0, 0
    answer, pair = float("inf"), []
    while i < len(arrayOne) and j < len(arrayTwo):
        diff = abs(arrayOne[i] - arrayTwo[j])
        if diff < answer:
            answer, pair = diff, [arrayOne[i], arrayTwo[j]]
        if arrayOne[i] < arrayTwo[j]: i += 1
        elif arrayOne[i] > arrayTwo[j]: j += 1
        else: break

    return pair
