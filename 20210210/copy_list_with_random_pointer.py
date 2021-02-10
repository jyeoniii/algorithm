# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3635/

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None

        d = { head: Node(head.val) }  # d[prev]=new
        dummy = tail = Node(0)
        while True:
            new_node = d[head]
            tail.next = new_node
            if head.random not in d:
                d[head.random] = Node(head.random.val) if head.random else None
            new_node.random = d[head.random]

            if not head.next: break

            if head.next not in d:
                d[head.next] = Node(head.next.val)
            new_node.next = d[head.next]

            head, tail = head.next, tail.next

        return dummy.next


