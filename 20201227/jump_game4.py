# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/572/week-4-december-22nd-december-28th/3582/

from typing import List
from collections import defaultdict, deque


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        d = defaultdict(list)
        for i, num in enumerate(arr):
            d[num].append(i)

        queue = deque([(0, 0)])
        visited = [False] * len(arr)
        visited[0] = True
        visited_values = {0:True}

        while queue:  # BFS
            i, dist = queue.popleft()
            if i == len(arr)-1: return dist

            for j in [i-1, i+1]:
                if 0 <= j < len(arr) and not visited[j]:
                    visited[j] = True
                    queue.append((j, dist+1))

            if arr[i] not in visited_values:
                for j in d[arr[i]]:
                    if not visited[j]:
                        visited[j] = True
                        queue.append((j, dist + 1))
                visited_values[arr[i]] = True


# import bisect
#
#
# # Wrong Answer
# class Solution:
#     def minJumps(self, arr: List[int]) -> int:
#         d = defaultdict(list)
#         for i, num in enumerate(arr):
#             d[num].append(i)
#
#         dp = [len(arr)] * len(arr)
#         dp[len(arr) - 1] = 0
#
#         for i in range(len(arr) - 1, -1, -1):
#             if i < len(arr)-1:
#                 dp[i] = min(dp[i + 1] + 1, dp[i])
#                 if i - 1 >= 0: dp[i] = min(dp[i - 1] + 1, dp[i])
#
#             j = bisect.bisect_left(d[arr[i]], i)
#             idx_list = d[arr[i]][:j]
#             for x in idx_list:
#                 if dp[x] + 1 < dp[i]: dp[i] = dp[x] + 1
#
#             for x in idx_list: dp[x] = min(dp[x], dp[i] + 1)
#
#         return dp[0]
