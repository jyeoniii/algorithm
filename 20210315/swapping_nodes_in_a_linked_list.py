# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3671/

from common.common_data import ListNode


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        length = 0
        node, node1 = head, None
        while node:
            length += 1
            if length == k:
                node1 = node
            node = node.next

        node = head
        while length - k > 0:
            node = node.next
            length -= 1

        node2 = node
        node1.val, node2.val = node2.val, node1.val

        return head


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        slow, fast = head, head
        while k > 1:
            fast = fast.next
            k -= 1

        node1 = fast
        while fast.next:
            slow, fast = slow.next, fast.next
        node2 = slow

        node1.val, node2.val = node2.val, node1.val
        return head


# Swapping node itself, not just a value
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        prev, nodes = {}, []
        node = head
        while node.next:
            prev[node.next] = node
            nodes.append(node)
            node = node.next
        nodes.append(node)

        node1, node2 = (nodes[k - 1], nodes[len(nodes) - k]) if k - 1 <= len(nodes) - k else (nodes[len(nodes) - k], nodes[k - 1])
        node1.next, node2.next = node2.next, node1.next if node1.next != node2 else node1
        if node1 in prev and prev[node1] != node2:
            prev[node1].next = node2
        if node2 in prev and prev[node2] != node1:
            prev[node2].next = node1

        return head if node1 != head else node2
