# https://leetcode.com/problems/path-sum-ii/

from typing import List
from common.common_data import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        answer = []
        def helper(node: TreeNode, curr_sum: int, path: List[int]):
            if not node: return

            path.append(node.val)
            if not node.left and not node.right and curr_sum + node.val == sum: # Leaf Node
                answer.append(path[:])
            else:
                helper(node.left, curr_sum + node.val, path)
                helper(node.right, curr_sum + node.val, path)
            path.pop()

        helper(root, 0, [])
        return answer




