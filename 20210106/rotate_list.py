# https://leetcode.com/problems/rotate-list/

from common.common_data import ListNode


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head: return None
        node, tail = head, None
        length = 0
        while node:
            if not node.next: tail = node
            node = node.next
            length += 1

        node = head
        k = k % length
        if k == 0: return head

        while length - k > 1:
            node = node.next
            k += 1

        new_head, node.next = node.next, None
        tail.next = head

        return new_head



