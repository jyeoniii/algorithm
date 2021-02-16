# https://leetcode.com/problems/restore-ip-addresses/

from typing import List

class Solution:
    def __init__(self):
        self.answer = []

    def restoreIpAddresses(self, s: str, ips: List[str]=[]) -> List[str]:
        if len(ips) == 4 and not s:
            self.answer.append('.'.join(ips))
        elif len(ips) < 4 and s:
            for length in range(1, min(3, len(s)) + 1):
                num = s[:length]
                if num == str(int(num)) and int(num) < 256:
                    ips.append(num)
                    self.restoreIpAddresses(s[length:], ips)
                    ips.pop()
        return self.answer
