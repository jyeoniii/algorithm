# https://leetcode.com/problems/middle-of-the-linked-list/

from common.common_data import ListNode


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow