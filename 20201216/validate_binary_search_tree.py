# Validate Binary Search Tree

from common.common_data import TreeNode
from typing import Tuple

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        answer = True
        def recursive(node: TreeNode) -> Tuple[TreeNode, TreeNode]:
            nonlocal answer
            if not node or not answer: return None, None

            left_min, left_max = recursive(node.left)
            right_min, right_max = recursive(node.right)

            min = left_min if left_min else node
            max = right_max if right_max else node

            if (left_max and left_max.val >= node.val) or (right_min and node.val >= right_min.val):
                answer = False

            return min, max

        recursive(root)
        return answer