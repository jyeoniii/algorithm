# https://leetcode.com/problems/binary-tree-maximum-path-sum/

from common.common_data import TreeNode

class Solution:
    inner_max = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        def recursive(node: TreeNode):
            if not node: return float("-inf")
            left, right = recursive(node.left), recursive(node.right)
            self.inner_max = max(self.inner_max, left + right + node.val, left, right)
            return max(node.val, left + node.val, right + node.val)

        from_root_max = recursive(root)
        return max(self.inner_max, from_root_max)