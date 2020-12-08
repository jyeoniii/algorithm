# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return None

        node, head, tail = head, None, None
        while node:
            original = node
            while node.next and node.next.val == node.val:
                node = node.next

            if node != original:
                node = node.next
                if tail: tail.next = None
                continue

            if not head: head = node
            if tail: tail.next = node

            tail, node = node, node.next

        return head

