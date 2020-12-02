# Definition for singly-linked list.
# December Leetcode challenge Day2
# TODO: Study Reservoir sampling(https://en.wikipedia.org/wiki/Reservoir_sampling)
import random

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.arr = []
        idx, node = 0, head
        while node:
            self.arr.append(node.val)
            idx, node = idx+1, node.next
        self.length = idx

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        rand = random.randint(0, self.length-1)
        return self.arr[rand]

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        node = self.head
        scope = 1
        answer = node.val
        while node:
            j = random.randint(1, scope)
            if j <= 1:
                answer = node.val
            scope += 1
            node = node.next
        return answer
