# https://leetcode.com/problems/sort-list/

from common.common_data import ListNode


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        pre = None
        slow = fast = head
        while fast and fast.next:  # Split List
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None

        left, right = self.sortList(head), self.sortList(slow)

        dummy = tail = ListNode(0)
        while left and right:  # Merge
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        if left: tail.next = left
        elif right: tail.next = right

        return dummy.next
