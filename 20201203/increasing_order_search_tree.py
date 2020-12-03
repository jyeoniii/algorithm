# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3553/

from typing import Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def _traversal(node: TreeNode) -> Tuple[TreeNode, TreeNode]: # top, bottom
            if not node: return node, node

            left_top, left_bottom = _traversal(node.left)
            right_top, right_bottom = _traversal(node.right)

            node.left, node.right = None, right_top
            right_bottom = right_bottom if right_bottom else node

            if left_bottom:
                left_bottom.right = node
                return left_top, right_bottom
            else:
                return node, right_bottom

        return _traversal(root)[0]