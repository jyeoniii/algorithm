# https://www.algoexpert.io/questions/Task%20Assignment


def taskAssignment(k, tasks):
    sorted_tasks = sorted((x, i) for i, x in enumerate(tasks))
    l, r = 0, len(tasks)-1
    answer = []
    while l < r:
        answer.append([sorted_tasks[l][1], sorted_tasks[r][1]])
        l += 1
        r -= 1
    return answer
