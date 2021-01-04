# https://leetcode.com/problems/merge-two-sorted-lists/#

from common.common_data import ListNode

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(-1)
        tail = head
        while l1 and l2:
            if l1.val < l2.val:
                tail.next, l1 = l1, l1.next
                tail = tail.next
            else:
                tail.next, l2 = l2, l2.next
                tail = tail.next

        while l1:
            tail.next, l1 = l1, l1.next
            tail = tail.next
        while l2:
            tail.next, l2 = l2, l2.next
            tail = tail.next

        return head.next