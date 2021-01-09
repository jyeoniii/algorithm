# https://www.algoexpert.io/questions/Array%20Of%20Products

from functools import reduce


def arrayOfProducts(array):
    total_product = reduce(lambda x, y: x * y, array)
    zero_count = array.count(0)

    return [total_product / x if x != 0
            else 0 if zero_count > 1 else reduce(lambda x, y: x * y, filter(lambda x: x != 0, array))
            for x in array]


def arrayOfProducts(array):
    total_product, total_product_without_zero, zero_count = 1, 1, 0
    for num in array:
        total_product *= num
        if num == 0: zero_count += 1
        else: total_product_without_zero *= num

    result = [0] * len(array)
    for i, x in enumerate(array):
        if x != 0: result[i] = total_product // x
        elif zero_count <= 1: result[i] = total_product_without_zero

    return result
