# https://www.algoexpert.io/questions/Spiral%20Traverse

def spiralTraverse(array):
    M, N = len(array), len(array[0])
    arr = [0] * (M * N)
    di, dj, k = [0, 1, 0, -1], [1, 0, -1, 0], 0

    i, j, cnt = 0, 0, 0
    while cnt < M * N:
        arr[cnt] = array[i][j]
        array[i][j] = None
        cnt += 1

        next_i, next_j = i + di[k], j + dj[k]
        if 0 <= next_i < M and 0 <= next_j < N and array[next_i][next_j] is not None:
            i, j = next_i, next_j
        else:
            k = (k + 1) % 4
            i, j = i + di[k], j + dj[k]

    return arr


