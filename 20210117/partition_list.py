# https://leetcode.com/problems/partition-list/

from common.common_data import ListNode


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        left = left_tail = ListNode(0)
        right = right_tail = ListNode(0)

        while head:
            next_node = head.next
            if head.val < x:
                left_tail.next = head
                head.next = None
                head = next_node
                left_tail = left_tail.next
            elif head.val >= x:
                right_tail.next = head
                head.next = None
                head = next_node
                right_tail = right_tail.next

        left_tail.next = right.next

        return left.next