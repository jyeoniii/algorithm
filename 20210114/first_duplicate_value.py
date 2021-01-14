# https://www.algoexpert.io/questions/First%20Duplicate%20Value

# Time Complexity: O(N)
# Space Complexity: O(N)
def firstDuplicateValue(array):
    s = set()
    for num in array:
        if num in s: return num
        s.add(num)
    return -1

# Time Complexity: O(N)
# Space Complexity: O(1)
def firstDuplicateValue(array):
    for num in array:
        abs_val = abs(num)
        if array[abs_val-1] < 0: return abs_val
        array[abs_val-1] *= -1
    return -1