# https://leetcode.com/problems/maximum-profit-in-job-scheduling/

from typing import List, Tuple
from collections import defaultdict
import bisect

# left to right
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        job_schedules = sorted(zip(startTime, endTime, profit), key=lambda k: k[1])
        end_time_sorted = [job_schedules[i][1] for i in range(n)]
        dp = [0]*(n+1)
        for i in range(1, n+1):
            start, end, pro = job_schedules[i-1]
            j = bisect.bisect_right(end_time_sorted, start, hi=i-1)
            dp[i] = max(dp[i-1], pro + dp[j])

        return dp[n]


# right to left
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        job_schedules = sorted(zip(startTime, endTime, profit), key=lambda k: k[0])
        start_time_sorted = [job_schedules[i][0] for i in range(n)]
        dp = [0]*(n+1) # dp[i]: n-1 ~ i번째 job까지 보았을 때, maximum profit
        for i in range(n-1, -1, -1):
            start, end, pro = job_schedules[i]
            j = bisect.bisect_left(start_time_sorted, end, i+1) # 현재까지 살펴본 job들 중, job[i]랑 겹치지 않은 leftmost element 찾기
            dp[i] = max(dp[i+1], pro + dp[j]) # 이 job을 포함하지 않은 직전 profit 과 이 job을 포함하며 겹치지 않는 구간의 profit중 최대값
        return dp[0]


# class Solution:
#     def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
#         maxTime = max(endTime)
#         dp = [0 for _ in range(maxTime+1)]
#         jobSchedule = sorted(zip(startTime, endTime, profit), key=lambda t: t[1])
#         for start, end, pro in jobSchedule:
#             dp[end] = max(dp[end], dp[start]+pro)
#             for time in startTime:
#                 if time > end: dp[time] = max(dp[time], dp[end])
#             for time in endTime:
#                 if time > end: dp[time] = max(dp[time], dp[end])
#         return dp[maxTime]
#
#
# class Solution:
#     def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
#         job_schedules = sorted(zip(startTime, endTime, profit), key=lambda t: t[1])
#
#         def dfs(end_time: int, remaining_jobs: List[Tuple[int, int, int]], current_profit: int):
#             if not remaining_jobs: return current_profit
#
#             answer = current_profit
#             for i, (start, end, pro) in enumerate(remaining_jobs):
#                 if start >= end_time:
#                     answer = max(answer, dfs(end, remaining_jobs[i + 1:], current_profit + pro))
#             return answer
#
#         return dfs(0, job_schedules, 0)
#
#
# class Solution:
#     def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
#         job_schedules = sorted(zip(startTime, endTime, profit), key=lambda t: t[1])
#         max_profit_at_start = defaultdict(int)
#
#         def dfs(end_time: int, remaining_jobs: List[Tuple[int, int, int]], current_profit: int):
#             if not remaining_jobs: return current_profit
#             max_profit_at_start[end_time] = current_profit
#
#             answer = current_profit
#             for i, (start, end, pro) in enumerate(remaining_jobs):
#                 if start >= end_time and max_profit_at_start[start] < current_profit + pro:
#                     answer = max(answer, dfs(end, remaining_jobs[i + 1:], current_profit + pro))
#             return answer
#
#         return dfs(0, job_schedules, 0)
#
#
# class Solution:
#     def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
#         job_schedules = sorted(zip(startTime, endTime, profit), key=lambda t: t[1])
#         max_profit_at_start = defaultdict(int)
#
#         def dfs(end_time: int, remaining_jobs: List[Tuple[int, int, int]], current_profit: int):
#             if not remaining_jobs: return current_profit
#             max_profit_at_start[end_time] = current_profit
#
#             answer = current_profit
#             filtered_jobs = list(filter(lambda t: t[0] >= end_time, remaining_jobs))
#             for i, (start, end, pro) in enumerate(filtered_jobs):
#                 if max_profit_at_start[start] < current_profit + pro:
#                     answer = max(answer, dfs(end, filtered_jobs[i + 1:], current_profit + pro))
#             return answer
#
#         return dfs(0, job_schedules, 0)
#
# import bisect
#
# class Solution:
#     def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
#         job_schedules = sorted(zip(startTime, endTime, profit))
#         startTime = [x[0] for x in job_schedules]
#         max_profit_at_start = defaultdict(int)
#
#         # max_profit_at_start[~end_time]까지 가질 수 있는 maximum profit
#         # dfs: end_time~ 에서 가질 수 있는 maximum profit을 구하는
#         def dfs(end_time: int, current_profit: int):
#             max_profit_at_start[end_time] = current_profit
#
#             idx = bisect.bisect_left(startTime, end_time)
#             if idx == len(startTime): return current_profit
#
#             answer = current_profit
#             for i in range(idx, len(job_schedules)):
#                 start, end, pro = job_schedules[i]
#                 if max_profit_at_start[start] < current_profit + pro:
#                     answer = max(answer, dfs(end, current_profit + pro))
#             return answer
#
#         return dfs(0, 0)

