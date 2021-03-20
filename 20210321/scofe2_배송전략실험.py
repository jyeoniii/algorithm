# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N = int(input())
road = list(input())
dp = [0] * N # dp[i]: i번째 배송지까지 도달할 수 있는 경우의 수
dp[0], dp[1] = 1, 0 if road[1] == '0' else 1
for i in range(2, N):
	if road[i] == '0':
		continue
	dp[i] = dp[i-2] + dp[i-1]

print(dp[-1])
