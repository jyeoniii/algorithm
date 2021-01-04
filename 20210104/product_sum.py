# https://www.algoexpert.io/questions/Product%20Sum

from functools import reduce

# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array, depth=1):
    result = 0
    for x in array:
        result += x if type(x) == int else productSum(x, depth + 1)
        return depth * result

def productSum(array, depth=1):
    return sum(x if type(x) == int else productSum(x, depth+1) for x in array) * depth

