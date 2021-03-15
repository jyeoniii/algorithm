# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/590/week-3-march-15th-march-21st/3673/


class Codec:
    def __init__(self):
        self.urlMap = {}
        self.cnt = 1
        self.urlBase = "http://tinyurl.com"

    def encode(self, longUrl: str) -> str:
        self.urlMap[self.cnt] = longUrl
        encoded = f"{self.urlBase}/{self.cnt}"
        self.cnt += 1
        return encoded

    def decode(self, shortUrl: str) -> str:
        key = shortUrl.split("/")[-1]
        return self.urlMap[int(key)]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))