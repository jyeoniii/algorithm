# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, contains, answer = 0, set(), 0
        for r in range(len(s)):
            while s[r] in contains:
                contains.remove(s[l])
                l += 1
            contains.add(s[r])
            answer = max(r - l + 1, answer)
        return answer


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, pos, answer = 0, {}, 0
        for r in range(len(s)):
            if s[r] in pos and pos[s[r]] >= l:
                answer = max(r - l, answer)
                l = pos[s[r]] + 1
            pos[s[r]] = r

        return max(answer, len(s) - l)
