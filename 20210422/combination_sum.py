# https://leetcode.com/problems/combination-sum/

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def recursive(curr: List[int], idx: int, curr_sum: int):
            if curr_sum == target:
                answer.append(curr[:])
                return
            if idx == len(candidates):
                return

            recursive(curr, idx + 1, curr_sum)
            cnt = 0
            while curr_sum + (cnt + 1) * candidates[idx] <= target:
                curr.append(candidates[idx])
                cnt += 1
                recursive(curr, idx + 1, curr_sum + cnt * candidates[idx])

            for _ in range(cnt):
                curr.pop()

        recursive([], 0, 0)
        return answer


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def recursive(curr: List[int], curr_sum: int):
            if curr_sum == target:
                answer.append(curr[:])
                return

            for num in candidates:
                if (not curr or curr[-1] <= num) and curr_sum + num <= target:
                    curr.append(num)
                    recursive(curr, curr_sum + num)
                    curr.pop()

        recursive([], 0)
        return answer


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        candidates.sort()

        def recursive(curr: List[int], idx: int, curr_sum: int):
            if curr_sum == target:
                answer.append(curr[:])
                return

            for i in range(idx, len(candidates)):
                num = candidates[i]
                if curr_sum + num <= target:
                    curr.append(num)
                    recursive(curr, i, curr_sum + num)
                    curr.pop()

        recursive([], 0, 0)
        return answer