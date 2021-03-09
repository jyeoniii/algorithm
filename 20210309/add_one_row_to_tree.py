# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3666/

from common.common_data import TreeNode


class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            return TreeNode(v, left=root)
        elif d == 2:
            root.left = TreeNode(val=v, left=root.left)
            root.right = TreeNode(val=v, right=root.right)
            return root
        else:
            if root.left:
                root.left = self.addOneRow(root.left, v, d-1)
            if root.right:
                root.right = self.addOneRow(root.right, v, d-1)
            return root