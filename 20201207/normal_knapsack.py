# https://www.acmicpc.net/problem/12865

def solutionNK():
    N, K = map(int, input().split(" "))

    dp = [[0] * (K+1) for _ in range(N)] # dp[i][k]: i번째 짐까지 보았을때,의 무게 제한이 k일 때의 max value 값
    for i in range(N):
        W, V = map(int, input().split(" "))
        for k in range(K+1):
            if k < W:
                dp[i][k] = dp[i-1][k]
            else:
                dp[i][k] = max(dp[i-1][k], dp[i-1][k-W] + V)

    print(dp[-1][-1])

def solutionK():
    N, K = map(int, input().split(" "))

    dp = [0] * (K+1) # dp[k]: 무게 제한이 k일 때의 max value 값
    for i in range(N):
        W, V = map(int, input().split(" "))
        for k in range(K, -1, -1):
            if k >= W:
                dp[k] = max(dp[k], dp[k-W] + V)

    print(dp[-1])

if __name__ == "__main__":
    solutionK()
