# https://www.algoexpert.io/questions/Move%20Element%20To%20End


def moveElementToEnd(array, toMove):
    i, j = 0, len(array) - 1
    while i < j:
        while i < j and array[j] == toMove: j -= 1
        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]
        i += 1

    return array

