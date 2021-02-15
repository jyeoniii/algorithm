# https://www.algoexpert.io/questions/Valid%20Starting%20City


def validStartingCity(distances, fuel, mpg):
    def isValid(i: int, N: int):
        fuel_remain = fuel[i] * mpg
        curr = (i + 1) % N
        while curr != i:
            fuel_remain -= distances[curr - 1]
            if fuel_remain < 0: return False

            fuel_remain += fuel[curr] * mpg
            curr = (curr + 1) % N

        return True

    for i in range(len(distances)):
        if isValid(i, len(distances)): return i


def validStartingCity(distances, fuel, mpg):
    min_cost, min_cost_idx, curr_cost = 0, 0, 0
    for i in range(1, len(distances)):
        curr_cost += (fuel[i - 1] * mpg) - distances[i - 1]
        if curr_cost < min_cost:
            min_cost, min_cost_idx = curr_cost, i

    return min_cost_idx

