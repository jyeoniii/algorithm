# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0

        d = {}
        start, end, answer = 0, 0, 0
        while end < len(s):
            c = s[end]
            if c in d:
                for x in range(start, d[c]): del d[s[x]]
                start = d[c] + 1
                d[c] = end
            else:
                d[c] = end
            end += 1
            answer = max(end - start, answer)

        return answer


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        answer, start = 0, 0

        for end in range(len(s)):
            while s[end] in char_set:
                char_set.remove(s[start])
                start += 1
            char_set.add(s[end])
            answer = max(answer, end - start + 1)
        return answer