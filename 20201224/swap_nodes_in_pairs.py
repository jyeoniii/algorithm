# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/572/week-4-december-22nd-december-28th/3579/

from common.common_data import ListNode


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        node_to_swap = head.next
        head.next, node_to_swap.next = self.swapPairs(node_to_swap.next), head
        return node_to_swap