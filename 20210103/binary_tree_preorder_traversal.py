# https://leetcode.com/problems/binary-tree-preorder-traversal/

from common.common_data import TreeNode
from typing import List


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def helper(node: TreeNode, li: List[int]) -> List[int]:
            if not node: return
            li.append(node.val)
            helper(node.left, li)
            helper(node.right, li)
            return li

        return helper(root, [])

