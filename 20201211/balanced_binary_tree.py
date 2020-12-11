# https://leetcode.com/problems/balanced-binary-tree/

from common.common_data import TreeNode


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True

        def getHeight(node: TreeNode) -> int:
            if not node: return 0
            left_height = getHeight(node.left)
            right_height = getHeight(node.right)
            if left_height == -1 or right_height == -1:
                return -1

            diff = abs(left_height - right_height)

            return -1 if diff > 1 else max(left_height, right_height) + 1

        return getHeight(root) != -1