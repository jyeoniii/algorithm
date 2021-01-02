# https://leetcode.com/problems/binary-tree-postorder-traversal/

from common.common_data import TreeNode
from typing import List

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def helper(node: TreeNode, li: List[int]):
            if not node: return
            helper(node.left, li)
            helper(node.right, li)
            li.append(node.val)
            return li
        return helper(root, [])