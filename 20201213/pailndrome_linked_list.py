# https://leetcode.com/problems/palindrome-linked-list/

from common.common_data import ListNode
from collections import deque
from typing import Tuple


# O(n) Time complexity, O(n) Memory Complexity
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        queue = deque()
        node = head
        while node:
            queue.append(node.val)
            node = node.next

        while len(queue) > 1:
            if queue.popleft() != queue.pop(): return False
        return True

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow if not fast else slow.next

        def reverse_list(node: ListNode) -> Tuple[ListNode, ListNode]:
            if not node: return node, node

            reversed_head, reversed_tail = reverse_list(node.next)
            if reversed_tail:
                reversed_tail.next = node
                node.next = None
                return reversed_head, node
            else:
                return node, node

        node1, node2 = head, reverse_list(mid)[0]
        while node2:
            if node1.val != node2.val:
                return False
            node1, node2 = node1.next, node2.next
        return True



