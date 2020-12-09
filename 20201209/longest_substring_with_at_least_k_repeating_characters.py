# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
# result에 있는 char는 모두 k번 이상 나타났다 <=> s에 있는 char 중 k번 아래로 나타난 것은 result에 포함될 수 없다

from collections import defaultdict, Counter


# Divide and Conquer
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s: return 0

        invalid_c = [c for c, cnt in Counter(s).items() if cnt < k]
        for i, c in enumerate(s):
            if c in invalid_c:
                return max(self.longestSubstring(s[i+1:], k), self.longestSubstring(s[:i], k))

        return len(s)

# Divide and Conquer 2
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s: return 0

        counter = Counter(s)
        min_char = min(counter, key=lambda x: counter[x])

        if counter[min_char] >= k: return len(s)

        return max([self.longestSubstring(sub_str, k) for sub_str in s.split(min_char)])


# Sliding Window
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s: return 0

        max_unique = len(Counter(s))

        # curr_unique: maximum number of unique characters that must be present in the sliding window
        answer = 0
        for curr_unique in range(1, max_unique+1):
            start, end = 0, 0
            num_unique_c, c_at_least_k_count, max_len = 0, 0, 0
            counter = defaultdict(int)

            while end < len(s):
                if num_unique_c <= curr_unique: # expand - include end
                    c = s[end]
                    if counter[c] == 0: num_unique_c += 1 # new character
                    counter[c] += 1

                    if counter[c] == k:
                        c_at_least_k_count += 1
                    if counter[c] >= k and c_at_least_k_count == curr_unique:
                        max_len = max(max_len, end - start + 1)
                    end += 1
                else: # shrink - exclude start
                    c = s[start]
                    if counter[c] == k: c_at_least_k_count -= 1

                    counter[c] -= 1
                    if counter[c] == 0: num_unique_c -= 1
                    start += 1

            answer = max(answer, max_len)

        return answer





