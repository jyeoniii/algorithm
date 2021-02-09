# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3634/


from common.common_data import TreeNode


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def helper(node: TreeNode, add: int) -> int:
            if not node: return 0
            node.val += helper(node.right, add) + add
            return node.val - add + helper(node.left, node.val)

        helper(root, 0)
        return root


class Solution:
    def __init__(self):
        self.curr_sum = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root: return
        self.convertBST(root.right)
        self.curr_sum += root.val
        root.val = self.curr_sum
        self.convertBST(root.left)

        return root