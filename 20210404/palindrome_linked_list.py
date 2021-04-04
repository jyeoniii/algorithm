# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/593/week-1-april-1st-april-7th/3693/

from common.common_data import ListNode
from collections import deque


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q = deque()
        while head:
            q.append(head.val)
            head = head.next

        while q:
            l = q.popleft()
            if q:
                r = q.pop()
                if l != r:
                    return False
            else:
                return True

        return True


# O(1) Space Complexity
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        if fast:  # odd number of nodes
            slow = slow.next

        def recursive(node: ListNode):
            if not node or not node.next:
                return node, node
            h, t = recursive(node.next)
            t.next = node
            node.next = None

            return h, node

        back, _ = recursive(slow)
        while head and back:
            if head.val != back.val: return False
            head, back = head.next, back.next
        return True
