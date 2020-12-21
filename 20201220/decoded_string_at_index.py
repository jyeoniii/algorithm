# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/571/week-3-december-15th-december-21st/3572/


class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        decoded = ""
        for c in S:
            if c >= 'a' and c <= 'z': # letter
                decoded += c
            else: # digit
                cnt = int(c)
                if len(decoded) < K < len(decoded) * cnt:
                    tmp = K % len(decoded)
                    return decoded[tmp-1]
                decoded = decoded * cnt
            if len(decoded) >= K: break
        return decoded[K-1]

class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        N=0
        for x in range(len(S)):
            if S[x].isdigit():
                N*=int(S[x])
            else:
                N+=1
            if N>=K:
                break
        for back in range(x,-1,-1):
            if S[back].isdigit():
                N/=int(S[back])
                K%=N
            else:
                if K==N or K==0:
                    return S[back]
                N-=1

class Solution:
    def decodeAtIndex(self, S, K):
        lens, n = [0], len(S)
        for c in S:
            if c.isdigit():
                lens.append(lens[-1] * int(c))
            else:
                lens.append(lens[-1] + 1)

        for i in range(n, 0, -1):
            K %= lens[i]
            if K == 0 and S[i - 1].isalpha():
                return S[i - 1]


if __name__=="__main__":
    s = Solution()
    print(s.decodeAtIndex("leet2code3", 10))
    print(s.decodeAtIndex("ha22", 5))
