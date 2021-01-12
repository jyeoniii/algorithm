# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3601/

from common.common_data import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = tail = ListNode(0)
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            tail.next = ListNode((val1 + val2 + carry) % 10)
            carry = 1 if val1 + val2 + carry >= 10 else 0
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            tail = tail.next

        return head.next
