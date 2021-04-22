# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from common.common_data import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow, fast = head, head
        while n > 0:
            fast = fast.next
            n -= 1
        if not fast:
            return head.next
        while fast.next:
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next
        return head
