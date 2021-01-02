# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

from common.common_data import TreeNode

class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root: return None, None

        l_head, l_tail = self.flatten(root.left)
        r_head, r_tail = self.flatten(root.right)

        if l_head:
            root.right = l_head
            l_tail.right = r_head
        else:
            root.right = r_head

        root.left = None
        return root, r_tail or l_tail or root


class Solution:

    def __init__(self):
        self.prev = None

    def flatten(self, root: TreeNode) -> None:
        if not root: return None

        self.flatten(root.right)
        self.flatten(root.left)

        root.left = None
        root.right = self.prev
        self.prev = root
