# https://www.algoexpert.io/questions/Sort%20K-Sorted%20Array

# Time Complexity: O(nlogk)
def sortKSortedArray(array, k):
    for i in range(len(array)):
        array[i:i+k+1] = sorted(array[i:i+k+1])
    return sorted(array)


import heapq

# Time Complexity: O(nlogk)
def sortKSortedArray(array, k):
    h, answer = [], []
    for num in array:
        heapq.heappush(h, num)
        if len(h) > k: answer.append(heapq.heappop(h))

    while h: answer.append(heapq.heappop(h))
    return answer

