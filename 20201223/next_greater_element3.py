# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/572/week-4-december-22nd-december-28th/3578/

MAX_INT = 2147483647

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        num = list(str(n))
        answer = float("inf")
        for i in range(len(num)-1, 0, -1):
            for j in range(i-1, -1, -1):
                if num[j] >= num[i]: continue
                num[j], num[i] = num[i], num[j]
                tmp = int(''.join(num[:j+1] + sorted(num[j+1:])))
                if tmp > n:
                    answer = min(tmp, answer)
                num[j], num[i] = num[i], num[j]

        return answer if answer <= MAX_INT else -1


import  bisect

# https://leetcode.com/problems/next-greater-element-iii/discuss/644856/Python3-concise-O(n)-solution-using-bisect-and-reduce-Next-Greater-Element-III
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                break
        else:
            return -1

        nums[i:] = nums[i:][::-1]
        j = bisect.bisect(nums, nums[i - 1], lo=i)
        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        ans = int(''.join(nums))
        return ans if ans <= MAX_INT else -1

