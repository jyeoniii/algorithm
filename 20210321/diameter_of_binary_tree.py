# https://leetcode.com/problems/diameter-of-binary-tree/

from common.common_data import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        inner_max = 0

        def recursive(node: TreeNode) -> int:  # node must not be none
            if not node: return -1
            left = 1 + recursive(node.left)
            right = 1 + recursive(node.right)

            nonlocal inner_max
            inner_max = max(inner_max, left + right)

            return max(left, right)

        return max(recursive(root), inner_max)
