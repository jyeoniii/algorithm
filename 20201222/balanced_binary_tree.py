# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/572/week-4-december-22nd-december-28th/3577/

from common.common_data import TreeNode

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def getHeight(node: TreeNode) -> int:
            if not node: return 0

            left, right = getHeight(node.left), getHeight(node.right)
            if left < 0 or right < 0:
                return -1
            if abs(left - right) <= 1:  # valid
                return max(left, right) + 1
            else:
                return -1

        return getHeight(root) >= 0
