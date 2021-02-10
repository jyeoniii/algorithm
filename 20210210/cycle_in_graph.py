# https://www.algoexpert.io/questions/Cycle%20In%20Graph


def cycleInGraph(edges):
    no_cycle = set()
    def hasCycle(v, visited):
        visited.add(v)
        result = False
        for e in edges[v]:
            if e in no_cycle: continue
            if e in visited or hasCycle(e, visited):
                result = True
                break
            else:
                no_cycle.add(e)

        visited.remove(v)
        return result

    for v in range(len(edges)):
        if hasCycle(v, set()): return True
    return False
