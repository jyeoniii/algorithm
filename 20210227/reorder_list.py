# https://leetcode.com/problems/reorder-list/

from common.common_data import ListNode
from typing import Tuple


class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next: return head
        slow, fast = head, head.next.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        if not fast:  # even
            right = slow.next
            slow.next = None
        else:
            right = slow.next.next
            slow.next.next = None

        stack = []
        while right:
            stack.append(right)
            right = right.next

        node = head
        while node and stack:
            next_node = node.next
            node.next = stack.pop()
            node.next.next = next_node
            node = next_node

        return head


class Solution:
    def reverseList(self, node: ListNode) -> Tuple[ListNode, ListNode]:
        if not node.next: return node, node
        head, tail = self.reverseList(node.next)
        node.next = None
        tail.next = node
        return head, node

    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next: return head
        slow, fast = head, head.next.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        if not fast:  # even
            right = slow.next
            slow.next = None
        else:
            right = slow.next.next
            slow.next.next = None

        right, _ = self.reverseList(right)

        node = head
        while right:
            next_node = node.next
            node.next = right
            right = right.next
            node.next.next = next_node
            node = next_node

        return head