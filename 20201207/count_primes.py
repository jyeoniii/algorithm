# https://leetcode.com/problems/count-primes/

import math


class Solution:
    def countPrimes(self, n: int) -> int:
        def is_prime(x: int):
            sqrt_x = math.floor(math.sqrt(x))
            for i in range(2, sqrt_x + 1):
                if x % i == 0: return False
            return True

        seen = [False] * (n+1)
        count = 0
        for i in range(2, n):
            if seen[i]: continue
            if is_prime(i):
                for j in range (i, n+1, i):
                    seen[j] = True
                    count += 1
        return count


# eratosthenes sieve
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3: return 0

        prime = [1] * (n)
        for i in range(2, int(math.sqrt(n - 1)) + 1):
            if prime[i]:
                for j in range(i * i, n, i):
                    prime[j] = 0

        return sum(prime) - 2  # 0,1