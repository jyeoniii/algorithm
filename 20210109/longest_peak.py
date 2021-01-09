# https://www.algoexpert.io/questions/Longest%20Peak


def longestPeak(array):
    i, answer = 1, 0
    while i < len(array) - 1:
        if array[i - 1] < array[i] and array[i] > array[i + 1]:  # peak
            l = 1
            for j in range(i - 1, -1, -1):
                if array[j] < array[j + 1]: l += 1
                else: break
            for j in range(i + 1, len(array)):
                if array[j - 1] > array[j]: l += 1
                else: break

            answer = max(answer, l)
            i = j
        else:
            i += 1

    return answer

