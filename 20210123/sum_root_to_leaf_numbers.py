# https://leetcode.com/problems/sum-root-to-leaf-numbers/

from common.common_data import TreeNode
from typing import List


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, num: int) -> List[int]:
            if not node: return []
            if not node.left and not node.right: return [num * 10 + node.val]

            new_num = num * 10 + node.val
            return dfs(node.left, new_num) + dfs(node.right, new_num)

        return sum(dfs(root, 0))