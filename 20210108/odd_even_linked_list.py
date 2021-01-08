# https://leetcode.com/problems/odd-even-linked-list/

from common.common_data import ListNode


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head: return None

        i, odd_tail = 1, head
        even_head = even_tail = ListNode(-1)
        i, node = 2, head.next
        while node:
            if i % 2 == 1:
                odd_tail.next, odd_tail = node, node
            else:
                even_tail.next, even_tail = node, node
            next = node.next
            node.next = None
            node = next
            i += 1

        odd_tail.next = even_head.next
        return head


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head: return None

        odd_tail = head
        even, even_start = head.next, head.next

        while odd_tail.next and even.next:
            odd_tail.next = even.next
            even.next = odd_tail.next.next

            odd_tail = odd_tail.next
            even = even.next

        odd_tail.next = even_start
        return head


