# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

from common.common_data import TreeNode
from typing import List


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        elif len(inorder) == 1:
            return TreeNode(inorder[0])

        root_val = postorder[-1]
        idx = inorder.index(root_val)

        right_length = len(inorder) - idx - 1  # left_length = idx

        left = self.buildTree(inorder[:idx], postorder[: -1-right_length])
        right = self.buildTree(inorder[idx + 1:], postorder[-1-right_length:-1])

        return TreeNode(root_val, left, right)


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder: return None

        root_val = postorder[-1]
        idx = inorder.index(root_val)

        left = self.buildTree(inorder[:idx], postorder[:idx])
        right = self.buildTree(inorder[idx+1:], postorder[idx:-1])

        return TreeNode(postorder[-1], left, right)
