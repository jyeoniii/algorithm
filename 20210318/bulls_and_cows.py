# https://leetcode.com/problems/bulls-and-cows/

from collections import Counter, defaultdict


class Solution:

    def getHint(self, secret: str, guess: str) -> str:
        c1, c2 = Counter(secret), Counter(guess)
        bulls = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                c1[secret[i]] -= 1
                c2[secret[i]] -= 1
                bulls += 1

        cows = len(secret) - sum(v for k, v in (c1 - c2).items()) - bulls

        return f"{bulls}A{cows}B"


class Solution:

    def getHint(self, secret: str, guess: str) -> str:
        counter, bulls = defaultdict(int), 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                counter[secret[i]] += 1
                counter[guess[i]] -= 1

        cows = len(secret) - sum(v for k, v in counter.items() if v > 0) - bulls

        return f"{bulls}A{cows}B"