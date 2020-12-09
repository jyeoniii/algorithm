# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3560/

from common.common_data import TreeNode, ListNode
from typing import Tuple
from collections import deque


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = deque()
        def _traversal(node: TreeNode):
            if not node: return

            _traversal(node.left)
            self.stack.append(node)
            _traversal(node.right)
        _traversal(root)

    def next(self) -> int:
        return self.stack.popleft().val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


class BSTIterator:
    def __init__(self, root: TreeNode):
        def _traversal(node: TreeNode) -> Tuple[ListNode, ListNode]:
            if not node: return None, None

            left_head, left_tail = _traversal(node.left)
            right_head, right_tail = _traversal(node.right)

            curr = ListNode(node.val, right_head)

            tail = right_tail if right_tail else curr
            if left_tail:
                left_tail.next = curr
                return left_head, tail
            else:
                return curr, tail

        head, tail = _traversal(root)
        self.head = ListNode(head.val - 1, head)
        self.cursor = self.head

    def next(self) -> int:
        self.cursor = self.cursor.next
        return self.cursor.val

    def hasNext(self) -> bool:
        return self.cursor.next is not None
