# https://leetcode.com/problems/reverse-linked-list-ii/

from common.common_data import ListNode


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        stack = []

        def helper(node: ListNode, idx: int):
            if not node: return None

            if idx < m:
                node.next = helper(node.next, idx + 1)
                return node
            elif m <= idx < n:
                stack.append(node)
                return helper(node.next, idx + 1)
            else:  # n <= idx
                tail, next = node, node.next
                while stack:
                    tail.next = stack.pop()
                    tail = tail.next
                tail.next = next
                return node

        return helper(head, 1)


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        stack, idx = [], 1
        node = head
        left = dummy = ListNode(1)
        while node:
            if idx < m:
                left = node
            if m <= idx < n:
                stack.append(node)
            elif n <= idx:
                tail, next = node, node.next
                while stack:
                    tail.next = stack.pop()
                    tail = tail.next
                tail.next, left.next = next, node
                break

            idx += 1
            node = node.next

        return head if left != dummy else dummy.next