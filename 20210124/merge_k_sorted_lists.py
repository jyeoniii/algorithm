# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3615/

from typing import List
from common.common_data import ListNode
import heapq


# Time Complexity: O(NlogK), Where N is the total number of nodes
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ListNode.__lt__=lambda self, other: self.val <= other.val
        head = tail = ListNode(0)
        h = []
        for list in lists:
            if list: heapq.heappush(h, list)

        while h:
            node = heapq.heappop(h)
            tail.next = node
            tail = tail.next
            node = node.next
            if node:
                heapq.heappush(h, node)

        return head.next


# Time Complexity: O(NlogN), Where N is the total number of nodes
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        values = []
        head = tail = ListNode(0)
        for node in lists:
            while node:
                values.append(node.val)
                node = node.next

        for val in sorted(values):
            tail.next = ListNode(val)
            tail = tail.next

        return head.next


from collections import deque

# Divide And Conquer
# Time Complexity: O(NlogK), Where N is the total number of nodes in two lists
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def mergeTwoLists(l1: ListNode, l2: ListNode):
            head = tail = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next

            if l1: tail.next = l1
            if l2: tail.next = l2

            return head.next

        q = deque(lists)
        while len(q) > 1:
            l1, l2 = q.popleft(), q.popleft()
            q.append(mergeTwoLists(l1, l2))

        return q.pop() if q else None


