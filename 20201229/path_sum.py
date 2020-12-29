# https://leetcode.com/problems/path-sum/

from common.common_data import TreeNode


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False

        def helper(node: TreeNode, s: int) -> bool: # node should not be None
            if not node.left and not node.right: return s == node.val
            return (node.left and helper(node.left, s-node.val)) or (node.right and helper(node.right, s-node.val))

        return helper(root, sum)