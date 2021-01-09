# https://www.algoexpert.io/questions/Monotonic%20Array

INC, DEC = 1, -1
def isMonotonic(array):
    if len(array) <= 2: return True

    direction = None
    for i in range(1, len(array)):
        if array[i-1] == array[i]: continue

        curr_direction = INC if array[i-1] < array[i] else DEC
        if direction is None: direction = curr_direction
        elif direction != curr_direction: return False

    return True
