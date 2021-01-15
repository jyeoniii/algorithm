# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

from common.common_data import ListNode


class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        d = {}
        dummy = prev = ListNode(0, head)
        node = head
        while node:
            if node.val == 0: prev.next = node.next
            elif -node.val in d:
                prev = d[-node.val]
                prev.next = node.next
                while -node.val in d: d.popitem()
                d = {x+node.val: d[x] for x in d}
            else:
                d = {x+node.val: d[x] for x in d}
                d[node.val] = prev
                prev = node
            node = node.next
        return dummy.next


# prefix sum: if l1+l2 = l1+l2+...+l5 => l3+...+l5 = 0 -> consecutive sequence of nodes: l3 ~ l5
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prefix = 0
        d = {0: dummy}
        while head:
            prefix += head.val
            d[prefix] = head
            head = head.next

        head, prefix = dummy, 0
        while head:
            prefix += head.val
            head.next = d[prefix].next
            head = head.next

        return dummy.next