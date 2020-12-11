# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

from common.common_data import TreeNode


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []

        def recursive(node: TreeNode, k: int) -> int:
            if not node: return None

            left_result = recursive(node.left, k)
            if left_result is not None: return left_result

            stack.append(node)
            if len(stack) == k:
                return node.val

            right_result = recursive(node.right, k)
            if right_result is not None: return right_result

            return None

        return recursive(root, k)
