# https://leetcode.com/problems/lru-cache/


class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = self.tail = ListNode("dummy", 0)
        self.length = 0

    def remove(self, node: ListNode):
        if node == self.tail:
            self.tail = self.tail.prev

        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        node.prev = node.next = None

    def insert(self, after: ListNode, target: ListNode):
        next = after.next
        after.next = target
        target.prev = after
        target.next = next
        if next:
            next.prev = target
        if after == self.tail:
            self.tail = target

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(self.head, node)
            return

        node = ListNode(key, value)
        if self.length == self.capacity:  # evict
            del_key = self.tail.key
            self.remove(self.tail)

            del self.cache[del_key]
            self.length -= 1

        self.insert(self.head, node)
        self.cache[key] = node
        self.length += 1

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]
        if self.head.next == self.cache[key]:
            return node.val

        self.remove(node)
        self.insert(self.head, node)

        return self.cache[key].val