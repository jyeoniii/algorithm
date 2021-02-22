# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3649/

from typing import List


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        answer, del_cnt = "", float("inf")
        for word in d:
            i, j, cnt = 0, 0, 0
            while i < len(s) and j < len(word):
                if s[i] == word[j]: j += 1
                else: cnt += 1
                i += 1
            if j < len(word): continue
            cnt += len(s) - i
            if cnt < del_cnt or (del_cnt == cnt and (not answer or word < answer)):
                answer, del_cnt = word, cnt

        return answer


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d = sorted(d, key=lambda x: (-len(x), x))
        for word in d:
            last_idx = 0
            for c in word:
                prev, last_idx = last_idx, s.find(c, last_idx) + 1
                if last_idx == 0: break
            else:
                return word

        return ""


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        answer, del_cnt = "", float("inf")
        for word in d:
            last_idx, cnt = -1, 0
            for c in word:
                prev, last_idx = last_idx, s.find(c, last_idx+1)
                if last_idx == -1: break
                else: cnt += last_idx - prev - 1
            else:
                cnt += len(s) - last_idx - 1
                if cnt < del_cnt or (del_cnt == cnt and (not answer or word < answer)):
                    answer, del_cnt = word, cnt

        return answer


