# https://www.algoexpert.io/questions/Subarray%20Sort


def subarraySort(array):
    stack = []
    max_val = 0
    min_idx, max_idx = float("inf"), float("-inf")
    for i, num in enumerate(array):
        if stack and stack[-1][0] > num:
            max_idx = max(max_idx, i)
            while stack and stack[-1][0] > num:
                val, idx = stack.pop()
                max_val = max(max_val, val)
                min_idx = min(min_idx, idx)
        stack.append((num, i))
        if num < max_val: max_idx = i

    return [min_idx, max_idx] if len(stack) != len(array) else [-1, -1]


def subarraySort(array):
    min_val, max_val = float("inf"), float("-inf")

    def isInvalid(i) -> bool:
        if i == 0: return array[i] > array[i + 1]
        elif i == len(array) - 1: return array[i - 1] > array[i]
        else: return array[i - 1] > array[i] or array[i] > array[i + 1]

    for i, num in enumerate(array):
        if isInvalid(i): min_val, max_val = min(num, min_val), max(num, max_val)

    if min_val == float("inf"): return [-1, -1]

    min_idx, max_idx = 0, len(array) - 1
    while min_val >= array[min_idx]: min_idx += 1
    while max_val <= array[max_idx]: max_idx -= 1

    return [min_idx, max_idx]
