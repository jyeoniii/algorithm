# https://leetcode.com/problems/linked-list-cycle/

from common.common_data import ListNode


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        s = set()
        while head:
            if head.next in s: return True
            s.add(head)
            head = head.next

        return False


# Space Complexity: O(1)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        dummy = ListNode(0)
        while head:
            if head.next == dummy: return True
            next = head.next
            head.next = dummy
            head = next
        return False