# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3655/

from collections import defaultdict


class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.max_freq = 0

    def push(self, x: int) -> None:
        self.freq[x] += 1
        if self.freq[x] > self.max_freq:
            self.max_freq = self.freq[x]

        self.group[self.freq[x]].append(x)

    def pop(self) -> int:
        x = self.group[self.max_freq].pop()
        self.freq[x] -= 1
        while self.max_freq > 0 and not self.group[self.max_freq]:
            self.max_freq -= 1

        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()