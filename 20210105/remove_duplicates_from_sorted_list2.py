# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3593/

from common.common_data import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return None

        last, last_count, node = head, 1, head.next
        new_head = tail = ListNode(-1)
        while node:
            if node.val != last.val:
                if last_count == 1:
                    tail.next, last.next = last, None
                    tail = tail.next
                last, last_count = node, 1
            else:
                last_count += 1
            node = node.next
        if last_count == 1: tail.next, last.next = last, None

        return new_head.next
