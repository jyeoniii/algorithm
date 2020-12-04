# https://leetcode.com/problems/reverse-linked-list/submissions/

from typing import List, Tuple


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return None
        def dfs(node: ListNode) -> Tuple[ListNode, ListNode]:
            if node.next:
                head, tail = dfs(node.next)
                tail.next, node.next = node, None
                return head, node
            else:
                return node, node

        return dfs(head)[0]