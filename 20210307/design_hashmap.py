# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3663/

from collections import defaultdict


class MyHashMap:

    def __init__(self):
        self.map = defaultdict(list)

    def put(self, key: int, value: int) -> None:
        key_hash = hash(key)
        if key_hash in self.map:
            for kv in self.map[key_hash]:
                if kv[0] == key:
                    kv[1] = value
                    break
            else:
                self.map[hash(key)].append([key, value])
        else:
            self.map[hash(key)].append([key, value])

    def get(self, key: int) -> int:
        key_hash = hash(key)
        if key_hash not in self.map:
            return -1
        else:
            for k, v in self.map[key_hash]:
                if k == key:
                    return v
            return -1

    def remove(self, key: int) -> None:
        key_hash = hash(key)
        if key_hash in self.map:
            for kv in self.map[key_hash]:
                if kv[0] == key:
                    self.map[key_hash].remove(kv)
                    return


class MyHashMap:

    def __init__(self):
        self.key_space = 2069 # Prime number
        self.buckets = [[] for _ in range(self.key_space)]

    def put(self, key: int, value: int) -> None:
        key_hash = self.getHash(key)
        for kv in self.buckets[key_hash]:
            if kv[0] == key:
                kv[1] = value  # update
                break
        else:
            self.buckets[key_hash].append([key, value])

    def get(self, key: int) -> int:
        key_hash = self.getHash(key)
        for kv in self.buckets[key_hash]:
            if kv[0] == key:
                return kv[1]
        return -1

    def remove(self, key: int) -> None:
        key_hash = self.getHash(key)
        for kv in self.buckets[key_hash]:
            if kv[0] == key:
                self.buckets[key_hash].remove(kv)
                return

    def getHash(self, key: int) -> int:
        return key % self.key_space


