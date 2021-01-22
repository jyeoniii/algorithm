# https://www.algoexpert.io/questions/Powerset


def powerset(array):
    def helper(idx: int):  # array[idx:]의 powerset
        if idx == len(array): return [[]]
        li = helper(idx + 1)
        li.extend([[array[idx]] + x for x in li])
        return li

    return helper(0)
