# https://leetcode.com/problems/longest-substring-without-repeating-characters/#

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        d = defaultdict(int)
        answer = 0
        while end < len(s):
            while d[s[end]] > 0:
                d[s[start]] -= 1
                start += 1

            answer = max(answer, end - start + 1)
            d[s[end]] += 1
            end += 1
        return answer